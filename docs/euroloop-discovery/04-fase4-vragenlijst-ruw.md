# Fase 4 (ruwe versie) — Vragenlijst offertevorming EuroLoop

> **Status: ruwe werkversie.** Deze lijst is de directe vertaling van de gap-analyse (fase 3). De definitieve, klant-klare versie ontstaat door deze lijst door de Template orchestrator-methodiek te halen (kompasvragen front-loaden, expert-review, klanttaal-redactie) — zie `05-vragenlijst-definitief.md`.
> Per vraag: **(a)** de vraag in klanttaal · **(b)** waarom we dit vragen · **(c)** welk offerte-element het antwoord bepaalt.

## Thema 1 — Planningsprocessen

- **V-01** (a) Loop ons in gedachten eens door een gemiddelde kalibratie-opdracht heen, van offerte tot certificaat: wie doet wat, en waar wordt gewacht? (b) Valideert de procesvolgorde waarop de hele demo is gebouwd; onthult uitzonderingen. (c) Scope + uren (procesbreedte).
- **V-02** (a) Wij gaan uit van zo'n 3 kalibraties per dag. Klopt dat, en is dat per testinstallatie (gas/vloeistof) of in totaal? (b) De klant-claim "3/dag" is onbevestigd; bepaalt het capaciteitsmodel. (c) Uren (complexiteit plannings-engine).
- **V-03** (a) Wat bepaalt of twee opdrachten ná elkaar handig of juist onhandig zijn — bijvoorbeeld ombouwtijd bij een andere metermaat of het wisselen van vloeistof? (b) Beslist of een simpel slot-model volstaat of dat volgorde-/omstelregels nodig zijn (groot verschil in bouwwerk). (c) Uren + fasering.
- **V-04** (a) Wanneer is een opdracht "klaar om ingepland te worden" — wat moet er dan al binnen of geregeld zijn (meter aanwezig, specificaties compleet, betaling)? (b) Definieert de gereedheids-check die de planner nu uit zijn hoofd doet. (c) Scope.
- **V-05** (a) Hoe vaak schuift een geplande kalibratie, en waardoor meestal (klant, transport/douane, techniek)? Wat moet er dan allemaal geregeld worden? (b) Herplanning en het kettingeffect (witness, hotel, vloer) zijn de duurste momenten; bepaalt hoeveel het systeem daarvan moet dragen. (c) Scope + uren.
- **V-06** (a) Hoe krijgt de werkvloer nu zijn opdracht (werkorder, briefing, lijst), en wat moet daarop staan? (b) Werkorder bestaat in de demo alleen als vinkje; bepaalt of een vloer-module nodig is. (c) Scope + fasering.
- **V-07** (a) Wie regelt bezoekers die een kalibratie bijwonen (aanmelding, toegang tot het terrein, hotel) — en boekt EuroLoop hotels zelf of doet de klant dat? (b) Bepaalt of witness/hotel registratie blijft of een boekings-/communicatiefunctie moet worden. (c) Scope.
- **V-08** (a) Welk gepland onderhoud of welke keuringen blokkeren de installaties (bijv. herkalibratie van jullie eigen referentiemeters), en wie plant dat nu? (b) Onderhoudsvensters concurreren om dezelfde capaciteit. (c) Scope.
- **V-09** (a) Hoe ver vooruit staat de agenda vol, en hoe hard is een datum die sales met de klant afspreekt? (b) Bepaalt de bewaking "belofte vs. planning" (kernscenario demo). (c) Uren.

## Thema 2 — Gebruikers en rollen

- **V-10** (a) Welke functies/rollen gaan met het systeem werken, met hoeveel mensen per rol? (Denk aan: verkoop, werkvoorbereiding, planning, operators, monteurs (MNR), management, administratie.) (b) De zes demo-rollen zijn verzonnen; dit bepaalt het rechtenmodel én de gebruikersaantallen. (c) Licenties + uren (rechtenmodel).
- **V-11** (a) Wie mag prijzen en offertebedragen zien — iedereen of alleen verkoop/management? (b) Veld-afscherming van prijzen is bouwerk; nu ziet (technisch) iedereen alles. (c) Uren.
- **V-12** (a) Moeten er ook mensen van buiten in het systeem kunnen kijken — klanten, auditors (RvA), Kiwa, de machinebouwer? (b) Externe toegang verandert beveiligings- en licentiemodel wezenlijk. (c) Scope + licenties.
- **V-13** (a) In welke taal moet het systeem werken: Nederlands, Engels of beide? (b) De demo is NL met Engelse vaktermen; meertaligheid raakt elk scherm. (c) Uren.
- **V-14** (a) Werken de drie ploegen ook 's nachts met het systeem, en wie lost dan problemen op? (b) Bepaalt beschikbaarheids- en supporteisen. (c) Scope (SLA) + fasering.

## Thema 3 — Aangesloten bedrijven en samenwerking

- **V-15** (a) Er staan drie EuroLoop-vennootschappen ingeschreven (EuroLoop B.V., EuroLoop Calibrations B.V., EuroLoop Services B.V.). Welke doet wat, en welke gaat dit contract aan? (b) Publiek niet vast te stellen; bepaalt contractpartij én of het systeem meerdere administraties moet scheiden. (c) Scope + licenties.
- **V-16** (a) Is MNR (meteronderhoud en -reparatie) een eigen vennootschap met eigen administratie en facturatie, of een afdeling die als apart bedrijf wérkt? (b) "Apart bedrijf" kan commercieel of juridisch zijn — dat scheelt een compleet gescheiden administratie-inrichting. (c) Scope + uren + licenties.
- **V-17** (a) Als een meter na reparatie opnieuw gekalibreerd moet worden: hoe loopt die overdracht nu, en wat moet er automatisch meegaan (metergegevens, klant, historie)? (b) Het scherpst benoemde pijnpunt (hertypen); bepaalt de overdracht-flow en het gedeelde meterregister. (c) Scope.
- **V-18** (a) Speelt Kiwa een rol in de dagelijkse systemen of rapportages (bijv. verplichte rapportagelijnen), of alleen als aandeelhouder? (b) Bepaalt of er rapportage-/toegangseisen van bovenaf zijn. (c) Scope.

## Thema 4 — Integraties (mail, agenda, ERP, boekhouding)

- **V-19** (a) Welk mailplatform gebruiken jullie (Microsoft 365/Outlook, Google, anders), en werken jullie met gedeelde mailboxen (zoals info@ of planning@) of ieder zijn eigen postbus? (b) De mailkoppeling is de kern van het hele traject; platform en mailboxstructuur bepalen de bouwroute. (c) Scope + uren — grootste maatwerkblok.
- **V-20** (a) Hoe zou een binnenkomende mail bij de juiste opdracht terecht moeten komen: zetten jullie een kenmerk in het onderwerp, moet het systeem het slim herkennen, of wijst iemand hem handmatig toe? (b) Dé haalbaarheidsvraag achter mail-op-het-dossier; elk antwoord is een andere oplossing met andere kosten. (c) Uren + fasering.
- **V-21** (a) Mogen alle collega's klantcorrespondentie kunnen teruglezen, en hoe lang moet die bewaard blijven (privacy/AVG)? (b) Correspondentie breed leesbaar maken is juridisch gevoelig; retentie bepaalt archiefbouw. (c) Scope + uren.
- **V-22** (a) Welke systemen draaien er nu rond dit proces — het door iHomer gebouwde "Flow", het Bisbrick-platform, de Calibration Verification Tool (Beyonder), My Euroloop, het remote-witness-systeem — en wat moet het nieuwe systeem vervangen, en waarmee moet het samenwerken? (b) Bepaalt de systeemgrens: vervangen vs. koppelen vs. laten staan. Zonder dit geen scope. (c) Scope + migratie + fasering.
- **V-23** (a) Waarom is het eerdere klantportaal (met de stap-voor-stap intake) er niet gekomen — wat werkte daar niet? (b) Wij willen die fout niet herhalen; de les bepaalt onze aanpak van de intake. (c) Scope + fasering (risicobeheersing).
- **V-24** (a) Hoe komt de ingevulde specificatie (DCS) nu bij de procesautomatisering die de fabriek instelt — een bestand, een koppeling, of typt iemand het over? En wie beheert die automatisering? (b) Interfacevorm en eigenaarschap bepalen een van de duurste koppelingen (afhankelijkheid van derde partij). (c) Uren + risico-opslag + fasering.
- **V-25** (a) Met welk boekhoud-/facturatiepakket werken jullie, en moet het nieuwe systeem facturen aanmaken, doorgeven of alleen voorbereiden? (b) Facturatie zat bewust niet in de demo maar hoort bij "van offerte tot factuur". (c) Scope + uren.
- **V-26** (a) Gebruiken jullie een gedeelde agenda (Outlook/Teams) voor de planning, en moet de nieuwe planning daarin zichtbaar zijn? (b) Agenda-sync is vaak een stille verwachting die laat opduikt. (c) Scope.
- **V-27** (a) Zijn er nog andere plekken waar planning of opdracht-informatie leeft — whiteboard, WhatsApp, Excel-lijsten, papieren mappen? (b) Schaduw-administratie onthult verborgen eisen. (c) Scope.

## Thema 5 — Data en migratie

- **V-28** (a) Waar staan nu de klantgegevens, de prijstabel en het meterbestand — en kunnen we daar exports van krijgen (Excel/CSV)? (b) Migratiebronnen en exporteerbaarheid zijn de nummer-1 reden dat vaste prijzen onder druk komen. (c) Uren + risico-opslag.
- **V-29** (a) Om hoeveel gaat het ongeveer: klanten, meters, kalibraties per jaar, lopende offertes? (b) Volumes bepalen migratie-omvang én performance-eisen. (c) Uren.
- **V-30** (a) Hoeveel historie moet mee naar het nieuwe systeem — alleen lopende zaken, een paar jaar, of alles? (b) Klassieke scope-afbakening; "alles" is een veelvoud van "lopend". (c) Uren + fasering.
- **V-31** (a) Moet oude e-mailcorrespondentie van lopende opdrachten mee het systeem in, of beginnen we schoon? (b) Mailhistorie migreren is wezenlijk ander werk dan vanaf nu koppelen. (c) Uren + fasering.
- **V-32** (a) Wie bij jullie kan tijd vrijmaken om data te controleren en op te schonen? (b) Datakwaliteit is klantverantwoordelijkheid; zonder eigenaar loopt migratie uit. (c) Fasering + aannames in offerte.
- **V-33** (a) Welke vaste gegevens moeten we vooraf inladen: de normen waartegen jullie kalibreren met bijbehorende meetreeksen, de installatiegrenzen (maten/gewichten), de prijstabel? (b) De demo-normbibliotheek is verzonnen; deze referentiedata bepaalt de configuratie-inspanning. (c) Uren.

## Thema 6 — Niet-functionele eisen (beveiliging, beschikbaarheid, devices)

- **V-34** (a) Waar moet het systeem draaien: in de cloud, of (deels) op eigen servers — en zijn er klanten of auditors die daar eisen aan stellen? (b) Hosting-keuze bepaalt infra-inrichting en terugkerende kosten. (c) Licenties/hosting + scope.
- **V-35** (a) Welke eisen stelt jullie ISO/IEC 17025-accreditatie (RvA) aan software: denk aan wie-wijzigde-wat-vastlegging, bevriezen van meetgegevens na certificering, tekenbevoegdheid? (b) Compliance-eisen zijn niet-onderhandelbaar en bepalen kernontwerp (audittrail, versiebeheer). (c) Scope + uren.
- **V-36** (a) Op welke apparaten wordt gewerkt: kantoor-pc's, schermen in de controlekamer, tablets op de werkvloer? Zijn er zones waar apparatuur beperkt is (ATEX)? (b) Devices bepalen responsive/mobiel-scope; de offline/mobiele laag is nu ongebruikt. (c) Scope + uren.
- **V-37** (a) Wat mag er maximaal gebeuren als het systeem er een uur uit ligt — en een dag? (b) Vertaalt zich naar beschikbaarheids-/back-up-eisen en SLA. (c) Licenties/hosting + SLA-prijs.
- **V-38** (a) Wat moet er gebeuren met de slimme assistent (AI) uit de demo — is dat iets voor de eerste oplevering of later? (b) AI-assistent vergt API-kosten, beheer en gegevensafspraken; bewuste go/no-go nodig. (c) Scope + fasering + terugkerende kosten.

## Thema 7 — Budget en doorlooptijd

- **V-39** (a) Is er een richtbedrag of budgetbandbreedte voor dit traject? (b) Expliciet richtbedrag voorkomt een stil anker en stuurt de pakketindeling — het is een toets, geen rekenbasis. (c) Pakketindeling + fasering.
- **V-40** (a) Wanneer moet het eerste bruikbare deel draaien, en is er een harde deadline (bijv. vóór een audit of drukke periode)? (b) Deadline bepaalt fasering en teaminzet. (c) Fasering + uren.
- **V-41** (a) Wat moet er minimaal werken om te zeggen: "dit is geslaagd"? Noem 2–3 concrete uitkomsten. (b) Succescriteria = de kern van pakket "Basis" en de acceptatiegrens. (c) Scope + pakketindeling.
- **V-42** (a) Zijn er onderdelen die u bewust NIET in dit traject wil — bijvoorbeeld het klantportaal, facturatie of de koppeling met de fabriek? (b) De buiten-scope-lijst is de belangrijkste bescherming van een vaste prijs. (c) Scope (buiten-scope-lijst).
- **V-43** (a) Wie is bij jullie de beslisser voor dit traject, en wie zijn de aanspreekpunten per onderwerp (planning, techniek/automatisering, administratie)? Kunnen zij wekelijks tijd vrijmaken? (b) Beschikbaarheid van beslissers/testers is een prijsaanname met gevolg-als-onjuist. (c) Fasering + aannames in offerte.
- **V-44** (a) Hoe wilt u betalen: per mijlpaal, per fase, of anders? (b) Betaalritme hoort in de offerte. (c) Offerte-voorwaarden.

## Top-5 vragen met de grootste invloed op de prijs

1. **V-22 — Systeemgrens**: wat vervangen we en waarmee koppelen we (iHomer-Flow, Bisbrick, CVT, portalen)? *Elke extra koppeling of overname is een eigen bouwblok; dit kan de scope zomaar verdubbelen.*
2. **V-19/V-20 — Mailplatform + job-matching**: de kern van het maatwerk; het antwoord bepaalt of dit een beheersbare koppeling is of een groot integratieproject.
3. **V-16 — Juridische status MNR**: één administratie met rollen, of gescheiden administraties/facturatie voor meerdere entiteiten — een structureel scope-verschil.
4. **V-24 — Koppeling procesautomatisering**: onbekende interface bij een derde partij = grootste risico-opslag of expliciete uitsluiting.
5. **V-28/V-29/V-30 — Migratiebronnen en -omvang**: het klassieke vaste-prijs-risico; bepaalt uren én aannames-hoofdstuk.
