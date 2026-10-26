/* Stiftung Universität Heidelberg / Gesellschaft der Freunde – Seitenverhalten und Artikelanzeige.
   Artikel liegen als JSON in content/articles/ und werden hier im Browser dargestellt.
   Die Funktionen in window.UH werden auch vom Autorenpanel (admin/) für die Vorschau benutzt. */
(function () {
  "use strict";
  var body = document.body;
  var ROOT = body.getAttribute("data-root") || "";
  var LANG = body.getAttribute("data-lang") || "de";
  var SITE = body.getAttribute("data-site") || "stiftung";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var I18N = {
    de: { stiftung: "Stiftung", gdf: "Gesellschaft der Freunde", both: "Stiftung & Freunde", read: "Weiterlesen", back: "← Alle Neuigkeiten",
          none: "Noch keine Artikel.", notfound: "Dieser Artikel wurde nicht gefunden.", links: "Weiterführende Links", gallery: "Fotos",
          video: "Video abspielen", videoNote: "Mit dem Klick wird das Video vom Anbieter geladen.", filterSite: "Diese Einrichtung", filterAll: "Alle", share: "Teilen", copied: "Link kopiert", copy: "Kopiert", err: "Kopieren nicht möglich" },
    en: { stiftung: "Foundation", gdf: "Friends’ Association", both: "Foundation & Friends", read: "Read more", back: "← All news",
          none: "No articles yet.", notfound: "This article could not be found.", links: "Further links", gallery: "Photos",
          video: "Play video", videoNote: "Clicking loads the video from the provider.", filterSite: "This organisation", filterAll: "All", share: "Share", copied: "Link copied", copy: "Copied", err: "Could not copy" }
  };
  var L = I18N[LANG] || I18N.de;

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function asset(p) { return /^(data:|blob:|https?:)/.test(p) ? p : ROOT + p; }
  function safeUrl(u) { u = String(u || "").trim(); return /^(https?:\/\/|mailto:)/i.test(u) ? u : ""; }

  /* ---- kleines Markdown: ## Überschrift, - Liste, **fett**, *kursiv*, [Text](URL) ---- */
  function inline(t) {
    t = esc(t);
    t = t.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (m, a, u) {
      var url = safeUrl(u.replace(/&amp;/g, "&")); return url ? '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + a + "</a>" : a;
    });
    t = t.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>").replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");
    return t;
  }
  function md(src) {
    var out = [], blocks = String(src || "").replace(/\r/g, "").split(/\n{2,}/);
    blocks.forEach(function (b) {
      b = b.trim(); if (!b) return;
      var lines = b.split("\n");
      if (/^###\s/.test(b)) out.push("<h3>" + inline(b.replace(/^###\s+/, "")) + "</h3>");
      else if (/^##\s/.test(b)) {
        out.push("<h2>" + inline(lines[0].replace(/^##\s+/, "")) + "</h2>");
        if (lines.length > 1) out.push(md(lines.slice(1).join("\n")));
      } else if (lines.every(function (l) { return /^[-*]\s+/.test(l); })) {
        out.push("<ul>" + lines.map(function (l) { return "<li>" + inline(l.replace(/^[-*]\s+/, "")) + "</li>"; }).join("") + "</ul>");
      } else out.push("<p>" + lines.map(inline).join("<br>") + "</p>");
    });
    return out.join("\n");
  }
  function fmtDate(d, lang) {
    var dt = new Date(d + "T12:00:00");
    if (isNaN(dt)) return d;
    return dt.toLocaleDateString(lang === "en" ? "en-GB" : "de-DE", { day: "numeric", month: "long", year: "numeric" });
  }
  function pick(obj, lang) { return (obj && (obj[lang] || obj[lang === "de" ? "en" : "de"])) || {}; }
  window.UH = { asset: asset, esc: esc, md: md, fmtDate: fmtDate, safeUrl: safeUrl, pick: pick };

  /* ---- Menü, Kopieren ---- */
  var toggle = $(".nav-toggle"), nav = $(".side-nav");
  if (toggle && nav) toggle.addEventListener("click", function () {
    var o = nav.classList.toggle("open"); toggle.setAttribute("aria-expanded", o);
  });
  function toast(m) { var e = document.createElement("div"); e.className = "toast"; e.setAttribute("role", "status"); e.textContent = m; document.body.appendChild(e); setTimeout(function () { e.remove(); }, 2200); }
  window.UH.toast = toast;
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-copy");
      (navigator.clipboard ? navigator.clipboard.writeText(v) : Promise.reject()).then(function () { toast(L.copy); }, function () { toast(L.err); });
    });
  });

  /* ---- Artikelliste ---- */
  function fetchJSON(path) {
    return fetch(ROOT + path + "?v=" + Date.now()).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); });
  }
  function forSite(list, all) { return list.filter(function (a) { return all || a.category === SITE || a.category === "both"; }); }
  function tagHtml(cat) {
    var labels = cat === "both" ? [L.stiftung, L.gdf] : [L[cat]];
    return labels.map(function (l, i) { var c = cat === "both" ? (i ? "gdf" : "stiftung") : cat; return '<span class="tag t-' + c + '">' + esc(l) + "</span>"; }).join(" ");
  }
  function card(a) {
    var c = pick(a, LANG);
    var img = a.cover ? '<img src="' + esc(asset(a.cover)) + '" alt="" loading="lazy">' : "";
    return '<a class="card" href="artikel.html?id=' + encodeURIComponent(a.id) + '">' + img + '<div class="c-body">' + tagHtml(a.category) +
      "<time datetime=\"" + esc(a.date) + "\">" + esc(fmtDate(a.date, LANG)) + "</time><h3>" + esc(c.title) + "</h3><p>" + esc(c.summary || "") + "</p></div></a>";
  }

  var indexPromise = null;
  function loadIndex() { return indexPromise || (indexPromise = fetchJSON("content/articles/index.json").then(function (j) { return (j.articles || []).slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; }); })); }

  var aside = $("[data-news-aside]");
  if (aside) loadIndex().then(function (list) {
    var items = forSite(list).slice(0, parseInt(aside.getAttribute("data-limit") || "3", 10));
    aside.innerHTML = items.length ? items.map(card).join("") : '<p class="empty">' + L.none + "</p>";
  }, function () { aside.innerHTML = ""; });

  var listBox = $("[data-news-list]");
  if (listBox) loadIndex().then(function (list) {
    var all = false;
    function draw() {
      var items = forSite(list, all);
      listBox.querySelector(".news-grid").innerHTML = items.length ? items.map(card).join("") : '<p class="empty">' + L.none + "</p>";
    }
    listBox.innerHTML = '<div class="filter"><button type="button" aria-pressed="true" data-f="site">' + L.filterSite + '</button><button type="button" aria-pressed="false" data-f="all">' + L.filterAll + '</button></div><div class="news-grid"></div>';
    $$(".filter button", listBox).forEach(function (b) {
      b.addEventListener("click", function () {
        all = b.getAttribute("data-f") === "all";
        $$(".filter button", listBox).forEach(function (x) { x.setAttribute("aria-pressed", x === b); });
        draw();
      });
    });
    draw();
  }, function () { listBox.innerHTML = '<p class="empty">' + L.none + "</p>"; });

  /* ---- Einzelner Artikel ---- */
  function videoHtml(v) {
    if (!v || !v.url) return "";
    var u = String(v.url), id;
    if (v.kind === "file") {
      if (!/^content\/media\/[\w.\-\/]+$/.test(u) || u.indexOf("..") > -1) return "";
      return '<div class="video"><video controls preload="metadata" src="' + esc(ROOT + u) + '"></video></div>';
    }
    var src = "";
    if (v.kind === "youtube") { id = (u.match(/(?:v=|youtu\.be\/|embed\/|shorts\/)([\w-]{11})/) || [])[1]; if (id) src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0"; }
    if (v.kind === "vimeo") { id = (u.match(/vimeo\.com\/(?:video\/)?(\d+)/) || [])[1]; if (id) src = "https://player.vimeo.com/video/" + id + "?autoplay=1&dnt=1"; }
    if (!src) return "";
    return '<div class="video" data-embed="' + esc(src) + '"><button type="button"><span class="play"><svg width="26" height="26" viewBox="0 0 24 24" fill="#1d0d00"><path d="M8 5v14l11-7z"/></svg></span>' + L.video + "<small>" + L.videoNote + "</small></button></div>";
  }
  function renderArticle(a, lang) {
    var c = pick(a, lang);
    var h = '<article class="article"><a class="back" href="news.html">' + L.back + "</a><div class=\"article-head\"><div class=\"meta\">" + tagHtml(a.category) +
      "<time datetime=\"" + esc(a.date) + "\">" + esc(fmtDate(a.date, lang)) + "</time></div><h2 class=\"a-title\">" + esc(c.title) + "</h2>" +
      (c.summary ? '<p class="a-sum">' + esc(c.summary) + "</p>" : "") + "</div>" +
      (a.cover ? '<img class="a-cover" src="' + esc(asset(a.cover)) + '" alt="">' : "") +
      '<div class="a-body">' + md(c.body) + "</div>" + videoHtml(a.video);
    if (a.images && a.images.length) {
      h += '<div class="gallery">' + a.images.map(function (im) {
        var cap = (im[lang] || im[lang === "de" ? "en" : "de"] || "");
        return "<figure><img src=\"" + esc(asset(im.src)) + "\" alt=\"" + esc(cap) + "\" loading=\"lazy\">" + (cap ? "<figcaption>" + esc(cap) + "</figcaption>" : "") + "</figure>";
      }).join("") + "</div>";
    }
    if (a.links && a.links.length) {
      h += "<h3>" + L.links + '</h3><ul class="links">' + a.links.map(function (l) {
        var url = safeUrl(l.url); if (!url) return "";
        return '<li><a href="' + esc(url) + '" target="_blank" rel="noopener">↗ ' + esc(l[lang] || l[lang === "de" ? "en" : "de"] || url) + "</a></li>";
      }).join("") + "</ul>";
    }
    return h + "</article>";
  }
  window.UH.renderArticle = renderArticle;
  function wireArticle(root) {
    $$(".video[data-embed]", root).forEach(function (v) {
      $("button", v).addEventListener("click", function () {
        v.innerHTML = '<iframe src="' + v.getAttribute("data-embed") + '" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>';
      });
    });
    $$(".gallery img", root).forEach(function (img) {
      img.addEventListener("click", function () {
        var lb = document.createElement("div"); lb.className = "lightbox"; lb.innerHTML = '<img alt="">'; lb.firstChild.src = img.src;
        lb.addEventListener("click", function () { lb.remove(); }); document.body.appendChild(lb);
      });
    });
  }
  window.UH.wireArticle = wireArticle;

  var art = $("[data-article]");
  if (art) {
    var id = (new URLSearchParams(location.search).get("id") || "");
    if (!/^[a-z0-9-]+$/.test(id)) art.innerHTML = '<p class="empty">' + L.notfound + "</p>";
    else fetchJSON("content/articles/" + id + ".json").then(function (a) {
      art.innerHTML = renderArticle(a, LANG); wireArticle(art);
      var t = pick(a, LANG).title; if (t) document.title = t + " – " + document.title.split(" – ").pop();
    }, function () { art.innerHTML = '<p class="empty">' + L.notfound + "</p>"; });
  }

  /* ---- Einblenden beim Scrollen ---- */
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .08 });
    $$("main > .fig, main > .box, main > .person, main > .photo, main > .timeline, main > table, main > h2").forEach(function (el) { el.classList.add("reveal"); io.observe(el); });
  }
})();
