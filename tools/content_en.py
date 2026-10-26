"""English page content. Same slugs as content_de.py; prize and event names stay in German where they are proper names."""
from content_de import fig, person, photo, MAIL

pages = {"stiftung": {}, "gdf": {}}


def page(site, slug, title, body):
    pages[site][slug] = dict(title=title, body=body)


def bank(name, iban, bic, extra=""):
    raw = iban.replace(" ", "")
    ex = f'<tr><th>Reference</th><td>{extra}</td></tr>' if extra else ""
    return f'''<table class="data"><tbody>
<tr><th>Recipient</th><td>{name}</td></tr><tr><th>Bank</th><td>Deutsche Bank Heidelberg</td></tr>
<tr><th>IBAN</th><td><span class="iban">{iban}</span><button class="copy" data-copy="{raw}" type="button">Copy</button></td></tr>
<tr><th>BIC (SWIFT)</th><td><span class="iban">{bic}</span></td></tr>{ex}</tbody></table>'''


CONTACT = f'''<div class="person"><div class="avatar" aria-hidden="true">SP</div><p><span class="role">Head of the office</span><b>Sabine zu Putlitz</b>Marstallstraße 6, Room 018c · 69117 Heidelberg, Germany<br>Phone +49 (0)6221 54-3446 · Fax +49 (0)6221 54-3447<br><a href="mailto:sabine.putlitz@uni-heidelberg.de">sabine.putlitz@uni-heidelberg.de</a></p></div>
<div class="person"><div class="avatar" aria-hidden="true">CK</div><p><span class="role">Assistant</span><b>Carl Kraus</b>Marstallstraße 6, Room 002a · 69117 Heidelberg, Germany<br>Phone +49 (0)6221 54-19045 · Fax +49 (0)6221 54-3447<br><a href="mailto:{MAIL}">{MAIL}</a></p></div>'''

CREATOR = person("AB", "Arsenii Bazhenov", "Website", "Concept, design and development of this website – a voluntary initiative, done free of charge and for the joy of it.")

# ================================================================= FOUNDATION
S = "stiftung"
page(S, "index", "Welcome", '''
<h1>Welcome!</h1>
<p class="lead">Thank you for your interest in the Stiftung Universität Heidelberg (Heidelberg University Foundation), its history and its work for Ruprecht-Karls-Universität Heidelberg – Germany’s oldest university and one of the leading universities in Europe.</p>
<figure class="photo"><img src="{R}assets/img/stiftung/startseite_stiftung.jpg" alt="The Neue Universität in Heidelberg with the inscription “Dem lebendigen Geist”, students sitting on the steps" width="1023" height="681"><figcaption>Photo: Christoph Bastert</figcaption></figure>
<p>The foundation was established at the end of 1984, ahead of the 600th anniversary of Ruperto Carola, with the aim of promoting science and scholarship. It was initiated by the then Rector Prof. Dr. Gisbert Freiherr zu Putlitz, the former chairman of the Volkswagen board Kurt Lotz, and the constitutional and tax law scholar Prof. Dr. Paul Kirchhof.</p>
<div class="actions"><a class="btn" href="spenden.html">Donate now</a><a class="btn ghost" href="idee.html">Our idea</a><a class="btn ghost" href="preise.html">Ruprecht-Karls Prizes</a></div>
<div class="box"><h3>Partner association</h3><p>Together with the <a href="gdf/index.html">Gesellschaft der Freunde Universität Heidelberg e.V.</a> – the alumni and supporters’ association with about 1,400 members – the foundation shares an office in the Marstallhof.</p></div>
''')

page(S, "idee", "Idea", '''
<h1>Idea</h1>
<blockquote class="box"><p>“Whenever a person, the economy or the state falls into crisis, university knowledge promises help – and from this follow financial consequences.”</p><p class="credit">Paul Kirchhof, 1997 (translated)</p></blockquote>
<p>The Stiftung Universität Heidelberg has set itself the task of improving, through financial investment, the conditions for increasing and sharing university knowledge in Heidelberg. It therefore supports Ruprecht-Karls-Universität, its members and institutions in fulfilling their many tasks in research and teaching.</p>
''' + fig("stiftung/175_stiftung_idee.jpg", "Cover of the statutes", '''<p>The foundation is an independent foundation under civil law. It pursues exclusively and directly charitable purposes. Its aims are laid down in the statutes, which also describe the tasks of its two bodies, the <a href="personen.html">Board</a> and the <a href="kuratorium.html">Board of Trustees (Kuratorium)</a>.</p>
<p><a class="btn alt" href="{R}assets/files/stiftung-satzung.pdf" target="_blank" rel="noopener">Read the statutes (PDF, German)</a></p>''') + '''
<h2>Milestones</h2>
<div class="timeline">
<div><b>1984</b> – The foundation is established ahead of the 600th anniversary of Ruperto Carola.</div>
<div><b>1990</b> – The Ruprecht-Karls Prizes are awarded for the first time.</div>
<div><b>May 2000</b> – Cooperation agreement with the Gesellschaft der Freunde.</div>
<div><b>2003</b> – The activities of foundation and association are legally consolidated as far as permitted.</div>
<div><b>2011</b> – The courtyard of the “Neue Universität”, co-funded by the foundation, reopens.</div>
<div><b>Since 2022</b> – Donation campaign UniHD<i>hilft</i> for students and researchers affected by the war in Ukraine.</div>
</div>''')

page(S, "personen", "People", '''
<h1>People</h1>
<h2>Board (Vorstand)</h2>
''' + person("MV", "Dr. Monika Vierheilig", "Chair of the Board", "Former head of the Health department at the Ministry of Social Affairs and Integration of Baden-Württemberg")
+ person("TH", "PD Dr. Thorsten Helm", "Deputy chair", "Adjunct professor, partner at KPMG AG, Tax")
+ person("TB", "Prof. Dr. Tanja Bipp", "Board member", "Professor at the Institute of Psychology, Heidelberg University") + '''
<p>The Board’s work is supervised by a <a href="kuratorium.html">Board of Trustees</a>, which also supports the Board in fulfilling the foundation’s purpose.</p>
<h2>Office</h2>
<p>The office in the Marstallhof runs day-to-day business and is shared with the Gesellschaft der Freunde.</p>''' + CONTACT + '<h2>The website</h2>' + CREATOR)

page(S, "kuratorium", "Board of Trustees", '''
<h1>Board of Trustees</h1>
<p>The Kuratorium is elected for a term of five years and consists of people who have shown particular commitment to the foundation’s purpose. The members listed here were elected in autumn 2021. We were saddened by the loss of our highly valued trustee Dr. Jobst Wellensiek, who passed away in November 2022.</p>
<div class="cols"><ul>
<li><b>Dr. Dominik von Achten</b><br>CEO, HeidelbergCement AG</li>
<li><b>Dieter Berg</b><br>Former chair of the management, Robert Bosch Stiftung GmbH</li>
<li><b>Andrea Y. Combé</b><br>Lawyer, SFC Rechtsanwälte, Heidelberg</li>
<li><b>Prof. Dr. Dr. Jürgen Debus</b><br>Medical Director, Radiation Oncology</li>
<li><b>Prof. Dr. Lutz Gade</b><br>Institute of Inorganic Chemistry</li>
<li><b>Prof. Dr. Timo Goeschl</b><br>Alfred Weber Institute for Economics</li>
<li><b>Georg von Hohnhorst</b><br>Auditor, former partner at KPMG, Mannheim</li>
<li><b>Prof. Dr. Dieter Jahn</b><br>Former Senior Vice President, BASF Group</li>
</ul><ul>
<li><b>Prof. Dr. Selim Jochim</b><br>Institute of Physics</li>
<li><b>Prof. Dr. Hanno Kube</b><br>Institute of Finance and Tax Law</li>
<li><b>Dr. h.c. Manfred Lautenschläger</b><br>Honorary chairman of the Supervisory Board, MLP SE</li>
<li><b>Dr. Michael Litterer</b><br>Management, Franz Litterer GmbH &amp; Co KG, Weinheim</li>
<li><b>Prof. Dr. Stefan M. Maul</b><br>Department of Languages and Cultures of the Near East</li>
<li><b>Markwart von Pentz</b><br>President, Worldwide Agriculture &amp; Turf Division, Deere &amp; Company, Mannheim</li>
<li><b>Dr. Wolfgang Niopek</b><br>Former deputy managing director, IHK Rhein-Neckar</li>
<li><b>Dr. Volker Reimann-Dubbers</b><br>Chair of the Foundation Council, VRD Stiftung für erneuerbare Energien</li>
<li><b>Dr. Christopher Sessar</b><br>Chief Accounting Officer, SAP SE, Walldorf</li>
</ul></div>''')

page(S, "partner", "Partners", '''
<h1>Partners</h1>
<p>In May 2000 the foundation concluded a cooperation agreement with the Gesellschaft der Freunde Universität Heidelberg e.V. One aim of this cooperation is to pursue shared goals – such as promoting research and teaching at Heidelberg University – even more effectively.</p>
<p>In 2003 the foundation and the association legally consolidated their activities as far as permitted. Thanks to largely identical boards and a shared office, the two institutions can since then “appear and act as one” (preamble to the association’s statutes).</p>
''' + fig("stiftung/175_stiftung_partner.jpg", "Joint board meeting", '<p><b>Partners in every respect</b></p><p>At regular intervals the affairs of the foundation and the association are discussed in joint board meetings.</p><p><a href="gdf/index.html">To the Gesellschaft der Freunde →</a></p>'))

page(S, "aktivitaeten", "Activities", '''
<h1>Activities</h1>
<p>The foundation awards prizes to young researchers and funds measures that improve, on site in Heidelberg, the conditions for lively academic exchange among university members and with guests from foreign universities. It also launches fundraising campaigns to help the university with grants for larger projects.</p>
''' + fig("stiftung/175_kant.jpg", "Immanuel Kant", '<p><b>Kant 2024</b><br>For the 300th birthday of Immanuel Kant, the foundation supported a seminar series with the philosopher Omri Boehm on the spirit of the Enlightenment in January 2024 and invited students and staff to visit the Bonn exhibition “Kant und die offenen Fragen” together in March 2024.</p>')
+ fig("stiftung/175_stiftung_aktivitaeten_1.jpg", "Award ceremony", '<p><b>Ruprecht-Karls Prizes</b><br>With the Ruprecht-Karls Prizes the foundation highlights the achievements of talented young researchers and motivates them to continue their academic careers. The prizes are awarded for outstanding scholarly work from all fields.</p><p><a href="preise.html">More about the prizes →</a></p>')
+ fig("stiftung/UniHDhilft-Karte.jpg", "UniHDhilft postcard", '<p><b>“UniHD<i>hilft</i>” campaign</b><br>Prompted by Putin’s war, the foundation – together with colleagues from the university’s service units and academic institutes – supports students, prospective students and early-career researchers who had to flee Ukraine and are now seeking a new academic home in Heidelberg.</p><p><a href="spenden.html">Donate &amp; get involved →</a></p>')
+ '''<div class="box"><p><b>Has the war in Ukraine disrupted your studies or research?</b> UniHD<i>hilft</i> supports students and junior researchers from Ukraine who want to continue their work or studies at Heidelberg University. Contact us at <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a>.</p></div>''')

page(S, "preise", "Prizes", '''
<h1>Prizes</h1>
<p>Since 1990 the foundation has awarded the Ruprecht-Karls Prizes. They honour young researchers at Heidelberg University who have achieved outstanding research results. As a rule, the five best doctoral theses of the year are recognised. The multi-stage, university-wide selection process considers first scholarly works from all disciplines.</p>
<p>The decision is made by a jury appointed by the foundation’s Board on the Rector’s proposal. The jury, chaired by Prof. Dr. Rohini Kuner, decides on the basis of nominations from the faculties. <strong>Individual applications are not possible.</strong></p>
<h2>Award ceremony 2025</h2>
<p>On 24 October 2025 the prizes, worth €3,000 each, were presented in the Alte Aula of the university. The winners:</p>
<ul class="winners"><li>Dr. Nicole Sara Colaianni (history)</li><li>Dr. Julia Lemp (global health)</li><li>Dr. Letitia Parcalabescu (computational linguistics)</li><li>Dr. Felix Draxler (computer science and mathematics)</li><li>Dr. Lukas Maximilian Sigmund (chemistry)</li></ul>
<p><b>Fritz Grunebaum Prize:</b> Dr. Sina Allgeier (law)</p>
<h2>Award ceremony 2024</h2>
<ul class="winners"><li>Dr. Lynton Ardizzone (computer science)</li><li>Dr. Ioannis Sarropoulos (life sciences)</li><li>Dr. Friederike Ihssen (physics)</li><li>Dr. Norina Ullmann (theology)</li><li>Dr. Philipp Mai (political science)</li></ul>
<p><b>Fritz Grunebaum Prize:</b> Dr. Nina Benz (law)</p>
<h2>Prize winners’ reunion</h2>
<p>After the first meeting in November 2019, former prize winners came together again in Heidelberg from 25 to 27 October 2024 – with the award ceremony, short talks by earlier winners, a trip to the observatory and plenty of networking, under the motto “Auf ein Wiedersehen!” (“See you again!”).</p>
<p class="credit">Since 1990, more than 190 people have been honoured (source: Heidelberg University press release, 20 October 2025).</p>''')

page(S, "projekte", "Projects", '''
<h1>Projects</h1>
<p>Many university projects depend on financial support. In recent years the foundation has championed the following larger projects:</p>
<h2>1st Heidelberg Foundation Symposium (2018)</h2>
<p>With the symposium the foundation wanted to stimulate and promote international, interdisciplinary academic exchange on socially relevant topics. It took place at the International Science Forum Heidelberg – in the heart of the Old Town, an attractive setting for exchange between Heidelberg scholars and their guests from abroad.</p>
<h2>New courtyard for the “Neue Universität”</h2>
''' + fig("stiftung/175_stiftung_projekte_3.jpg", "Courtyard of the Neue Universität", '''<p>For the university’s 625th birthday there was a gift: the foundation had collected donations for the modernisation of the “Neue Universität”, which made it possible to include the green courtyard of the lecture-hall building in the modernisation concept. The aim was to make the courtyard more visible as an outdoor space and more attractive as a place to linger. Trustees, board and friends of the foundation raised <strong>€250,000</strong> for this project.</p>
<p>After a nearly two-year conversion, the building and its courtyard were ceremonially reopened on 25 June 2011. <a href="http://625.uni-heidelberg.de/md/kampagnen/625jahre/festschrift_neue_universitaet.pdf" target="_blank" rel="noopener">University commemorative publication (PDF, German)</a></p>'''))

page(S, "spenden", "Donate", '''
<h1>Donate</h1>
<p>The foundation is grateful for the many forms of support it has received in the past. Whether small or large, one-off or regular: every gesture of financial commitment strengthens our work for the benefit of Ruperto Carola.</p>
<h2>UniHD<i>hilft</i> – donations for refugee students and researchers</h2>
<p>Prompted by the war in Ukraine, the foundation – together with <a href="mitwirken.html">colleagues and staff</a> from the university’s service units and academic institutes – has launched a support campaign.</p>
<p>Many refugees from Ukraine have also arrived in Heidelberg, among them students, early-career researchers and researchers who are seeking – or have recently found – an academic home at Heidelberg University. The war has taken almost everything from them and their families; what remains is the hope of pursuing their studies and scientific ambitions in Heidelberg.</p>
<p>So that taking part in academic life succeeds quickly, a start-up programme is meant to remove financial hurdles. Donations are needed to pay for learning materials, language courses, tutorials, study and meeting spaces, or the translation of Ukrainian certificates and expert opinions. They are also meant to fund study and research grants lasting several months, bridging the time until secure, longer-term self-funding. Besides money, <a href="mitwirken.html">donations of time</a> are very welcome.</p>
<div class="actions"><a class="btn" href="https://www.betterplace.org/de/projects/107929" target="_blank" rel="noopener">Donate online via betterplace ↗</a></div>
<h2>Donation account for direct transfers</h2>
''' + bank("Stiftung Universität Heidelberg", "DE08 6727 0003 0033 7337 00", "DEUTDESM672", "UniHDhilft") + '''
<p class="credit">Questions about donation receipts are answered by the office: <a href="kontakt.html">Contact</a>.</p>''')

page(S, "mitwirken", "Get involved", '''
<h1>Get involved</h1>
''' + fig("stiftung/team_mitwirken.jpg", "The UniHDhilft team", '''<p>The UniHD<i>hilft</i> campaign is an initiative of staff members who see the need for support of Ukrainian students and early-career researchers in their daily work. The team comes from several institutes (including Slavic studies, East European history, sociology, psychology, theology, finance and tax law), service units such as the Studierendenwerk Heidelberg, as well as the foundation and the Gesellschaft der Freunde.</p>''') + '''
<h2>The team includes</h2>
<p>Dr. Marlene Bainczyk-Crescentini, Dr. Stefan Beljean, Jonas Dinkelaker, Dr. Felicitas Fischer von Weikersthal, Prof. Dr. Joachim Funke, PD Dr. Thorsten Helm, Dr. Bettina Kaibach, PD Dr. Stefaniya Ptashnyk, Sabine zu Putlitz, PD Dr. Franziska Schedewie, Dr. Ivan Sablin, PD Dr. Karoline Thaidigsmann, Kristian Willenbacher</p>
<h2>Mentorship programme</h2>
<p>The UniHD<i>hilft</i> mentorship programme goes beyond financial support and helps refugees find their place in the Heidelberg community. Each scholarship holder is paired with a Heidelberg student or early-career researcher who helps with the first steps – enrolment, finding the lecture hall, setting up the canteen card or looking for housing. We hope lasting friendships will grow from it.</p>
<div class="box"><p><b>Would you like to help?</b> For example as a mentor, or by donating your time? Get in touch: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p></div>''')

page(S, "kontakt", "Contact", '''
<h1>Contact</h1>
<p>We are glad about your interest in our activities and look forward to getting to know you. Write to us, call us, or simply drop by when you are in Heidelberg.</p>
''' + CONTACT + '''
<h2>Support campaign UniHD<i>hilft</i></h2>
''' + person("SB", "Dr. Stefan Beljean", "Contact for UniHDhilft", "Former research associate at the Max Weber Institute of Sociology. He makes sure UniHDhilft becomes known and welcomes suggestions.") + '''
<h2>Bank details</h2>
''' + bank("Stiftung Universität Heidelberg", "DE08 6727 0003 0033 7337 00", "DEUTDESM672") + '''
<div class="actions"><a class="btn" href="mailto:''' + MAIL + '''">Send an email</a></div>''')

page(S, "impressum", "Legal notice", '''
<h1>Legal notice</h1>
<h2>Responsible for the content</h2><p>Stiftung Universität Heidelberg</p>
<h2>Authorised representatives (Board)</h2><p>Dr. Monika Vierheilig (chair)<br>PD Dr. Thorsten Helm (deputy chair)</p>
<h2>Editorial</h2><p>Sabine zu Putlitz (office)</p>
<h2>Website</h2><p>Concept, design and development: Arsenii Bazhenov (voluntary, on his own initiative)</p>
<h2>Photo credits</h2><p>Stiftung Universität Heidelberg · Heidelberg University, Communications &amp; Marketing · Christoph Bastert</p>
<h2>Visiting and delivery address</h2><p>Marstallstraße 6, 69117 Heidelberg, Germany<br>Phone +49 (0)6221 54-3446 · Fax +49 (0)6221 54-3447<br>Email: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p>
<h2>Further information</h2><p>Regierungspräsidium Karlsruhe, foundation register<br>Finanzamt Heidelberg, tax number 2832/10421/1</p>
<h2>Disclaimer</h2>
<p>The foundation provides information on this website that is updated regularly. Owing to the technical nature of the internet, however, no liability can be accepted for completeness and accuracy.</p>
<p>This website contains links to third-party sites. Their operators are solely responsible for their content.</p>''')

# ================================================================= ASSOCIATION
G = "gdf"
page(G, "index", "Welcome", '''
<h1>Welcome!</h1>
<p class="lead">Take us at our word! We are not only committed with our heads but also with our hearts when it comes to offering interested alumni, friends and supporters of Heidelberg University a pleasant setting for their contacts with one another and with their alma mater.</p>
''' + fig("gdf/175_team.jpg", "The office team", '<p>As a non-profit supporters’ association we have shaped and supported dialogue and exchange for many years with everyone who feels connected to Ruprecht-Karls-Universität Heidelberg and the city that has been its home for over 625 years. We work hand in hand – and since 2010 also door to door – with <i>Heidelberg Alumni International</i>, the worldwide alumni network of <i>Ruperto Carola</i>.</p>') + '''
<figure class="photo"><img src="{R}assets/img/gdf/540_gruppe.jpg" alt="Members of the Gesellschaft der Freunde in a group" width="596" height="387"><figcaption>Photo: Christoph Bastert PHOTOGRAPHIE</figcaption></figure>
<p>Do you, too, have a heart for Heidelberg University? However you feel connected to the old but lively lady <i>Ruperto Carola</i> – through your studies, your doctorate, your work or simply your love of the city – a membership of the <strong>Gesellschaft der Freunde Universität Heidelberg e.V.</strong> lets you give that connection visible expression.</p>
<div class="actions"><a class="btn" href="werden.html">Become a member</a><a class="btn ghost" href="veranstaltungen.html">Events</a><a class="btn ghost" href="idee.html">Our idea</a></div>''')

page(G, "idee", "Idea", '''
<h1>Idea</h1>
<p>Together with its <a href="partner.html">partners</a>, the Gesellschaft der Freunde Universität Heidelberg e.V. aims to build a network that is robust in several respects: it connects alumni with one another and with their university, promotes the exchange of experience between the university and its friends in business and culture, and pools ideal and material commitment to university projects and concerns that could not be realised without outside support.</p>
<p>The association was founded in 2003. It is a non-profit registered association (Registergericht Heidelberg) with subdivisions (<a href="sektionen.html">sections</a>) at faculty and institute level.</p>
''' + fig("gdf/gdf_satzung.jpg", "Cover of the statutes", '<p>The statutes are the written constitution of our association. They name, among other things, the association’s goals and the tasks of the general assembly, and their preamble explains the legal predecessors of the society.</p><p><a class="btn alt" href="{R}assets/files/gdf_satzung.pdf" target="_blank" rel="noopener">Read the statutes (PDF, German)</a></p>') + '''
<p>The society emerged in 2003 from the merger of the <i>Verein der Freunde der Universität Heidelberg e.V.</i> and the <i>Universitäts-Gesellschaft Heidelberg e.V.</i></p>''')

page(G, "personen", "People", '''
<h1>People</h1>
<h2>Board (Vorstand)</h2>
''' + person("TH", "PD Dr. Thorsten Helm", "Chair", "Partner at KPMG AG, Tax")
+ person("JF", "Prof. Dr. Joachim Funke", "Deputy chair", "Institute of Psychology, Heidelberg University")
+ person("MV", "Dr. Monika Vierheilig", "Deputy chair", "Former head of the Health department at the Ministry of Social Affairs and Integration of Baden-Württemberg")
+ person("TB", "Prof. Dr. Tanja Bipp", "Board member", "Professor at the Institute of Psychology, Heidelberg University") + '''
<p>The Rector of Heidelberg University and the head of the university’s Foundations and Assets department are ex officio members of the Board.</p>
<h2>Office</h2>''' + CONTACT + '<h2>The website</h2>' + CREATOR)

page(G, "partner", "Partners", '''
<h1>Partners</h1>
<blockquote class="box"><p>“Coming together is a beginning, staying together is progress, and working together is success.”</p><p class="credit">Henry Ford</p></blockquote>
<p>The Gesellschaft der Freunde Universität Heidelberg e.V. is the legal successor of two long-established associations that had already concluded a cooperation agreement with the <a href="../index.html">Stiftung Universität Heidelberg</a> in May 2000. One aim of this agreement, still in force today, is to pursue shared goals such as promoting research and teaching even more effectively.</p>
<p>In 2003 the society and the foundation legally consolidated their activities as far as permitted. Thanks to largely identical boards and a shared office they can since then “appear and act as one” (preamble to the statutes).</p>
''' + fig("gdf/teamsitzung.jpg", "Team meeting", '<p>Another partner of our association is <i><a href="http://www.alumni.uni-heidelberg.de" target="_blank" rel="noopener">Heidelberg Alumni International</a></i>. Together we work to expand the existing alumni network and turn loose ties between alumni and the university into firm, lasting and positive relationships – so that alumni become friends.</p>'))

page(G, "aktivitaeten", "Activities", '''
<h1>Activities</h1>
<p>The activities of the Gesellschaft der Freunde are as varied as its tasks. A short overview.</p>
''' + fig("gdf/175_aktivitaeten_1.jpg", "Event", '<p><b>Events</b><br>Encounters need occasions. So that our members stay in conversation with one another and with the university, we organise talks, alumni meetings, readings and excursions under expert guidance. And once a year, in summer, we invite everyone to the <a href="veranstaltungen.html">Tag der Freunde</a> (Friends’ Day).</p>')
+ fig("gdf/175_aktivitaeten_2.jpg", "Sections", '<p><b>Sections</b><br>In our seven sections, section heads – mostly active Heidelberg professors and alumni – develop subject-specific contact and information offers. <a href="sektionen.html">More about the sections →</a></p>')
+ fig("gdf/scheck.jpg", "Cheque presentation", '<p><b>Funding</b><br>“No money, no fun.” We look for – and have often found – generous supporters and partners who help us to help: from alumni work to the digitisation workshop of the university library. <a href="foerdern.html">More →</a></p>')
+ fig("gdf/ueberreichung.jpg", "Prize presentation", '<p><b>Prizes</b><br>Good ideas and special achievements by student groups, individual students and young researchers deserve recognition – with the <a href="preise.html">Preis der Freunde</a> as well as individual grants and subsidies for student projects.</p>'))

page(G, "veranstaltungen", "Events", '''
<h1>Events</h1>
<p>Members of the Gesellschaft der Freunde are regularly invited to events organised by the association, partly together with its partners. A fixed date in the annual calendar is the <strong>Tag der Freunde</strong> (Friends’ Day): every year on a Friday in late June or early July.</p>
<h2>Tag der Freunde 2026</h2>
<p>On <strong>24 July 2026</strong> the friends of the university met at the International Science Forum Heidelberg in the Old Town.</p>
<div class="timeline"><div><b>4:00 pm</b> – General assembly</div><div><b>about 5:15 pm</b> – Presentation of the Preis der Freunde, followed by drinks on the terrace</div><div><b>from 6:00 pm</b> – Walk together to the university’s summer party in the Marstallhof</div></div>
<h2>Tag der Freunde 2025</h2>
<p>On Friday, 4 July 2025, the society invited members to the Hotel Königstuhl: general assembly (4:30 pm), a talk “New gene therapies are revolutionising cancer medicine” by Prof. Dr. Carsten Müller-Tidow, Medical Director of the Department of Haematology, Oncology and Rheumatology (6:15 pm), the Preis der Freunde ceremony (7:15 pm) and a summer party with a view over Heidelberg and the Neckar.</p>
<h2>New Year’s reception</h2>
<p>For some years the society has invited its members in January to a lecture followed by a reception. On 10 January 2025 Prof. Dr. Anne Peters of the Max Planck Institute for Comparative Public Law and International Law spoke on “Brave new world order? International law in transition”.</p>
<h2>Universitätsfreunde unterwegs (University friends on tour)</h2>
<p>Themed excursions to places where influential current or former members of Heidelberg University live or work, and to places, institutions and companies that play an important role in business, culture, politics, art or science.</p>
<ul><li>Europe in Strasbourg, May 2018</li><li>The old new Potsdam, April 2017 – including the GFZ research centre in the Albert Einstein Science Park and the Palais Barberini</li><li>Paris – experiencing history, April 2016</li><li>The Deutsche Bundesbank – more than just a bank, October 2015</li><li>Babylon in Berlin, April 2015</li></ul>''')

page(G, "preise", "Preis der Freunde", '''
<h1>Preis der Freunde (Friends’ Prize)</h1>
<p>Since 1995 the Gesellschaft der Freunde has awarded the “Preis der Freunde”, worth <strong>€2,500</strong>, every year to student groups that have stood out with an exceptional initiative. The list of past winners stands for extraordinary student commitment.</p>
<div class="box"><h3>Call for applications</h3><p>Are you a student at Heidelberg University who has started a project or initiative that matters to other students, an institute, a subject, a faculty or student life beyond the curriculum? Then apply! The call runs every spring; for 2026 the deadline was 4 May 2026. Poster of the last call (2025): <a href="{R}assets/files/preisderfreunde2025.pdf" target="_blank" rel="noopener">PDF</a></p></div>
<h2>Winners 2025: Cheaper than therapy run club</h2>
<p>The Cheaper than therapy run club is Heidelberg’s first social run club. Founded by four dentistry students, the initiative offers students a low-threshold, regular way to exercise and meet through weekly runs and further activities. With its focus on mental health, it draws attention to a topic that is often neglected in everyday university life.</p>
<h2>Winner 2024: StudyTutors Heidelberg</h2>
''' + photo("gdf/544_studytutors.jpg", "Prize presented to StudyTutors Heidelberg", "Photo: Christoph Bastert PHOTOGRAPHIE") + '''
<p>With about 100 committed students, StudyTutors Heidelberg is part of a nationwide association that helps pupils from socially or financially disadvantaged backgrounds through free tutoring organised and delivered by students. The prize was presented on 12 July 2024 at the Tag der Freunde.</p>
<h2>Winner 2022: “Situs Inversus – Der Vorklinik-Podcast”</h2>
<p>Founded in summer 2020 by five human-medicine students as a volunteer project: a podcast in the style of a tutorial that explains the essential topics of pre-clinical medicine from a student perspective. The prize was presented on 21 July 2023.</p>
<h2>Other winners since 1995</h2>
<ul class="chips">
<li>MediNetz Rhein-Neckar</li><li>Match4healthcare</li><li>Chancen gestalten Heidelberg</li><li>Querfeldein Heidelberg</li><li>Heidelberger Lupe</li><li>Weitblick Heidelberg</li><li>ROCK YOUR LIFE! Heidelberg</li><li>Pro Bono Heidelberg</li><li>HCWK</li><li>HIIK</li><li>artefakt</li><li>ikulE</li><li>Interdisziplinäres Forum</li><li>Delta – The Philosophers Club</li><li>Forum für Kritische Theorie</li><li>RadioAktiv</li><li>StudzR</li><li>Gärtnerei Wildwuchs</li><li>Praktikumsinitiative Geografie</li><li>Romanischer Keller</li><li>Sozialhandbuch der Fachschaften</li><li>ruprecht</li><li>Nightline</li><li>Anatomie am Lebenden</li><li>Die Anstifter</li><li>URRmEL</li><li>Theatergruppe Anglistik</li><li>Emsa Heidelberg</li></ul>''')

page(G, "foerdern", "Funding", '''
<h1>Funding</h1>
<p>Every university needs friends who support it in fulfilling its tasks in research and teaching. With the help of its members, the society champions projects that arise at Ruprecht-Karls-Universität and benefit its students, teachers and institutions.</p>
<p>Our funding activities focus on supporting students and student initiatives, interdisciplinary projects of central institutions, and expanding alumni work.</p>
<h2>Exceptional, interdisciplinary projects</h2>
<p>These include the <strong>digitisation workshop</strong>, with which Germany’s oldest university library can not only preserve its cultural heritage of early prints and manuscripts but also make it accessible to scholars and the public. The book table, scanner and camera were financed from the association’s funds.</p>
<h2>Students and student initiatives</h2>
<p>Among the initiatives we support regularly is <strong>Nightline Heidelberg</strong>, a listening phone by students for students. Individual help such as grants towards the living costs of students during their exam phase is also part of this.</p>
<h2>Expanding alumni work</h2>
<p>Above all with our subject-based sections we support encounters between students and graduates, alumni days, graduation ceremonies and faculty days. The association also invests in the technical foundations of better, digital networking within Heidelberg Alumni International.</p>
<div class="actions"><a class="btn alt" href="{R}assets/files/gdf_foerderrichtlinien.pdf" target="_blank" rel="noopener">Funding guidelines (PDF, German)</a></div>''')

page(G, "jahrbuecher", "Yearbooks", '''
<h1>Heidelberger Jahrbücher</h1>
<p>The Gesellschaft der Freunde publishes the long-standing series <i>Heidelberger Jahrbücher</i>. It was founded in 1807 by Heidelberg professors as <i>Heidelbergische Jahrbücher der Literatur</i> and has an eventful history, interrupted by two world wars.</p>
<p>Since 2016 the yearbooks have appeared as <a href="http://heiup.uni-heidelberg.de/campusmedia/heidelberger_jahrbuecher" target="_blank" rel="noopener">“Heidelberger Jahrbücher Online”</a> with Heidelberg University Publishing (heiUP): electronic, open access and, on request, as print on demand. The first online volume is titled <i>Stabilität im Wandel</i>.</p>
''' + fig("gdf/175_jahrbuch_2013_2.jpg", "Yearbook", '<p><b>Portrait volume “Universität Heidelberg. Menschen, Lebenswege, Forschung”</b><br>In the last printed volume 55, almost 100 active Heidelberg scholars introduce themselves in short, personal portraits. Available for €18.70 in bookshops or at the office; members receive a copy free of charge on request.</p><p><a href="{R}assets/files/leseprobe.pdf" target="_blank" rel="noopener">Reading sample (PDF, German)</a></p>') + '''
<h2>Volume topics of earlier years</h2>
<p>Intoxication (1999), Creativity (2000), Milieu + Heredity (2001), Delusion–World–Image (2002), Worldviews (2003), Conflict (2004), Education and Science (2005), Health (2006), 200 Years of Heidelberg Romanticism (2007), Strategies of Persuasion (2008), Language (2009). Issues from 1999 to 2006 are available online via the <a href="http://www.ub.uni-heidelberg.de/helios/epubl/hdjb/" target="_blank" rel="noopener">university library</a>.</p>''')

page(G, "mitglieder", "Members", '''
<h1>Members</h1>
<p>With about 1,400 members the <i>Gesellschaft der Freunde</i> is the largest association active at Ruprecht-Karls-Universität. More than three quarters of our members are alumni – people who have studied, taught, researched or worked in another capacity at Heidelberg University for a time.</p>
<p>As a member you support the alumni and funding work of our association. You get preferred access to our events and are regularly informed about what is happening at the university. In the general assembly, which must be convened at least once a year under the statutes, your vote counts in all resolutions.</p>
<div class="actions"><a class="btn" href="werden.html">Become a member</a><a class="btn ghost" href="service.html">Member services</a><a class="btn ghost" href="sektionen.html">Sections</a></div>''')

page(G, "service", "Service", '''
<h1>Service</h1>
<h2>Events</h2>
<p>Whether talks, alumni meetings, panel discussions, workshops or a museum visit under expert guidance: our events build bridges between business, culture and science. Together with our <a href="partner.html">partners</a> we regularly invite you to discover Heidelberg University and its worldwide network.</p>
<h2>Information</h2>
<p>We send print media to all members:</p>
<ul><li><b>“Ruperto Carola”</b> – the university’s research magazine, three times a year, with topics from the humanities, social sciences, natural sciences and medicine.</li><li><b>“HAIlife”</b> – the alumni magazine, usually once a year, about alumni networks and activities as well as research, teaching and city life.</li></ul>''')

page(G, "sektionen", "Sections", '''
<h1>Sections</h1>
<p>Many students, graduates, staff and friends of Ruperto Carola want to stay in direct, long-term contact with the subject, institute or faculty they feel they belong to. That is why the statutes allow sections to be founded at faculty and institute level. There are seven so far; here is a selection:</p>
<div class="box"><h3><a href="http://www.psychologie.uni-heidelberg.de/alumni/index.html" target="_blank" rel="noopener">Alumni Psychologici</a></h3><p>The oldest section, founded by Prof. Joachim Funke and Dr. Herbert Wettig. Section head: Prof. Dr. Tanja Bipp, Institute of Psychology.</p></div>
<div class="box"><h3>Physics and Astronomy</h3><p>Founded by the former dean Prof. Dr. Christof Wetterich. Section head: the current dean of the Faculty of Physics and Astronomy.</p></div>
<div class="box"><h3>Alumni, Friends and Supporters of Law</h3><p>Created from an initiative of association members who teach at the Faculty of Law.</p></div>
<div class="box"><h3><a href="http://www.uni-heidelberg.de/fakultaeten/wiso/awi/awinet/gdf.html" target="_blank" rel="noopener">Alumni Economics</a></h3><p>Started at the Alfred Weber Institute by Prof. Günter Liesegang. Section head: Barbara Neef, faculty officer at the Faculty of Economics and Social Sciences.</p></div>
<p>Members can join a section at any time.</p>''')

page(G, "werden", "Become a member", '''
<h1>Become a member</h1>
<p>Members can be natural and legal persons as well as partnerships with legal capacity (§ 3 para. 1 of the <a href="{R}assets/files/gdf_satzung.pdf" target="_blank" rel="noopener">statutes</a>, in German). Members pay annual fees; the minimum fee is set by the general assembly, beyond that the amount is left to the member’s own assessment (§ 4 para. 1).</p>
<h2>Annual fees</h2>
<p>Following the general assembly’s resolution of 30 January 2004, the following apply since 2004:</p>
<table class="data"><tbody>
<tr><th>Individuals</th><td><b>€50.00</b> minimum per year</td></tr>
<tr><th>Companies / legal entities</th><td><b>€250.00</b> minimum per year</td></tr>
<tr><th>Students</th><td><b>€10.00</b> – for the duration of studies up to the first academic degree</td></tr>
<tr><th>Graduates</th><td><b>€25.00</b> – for at most three years after the first academic degree</td></tr></tbody></table>
<h2>How it works</h2>
<p>Membership is established by a declaration of accession to the Board and its acceptance by the Board (§ 3 para. 2 of the statutes). Download the form, fill it in and send it to us signed.</p>
<div class="actions"><a class="btn" href="{R}assets/files/gdf_beitritt.pdf" target="_blank" rel="noopener">Application form (PDF, German)</a><a class="btn ghost" href="kontakt.html">Questions? Contact</a></div>
<h2>Membership fee and donation account</h2>
''' + bank("Gesellschaft der Freunde Universität Heidelberg e.V.", "DE22 6727 0003 0049 4005 00", "DEUTDESM672") + "<p>We look forward to welcoming you!</p>")

page(G, "mitwirken", "Engagement", '''
<h1>Engagement</h1>
<p>We are grateful for the personal and financial commitment with which our members contribute to promoting and developing Ruperto Carola. Students and alumni at home and abroad, Heidelberg citizens and companies support the society’s goals as advisers, ambassadors, cooperation partners or donors. Your time, ideas, knowledge, experience and connections are of great value to us. A few examples:</p>
''' + fig("gdf/175_engagement_1.jpg", "Student jury", '<p><b>Student involvement</b><br>For many years students have worked on the “Preis der Freunde”: they take care of the call for applications, review submissions and, as student jurors, prepare the selection. At the ceremony one of them gives the laudatory speech for the winning project group.</p>')
+ fig("gdf/175_engagement_2.jpg", "Active alumni", '<p><b>Active alumni</b><br>Former students, staff and scholars such as the film director Gero von Boehm or the writer Peter Bieri enrich our events as speakers, discussion partners, moderators or multipliers.</p>')
+ fig("gdf/175_engagement_3.jpg", "Companies", '<p><b>Companies</b><br>help us with know-how, professional services and donations: from the association’s bookkeeping, annual reports and legal advice to printing costs – and the challenge trophy “Preis der Freunde”, made in a company’s training workshop.</p>') + '''
<div class="box"><p><b>Would you like to get involved too?</b> Then talk to us – we welcome your ideas and your interest: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p></div>''')

page(G, "kontakt", "Contact", '''
<h1>Contact</h1>
<p>We are glad about your interest in our activities and look forward to getting to know you. Write to us, call us, or simply drop by when you are in Heidelberg.</p>
''' + CONTACT + '''
<h2>Bank details</h2>
''' + bank("Gesellschaft der Freunde Universität Heidelberg e.V.", "DE22 6727 0003 0049 4005 00", "DEUTDESM672") + '''
<div class="actions"><a class="btn" href="mailto:''' + MAIL + '''">Send an email</a></div>
<p>You can also find the Heidelberg university friends on <a href="https://www.facebook.com/GdFUniHD" target="_blank" rel="noopener">Facebook</a>.</p>''')

page(G, "impressum", "Legal notice", '''
<h1>Legal notice</h1>
<p>Gesellschaft der Freunde Universität Heidelberg e.V.</p>
<h2>Authorised representatives (Board)</h2><p>PD Dr. Thorsten Helm (chair)<br>Prof. Dr. Joachim Funke (deputy chair)<br>Dr. Monika Vierheilig (deputy chair)</p>
<h2>Editorial</h2><p>Sabine zu Putlitz (office)</p>
<h2>Website</h2><p>Concept, design and development: Arsenii Bazhenov (voluntary, on his own initiative)</p>
<h2>Photo credits</h2><p>Gesellschaft der Freunde Universität Heidelberg e.V. · Heidelberg University, Communications &amp; Marketing · Heidelberg Alumni International · Heidelberg University Library · Christoph Bastert</p>
<h2>Visiting and delivery address</h2><p>Marstallstraße 6, 69117 Heidelberg, Germany<br>Phone +49 (0)6221 54-3446 · Fax +49 (0)6221 54-3447<br>Email: <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a></p>
<h2>Further information</h2><p>Registergericht Heidelberg, register number VR 2905<br>Finanzamt Heidelberg, tax number 32489/43808</p>
<h2>Disclaimer</h2>
<p>The society provides information on this website that is updated regularly. Owing to the technical nature of the internet, however, no liability can be accepted for completeness and accuracy. Operators of linked external sites are solely responsible for their content.</p>''')
