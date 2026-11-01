"""Builds the public index.html for manasa.nl from the page source (yoga-met-anjana.html)."""
import json, sys
src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
cut = s.index('</style>') + len('</style>')
head = s[:cut].replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = head.replace('<title>Manasa – Yoga met Anjana</title>',
                    '<title>Stoelyoga voor ouderen in Utrecht | Manasa – Yoga met Anjana</title>')
head = head.replace('<meta name="description" content="Zachte senioren- en stoelyoga voor zorginstellingen, dagbesteding en buurtgroepen in Utrecht en omgeving.">',
                    '<meta name="description" content="Stoelyoga en seniorenyoga voor verpleeghuizen, woonzorgcentra en dagbesteding in Utrecht, Leidsche Rijn, Vleuten, Nieuwegein en Zeist. Yogadocent Anjana Sasidharan, met ervaring in ouderenzorg, ziekenhuis en speciaal onderwijs. Plan een proefles.">')
ld = [{
  "@context": "https://schema.org", "@type": "ProfessionalService",
  "name": "Manasa – Yoga met Anjana", "url": "https://manasa.nl/",
  "image": "https://manasa.nl/og-image.jpg", "logo": "https://manasa.nl/og-image.jpg",
  "description": "Zachte stoel- en seniorenyoga voor zorginstellingen, dagbesteding en buurthuizen in Utrecht en omgeving.",
  "founder": {"@type": "Person", "name": "Anjana Sasidharan", "jobTitle": "Yogadocent"},
  "address": {"@type": "PostalAddress", "addressLocality": "Utrecht", "addressCountry": "NL"},
  "areaServed": ["Utrecht", "Leidsche Rijn", "Vleuten", "De Meern", "Maarssen", "Nieuwegein", "Houten", "Zeist"],
  "email": "info@manasa.nl",
  "knowsLanguage": ["nl", "en"],
  "serviceType": ["Stoelyoga", "Seniorenyoga", "Yoga voor ouderen", "Ademhaling en ontspanning"],
  "identifier": {"@type": "PropertyValue", "propertyID": "KvK", "value": "92138586"}
}, {
  "@context": "https://schema.org", "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Wat is stoelyoga?", "acceptedAnswer": {"@type": "Answer", "text": "Stoelyoga is zachte yoga die u zittend op een stoel doet, of staand met steun van de stoel. Het is geschikt voor ouderen met beperkte mobiliteit, ook voor bewoners in een rolstoel."}},
    {"@type": "Question", "name": "Voor welke organisaties geeft u les?", "acceptedAnswer": {"@type": "Answer", "text": "Voor verpleeghuizen, woonzorgcentra, kleinschalige woonvormen, dagbesteding en buurthuizen. Ook bedrijven en particulieren zijn welkom."}},
    {"@type": "Question", "name": "In welke plaatsen komt u lesgeven?", "acceptedAnswer": {"@type": "Answer", "text": "In Utrecht en omgeving, waaronder Leidsche Rijn, Vleuten, De Meern, Maarssen, Nieuwegein, Houten en Zeist."}},
    {"@type": "Question", "name": "Kan ik eerst een proefles plannen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Met een proefles ziet u of de lessen bij uw bewoners passen. Elke les wordt afgestemd op de gezondheid, mobiliteit en wensen van de groep."}}
  ]}]
extra = ('<link rel="canonical" href="https://manasa.nl/">\n'
         '<link rel="icon" type="image/png" href="/favicon.png">\n'
         '<meta property="og:type" content="website">\n'
         '<meta property="og:locale" content="nl_NL">\n'
         '<meta property="og:title" content="Manasa – Yoga met Anjana">\n'
         '<meta property="og:description" content="Zachte stoel- en seniorenyoga voor zorginstellingen in Utrecht, met ervaring uit ouderenzorg, ziekenhuis, speciaal onderwijs en counseling.">\n'
         '<meta property="og:url" content="https://manasa.nl/">\n'
         '<meta property="og:image" content="https://manasa.nl/og-image.jpg">\n'
         '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>\n')
doc = ('<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + extra + head + '\n</head>\n<body>' + s[cut:] + '\n</body>\n</html>\n')
open(out, 'w').write(doc)
