#!/usr/bin/env python3
"""Generate the bilingual static site.

German pages live in the project root (/ and /gdf/), English pages in /en/ and /en/gdf/.
Run from anywhere:  python3 tools/build.py
Articles are NOT built here - they are JSON files in content/articles/ rendered in the browser.
"""
import os, re, html, hashlib
import content_de, content_en

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ver(path):
    """Short content hash appended as ?v=… so browsers never combine new pages with a cached old stylesheet."""
    with open(os.path.join(OUT, path), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


V_CSS, V_JS = ver("assets/style.css"), ver("assets/main.js")
UNI_DS = "https://www.uni-heidelberg.de/datenschutzerklaerung_web.html"
MAIL = "freunde@uni-heidelberg.de"

T = {  # interface strings
    "de": dict(lang_name="Deutsch", skip="Zum Inhalt springen", menu="Menü", news="Aktuelles", all_news="Alle Neuigkeiten",
               contact="Kontakt", imprint="Impressum", privacy="Datenschutz", other_lang="English", other_lang_code="EN",
               switch_label="Wechsel zwischen den Einrichtungen", nav_label="Hauptnavigation", lang_label="Sprache wählen",
               volunteer="Diese Website entsteht ehrenamtlich auf freiwilliger Initiative.", authors="Autorenpanel", with_uni="In Verbindung mit der",
               read_more="Weiterlesen", site_short={"stiftung": "Stiftung", "gdf": "Gesellschaft der Freunde"}),
    "en": dict(lang_name="English", skip="Skip to content", menu="Menu", news="News", all_news="All news",
               contact="Contact", imprint="Legal notice", privacy="Privacy", other_lang="Deutsch", other_lang_code="DE",
               switch_label="Switch between the institutions", nav_label="Main navigation", lang_label="Choose language",
               volunteer="This website is built voluntarily, on personal initiative.", authors="Author panel", with_uni="In association with",
               read_more="Read more", site_short={"stiftung": "Foundation", "gdf": "Friends’ Association"}),
}

SITES = {
    "stiftung": {
        "de": dict(name="Stiftung Universität Heidelberg", tag="Seit 1984 für die Ruperto Carola",
                   desc="Die Stiftung Universität Heidelberg fördert seit 1984 Forschung und Lehre der Ruprecht-Karls-Universität durch Preise, Projekte und die Aktion UniHDhilft.",
                   cta=("Spenden", "spenden.html"), cta2=("Preise", "preise.html"),
                   stats=[("1984", "gegründet"), ("1990", "erste Ruprecht-Karls-Preise"), ("190+", "ausgezeichnete Nachwuchsforschende"), ("250.000 €", "für den Innenhof der Neuen Universität")],
                   nav=[("index", "Die Stiftung", [("idee", "Idee"), ("personen", "Personen"), ("kuratorium", "Kuratorium"), ("partner", "Partner")]),
                        ("aktivitaeten", "Aktivitäten", [("preise", "Preise"), ("projekte", "Projekte")]),
                        ("spenden", "Spenden", [("mitwirken", "Mitwirken")]),
                        ("news", "Aktuelles", []), ("kontakt", "Kontakt", [])]),
        "en": dict(name="Heidelberg University Foundation", tag="For Ruperto Carola since 1984",
                   desc="The Stiftung Universität Heidelberg has supported research and teaching at Ruprecht-Karls-Universität since 1984 through prizes, projects and the UniHDhilft campaign.",
                   cta=("Donate", "spenden.html"), cta2=("Prizes", "preise.html"),
                   stats=[("1984", "established"), ("1990", "first Ruprecht-Karls Prizes"), ("190+", "early-career researchers honoured"), ("€250,000", "for the Neue Universität courtyard")],
                   nav=[("index", "The Foundation", [("idee", "Idea"), ("personen", "People"), ("kuratorium", "Board of Trustees"), ("partner", "Partners")]),
                        ("aktivitaeten", "Activities", [("preise", "Prizes"), ("projekte", "Projects")]),
                        ("spenden", "Donate", [("mitwirken", "Get involved")]),
                        ("news", "News", []), ("kontakt", "Contact", [])]),
    },
    "gdf": {
        "de": dict(name="Gesellschaft der Freunde Universität Heidelberg e.V.", tag="Herz und Verstand für die Ruperto Carola",
                   desc="Die Gesellschaft der Freunde Universität Heidelberg e.V. – Alumni- und Förderverein mit rund 1.400 Mitgliedern.",
                   cta=("Mitglied werden", "werden.html"), cta2=("Veranstaltungen", "veranstaltungen.html"),
                   stats=[("1.400", "Mitglieder"), ("2003", "gegründet"), ("7", "Sektionen"), ("2.500 €", "Preis der Freunde seit 1995")],
                   nav=[("index", "Der Verein", [("idee", "Idee"), ("personen", "Personen"), ("partner", "Partner")]),
                        ("aktivitaeten", "Aktivitäten", [("veranstaltungen", "Veranstaltungen"), ("preise", "Preis der Freunde"), ("foerdern", "Fördern"), ("jahrbuecher", "Jahrbücher")]),
                        ("mitglieder", "Mitglieder", [("service", "Service"), ("sektionen", "Sektionen"), ("werden", "Mitglied werden")]),
                        ("mitwirken", "Engagement", []), ("news", "Aktuelles", []), ("kontakt", "Kontakt", [])]),
        "en": dict(name="Gesellschaft der Freunde Universität Heidelberg e.V.", tag="Heart and mind for Ruperto Carola",
                   desc="The Gesellschaft der Freunde Universität Heidelberg e.V. – alumni and supporters’ association with about 1,400 members.",
                   cta=("Become a member", "werden.html"), cta2=("Events", "veranstaltungen.html"),
                   stats=[("1,400", "members"), ("2003", "founded"), ("7", "sections"), ("€2,500", "Preis der Freunde since 1995")],
                   nav=[("index", "The Association", [("idee", "Idea"), ("personen", "People"), ("partner", "Partners")]),
                        ("aktivitaeten", "Activities", [("veranstaltungen", "Events"), ("preise", "Friends’ Prize"), ("foerdern", "Funding"), ("jahrbuecher", "Yearbooks")]),
                        ("mitglieder", "Members", [("service", "Service"), ("sektionen", "Sections"), ("werden", "Become a member")]),
                        ("mitwirken", "Engagement", []), ("news", "News", []), ("kontakt", "Contact", [])]),
    },
}
DIR = {("de", "stiftung"): "", ("de", "gdf"): "gdf/", ("en", "stiftung"): "en/", ("en", "gdf"): "en/gdf/"}

# extra pages that exist in both languages (content is filled in the browser from content/articles)
EXTRA = {
    "de": {"news": ("Aktuelles", '<h1>Aktuelles</h1><p class="lead">Neuigkeiten aus Stiftung und Verein – mit Fotos, Videos und weiterführenden Links.</p><div data-news-list></div>'),
           "artikel": ("Aktuelles", '<h1>Aktuelles</h1><div data-article></div>')},
    "en": {"news": ("News", '<h1>News</h1><p class="lead">News from the foundation and the association – with photos, videos and further links.</p><div data-news-list></div>'),
           "artikel": ("News", '<h1>News</h1><div data-article></div>')},
}


def pages_for(lang, site):
    src = content_de.pages if lang == "de" else content_en.pages
    out = dict(src[site])
    for slug, (title, body) in EXTRA[lang].items():
        out[slug] = dict(title=title, body=body)
    return out


def rel(from_dir, to_path):
    return os.path.relpath(os.path.join(OUT, to_path), os.path.join(OUT, from_dir)) if from_dir else to_path


def render(lang, site, slug):
    s = SITES[site][lang]; t = T[lang]
    pg = pages_for(lang, site)[slug]
    d = DIR[(lang, site)]
    root = "../" * (d.count("/"))
    other_lang = "en" if lang == "de" else "de"
    other_site = "gdf" if site == "stiftung" else "stiftung"
    own = SITES[other_site][lang]
    # relative links
    def to(lang2, site2, slug2="index"):
        return os.path.relpath(os.path.join(OUT, DIR[(lang2, site2)], slug2 + ".html"), os.path.join(OUT, d)) if True else ""
    lang_href = to(other_lang, site, slug)
    stiftung_href = to(lang, "stiftung"); gdf_href = to(lang, "gdf")

    # split title out of body
    body = pg["body"].replace("{R}", root)
    m = re.search(r"<h1>(.*?)</h1>", body, re.S)
    h1 = m.group(1) if m else pg["title"]
    body = body.replace(m.group(0), "", 1) if m else body
    lead = ""
    m2 = re.search(r'<p class="lead">(.*?)</p>', body, re.S)
    if m2:
        lead = m2.group(1); body = body.replace(m2.group(0), "", 1)
    is_home = slug == "index"

    # side navigation
    nav = []
    for sl, lab, kids in s["nav"]:
        branch = sl == slug or any(k[0] == slug for k in kids) or (sl == "news" and slug == "artikel")
        cur = ' aria-current="page"' if (sl == slug or (sl == "news" and slug == "artikel")) else ""
        li = f'<li><a href="{sl}.html"{cur}>{lab}</a>'
        if kids and branch:
            li += "<ul>" + "".join(f'<li><a href="{k}.html"' + (' aria-current="page"' if k == slug else "") + f'>{kl}</a></li>' for k, kl in kids) + "</ul>"
        nav.append(li + "</li>")
    other_href = gdf_href if site == "stiftung" else stiftung_href
    nav_html = "<ul>" + "".join(nav) + "</ul>" + f'<a class="other" href="{other_href}">{own["name"]} <span aria-hidden="true">→</span></a>'

    seal = '<span class="seal" role="img" aria-label="Siegel der Universität Heidelberg"></span>'
    if site == "stiftung":
        b1, b2 = "Stiftung", "Universität Heidelberg"
    else:
        b1, b2 = "Gesellschaft der Freunde", "Universität Heidelberg e.V."
    brand = f'<a class="brand" href="index.html">{seal}<span class="brand-text"><b>{b1}</b><small>{b2}</small></span></a>'

    crumbs = f'<p class="eyebrow">{s["name"]}</p>'
    if is_home:
        stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in s["stats"])
        photo_src = "assets/img/stiftung/startseite_stiftung.jpg" if site == "stiftung" else "assets/img/gdf/540_gruppe.jpg"
        photo_alt = "Die Neue Universität in Heidelberg" if site == "stiftung" else "Mitglieder der Gesellschaft der Freunde"
        if lang == "en": photo_alt = "The Neue Universität in Heidelberg" if site == "stiftung" else "Members of the Gesellschaft der Freunde"
        hero = f'''<section class="hero hero-home">
  <div class="hero-copy">{crumbs}<h1>{s["tag"]}</h1><p class="lede">{lead}</p>
  <div class="actions"><a class="btn light" href="{s["cta"][1]}">{s["cta"][0]}</a><a class="btn outline-light" href="{s["cta2"][1]}">{s["cta2"][0]}</a></div></div>
  <div class="hero-visual"><img src="{root}{photo_src}" alt="{photo_alt}" width="1023" height="681" fetchpriority="high"></div>
  <div class="stats">{stats}</div></section>'''
    else:
        hero = f'''<section class="hero hero-page">{crumbs}<h1>{h1}</h1></section>'''
        if lead: body = f'<p class="lead">{lead}</p>' + body

    news_head = t["news"]
    aside = f'''<aside class="news" aria-label="{news_head}"><h2>{news_head}</h2><div data-news-aside data-limit="3"></div><a class="all" href="news.html">{t["all_news"]} →</a></aside>'''
    title_txt = (pg["title"] + " – " if not is_home else "") + s["name"]
    full_tag = html.escape(title_txt, quote=False)

    return f'''<!DOCTYPE html>
<html lang="{lang}" data-site="{site}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_tag}</title>
<meta name="description" content="{html.escape(s["desc"])}">
<meta name="theme-color" content="#b21f17">
<link rel="icon" href="{root}assets/img/uni-hd-seal.jpeg">
<link rel="stylesheet" href="{root}assets/style.css?v={V_CSS}">
</head>
<body data-root="{root}" data-lang="{lang}" data-site="{site}" data-page="{slug}">
<a class="skip" href="#inhalt">{t["skip"]}</a>
<div class="shell">
<header class="bar">
  {brand}
  <nav class="switch" aria-label="{t["switch_label"]}">
    <a href="{stiftung_href}"{' aria-current="true"' if site=="stiftung" else ""}>{T[lang]["site_short"]["stiftung"]}</a>
    <a href="{gdf_href}"{' aria-current="true"' if site=="gdf" else ""}>{T[lang]["site_short"]["gdf"]}</a>
  </nav>
  <div class="bar-right">
    <a class="lang" href="{lang_href}" hreflang="{other_lang}" lang="{other_lang}" aria-label="{t["lang_label"]}: {t["other_lang"]}"><span>{t["other_lang_code"]}</span></a>
    <a class="btn cta" href="{s["cta"][1]}">{s["cta"][0]}</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="sitenav"><span class="bars" aria-hidden="true"></span><span class="sr">{t["menu"]}</span></button>
  </div>
</header>
{hero}
<div class="layout">
  <nav class="side-nav" id="sitenav" aria-label="{t["nav_label"]}">{nav_html}</nav>
  <main id="inhalt">
{body}
  </main>
  {aside}
</div>
<div class="with-uni"><span>{t["with_uni"]}</span><img src="{root}assets/img/uni-hd-lockup-transparent.png" alt="Universität Heidelberg – Zukunft seit 1386" width="480" height="252" loading="lazy"></div>
<footer>
  <div class="foot-brand">{seal}<p><b>{s["name"]}</b><br>Marstallstraße 6 · 69117 Heidelberg<br><a href="mailto:{MAIL}">{MAIL}</a></p></div>
  <div class="foot-links"><a href="kontakt.html">{t["contact"]}</a><a href="impressum.html">{t["imprint"]}</a><a href="{UNI_DS}" target="_blank" rel="noopener">{t["privacy"]}</a><a href="{root}admin/" rel="nofollow">{t["authors"]}</a></div>
  <p class="volunteer">{t["volunteer"]}</p>
</footer>
</div>
<script src="{root}assets/main.js?v={V_JS}"></script>
</body>
</html>
'''


def main():
    n = 0
    for lang in ("de", "en"):
        for site in ("stiftung", "gdf"):
            d = os.path.join(OUT, DIR[(lang, site)])
            os.makedirs(d, exist_ok=True)
            for slug in pages_for(lang, site):
                with open(os.path.join(d, slug + ".html"), "w", encoding="utf-8") as f:
                    f.write(render(lang, site, slug))
                n += 1
    # the author panel is hand-written; only refresh its asset versions
    adm = os.path.join(OUT, "admin", "index.html")
    with open(adm, encoding="utf-8") as f:
        a = f.read()
    for name, v in (("../assets/style.css", V_CSS), ("../assets/main.js", V_JS),
                    ("admin.css", ver("admin/admin.css")), ("admin.js", ver("admin/admin.js"))):
        a = re.sub(r'"' + re.escape(name) + r'(\?v=[0-9a-f]+)?"', '"' + name + "?v=" + v + '"', a)
    with open(adm, "w", encoding="utf-8") as f:
        f.write(a)
    print("pages written:", n)


if __name__ == "__main__":
    main()
