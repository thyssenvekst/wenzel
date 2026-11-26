# Website Rechtsanwalt Steffen Welz

Statische Website (HTML, CSS, JavaScript) ohne Build-Schritt, lauffähig auf jedem Webspace.

## Starten

`index.html` im Browser öffnen oder lokal ausliefern:

```
python3 -m http.server 8000
```

## Seiten

`index.html`, `kanzlei.html` (Person, Werdegang, Bürogemeinschaft), `rechtsgebiete.html`, `kontakt.html` (inkl. Anfahrt), `impressum.html`, `datenschutz.html`, `404.html`, dazu `robots.txt` und `sitemap.xml`.

## Pflege

Inhalte: `_quellen/seiten/*.html`. Kopf, Navigation, Fuß und Kontaktdaten zentral in `_quellen/build.py`. Nach Änderungen `python3 _quellen/build.py` ausführen.

## Technik

- Keine Cookies, kein Tracking, keine externen Dienste oder CDNs; Karte nur als Link zu OpenStreetMap.
- Schriften lokal: Source Serif 4 und Hanken Grotesk (SIL Open Font License 1.1).
- Dezente Einblend-Animation per IntersectionObserver; respektiert „Bewegung reduzieren“, ohne JavaScript ist alles sichtbar.
- Quelle aller Inhalte: www.rechtsanwalt-welz.de (Stand 26.11.2026). Nicht übernommen: Platzhalter „Neues Textfeld“, Baukasten-Meldungen unter „Aktuelles“ (sprachen fälschlich von „Sozietät“), Google-Analytics-Abschnitt der alten Datenschutzerklärung (neue Seite nutzt kein Tracking).

## Offene Punkte – vom Kanzleiinhaber zu bestätigen (intern)

1. **Festnetz 08092 3059201 / Fax 08092 3008308:** Vorwahl 08092 gehört zu Grafing b. München, die Kanzlei sitzt in München (81675). Nummern bitte bestätigen.
2. **Porträtfoto:** Auf der alten Seite nur in 135 × 180 px vorhanden – zu klein. Die Seite ist bewusst typografisch gestaltet; ein professionelles Porträt kann auf `kanzlei.html` ergänzt werden.
3. **Impressum:** Anschrift der Rechtsanwaltskammer München, Anschrift und räumlicher Geltungsbereich der Berufshaftpflichtversicherung (Allianz) ergänzen. Optional: Hinweis zur Verbraucherstreitbeilegung / Schlichtungsstelle der Rechtsanwaltschaft.
4. **Datenschutz:** Hosting-Anbieter (Auftragsverarbeiter, bisher IONOS) und Speicherdauer der Server-Logfiles ergänzen; Text vor Veröffentlichung rechtlich prüfen. Keine Konformitätsaussage durch diese Vorlage.
5. **Domain:** Canonical-URLs, `sitemap.xml` und `robots.txt` gehen von https://www.rechtsanwalt-welz.de/ aus.
6. **Werdegang:** Enthält die früheren Bürogemeinschaften mit Namen wie auf der alten Website – Veröffentlichung bitte bestätigen. Vorname der „Kollegin Leucht“ (2013) fehlt in der Quelle.
7. **Kontaktformular:** Die alte Website erwähnt ein Formular, hat aber keines. Die neue Seite verzichtet bewusst darauf (Telefon/E-Mail); ein Formular bräuchte ein serverseitiges Skript.
