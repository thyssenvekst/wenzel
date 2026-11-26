#!/usr/bin/env python3
"""Setzt die statischen Seiten aus Kopf, Fuß und Seiteninhalt zusammen.
Aufruf: python3 _quellen/build.py   (Inhalte: _quellen/seiten/*.html)
Die fertigen .html-Dateien im Hauptordner sind reines statisches HTML."""
from pathlib import Path
import html

WURZEL = Path(__file__).resolve().parent.parent
QUELLE = Path(__file__).resolve().parent / "seiten"
DOMAIN = "https://www.rechtsanwalt-welz.de/"

ERSATZ = {
    "{{TEL}}": "08092 3059201", "{{TEL_LINK}}": "tel:+4980923059201",
    "{{MOBIL}}": "0177 3258123", "{{MOBIL_LINK}}": "tel:+491773258123",
    "{{FAX}}": "08092 3008308",
    "{{MAIL}}": "info@rechtsanwalt-welz.de",
    "{{ADRESSE}}": "Schneckenburgerstraße 34<br>81675 München",
}

NAV = [("index.html", "Start"), ("kanzlei.html", "Person &amp; Kanzlei"),
       ("rechtsgebiete.html", "Rechtsgebiete"), ("kontakt.html", "Kontakt")]

SEITEN = [
    ("index.html", "Rechtsanwalt Steffen Welz, München – Zivilrecht, Arbeitsrecht, Erbrecht, Strafrecht",
     "Rechtsanwalt Steffen Welz, Einzelkanzlei in München: Zivilrecht mit Vertrags-, Verkehrs-, Miet- und Gesellschaftsrecht, Arbeitsrecht, Erbrecht sowie Strafrecht und Ordnungswidrigkeiten."),
    ("kanzlei.html", "Person & Kanzlei – Rechtsanwalt Steffen Welz, München",
     "Steffen Welz, Rechtsanwalt seit 2010, seit 2011 selbständig. Einzelkanzlei in Bürogemeinschaft mit Rechtsanwältin Sandra M. Rosar und Rechtsanwältin Lydia Bergida – keine Sozietät."),
    ("rechtsgebiete.html", "Rechtsgebiete – Rechtsanwalt Steffen Welz, München",
     "Zivilrecht (Vertragsrecht, Verkehrsrecht, Mietrecht, Gesellschaftsrecht), Erbrecht, Arbeitsrecht sowie Strafrecht und Ordnungswidrigkeitenrecht – gerichtlich und außergerichtlich."),
    ("kontakt.html", "Kontakt & Anfahrt – Rechtsanwalt Steffen Welz, München",
     "Rechtsanwalt Steffen Welz, Schneckenburgerstraße 34, 81675 München. Telefon 08092 3059201, Mobil 0177 3258123, E-Mail info@rechtsanwalt-welz.de."),
    ("impressum.html", "Impressum – Rechtsanwalt Steffen Welz", "Impressum der Anwaltskanzlei Steffen Welz, München."),
    ("datenschutz.html", "Datenschutz – Rechtsanwalt Steffen Welz", "Datenschutzerklärung der Anwaltskanzlei Steffen Welz, München."),
    ("404.html", "Seite nicht gefunden – Rechtsanwalt Steffen Welz", "Diese Seite gibt es nicht."),
]

JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Attorney","name":"Rechtsanwalt Steffen Welz","url":"https://www.rechtsanwalt-welz.de/",
"telephone":"+49 8092 3059201","faxNumber":"+49 8092 3008308","email":"info@rechtsanwalt-welz.de",
"address":{"@type":"PostalAddress","streetAddress":"Schneckenburgerstraße 34","postalCode":"81675","addressLocality":"München","addressCountry":"DE"},
"areaServed":"München","knowsAbout":["Zivilrecht","Vertragsrecht","Verkehrsrecht","Mietrecht","Gesellschaftsrecht","Erbrecht","Arbeitsrecht","Strafrecht","Ordnungswidrigkeitenrecht"]}
</script>"""


def kopf(datei, titel, beschreibung):
    akt = ' aria-current="page"'

    def liste(einzug):
        return "\n".join(f'{einzug}<li><a href="{h}"{akt if h == datei else ""}>{n}</a></li>' for h, n in NAV)
    kanon = DOMAIN + ("" if datei == "index.html" else datei)
    robots = '\n  <meta name="robots" content="noindex">' if datei == "404.html" else f'\n  <link rel="canonical" href="{kanon}">'
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(titel)}</title>
  <meta name="description" content="{html.escape(beschreibung)}">{robots}
  <meta name="theme-color" content="#16212e">
  <meta property="og:title" content="{html.escape(titel)}">
  <meta property="og:description" content="{html.escape(beschreibung)}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <meta property="og:url" content="{kanon}">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="assets/fonts/source-serif-4-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/hanken-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/css/site.css">
  {JSONLD if datei == "index.html" else ""}
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>

<header class="kopf" data-kopf>
  <div class="wrap kopf-innen">
    <a class="marke" href="index.html" aria-label="Rechtsanwalt Steffen Welz – Startseite" translate="no">
      <span class="marke-name">Steffen Welz</span>
      <span class="marke-zusatz">Rechtsanwalt · München</span>
    </a>
    <nav class="hauptnav" aria-label="Hauptnavigation">
      <ul>
{liste("        ")}
      </ul>
    </nav>
    <a class="kopf-tel" href="{{{{TEL_LINK}}}}"><span class="kopf-tel-label">Telefon</span> {{{{TEL}}}}</a>
    <button class="menue-knopf" type="button" aria-expanded="false" aria-controls="menue" data-menue-knopf>
      <span data-menue-text>Menü</span><span class="striche" aria-hidden="true"></span>
    </button>
  </div>
  <div class="menue" id="menue" hidden data-menue>
    <nav class="wrap" aria-label="Hauptnavigation mobil">
      <ul>
{liste("        ")}
      </ul>
      <div class="menue-fuss">
        <a href="{{{{TEL_LINK}}}}">Telefon {{{{TEL}}}}</a>
        <a href="{{{{MOBIL_LINK}}}}">Mobil {{{{MOBIL}}}}</a>
        <a href="mailto:{{{{MAIL}}}}">{{{{MAIL}}}}</a>
      </div>
    </nav>
  </div>
</header>
"""


FUSS = """
<footer class="fuss">
  <div class="wrap">
    <div class="fuss-spalten">
      <div class="fuss-marke">
        <p class="marke-name" translate="no">Steffen Welz</p>
        <p>Rechtsanwalt<br>Einzelkanzlei in Bürogemeinschaft</p>
      </div>
      <div>
        <h2>Anschrift</h2>
        <p>{{ADRESSE}}</p>
      </div>
      <div>
        <h2>Kontakt</h2>
        <p><a href="{{TEL_LINK}}">Telefon {{TEL}}</a><br><a href="{{MOBIL_LINK}}">Mobil {{MOBIL}}</a><br>Telefax {{FAX}}<br><a href="mailto:{{MAIL}}">{{MAIL}}</a></p>
      </div>
      <div>
        <h2>Seiten</h2>
        <ul>
          <li><a href="kanzlei.html">Person &amp; Kanzlei</a></li>
          <li><a href="rechtsgebiete.html">Rechtsgebiete</a></li>
          <li><a href="kontakt.html">Kontakt &amp; Anfahrt</a></li>
        </ul>
      </div>
    </div>
    <div class="fuss-unten">
      <span>© 2026 Rechtsanwalt Steffen Welz · Rechtsanwaltskammer München</span>
      <ul>
        <li><a href="impressum.html">Impressum</a></li>
        <li><a href="datenschutz.html">Datenschutz</a></li>
      </ul>
    </div>
  </div>
</footer>

<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


def ersetze(text):
    for k, v in ERSATZ.items():
        text = text.replace(k, v)
    return text


def baue():
    for datei, titel, beschreibung in SEITEN:
        inhalt = (QUELLE / datei).read_text(encoding="utf-8").strip()
        seite = kopf(datei, titel, beschreibung) + '\n<main id="inhalt">\n' + inhalt + "\n</main>\n" + FUSS
        (WURZEL / datei).write_text(ersetze(seite), encoding="utf-8")
        print("gebaut:", datei)


if __name__ == "__main__":
    baue()
