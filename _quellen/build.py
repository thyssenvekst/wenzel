#!/usr/bin/env python3
"""Setzt die statischen Seiten aus Kopf, Fuß und Seiteninhalt zusammen.
Aufruf: python3 _quellen/build.py   (Inhalte: _quellen/seiten/*.html)
Erzeugt außerdem assets/css/fonts.css (Schriften als Data-URI, damit sie auch
per Doppelklick/file:// laden) und sitemap.xml."""
from pathlib import Path
import base64, html

WURZEL = Path(__file__).resolve().parent.parent
QUELLE = Path(__file__).resolve().parent / "seiten"
DOMAIN = "https://www.rechtsanwalt-welz.de/"

ERSATZ = {
    "{{TEL}}": "08092 3059201", "{{TEL_LINK}}": "tel:+4980923059201",
    "{{MOBIL}}": "0177 3258123", "{{MOBIL_LINK}}": "tel:+491773258123",
    "{{FAX}}": "08092 3008308",
    "{{MAIL}}": "info@rechtsanwalt-welz.de",
    "{{ADRESSE}}": "Schneckenburgerstraße 34<br>81675 München",
    "{{KARTE}}": "https://www.openstreetmap.org/search?query=Schneckenburgerstra%C3%9Fe%2034%2C%2081675%20M%C3%BCnchen",
}

GEBIETE = ["rechtsgebiete.html", "zivilrecht.html", "arbeitsrecht.html", "strafrecht.html"]
NAV = [("kanzlei.html", "Person &amp; Kanzlei", ["kanzlei.html"]),
       ("rechtsgebiete.html", "Rechtsgebiete", GEBIETE),
       ("kontakt.html", "Kontakt", ["kontakt.html"])]
UNTER = [("zivilrecht.html", "Zivilrecht"), ("arbeitsrecht.html", "Arbeitsrecht"),
         ("strafrecht.html", "Strafrecht &amp; Ordnungswidrigkeiten")]

SEITEN = [
    ("index.html", "Rechtsanwalt Steffen Welz, München – Zivilrecht, Arbeitsrecht, Strafrecht",
     "Rechtsanwalt Steffen Welz, Einzelkanzlei in München: Zivilrecht mit Vertrags-, Verkehrs-, Miet-, Gesellschafts- und Erbrecht, Arbeitsrecht sowie Strafrecht und Ordnungswidrigkeiten.", "1.0"),
    ("kanzlei.html", "Person & Kanzlei – Rechtsanwalt Steffen Welz, München",
     "Steffen Welz, Rechtsanwalt seit 2010, seit 2011 mit eigener Kanzlei. Einzelkanzlei in Bürogemeinschaft mit Rechtsanwältin Sandra M. Rosar und Rechtsanwältin Lydia Bergida – keine Sozietät.", "0.8"),
    ("rechtsgebiete.html", "Rechtsgebiete – Rechtsanwalt Steffen Welz, München",
     "Zivilrecht, Arbeitsrecht sowie Strafrecht und Ordnungswidrigkeitenrecht: die Tätigkeitsgebiete von Rechtsanwalt Steffen Welz in München, gerichtlich und außergerichtlich.", "0.9"),
    ("zivilrecht.html", "Zivilrecht in München – Vertrags-, Verkehrs-, Miet-, Gesellschafts- und Erbrecht | RA Steffen Welz",
     "Rechtsanwalt Steffen Welz vertritt in gerichtlichen und außergerichtlichen Streitigkeiten des Zivilrechts: Vertragsrecht, Verkehrsrecht, Mietrecht, Gesellschaftsrecht und Erbrecht.", "0.8"),
    ("arbeitsrecht.html", "Arbeitsrecht in München – Kündigung, Abmahnung, Lohn, Zeugnis | RA Steffen Welz",
     "Arbeitsrecht bei Rechtsanwalt Steffen Welz, München: Kündigungen, Abmahnungen, Lohnforderungen, Zeugnisstreitigkeiten sowie Individual- und Kollektivarbeitsrecht.", "0.8"),
    ("strafrecht.html", "Strafrecht und Ordnungswidrigkeiten in München | RA Steffen Welz",
     "Rechtsanwalt Steffen Welz übernimmt strafrechtliche und ordnungswidrigkeitenrechtliche Mandate in München – vom Ermittlungsverfahren bis zum Bußgeldbescheid.", "0.8"),
    ("kontakt.html", "Kontakt & Anfahrt – Rechtsanwalt Steffen Welz, München",
     "Rechtsanwalt Steffen Welz, Schneckenburgerstraße 34, 81675 München. Telefon 08092 3059201, Mobil 0177 3258123, E-Mail info@rechtsanwalt-welz.de.", "0.7"),
    ("impressum.html", "Impressum – Rechtsanwalt Steffen Welz", "Impressum der Anwaltskanzlei Steffen Welz, München.", "0.2"),
    ("datenschutz.html", "Datenschutz – Rechtsanwalt Steffen Welz", "Datenschutzerklärung der Anwaltskanzlei Steffen Welz, München.", "0.2"),
    ("404.html", "Seite nicht gefunden – Rechtsanwalt Steffen Welz", "Diese Seite gibt es nicht.", None),
]

JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Attorney","name":"Rechtsanwalt Steffen Welz","url":"https://www.rechtsanwalt-welz.de/",
"telephone":"+49 8092 3059201","faxNumber":"+49 8092 3008308","email":"info@rechtsanwalt-welz.de",
"image":"https://www.rechtsanwalt-welz.de/assets/img/isar-weit-1600.jpg",
"address":{"@type":"PostalAddress","streetAddress":"Schneckenburgerstraße 34","postalCode":"81675","addressLocality":"München","addressCountry":"DE"},
"areaServed":"München","knowsAbout":["Zivilrecht","Vertragsrecht","Verkehrsrecht","Mietrecht","Gesellschaftsrecht","Erbrecht","Arbeitsrecht","Strafrecht","Ordnungswidrigkeitenrecht"]}
</script>"""

AKT = ' aria-current="page"'

SCHRIFTEN = [("Hanken Grotesk", "hanken-grotesk-latin-wght-normal.woff2", "100 900")]


def fonts_css():
    teile = ["/* Erzeugt von _quellen/build.py – Schriften lokal (SIL OFL 1.1), als Data-URI. */"]
    for name, datei, gewicht in SCHRIFTEN:
        b64 = base64.b64encode((WURZEL / "assets/fonts" / datei).read_bytes()).decode()
        teile.append(f'@font-face{{font-family:"{name}";font-style:normal;font-weight:{gewicht};font-display:swap;'
                     f'src:url(data:font/woff2;base64,{b64}) format("woff2");}}')
    (WURZEL / "assets/css/fonts.css").write_text("\n".join(teile) + "\n", encoding="utf-8")


def kopf(datei, titel, beschreibung):
    def aktuell(gruppe):
        return ' aria-current="page"' if datei in gruppe else ""

    desktop = "\n".join(f'        <li><a href="{h}"{aktuell(g)}>{n}</a></li>' for h, n, g in NAV)
    mobil = ['        <li><a href="index.html"' + (' aria-current="page"' if datei == "index.html" else "") + '>Start</a></li>']
    for h, n, g in NAV:
        mobil.append(f'        <li><a href="{h}"{AKT if datei == h else ""}>{n}</a></li>')
        if h == "rechtsgebiete.html":
            for uh, un in UNTER:
                mobil.append(f'        <li class="unterpunkt"><a href="{uh}"{AKT if datei == uh else ""}>{un}</a></li>')
    kanon = DOMAIN + ("" if datei == "index.html" else datei)
    robots = '\n  <meta name="robots" content="noindex">' if datei == "404.html" else f'\n  <link rel="canonical" href="{kanon}">'
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(titel)}</title>
  <meta name="description" content="{html.escape(beschreibung)}">{robots}
  <meta name="theme-color" content="#131b25">
  <meta property="og:title" content="{html.escape(titel)}">
  <meta property="og:description" content="{html.escape(beschreibung)}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <meta property="og:url" content="{kanon}">
  <meta property="og:image" content="{DOMAIN}assets/img/isar-weit-1600.jpg">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/fonts.css">
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
{desktop}
      </ul>
    </nav>
    <a class="kopf-tel" href="{{{{TEL_LINK}}}}">{{{{TEL}}}}</a>
    <button class="menue-knopf" type="button" aria-expanded="false" aria-controls="menue" data-menue-knopf>
      <span data-menue-text>Menü</span><span class="striche" aria-hidden="true"></span>
    </button>
  </div>
  <div class="menue" id="menue" hidden data-menue>
    <nav class="wrap" aria-label="Hauptnavigation mobil">
      <ul>
{chr(10).join(mobil)}
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
    <div class="fuss-oben">
      <div class="fuss-marke">
        <span class="marke-name" translate="no">Steffen Welz</span>
        <p>Rechtsanwalt · Einzelkanzlei<br>in Bürogemeinschaft, keine Sozietät</p>
      </div>
      <div>
        <h2>Kanzlei</h2>
        <p>{{ADRESSE}}</p>
        <p><a href="{{KARTE}}" target="_blank" rel="noopener">Auf der Karte ansehen ↗<span class="sr"> (OpenStreetMap, neues Fenster)</span></a></p>
      </div>
      <div>
        <h2>Kontakt</h2>
        <ul>
          <li><a href="{{TEL_LINK}}">Telefon {{TEL}}</a></li>
          <li><a href="{{MOBIL_LINK}}">Mobil {{MOBIL}}</a></li>
          <li>Telefax {{FAX}}</li>
          <li><a href="mailto:{{MAIL}}">{{MAIL}}</a></li>
        </ul>
      </div>
      <div>
        <h2>Rechtsgebiete</h2>
        <ul>
          <li><a href="zivilrecht.html">Zivilrecht</a></li>
          <li><a href="arbeitsrecht.html">Arbeitsrecht</a></li>
          <li><a href="strafrecht.html">Strafrecht &amp; Ordnungswidrigkeiten</a></li>
          <li><a href="kanzlei.html">Person &amp; Kanzlei</a></li>
        </ul>
      </div>
    </div>
    <div class="fuss-unten">
      <span>© 2026 Rechtsanwalt Steffen Welz · Mitglied der Rechtsanwaltskammer München</span>
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


KONTAKTBAND = """<section class="abschnitt dunkel" aria-labelledby="kontakt">
  <div class="wrap schluss-raster">
    <div class="zeige">
      <p class="marg">Kontakt</p>
      <h2 class="abschnitt-titel" id="kontakt">Ihr Anliegen besprechen</h2>
      <p class="einleitung">Rufen Sie an oder schreiben Sie eine E-Mail. Nennen Sie dabei, ob eine Frist läuft.</p>
    </div>
    <div class="zeige">
      <a class="schluss-tel" href="{{TEL_LINK}}">{{TEL}}</a>
      <ul class="schluss-wege">
        <li><span>Mobil</span> <a href="{{MOBIL_LINK}}">{{MOBIL}}</a></li>
        <li><span>E-Mail</span> <a href="mailto:{{MAIL}}">{{MAIL}}</a></li>
        <li><span>Kanzlei</span> <a href="kontakt.html">Schneckenburgerstraße 34, München</a></li>
      </ul>
    </div>
  </div>
</section>"""


def ersetze(text):
    text = text.replace("{{KONTAKTBAND}}", KONTAKTBAND)
    for k, v in ERSATZ.items():
        text = text.replace(k, v)
    return text


def baue():
    fonts_css()
    karte = []
    for datei, titel, beschreibung, prio in SEITEN:
        inhalt = (QUELLE / datei).read_text(encoding="utf-8").strip()
        seite = kopf(datei, titel, beschreibung) + '\n<main id="inhalt">\n' + inhalt + "\n</main>\n" + FUSS
        (WURZEL / datei).write_text(ersetze(seite), encoding="utf-8")
        if prio:
            karte.append(f"  <url><loc>{DOMAIN}{'' if datei == 'index.html' else datei}</loc><priority>{prio}</priority></url>")
        print("gebaut:", datei)
    (WURZEL / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                        + "\n".join(karte) + "\n</urlset>\n", encoding="utf-8")


if __name__ == "__main__":
    baue()
