# Website Rechtsanwalt Steffen Welz – Entwurf

Statische Website (HTML, CSS, wenig JavaScript), kein Build-Schritt nötig, läuft auf jedem Webspace und per Doppelklick auf `index.html`.

## Gestaltung
Ruhig, zeitgemäß, ohne klassische Kanzlei-Symbolik. Durchgehend eine Schrift (Hanken Grotesk, variabel) mit unterschiedlichen Gewichten, keine Kursiven. Buttons und Bildflächen mit 8–10 px Radius, Navigation mit dezent hinterlegtem aktivem Punkt, Telefon als dunkler Button. Startseite: Name und Leitsatz links, Einleitung und Aktionen rechts, darunter ein breites Isar-Bild und die Kontaktleiste. Rechtsgebiete als nummeriertes Register (01–03), Hinweise als ruhige Papierflächen.
Farben: Tinte `#131b25`, Papier `#f3efe7`/`#faf8f3`, Bordeaux `#7a2a34` als einziger Akzent.

## Seiten
`index` · `kanzlei` (Person, Werdegang, Bürogemeinschaft) · `rechtsgebiete` (Übersicht, Ablauf, Kosten) · `zivilrecht` (Vertrags-, Verkehrs-, Miet-, Gesellschafts-, Erbrecht) · `arbeitsrecht` · `strafrecht` (inkl. Ordnungswidrigkeiten) · `kontakt` · `impressum` · `datenschutz` · `404`, dazu `robots.txt`, `sitemap.xml`.

## Pflege
Inhalte in `_quellen/seiten/*.html`; Kopf, Fuß, Kontaktdaten, Metadaten in `_quellen/build.py`. Danach `python3 _quellen/build.py`.

## Technik
Keine Cookies, kein Tracking, keine externen Dienste/CDNs. Kartenlink nur zu OpenStreetMap. Einblendungen respektieren „Bewegung reduzieren“; ohne JavaScript bleibt alles sichtbar.

## Quellen
Alle Kanzleidaten von www.rechtsanwalt-welz.de (abgerufen 26.11.2026). Nicht übernommen: Meldungen unter „Aktuelles“ (sprechen fälschlich von „Sozietät“), Google-Maps-Koordinaten (zeigen nicht auf die Schneckenburgerstraße), Reste fremder Kanzleien in der alten Datenschutzerklärung.
Rechtliche Hinweistexte (Fristen) beruhen auf den genannten Normen: § 4 KSchG, § 67 OWiG, § 410 StPO, § 1944 BGB, §§ 195, 199 BGB, § 556 Abs. 3 BGB, § 109 GewO, § 12a ArbGG, § 136 StPO.

## Bilder und Lizenzen
| Datei | Quelle | Lizenz |
|---|---|---|
| `assets/img/isar-*.jpg` | Khyati Trehan, Unsplash, „Wittelsbacherbrücke, München“ | Unsplash-Lizenz |
| Schrift | Hanken Grotesk | SIL OFL 1.1 (`assets/fonts/LICENSE-*`) |

## Offen – vom Kanzleiinhaber zu bestätigen (intern)
1. **Festnetz/Fax mit Vorwahl 08092** (Grafing) bei Kanzleisitz München – bitte bestätigen.
2. **Branchenbuch muenchen.de nennt Obermaierstr. 2, 80538 München**, die eigene Website Schneckenburgerstraße 34, 81675 München. Verwendet: Angabe der eigenen Website. Aktuelle Anschrift klären.
3. **Porträtfoto** fehlt (alte Seite nur 135 × 180 px). Ein professionelles Porträt passt auf `kanzlei.html` und optional in den Auftakt der Startseite.
4. **Impressum:** Anschrift der Rechtsanwaltskammer München sowie Anschrift und räumlicher Geltungsbereich der Berufshaftpflichtversicherung ergänzen; Hinweis zur Verbraucherstreitbeilegung ergänzen.
5. **Datenschutz:** Hosting-Anbieter (Auftragsverarbeitung) und Speicherdauer der Logfiles ergänzen; Text vor Veröffentlichung rechtlich prüfen.
6. **Werdegang:** frühere Bürogemeinschaften mit Namen – Veröffentlichung bestätigen; Vorname „Kollegin Leucht“ fehlt.
7. **Fachtexte** zu den Rechtsgebieten (Beispiele typischer Anliegen, Fristen-Hinweise) sind neu formuliert und vom Anwalt fachlich freizugeben, ebenso ob Arbeitgeber- und/oder Arbeitnehmerseite vertreten wird.
8. **Sprechzeiten** sind nicht bekannt und daher nicht angegeben.
