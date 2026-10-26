"""German page content (Stiftung + Gesellschaft der Freunde). Rendered by build.py."""
MAIL = "freunde@uni-heidelberg.de"

pages = {"stiftung": {}, "gdf": {}}


def page(site, slug, title, body, banner=None):
    pages[site][slug] = dict(title=title, body=body, banner=banner)


def fig(img, alt, text):
    return f'<div class="fig"><img src="{{R}}assets/img/{img}" alt="{alt}" width="175" loading="lazy"><div>{text}</div></div>'


def person(initials, name, role, text=""):
    t = f"<br>{text}" if text else ""
    return f'<div class="person"><div class="avatar" aria-hidden="true">{initials}</div><p><span class="role">{role}</span><b>{name}</b>{t}</p></div>'


def photo(img, alt, cap):
    return f'<figure class="photo"><img src="{{R}}assets/img/{img}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>'


def bank(name, iban, bic, extra=""):
    raw = iban.replace(" ", "")
    ex = f'<tr><th>Verwendungszweck</th><td>{extra}</td></tr>' if extra else ""
    return f'''<table class="data"><tbody>
<tr><th>Empfänger</th><td>{name}</td></tr><tr><th>Bank</th><td>Deutsche Bank Heidelberg</td></tr>
<tr><th>IBAN</th><td><span class="iban">{iban}</span><button class="copy" data-copy="{raw}" type="button">Kopieren</button></td></tr>
<tr><th>BIC (SWIFT)</th><td><span class="iban">{bic}</span></td></tr>{ex}</tbody></table>'''


CONTACT = f'''<div class="person"><div class="avatar" aria-hidden="true">SP</div><p><span class="role">Geschäftsstellenleitung</span><b>Sabine zu Putlitz</b>Marstallstraße 6, Zimmer 018c · 69117 Heidelberg<br>Fon +49 (0)6221 54-3446 · Fax +49 (0)6221 54-3447<br><a href="mailto:sabine.putlitz@uni-heidelberg.de">sabine.putlitz@uni-heidelberg.de</a></p></div>
<div class="person"><div class="avatar" aria-hidden="true">CK</div><p><span class="role">Assistenz</span><b>Carl Kraus</b>Marstallstraße 6, Zimmer 002a · 69117 Heidelberg<br>Fon +49 (0)6221 54-19045 · Fax +49 (0)6221 54-3447<br><a href="mailto:{MAIL}">{MAIL}</a></p></div>'''
CREATOR = person("AB", "Arsenii Bazhenov", "Website", "Konzept, Gestaltung und Entwicklung dieser Website – auf freiwilliger Initiative, unentgeltlich und aus Freude an der Sache.")

# ================================================================= STIFTUNG
S = "stiftung"
page(S, "index", "Herzlich willkommen", '''
<h1>Herzlich willkommen!</h1>
<p class="lead">Wir freuen uns über Ihr Interesse an der Stiftung Universität Heidelberg, ihrer Geschichte und ihrem Wirken zum Wohle der Ruprecht-Karls-Universität Heidelberg, Deutschlands ältester Universität und einer der führenden Universitäten in Europa.</p>
<figure class="photo"><img src="{R}assets/img/stiftung/startseite_stiftung.jpg" alt="Die Neue Universität in Heidelberg mit der Inschrift „Dem lebendigen Geist“, davor Studierende auf den Stufen" width="1023" height="681"><figcaption>Foto: Christoph Bastert</figcaption></figure>
<p>Die Stiftung Universität Heidelberg wurde Ende 1984 zum bevorstehenden 600. Jubiläum der Ruperto Carola mit dem Ziel der Wissenschaftsförderung errichtet. Initiatoren der Stiftungsgründung waren der damalige Rektor Prof. Dr. Gisbert Freiherr zu Putlitz, der ehemalige Vorsitzende des VW-Vorstands Kurt Lotz und der Verfassungs- und Steuerrechtler Prof. Dr. Paul Kirchhof.</p>
<div class="actions"><a class="btn" href="spenden.html">Jetzt spenden</a><a class="btn ghost" href="idee.html">Unsere Idee</a><a class="btn ghost" href="preise.html">Ruprecht-Karls-Preise</a></div>
<div class="box"><h3>Partnerverein</h3><p>Gemeinsam mit der <a href="gdf/index.html">Gesellschaft der Freunde Universität Heidelberg e.V.</a> – dem Alumni- und Förderverein mit rund 1.400 Mitgliedern – teilt die Stiftung eine Geschäftsstelle im Marstallhof.</p></div>
''')

page(S, "idee", "Idee", '''
<h1>Idee</h1>
<blockquote class="box"><p>„Wann immer ein Mensch, die Wirtschaft, der Staat in eine Krise geraten, universitäres Wissen verspricht Hilfe; und daraus ergeben sich finanzwirtschaftliche Folgerungen.“</p><p class="credit">Paul Kirchhof, 1997</p></blockquote>
<p>Die Stiftung Universität Heidelberg hat es sich zur Aufgabe gemacht, die Bedingungen für die Mehrung und Vermittlung universitären Wissens in Heidelberg durch finanzielle Investitionen zu optimieren. Sie fördert deshalb die Ruprecht-Karls-Universität, ihre Mitglieder und Einrichtungen bei der Erfüllung ihrer vielfältigen Aufgaben in Forschung und Lehre.</p>
''' + fig("stiftung/175_stiftung_idee.jpg", "Titelseite der Satzung", '''<p>Die Stiftung Universität Heidelberg ist eine selbstständige Stiftung bürgerlichen Rechts. Sie verfolgt ausschließlich und unmittelbar gemeinnützige Zwecke. Die Stiftungsziele sind in der Satzung niedergelegt, die auch die Aufgaben der beiden Stiftungsorgane, <a href="personen.html">Vorstand</a> und <a href="kuratorium.html">Kuratorium</a>, beschreibt.</p>
<p><a class="btn alt" href="{R}assets/files/stiftung-satzung.pdf" target="_blank" rel="noopener">Satzung lesen (PDF)</a></p>''') + '''
<h2>Meilensteine</h2>
<div class="timeline">
<div><b>1984</b> – Errichtung der Stiftung zum bevorstehenden 600. Jubiläum der Ruperto Carola.</div>
<div><b>1990</b> – Erstmals werden die Ruprecht-Karls-Preise verliehen.</div>
<div><b>Mai 2000</b> – Kooperationsvereinbarung mit der Gesellschaft der Freunde.</div>
<div><b>2003</b> – Aktivitäten von Stiftung und Gesellschaft werden rechtlich weitgehend konzentriert.</div>
<div><b>2011</b> – Der von der Stiftung mitfinanzierte Innenhof der „Neuen Universität“ wird eröffnet.</div>
<div><b>Seit 2022</b> – Spendenaktion UniHD<i>hilft</i> für vom Krieg in der Ukraine betroffene Studierende und Forschende.</div>
</div>''')

page(S, "personen", "Personen", '''
<h1>Personen</h1>
<h2>Vorstand</h2>
''' + person("MV", "Dr. Monika Vierheilig", "Vorsitzende des Vorstands", "eh. Leiterin der Abteilung „Gesundheit“ im Ministerium für Soziales und Integration Baden-Württemberg")
+ person("TH", "PD Dr. Thorsten Helm", "Stellv. Vorsitzender", "Apl. Professor, Partner bei der KPMG AG, Tax")
+ person("TB", "Prof. Dr. Tanja Bipp", "Mitglied des Vorstands", "Professorin am Psychologischen Institut der Universität Heidelberg") + '''
<p>Die Arbeit des Vorstands wird von einem <a href="kuratorium.html">Kuratorium</a> beaufsichtigt, das auch die Aufgabe hat, den Vorstand bei der Erfüllung des Stiftungszwecks zu unterstützen.</p>
<h2>Geschäftsstelle</h2>
<p>Die Geschäftsstelle im Marstallhof führt das Tagesgeschäft und wird gemeinsam mit der Gesellschaft der Freunde betrieben.</p>''' + CONTACT + '<h2>Die Website</h2>' + CREATOR)

page(S, "kuratorium", "Kuratorium", '''
<h1>Kuratorium</h1>
<p>Das Kuratorium wird jeweils für eine Amtszeit von fünf Jahren gewählt und besteht aus Personen, die ihre Verbundenheit zum Zweck der Stiftung besonders dokumentiert haben. Die hier genannten Mitglieder wurden im Herbst 2021 gewählt. Wir sind traurig über den Verlust unseres hochgeschätzten Kurators Dr. Jobst Wellensiek, der im November 2022 verstarb.</p>
<div class="cols"><ul>
<li><b>Dr. Dominik von Achten</b><br>Vorstandsvorsitzender der HeidelbergCement AG</li>
<li><b>Dieter Berg</b><br>eh. Vorsitzender der Geschäftsführung der Robert Bosch Stiftung GmbH</li>
<li><b>Andrea Y. Combé</b><br>Rechtsanwältin, SFC Rechtsanwälte, Heidelberg</li>
<li><b>Prof. Dr. Dr. Jürgen Debus</b><br>Ärztlicher Direktor, Universitätsklinik für Radioonkologie und Strahlentherapie</li>
<li><b>Prof. Dr. Lutz Gade</b><br>Institut für Anorganische Chemie</li>
<li><b>Prof. Dr. Timo Goeschl</b><br>Alfred-Weber-Institut für Wirtschaftswissenschaften</li>
<li><b>Georg von Hohnhorst</b><br>Wirtschaftsprüfer, eh. Partner bei KPMG, Mannheim</li>
<li><b>Prof. Dr. Dieter Jahn</b><br>eh. Senior Vice President, BASF Gruppe</li>
</ul><ul>
<li><b>Prof. Dr. Selim Jochim</b><br>Physikalisches Institut</li>
<li><b>Prof. Dr. Hanno Kube</b><br>Institut für Finanz- und Steuerrecht</li>
<li><b>Dr. h.c. Manfred Lautenschläger</b><br>Ehrenvorsitzender des Aufsichtsrats der MLP SE</li>
<li><b>Dr. Michael Litterer</b><br>Geschäftsführung Franz Litterer GmbH &amp; Co KG, Weinheim</li>
<li><b>Prof. Dr. Stefan M. Maul</b><br>Seminar für Sprachen und Kulturen des Vorderen Orients</li>
<li><b>Markwart von Pentz</b><br>President, Worldwide Agriculture &amp; Turf Division, Deere &amp; Company, Mannheim</li>
<li><b>Dr. Wolfgang Niopek</b><br>eh. Stv. Hauptgeschäftsführer IHK Rhein-Neckar</li>
<li><b>Dr. Volker Reimann-Dubbers</b><br>Vorsitzender des Stiftungsrats der VRD Stiftung für erneuerbare Energien</li>
<li><b>Dr. Christopher Sessar</b><br>Chief Accounting Officer der SAP SE, Walldorf</li>
</ul></div>''')

page(S, "partner", "Partner", '''
<h1>Partner</h1>
<p>Die Stiftung Universität Heidelberg schloss im Mai 2000 mit der Gesellschaft der Freunde Universität Heidelberg e.V. eine Kooperationsvereinbarung. Ein Anliegen dieser Kooperation ist es, gemeinsame Ziele wie z. B. die Förderung von Forschung und Lehre an der Universität Heidelberg noch besser verfolgen zu können.</p>
<p>In 2003 haben die Stiftung Universität Heidelberg und die Gesellschaft der Freunde ihre Aktivitäten rechtlich soweit wie zulässig konzentriert. Durch eine weitgehend personengleiche Besetzung ihrer Vorstände und eine gemeinsame Geschäftsstelle können die beiden Einrichtungen seitdem „als Einheit auftreten und handeln“ (Präambel der Satzung der Gesellschaft der Freunde).</p>
''' + fig("stiftung/175_stiftung_partner.jpg", "Gemeinsame Vorstandssitzung", '<p><b>Partner in allen Belangen</b></p><p>In regelmäßigen Abständen werden die Angelegenheiten der Stiftung und des Vereins bei gemeinsamen Vorstandssitzungen beraten.</p><p><a href="gdf/index.html">Zur Gesellschaft der Freunde →</a></p>'))

page(S, "aktivitaeten", "Aktivitäten", '''
<h1>Aktivitäten</h1>
<p>Die Stiftung vergibt Preise an junge Nachwuchswissenschaftler:innen und fördert Maßnahmen, die vor Ort in Heidelberg die Bedingungen für einen regen wissenschaftlichen Austausch der Universitätsmitglieder untereinander und mit Gästen ausländischer Hochschulen optimieren. Sie initiiert darüber hinaus Aktionen zur Einwerbung von finanziellen Mitteln, um der Universität mit Zuschüssen für größere Projekte helfen zu können.</p>
''' + fig("stiftung/175_kant.jpg", "Immanuel Kant", '<p><b>Kant 2024</b><br>Zum 300. Geburtstag von Immanuel Kant förderte die Stiftung im Januar 2024 eine Seminarreihe mit dem Philosophen Omri Boehm zum Geist der Aufklärung und lud im März 2024 zum gemeinsamen Besuch der Bonner Ausstellung „Kant und die offenen Fragen“ ein.</p>')
+ fig("stiftung/175_stiftung_aktivitaeten_1.jpg", "Preisverleihung", '<p><b>Ruprecht-Karls-Preise</b><br>Mit den Ruprecht-Karls-Preisen will die Stiftung die Leistung junger talentierter Wissenschaftler:innen herausstellen und diese dazu motivieren, ihre akademische Laufbahn fortzusetzen. Die Preise werden für herausragende wissenschaftliche Arbeiten aus allen Themenbereichen vergeben.</p><p><a href="preise.html">Mehr zu den Preisen →</a></p>')
+ fig("stiftung/UniHDhilft-Karte.jpg", "Postkarte der Aktion UniHDhilft", '<p><b>Aktion „UniHD<i>hilft</i>“</b><br>Aus Anlass des Putin-Kriegs unterstützt die Stiftung gemeinsam mit Kolleg:innen aus den Serviceeinrichtungen und wissenschaftlichen Instituten der Universität Heidelberg Studierende, Studieninteressierte und Nachwuchswissenschaftler:innen, die aus der Ukraine flüchten mussten und hier eine neue akademische Heimat suchen.</p><p><a href="spenden.html">Spenden &amp; Mitwirken →</a></p>')
+ '''<div class="box"><p><b>Have your studies or research been disrupted by the war in Ukraine?</b> UniHD<i>hilft</i> supports students and junior researchers from Ukraine who want to continue their work or studies at Heidelberg University. Contact us at <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a>.</p></div>''')

page(S, "preise", "Preise", '''
<h1>Preise</h1>
<p>Die Stiftung verleiht seit 1990 die Ruprecht-Karls-Preise. Sie würdigt mit den Preisen junge Nachwuchswissenschaftler:innen der Universität Heidelberg, die eine herausragende Forschungsleistung erbracht haben. Ausgezeichnet werden in der Regel die jährlich fünf besten Doktorarbeiten. Dabei berücksichtigt das mehrstufige, universitätsweite Auswahlverfahren wissenschaftliche Erstlingswerke aus allen Fächern.</p>
<p>Die Entscheidung trifft eine Jury, die auf Vorschlag der Rektorin vom Vorstand der Stiftung berufen wird. Die Jury unter dem Vorsitz von Prof. Dr. Rohini Kuner entscheidet auf der Grundlage von Vorschlägen der Fakultäten. <strong>Individuelle Bewerbungen sind nicht möglich.</strong></p>
<h2>Preisverleihung 2025</h2>
<p>Am 24. Oktober 2025 wurden die Preise in der Alten Aula der Universität verliehen – mit je 3.000 € dotiert. Ausgezeichnet wurden:</p>
<ul class="winners"><li>Dr. Nicole Sara Colaianni (Geschichte)</li><li>Dr. Julia Lemp (Global Health)</li><li>Dr. Letitia Parcalabescu (Computerlinguistik)</li><li>Dr. Felix Draxler (Informatik und Mathematik)</li><li>Dr. Lukas Maximilian Sigmund (Chemie)</li></ul>
<p><b>Fritz-Grunebaum-Preis:</b> Dr. Sina Allgeier (Rechtswissenschaft)</p>
<h2>Preisverleihung 2024</h2>
<ul class="winners"><li>Dr. Lynton Ardizzone (Informatik)</li><li>Dr. Ioannis Sarropoulos (Biowissenschaften)</li><li>Dr. Friederike Ihssen (Physik)</li><li>Dr. Norina Ullmann (Theologie)</li><li>Dr. Philipp Mai (Politikwissenschaft)</li></ul>
<p><b>Fritz-Grunebaum-Preis:</b> Dr. Nina Benz (Rechtswissenschaft)</p>
<h2>Preisträgertreffen</h2>
<p>Nach dem ersten Treffen im November 2019 kamen ehemalige Preisträger:innen vom 25. bis 27. Oktober 2024 erneut in Heidelberg zusammen – mit Preisverleihung, Kurzvorträgen früherer Preisträger:innen, einem Ausflug zur Sternwarte und viel Networking unter dem Motto „Auf ein Wiedersehen!“.</p>
<p class="credit">Insgesamt wurden seit 1990 über 190 Personen ausgezeichnet (Quelle: Pressemitteilung der Universität Heidelberg, 20. Oktober 2025).</p>''')

page(S, "projekte", "Projekte", '''
<h1>Projekte</h1>
<p>Viele Vorhaben der Universität sind auf finanzielle Unterstützung angewiesen. Die Stiftung hat sich in den letzten Jahren für folgende größere Projekte eingesetzt:</p>
<h2>1. Heidelberger Stiftungssymposium (2018)</h2>
<p>Mit dem Symposium wollte die Stiftung den internationalen und fachübergreifenden wissenschaftlichen Austausch zu gesellschaftlich relevanten Themen anstoßen und fördern. Es fand im Internationalen Wissenschaftsforum Heidelberg statt – mitten in der Altstadt, mit attraktivem Ambiente für den Gedankenaustausch zwischen Heidelberger Wissenschaftler:innen und ihren Gästen aus dem Ausland.</p>
<h2>Neuer Innenhof für die „Neue Universität“</h2>
''' + fig("stiftung/175_stiftung_projekte_3.jpg", "Innenhof der Neuen Universität", '''<p>Zum 625. Geburtstag der Universität gab es ein Geschenk: Die Stiftung hatte für die Modernisierung der „Neuen Universität“ Spenden gesammelt, die es ermöglichten, auch den begrünten Innenhof des Hörsaalgebäudes in das Modernisierungskonzept einzubinden. Ziel war es, den Innenhof als Außenraum sichtbarer und als Aufenthaltsort attraktiver zu machen. Insgesamt <strong>250.000 Euro</strong> brachten Kuratoren, Vorstand und Freunde der Stiftung zusammen.</p>
<p>Das Gebäude und sein Innenhof wurden nach fast zweijähriger Umbauphase am 25. Juni 2011 feierlich wiedereröffnet. <a href="http://625.uni-heidelberg.de/md/kampagnen/625jahre/festschrift_neue_universitaet.pdf" target="_blank" rel="noopener">Festschrift der Universität (PDF)</a></p>'''))

page(S, "spenden", "Spenden", '''
<h1>Spenden</h1>
<p>Die Stiftung Universität Heidelberg ist dankbar für die vielfältigen Formen der Unterstützung, die sie in der Vergangenheit erfahren hat. Ob kleine oder große, einmalige oder regelmäßige Spenden: Jede Geste finanziellen Engagements stärkt unsere Aktivitäten zum Wohle der Ruperto Carola.</p>
<h2>UniHD<i>hilft</i> – Spenden für geflüchtete Studierende und Forscher:innen</h2>
<p>Aus Anlass des Kriegs in der Ukraine hat die Stiftung gemeinsam mit <a href="mitwirken.html">Kolleg:innen und Mitarbeiter:innen</a> aus den universitären Serviceeinrichtungen und wissenschaftlichen Instituten eine Unterstützungsaktion gestartet.</p>
<p>Auch in Heidelberg sind viele Geflüchtete aus der Ukraine angekommen, unter ihnen Studierende, Nachwuchswissenschaftler:innen und Forscher:innen, die an der Universität Heidelberg eine akademische Heimat suchen oder vor kurzem gefunden haben. Der Krieg hat ihnen und ihren Familien fast alles genommen; geblieben ist die Hoffnung, ihre Studieninteressen und wissenschaftlichen Ambitionen in Heidelberg verwirklichen zu können.</p>
<p>Damit die Teilhabe am akademischen Leben schnell gelingt, soll ein Starthilfe-Programm die finanziellen Hürden aus dem Weg räumen. Spenden werden benötigt, um z. B. Lernmaterialien, Sprachkurse, Tutorien, Lern- und Begegnungsräume oder die Übersetzungskosten für ukrainische Zeugnisse und Gutachten zu bezahlen. Zudem sollen sie mehrmonatige Studien- und Forschungsstipendien ermöglichen, die die Zeit bis zu einer gesicherten Selbstfinanzierung überbrücken. Neben Geldspenden sind auch <a href="mitwirken.html">Zeitspenden</a> sehr willkommen.</p>
<div class="actions"><a class="btn" href="https://www.betterplace.org/de/projects/107929" target="_blank" rel="noopener">Online spenden über betterplace ↗</a></div>
<h2>Spendenkonto für direkte Geldspenden</h2>
''' + bank("Stiftung Universität Heidelberg", "DE08 6727 0003 0033 7337 00", "DEUTDESM672", "UniHDhilft") + '''
<p class="credit">Fragen zu Spendenbescheinigungen beantwortet die Geschäftsstelle: <a href="kontakt.html">Kontakt</a>.</p>''')

page(S, "mitwirken", "Mitwirken", '''
<h1>Mitwirken</h1>
''' + fig("stiftung/team_mitwirken.jpg", "Das Team von UniHDhilft", '''<p>Die Spendenaktion UniHD<i>hilft</i> ist eine Initiative von Mitarbeiter:innen, die den Bedarf an Unterstützung ukrainischer Studierender und Nachwuchswissenschaftler:innen im Arbeitsalltag erleben. Das Team kommt aus verschiedenen Instituten (u. a. Slavistik, Osteuropäische Geschichte, Soziologie, Psychologie, Theologie, Finanz- und Steuerrecht), Serviceeinrichtungen wie dem Studierendenwerk Heidelberg sowie der Stiftung und der Gesellschaft der Freunde.</p>''') + '''
<h2>Zum Team gehören</h2>
<p>Dr. Marlene Bainczyk-Crescentini, Dr. Stefan Beljean, Jonas Dinkelaker, Dr. Felicitas Fischer von Weikersthal, Prof. Dr. Joachim Funke, PD Dr. Thorsten Helm, Dr. Bettina Kaibach, PD Dr. Stefaniya Ptashnyk, Sabine zu Putlitz, PD Dr. Franziska Schedewie, Dr. Ivan Sablin, PD Dr. Karoline Thaidigsmann, Kristian Willenbacher</p>
<h2>Mentorship-Programm</h2>
<p>Das Mentorship-Programm von UniHD<i>hilft</i> geht über die finanzielle Unterstützung hinaus und hilft Geflüchteten, ihren Platz in der Heidelberger Gemeinschaft zu finden. Jede:r Stipendiat:in wird mit einer:m Heidelberger Studierenden oder Nachwuchswissenschaftler:in zusammengebracht, der oder die bei den ersten Schritten hilft – bei der Immatrikulation, der Suche nach dem Hörsaal, der Mensa-Karte oder der Wohnungssuche. Wir hoffen, dass daraus dauerhafte Freundschaften entstehen.</p>
<div class="box"><p><b>Möchten Sie mitwirken?</b> Zum Beispiel als Mentor:in oder durch eine Zeitspende? Sprechen Sie uns an: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p></div>''')

page(S, "kontakt", "Kontakt", '''
<h1>Kontakt</h1>
<p>Wir freuen uns über Ihr Interesse an unseren Aktivitäten und darauf, mehr über Sie zu erfahren. Schreiben Sie uns, rufen Sie an oder kommen Sie einfach vorbei, wenn Sie in Heidelberg sind.</p>
''' + CONTACT + '''
<h2>Unterstützungsaktion UniHD<i>hilft</i></h2>
''' + person("SB", "Dr. Stefan Beljean", "Ansprechperson UniHDhilft", "eh. Akademischer Mitarbeiter am Max-Weber-Institut für Soziologie. Er sorgt dafür, dass UniHDhilft bekannt wird, und freut sich über Anregungen.") + '''
<h2>Bankverbindung</h2>
''' + bank("Stiftung Universität Heidelberg", "DE08 6727 0003 0033 7337 00", "DEUTDESM672") + '''
<div class="actions"><a class="btn" href="mailto:''' + MAIL + '''">E-Mail schreiben</a></div>''')

page(S, "impressum", "Impressum", '''
<h1>Impressum</h1>
<h2>Verantwortlich für den Inhalt</h2><p>Stiftung Universität Heidelberg</p>
<h2>Vertretungsberechtigter Vorstand</h2><p>Dr. Monika Vierheilig (Vorsitz)<br>PD Dr. Thorsten Helm (stellv. Vorsitzender)</p>
<h2>Redaktion</h2><p>Sabine zu Putlitz (Geschäftsstelle)</p>
<h2>Website</h2><p>Konzept, Gestaltung und Entwicklung: Arsenii Bazhenov (ehrenamtlich, auf freiwilliger Initiative)</p>
<h2>Fotonachweis</h2><p>Stiftung Universität Heidelberg · Universität Heidelberg, Kommunikation &amp; Marketing · Christoph Bastert</p>
<h2>Besucher- und Lieferanschrift</h2><p>Marstallstraße 6, 69117 Heidelberg<br>Fon +49 (0)6221 54-3446 · Fax +49 (0)6221 54-3447<br>Mail: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p>
<h2>Weitere Informationen</h2><p>Regierungspräsidium Karlsruhe, Stiftungsverzeichnis<br>Finanzamt Heidelberg, Steuernummer 2832/10421/1</p>
<h2>Haftungsausschluss</h2>
<p>Die Stiftung Universität Heidelberg stellt auf dieser Website Informationen zur Verfügung, die regelmäßig aktualisiert werden. Aufgrund der technischen Merkmale des Internets kann jedoch keine Haftung für Vollständigkeit und Richtigkeit übernommen werden.</p>
<p>Diese Website enthält Links zu Internetseiten anderer Anbieter. Für deren Inhalte sind ausschließlich die jeweiligen Betreiber verantwortlich.</p>''')

# ================================================================= GDF
G = "gdf"
page(G, "index", "Herzlich willkommen", '''
<h1>Herzlich willkommen!</h1>
<p class="lead">Nehmen Sie uns ruhig beim Wort! Wir sind nicht nur mit dem Verstand, sondern auch mit dem Herzen bei der Sache, wenn es darum geht, interessierten Ehemaligen, Freunden und Förderern der Universität Heidelberg einen angenehmen Rahmen für ihre Kontakte untereinander und zu ihrer Alma Mater zu bieten.</p>
''' + fig("gdf/175_team.jpg", "Das Team der Geschäftsstelle", '<p>Als gemeinnütziger Förderverein gestalten und unterstützen wir seit vielen Jahren den Dialog und Erfahrungsaustausch mit allen, die sich der Ruprecht-Karls-Universität Heidelberg und der Stadt, die seit über 625 Jahren ihre Heimat bildet, verbunden fühlen. Dabei arbeiten wir Hand in Hand – und seit 2010 auch Tür an Tür – mit <i>Heidelberg Alumni International</i>, dem weltumspannenden Alumni-Netzwerk der <i>Ruperto Carola</i>.</p>') + '''
<figure class="photo"><img src="{R}assets/img/gdf/540_gruppe.jpg" alt="Mitglieder der Gesellschaft der Freunde in einer Gruppe" width="596" height="387"><figcaption>Foto: Christoph Bastert PHOTOGRAPHIE</figcaption></figure>
<p>Haben auch Sie ein Herz für die Universität Heidelberg? Egal, auf welche Weise Sie sich der alten, aber quicklebendigen Dame <i>Ruperto Carola</i> verbunden fühlen – sei es durch das Studium, die Promotion, den Beruf oder einfach durch die Liebe zur Stadt –, mit einer Mitgliedschaft in der <strong>Gesellschaft der Freunde Universität Heidelberg e.V.</strong> können Sie dieser Verbundenheit sichtbar Ausdruck verleihen.</p>
<div class="actions"><a class="btn" href="werden.html">Mitglied werden</a><a class="btn ghost" href="veranstaltungen.html">Veranstaltungen</a><a class="btn ghost" href="idee.html">Unsere Idee</a></div>''')

page(G, "idee", "Idee", '''
<h1>Idee</h1>
<p>Die Gesellschaft der Freunde Universität Heidelberg e.V. hat es sich zur Aufgabe gemacht, gemeinsam mit ihren <a href="partner.html">Partnern</a> ein Netzwerk aufzuspannen, das in mehrfacher Hinsicht tragfähig ist: Es verbindet die Alumni miteinander und mit ihrer Universität, fördert den Erfahrungsaustausch der Universität mit ihren Freunden in Wirtschaft und Kultur und bündelt das ideelle und materielle Engagement für universitäre Projekte und Anliegen, die ohne Unterstützung von außen nicht realisierbar wären.</p>
<p>Die Gesellschaft wurde 2003 gegründet. Sie ist ein gemeinnütziger, beim Registergericht Heidelberg eingetragener Verein mit Unterabteilungen (<a href="sektionen.html">Sektionen</a>) auf Fakultäts- und Institutsebene.</p>
''' + fig("gdf/gdf_satzung.jpg", "Titelseite der Vereinssatzung", '<p>Die Satzung ist die schriftlich niedergelegte Verfassung unseres Vereins. Sie benennt u. a. die Vereinsziele, die Aufgaben der Mitgliederversammlung und gibt in ihrer Präambel Auskunft über die Rechtsvorgänger der Gesellschaft.</p><p><a class="btn alt" href="{R}assets/files/gdf_satzung.pdf" target="_blank" rel="noopener">Satzung lesen (PDF)</a></p>') + '''
<p>Die Gesellschaft ist 2003 aus dem Zusammenschluss des <i>Vereins der Freunde der Universität Heidelberg e.V.</i> und der <i>Universitäts-Gesellschaft Heidelberg e.V.</i> entstanden.</p>''')

page(G, "personen", "Personen", '''
<h1>Personen</h1>
<h2>Vorstand</h2>
''' + person("TH", "PD Dr. Thorsten Helm", "Vorsitzender", "Partner bei der KPMG AG, Tax")
+ person("JF", "Prof. Dr. Joachim Funke", "Stellv. Vorsitzender", "Psychologisches Institut der Universität Heidelberg")
+ person("MV", "Dr. Monika Vierheilig", "Stellv. Vorsitzende", "eh. Leiterin der Abteilung „Gesundheit“ im Ministerium für Soziales und Integration Baden-Württemberg")
+ person("TB", "Prof. Dr. Tanja Bipp", "Mitglied des Vorstands", "Professorin am Psychologischen Institut der Universität Heidelberg") + '''
<p>Der Rektor bzw. die Rektorin der Universität Heidelberg und die Leitung des Universitätsdezernats Stiftungen und Vermögen sind Vorstandsmitglieder von Amts wegen.</p>
<h2>Geschäftsstelle</h2>''' + CONTACT + '<h2>Die Website</h2>' + CREATOR)

page(G, "partner", "Partner", '''
<h1>Partner</h1>
<blockquote class="box"><p>„Zusammenkommen ist ein Beginn, zusammenbleiben ist ein Fortschritt, zusammenarbeiten ist ein Erfolg.“</p><p class="credit">Henry Ford</p></blockquote>
<p>Die Gesellschaft der Freunde Universität Heidelberg e.V. ist der Rechtsnachfolger zweier traditionsreicher Vereine, die bereits im Mai 2000 mit der <a href="../index.html">Stiftung Universität Heidelberg</a> eine Kooperationsvereinbarung schlossen. Ein Anliegen dieser bis heute gültigen Vereinbarung ist es, gemeinsame Ziele wie die Förderung von Forschung und Lehre noch besser verfolgen zu können.</p>
<p>In 2003 haben die Gesellschaft und die Stiftung ihre Aktivitäten rechtlich soweit wie zulässig konzentriert. Durch eine weitgehend personengleiche Besetzung ihrer Vorstände und eine gemeinsame Geschäftsstelle können sie seitdem „als Einheit auftreten und handeln“ (Präambel der Vereinssatzung).</p>
''' + fig("gdf/teamsitzung.jpg", "Teamsitzung", '<p>Ein weiterer Partner unseres Vereins ist <i><a href="http://www.alumni.uni-heidelberg.de" target="_blank" rel="noopener">Heidelberg Alumni International</a></i>. Gemeinsam arbeiten wir daran, das bestehende Ehemaligen-Netzwerk auszubauen und lose Verbindungen der Alumni zur Universität in feste und nachhaltig positive Beziehungen zu verwandeln – damit aus Alumni Freunde werden.</p>'))

page(G, "aktivitaeten", "Aktivitäten", '''
<h1>Aktivitäten</h1>
<p>Die Aktivitäten der Gesellschaft der Freunde sind so vielfältig wie ihre Aufgaben. Hier ein kurzer Überblick.</p>
''' + fig("gdf/175_aktivitaeten_1.jpg", "Veranstaltung", '<p><b>Veranstaltungen</b><br>Begegnungen brauchen Anlässe. Damit unsere Mitglieder miteinander und mit der Universität im Gespräch bleiben, organisieren wir Vorträge, Ehemaligen-Treffen, Lesungen oder Exkursionen unter fachkundiger Führung. Und natürlich laden wir einmal jährlich im Sommer zum <a href="veranstaltungen.html">Tag der Freunde</a> ein.</p>')
+ fig("gdf/175_aktivitaeten_2.jpg", "Sektionen", '<p><b>Sektionen</b><br>In unseren bislang sieben Sektionen entwickeln die Sektionsleiter, zumeist aktive Heidelberger Professor:innen und Alumni, fachspezifische Kontakt- und Informationsangebote. <a href="sektionen.html">Mehr zu den Sektionen →</a></p>')
+ fig("gdf/scheck.jpg", "Scheckübergabe", '<p><b>Fördern</b><br>„Ohne Moos, nichts los.“ Wir suchen und finden großherzige Unterstützer und Partner, die uns beim Helfen helfen – von der Alumni-Arbeit bis zur Digitalisierungswerkstatt der Universitätsbibliothek. <a href="foerdern.html">Mehr →</a></p>')
+ fig("gdf/ueberreichung.jpg", "Preisübergabe", '<p><b>Preise</b><br>Gute Ideen und besondere Leistungen studentischer Gruppen, einzelner Studierender sowie junger Wissenschaftler:innen verdienen Anerkennung – mit dem <a href="preise.html">Preis der Freunde</a> sowie individuellen Beihilfen und Zuschüssen zu studentischen Vorhaben.</p>'))

page(G, "veranstaltungen", "Veranstaltungen", '''
<h1>Veranstaltungen</h1>
<p>Mitglieder der Gesellschaft der Freunde werden regelmäßig zu Veranstaltungen eingeladen, die der Verein, zum Teil zusammen mit seinen Partnern, ausrichtet. Einen festen Termin im Jahreskalender bildet der <strong>Tag der Freunde</strong>: alljährlich an einem Freitag Ende Juni oder Anfang Juli.</p>
<h2>Tag der Freunde 2026</h2>
<p>Am <strong>24. Juli 2026</strong> trafen sich die Universitätsfreunde im Internationalen Wissenschaftsforum Heidelberg in der Altstadt.</p>
<div class="timeline"><div><b>16:00 Uhr</b> – Mitgliederversammlung</div><div><b>ca. 17:15 Uhr</b> – Verleihung des Preises der Freunde, anschließend Umtrunk auf der Terrasse</div><div><b>ab 18:00 Uhr</b> – gemeinsamer Gang zur Sommerparty der Universität im Marstallhof</div></div>
<h2>Tag der Freunde 2025</h2>
<p>Am Freitag, 4. Juli 2025, lud die Gesellschaft ins Hotel Königstuhl: Mitgliederversammlung (16:30 Uhr), Vortrag „Neue Gentherapien revolutionieren die Krebsmedizin“ von Prof. Dr. Carsten Müller-Tidow, Ärztlicher Direktor der Medizinischen Klinik für Hämatologie, Onkologie und Rheumatologie (18:15 Uhr), Verleihung des „Preises der Freunde“ (19:15 Uhr) und anschließend Sommerfest mit Blick auf Heidelberg und den Neckar.</p>
<h2>Neujahrsempfang</h2>
<p>Seit einigen Jahren lädt die Gesellschaft ihre Mitglieder im Januar zu einem Vortrag mit anschließendem Empfang ein. Am 10. Januar 2025 sprach Prof. Dr. Anne Peters vom Max-Planck-Institut für ausländisches öffentliches Recht und Völkerrecht über „Schöne neue Weltordnung? Völkerrecht im Umbruch“.</p>
<h2>Universitätsfreunde unterwegs</h2>
<p>Themenausflüge dorthin, wo einflussreiche aktive oder ehemalige Heidelberger Universitätsangehörige wohnen oder arbeiten, und zu Orten, Institutionen und Unternehmen, die in Wirtschaft, Kultur, Politik, Kunst oder Wissenschaft eine bedeutende Rolle spielen.</p>
<ul><li>Europa in Straßburg, Mai 2018</li><li>Das alte neue Potsdam, April 2017 – u. a. Geoforschungszentrum im Albert-Einstein-Wissenschaftspark und Palais Barberini</li><li>Paris – historisch erfahren, April 2016</li><li>Die Deutsche Bundesbank – mehr als nur eine Bank, Oktober 2015</li><li>Babylon in Berlin, April 2015</li></ul>''')

page(G, "preise", "Preis der Freunde", '''
<h1>Preis der Freunde</h1>
<p>Seit 1995 vergibt die Gesellschaft der Freunde jährlich den mit <strong>2.500 €</strong> dotierten „Preis der Freunde“ an studentische Gruppen, die mit einer herausragenden Initiative hervorgetreten sind. Die Liste der bisherigen Preisträger steht für außergewöhnliches studentisches Engagement.</p>
<div class="box"><h3>Ausschreibung</h3><p>Ihr seid Studierende an der Universität Heidelberg und habt ein Projekt oder eine Initiative gestartet, die für andere Studis, ein Institut, eine Fakultät oder das studentische Leben außerhalb der Curricula von Bedeutung ist? Dann bewerbt euch! Die Ausschreibung läuft jedes Jahr im Frühjahr; für 2026 endete die Frist am 4. Mai 2026. Das Plakat der letzten Ausschreibung (2025): <a href="{R}assets/files/preisderfreunde2025.pdf" target="_blank" rel="noopener">PDF</a></p></div>
<h2>Preisträgerinnen 2025: Cheaper than therapy run club</h2>
<p>Der Cheaper than therapy run club ist Heidelbergs erster Social Run Club. Gegründet von vier Zahnmedizinstudentinnen, bietet die Initiative Studierenden durch wöchentliche Lauftreffs und weitere Aktionen ein niedrigschwelliges und regelmäßiges Angebot zur gemeinsamen Bewegung und Begegnung. Mit ihrem Fokus auf mentale Gesundheit macht sie auf ein Thema aufmerksam, das im universitären Alltag häufig zu kurz kommt.</p>
<h2>Preisträger 2024: StudyTutors Heidelberg</h2>
''' + photo("gdf/544_studytutors.jpg", "Preisübergabe an StudyTutors Heidelberg", "Foto: Christoph Bastert PHOTOGRAPHIE") + '''
<p>StudyTutors Heidelberg ist mit ca. 100 engagierten Studierenden Teil eines bundesweit aktiven Vereins, der Schüler:innen aus sozial bzw. finanziell schwächeren Verhältnissen durch kostenfreien, studentisch organisierten Nachhilfeunterricht hilft. Die Preisverleihung fand am 12. Juli 2024 im Rahmen des Tags der Freunde statt.</p>
<h2>Preisträger 2022: „Situs Inversus – Der Vorklinik-Podcast“</h2>
<p>Im Sommer 2020 von fünf Studierenden der Humanmedizin als ehrenamtliches Projekt gegründet: ein Podcast im Stile eines Tutoriums, der die wesentlichen Themen der medizinischen Vorklinik aus studentischer Sicht erläutert. Die Preisverleihung fand am 21. Juli 2023 statt.</p>
<h2>Weitere Preisträger seit 1995</h2>
<ul class="chips">
<li>MediNetz Rhein-Neckar</li><li>Match4healthcare</li><li>Chancen gestalten Heidelberg</li><li>Querfeldein Heidelberg</li><li>Heidelberger Lupe</li><li>Weitblick Heidelberg</li><li>ROCK YOUR LIFE! Heidelberg</li><li>Pro Bono Heidelberg</li><li>HCWK</li><li>HIIK</li><li>artefakt</li><li>ikulE</li><li>Interdisziplinäres Forum</li><li>Delta – The Philosophers Club</li><li>Forum für Kritische Theorie</li><li>RadioAktiv</li><li>StudzR</li><li>Gärtnerei Wildwuchs</li><li>Praktikumsinitiative Geografie</li><li>Romanischer Keller</li><li>Sozialhandbuch der Fachschaften</li><li>ruprecht</li><li>Nightline</li><li>Anatomie am Lebenden</li><li>Die Anstifter</li><li>URRmEL</li><li>Theatergruppe Anglistik</li><li>Emsa Heidelberg</li></ul>''')

page(G, "foerdern", "Fördern", '''
<h1>Fördern</h1>
<p>Jede Universität braucht Freunde, die sie bei der Erfüllung ihrer Aufgaben in Forschung und Lehre unterstützen. Die Gesellschaft setzt sich mit Hilfe ihrer Mitglieder für Vorhaben und Projekte ein, die an der Ruprecht-Karls-Universität entstehen und deren Studierenden, Lehrenden und Einrichtungen zugutekommen.</p>
<p>Unsere Förderaktivitäten konzentrieren sich auf die Unterstützung von Studierenden und studentischen Initiativen, fachübergreifende Projekte zentraler Einrichtungen und den Ausbau der Alumni-Arbeit.</p>
<h2>Außergewöhnliche, fachübergreifende Projekte</h2>
<p>Dazu zählt z. B. die <strong>Digitalisierungswerkstatt</strong>, mit der Deutschlands älteste Universitätsbibliothek das kulturelle Erbe an frühen Drucken und Handschriften nicht nur bewahren, sondern der Wissenschaft und Öffentlichkeit zugänglich machen kann. Buchtisch, Scanner und Kamera wurden aus Vereinsmitteln finanziert.</p>
<h2>Studierende und studentische Initiativen</h2>
<p>Zu den Initiativen, die wir regelmäßig unterstützen, gehört z. B. die <strong>Nightline Heidelberg</strong>, ein Kummertelefon von Studierenden für Studierende. Auch individuelle Hilfen wie Zuschüsse zum Lebensunterhalt einzelner Studierender in der Examensphase gehören dazu.</p>
<h2>Ausbau der Alumni-Arbeit</h2>
<p>Vor allem mit unseren fachgebundenen Sektionen unterstützen wir Begegnungen zwischen Studierenden und Absolvent:innen, Alumni-Tage, Diplomfeiern und Fakultätstage. Am Ausbau des Netzwerks Heidelberg Alumni International beteiligt sich der Verein mit Investitionen in die technischen Grundlagen einer besseren, auch digitalen Vernetzung.</p>
<div class="actions"><a class="btn alt" href="{R}assets/files/gdf_foerderrichtlinien.pdf" target="_blank" rel="noopener">Förderrichtlinien (PDF)</a></div>''')

page(G, "jahrbuecher", "Jahrbücher", '''
<h1>Heidelberger Jahrbücher</h1>
<p>Die Gesellschaft der Freunde ist Herausgeber der traditionsreichen Schriftenreihe <i>Heidelberger Jahrbücher</i>. Die Publikation wurde 1807 von Heidelberger Professoren unter dem Namen <i>Heidelbergische Jahrbücher der Literatur</i> begründet und hat eine wechselvolle, durch zwei Weltkriege unterbrochene Geschichte hinter sich.</p>
<p>Seit 2016 erscheinen die Jahrbücher als <a href="http://heiup.uni-heidelberg.de/campusmedia/heidelberger_jahrbuecher" target="_blank" rel="noopener">„Heidelberger Jahrbücher Online“</a> bei Heidelberg University Publishing (heiUP): elektronisch, frei zugänglich, bei Bedarf auch als Print-on-demand. Der erste Online-Band trägt den Titel <i>Stabilität im Wandel</i>.</p>
''' + fig("gdf/175_jahrbuch_2013_2.jpg", "Jahrbuch", '<p><b>Porträtband „Universität Heidelberg. Menschen, Lebenswege, Forschung“</b><br>Im letzten gedruckten Band 55 stellen sich fast 100 aktive Heidelberger Wissenschaftler:innen in kurzen, persönlichen Porträts vor. Erhältlich für 18,70 € im Buchhandel oder in der Geschäftsstelle; Mitglieder erhalten auf Anfrage ein Exemplar kostenlos.</p><p><a href="{R}assets/files/leseprobe.pdf" target="_blank" rel="noopener">Leseprobe (PDF)</a></p>') + '''
<h2>Bandthemen früherer Jahre</h2>
<p>Rausch (1999), Kreativität (2000), Milieu+Vererbung (2001), WahnWeltBild (2002), Weltbilder (2003), Konflikt (2004), Bildung und Wissenschaft (2005), Gesundheit (2006), 200 Jahre Heidelberger Romantik (2007), Überzeugungsstrategien (2008), Sprache (2009). Die Ausgaben 1999 bis 2006 sind online über die <a href="http://www.ub.uni-heidelberg.de/helios/epubl/hdjb/" target="_blank" rel="noopener">Universitätsbibliothek</a> verfügbar.</p>''')

page(G, "mitglieder", "Mitglieder", '''
<h1>Mitglieder</h1>
<p>Mit rund 1.400 Mitgliedern ist die <i>Gesellschaft der Freunde</i> der größte an der Ruprecht-Karls-Universität tätige Verein. Mehr als drei Viertel unserer Mitglieder sind Alumni, also Personen, die an der Universität Heidelberg eine Zeit lang studiert, gelehrt, geforscht oder in anderer Funktion gearbeitet haben.</p>
<p>Als Mitglied unterstützen Sie die Alumni- und Förderarbeit unseres Vereins. Sie haben bevorzugten Zugang zu unseren Veranstaltungen und werden regelmäßig über das Geschehen an der Universität informiert. In der Mitgliederversammlung, die laut Satzung mindestens einmal im Jahr einzuberufen ist, wirken Sie mit Ihrer Stimme an allen Beschlüssen mit.</p>
<div class="actions"><a class="btn" href="werden.html">Mitglied werden</a><a class="btn ghost" href="service.html">Service für Mitglieder</a><a class="btn ghost" href="sektionen.html">Sektionen</a></div>''')

page(G, "service", "Service", '''
<h1>Service</h1>
<h2>Veranstaltungsangebote</h2>
<p>Ob Vorträge, Ehemaligen-Treffen, Podiumsdiskussionen, Workshops oder ein Museumsbesuch unter fachkundiger Führung: Unsere Veranstaltungen bauen Brücken zwischen Wirtschaft, Kultur und Wissenschaft. Gemeinsam mit unseren <a href="partner.html">Partnern</a> laden wir regelmäßig ein, die Universität Heidelberg und ihr weltweites Netzwerk zu entdecken.</p>
<h2>Informationsangebote</h2>
<p>Printmedien senden wir allen Mitgliedern zu:</p>
<ul><li><b>„Ruperto Carola“</b> – das Forschungsmagazin der Universität, dreimal jährlich, mit Themen aus Geistes-, Sozial- und Naturwissenschaften und Medizin.</li><li><b>„HAIlife“</b> – das Alumni-Magazin, in der Regel einmal jährlich, über Netzwerke und Aktivitäten der Alumni sowie das Geschehen in Forschung, Lehre und Stadt.</li></ul>''')

page(G, "sektionen", "Sektionen", '''
<h1>Sektionen</h1>
<p>Viele Studierende, Absolvent:innen, Mitarbeitende und Freunde der Ruperto Carola wollen mit dem Fach, dem Institut oder der Fakultät, der sie sich zugehörig fühlen, langfristig in Verbindung bleiben. Deshalb sieht die Satzung vor, dass sich auf Fakultäts- und Institutsebene Sektionen gründen können. Bislang gibt es sieben; hier eine Auswahl:</p>
<div class="box"><h3><a href="http://www.psychologie.uni-heidelberg.de/alumni/index.html" target="_blank" rel="noopener">Alumni Psychologici</a></h3><p>Die älteste Sektion, gegründet von Prof. Joachim Funke und Dr. Herbert Wettig. Sektionsvorsitz: Prof. Dr. Tanja Bipp, Psychologisches Institut.</p></div>
<div class="box"><h3>Physik und Astronomie</h3><p>Gegründet vom früheren Dekan Prof. Dr. Christof Wetterich. Sektionsvorsitz: der jeweilige Dekan der Fakultät für Physik und Astronomie.</p></div>
<div class="box"><h3>Alumni, Freunde und Förderer der Rechtswissenschaften</h3><p>Entstanden aus einer Initiative von Vereinsmitgliedern, die an der Juristischen Fakultät lehren.</p></div>
<div class="box"><h3><a href="http://www.uni-heidelberg.de/fakultaeten/wiso/awi/awinet/gdf.html" target="_blank" rel="noopener">Alumni Wirtschaftswissenschaften</a></h3><p>Am Alfred-Weber-Institut von Prof. Günter Liesegang ins Leben gerufen. Sektionsvorsitz: Barbara Neef, Fakultätsreferentin an der Fakultät für Wirtschafts- und Sozialwissenschaften.</p></div>
<p>Mitglieder können sich jederzeit einer Sektion anschließen.</p>''')

page(G, "werden", "Mitglied werden", '''
<h1>Mitglied werden</h1>
<p>Mitglieder können natürliche und juristische Personen sowie rechtsfähige Personengesellschaften werden (§ 3 Abs. 1 der <a href="{R}assets/files/gdf_satzung.pdf" target="_blank" rel="noopener">Satzung</a>). Die Mitglieder leisten Jahresbeiträge; der Mindestbeitrag wird von der Mitgliederversammlung festgelegt, darüber hinaus bleibt die Höhe der Selbsteinschätzung überlassen (§ 4 Abs. 1).</p>
<h2>Jahresbeiträge</h2>
<p>Gemäß Beschluss der Mitgliederversammlung vom 30. Januar 2004 gelten seit 2004:</p>
<table class="data"><tbody>
<tr><th>Einzelpersonen</th><td><b>50,00 €</b> Mindestbeitrag pro Jahr</td></tr>
<tr><th>Firmen / juristische Personen</th><td><b>250,00 €</b> Mindestbeitrag pro Jahr</td></tr>
<tr><th>Studierende</th><td><b>10,00 €</b> – für die Dauer des Studiums bis zum ersten akademischen Abschluss</td></tr>
<tr><th>Absolvent:innen</th><td><b>25,00 €</b> – längstens drei Jahre nach dem ersten akademischen Abschluss</td></tr></tbody></table>
<h2>So geht’s</h2>
<p>Die Mitgliedschaft wird durch Beitrittserklärung gegenüber dem Vorstand und deren Annahme durch den Vorstand begründet (§ 3 Abs. 2 der Satzung). Laden Sie das Formular herunter, füllen Sie es aus und senden Sie es unterschrieben an uns.</p>
<div class="actions"><a class="btn" href="{R}assets/files/gdf_beitritt.pdf" target="_blank" rel="noopener">Beitrittserklärung (PDF)</a><a class="btn ghost" href="kontakt.html">Fragen? Kontakt</a></div>
<h2>Beitrags- und Spendenkonto</h2>
''' + bank("Gesellschaft der Freunde Universität Heidelberg e.V.", "DE22 6727 0003 0049 4005 00", "DEUTDESM672") + "<p>Wir freuen uns auf Sie!</p>")

page(G, "mitwirken", "Engagement", '''
<h1>Engagement</h1>
<p>Wir sind dankbar für das persönliche und finanzielle Engagement, mit dem unsere Mitglieder zur Förderung und Entwicklung der Ruperto Carola beitragen. Studierende und Ehemalige im In- und Ausland, Heidelberger Bürger:innen und Unternehmen setzen sich als Ratgeber, Botschafter, Kooperationspartner oder Geldgeber für die Ziele der Gesellschaft ein. Ihre Zeit, Ideen, Ihr Wissen, Ihre Erfahrungen und Verbindungen sind für uns von großem Wert. Beispiele:</p>
''' + fig("gdf/175_engagement_1.jpg", "Studentische Jury", '<p><b>Studentische Mitwirkung</b><br>Seit vielen Jahren setzen sich Studierende für den „Preis der Freunde“ ein: Sie kümmern sich um die Ausschreibung, sichten Bewerbungen und bereiten als studentische Juror:innen die Auswahl vor. Bei der Preisübergabe hält eine:r von ihnen die Laudatio auf die prämierte Projektgruppe.</p>')
+ fig("gdf/175_engagement_2.jpg", "Aktive Alumni", '<p><b>Aktive Alumni</b><br>Ehemalige Studierende, Mitarbeitende und Wissenschaftler wie der Regisseur Gero von Boehm oder der Schriftsteller Peter Bieri bereichern unsere Veranstaltungen als Redner, Diskussionspartner, Moderatoren oder Multiplikatoren.</p>')
+ fig("gdf/175_engagement_3.jpg", "Unternehmen", '<p><b>Unternehmen</b><br>helfen uns mit Know-how, professioneller Dienstleistung und Spenden: von der Vereinsbuchhaltung über Geschäftsberichte und Rechtsberatung bis zu Druckkosten – und dem Wanderpokal „Preis der Freunde“, der in einer Ausbildungswerkstatt entstand.</p>') + '''
<div class="box"><p><b>Möchten auch Sie sich engagieren?</b> Dann sprechen Sie uns an – wir freuen uns über Ihre Ideen und Ihr Interesse: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p></div>''')

page(G, "kontakt", "Kontakt", '''
<h1>Kontakt</h1>
<p>Wir freuen uns über Ihr Interesse an unseren Aktivitäten und darauf, mehr über Sie zu erfahren. Schreiben Sie uns, rufen Sie an oder kommen Sie einfach vorbei, wenn Sie in Heidelberg sind.</p>
''' + CONTACT + '''
<h2>Bankverbindung</h2>
''' + bank("Gesellschaft der Freunde Universität Heidelberg e.V.", "DE22 6727 0003 0049 4005 00", "DEUTDESM672") + '''
<div class="actions"><a class="btn" href="mailto:''' + MAIL + '''">E-Mail schreiben</a></div>
<p>Die Heidelberger Universitätsfreunde finden Sie auch auf <a href="https://www.facebook.com/GdFUniHD" target="_blank" rel="noopener">Facebook</a>.</p>''')

page(G, "impressum", "Impressum", '''
<h1>Impressum</h1>
<p>Gesellschaft der Freunde Universität Heidelberg e.V.</p>
<h2>Vertretungsberechtigter Vorstand</h2><p>PD Dr. Thorsten Helm (Vorsitzender)<br>Prof. Dr. Joachim Funke (stellv. Vorsitzender)<br>Dr. Monika Vierheilig (stellv. Vorsitzende)</p>
<h2>Redaktion</h2><p>Sabine zu Putlitz (Geschäftsstelle)</p>
<h2>Website</h2><p>Konzept, Gestaltung und Entwicklung: Arsenii Bazhenov (ehrenamtlich, auf freiwilliger Initiative)</p>
<h2>Fotonachweis</h2><p>Gesellschaft der Freunde Universität Heidelberg e.V. · Universität Heidelberg, Kommunikation &amp; Marketing · Heidelberg Alumni International · Universitätsbibliothek Heidelberg · Christoph Bastert</p>
<h2>Besucher- und Lieferanschrift</h2><p>Marstallstraße 6, 69117 Heidelberg<br>Fon +49 (0)6221 54-3446 · Fax +49 (0)6221 54-3447<br>Mail: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p>
<h2>Weitere Informationen</h2><p>Registergericht Heidelberg, Registernummer VR 2905<br>Finanzamt Heidelberg, Steuernummer 32489/43808</p>
<h2>Haftungsausschluss</h2>
<p>Die Gesellschaft stellt auf dieser Website Informationen zur Verfügung, die regelmäßig aktualisiert werden. Aufgrund der technischen Merkmale des Internets kann jedoch keine Haftung für Vollständigkeit und Richtigkeit übernommen werden. Für die Inhalte verlinkter externer Seiten sind ausschließlich deren Betreiber verantwortlich.</p>''')


