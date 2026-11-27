# Website Rechtsanwalt Steffen Welz – Entwurf

Statische Website (HTML, CSS, wenig JavaScript), kein Build-Schritt nötig, läuft auf jedem Webspace und per Doppelklick auf `index.html`.

## Gestaltung – Leitidee „Direkt zum Anwalt“
Einzelkanzlei = ein Ansprechpartner. Die Startseite beginnt mit einem Satz, der zugleich in die drei Rechtsgebiete führt (verlinkt), darunter das Isar-Bild mit versetzter Bordeaux-Fläche und dem dunklen Feld „Direkt zum Anwalt“ (Telefon, Mobil, E-Mail) als einzige Handlung. Wortmarke „Steffen Welz.“ mit Bordeaux-Punkt, Navigation als ruhige Insel mit hervorgehobenem aktivem Punkt.
Durchgehend Hanken Grotesk (variabel), keine Kursiven; Buttons und Flächen mit 7–10 px Radius. Farben: Papier `#faf8f3`/`#f3efe7` als Grund, Bordeaux `#7a2a34`/`#6b2530` als Markenfläche (Kanzlei-Abschnitt, Frist-Hinweise), Tinte `#131b25` nur für Text, Direkt-Feld und Fuß.
Unterseiten: Zivilrecht mit Bereichsindex im Kopf und zweispaltigen Kapiteln; Arbeits- und Strafrecht mit eigenem Hinweis im Kopf (3-Wochen-Frist bzw. Schweigerecht) und Themenleiste; Person & Kanzlei mit Werdegang; Kontakt als Kontaktliste mit Anfahrt.
Kontaktformular bewusst nicht umgesetzt (bräuchte serverseitiges Skript/Hosting-Konfiguration); Kontakt über Telefon/E-Mail-Links.
Orientierung (nur Prinzipien): Kliemt (Wortmarke, eine Markenfarbe), YPOG (selbstbewusste Typo-Aussage, weiche Bauteile), SKW Schwarz (versetzte Farbfläche hinter Bild), Uta Hervol (eine tragende Leitidee).

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
