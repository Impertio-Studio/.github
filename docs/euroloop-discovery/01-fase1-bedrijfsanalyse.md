# Fase 1 — Bedrijfsanalyse EuroLoop

> **Traject:** pre-sales discovery planningssoftware EuroLoop · **Opsteller:** Impertio Studio (Claude-ondersteund) · **Datum:** 25-08-2026
> **Leeswijzer betrouwbaarheid:** `[FEIT]` = publiek gebrond · `[UIT GESPREK]` = klant-claim uit het telefoongesprek (EUROLOOP_CONTEXT.md) · `[AANNAME]` = te verifiëren via de vragenlijst · `[NIET GEVONDEN]` = online niet aangetroffen.
> **Methodische noot:** de netwerk-proxy van de onderzoeksomgeving blokkeerde directe paginafetches (o.a. euroloop.nl, rva.nl); feiten komen uit zoekmachine-indexen van die bronnen plus het geverifieerde deel van `EUROLOOP_CONTEXT.md` in de repo.

## 1.1 Wat EuroLoop doet

| Aspect | Bevinding | Status |
|---|---|---|
| Kernactiviteit | Onafhankelijk kalibratie-instituut voor high-flow gas- en vloeistofmeters (custody-transfer/fiscale metingen, olie & gas); positioneert zich als grootste en nauwkeurigste ter wereld | `[FEIT]` — [euroloop.nl](https://euroloop.nl/), [Kiwa 2017](https://www.kiwa.com/en/media/news/2017/euroloop-and-kiwa-united-in-worldwide-oil-and-gas-calibration-market/) |
| Locatie | Petroleumweg 36, 3196 KD Vondelingenplaat (Botlek, Rotterdam) | `[FEIT]` — RvA, KvK-aggregators |
| Faciliteiten | Twee aangrenzende closed-loop testfaciliteiten: vloeistof (tot ~4.500 m³/h, piston provers, onzekerheid <0,02%, viscositeiten 1/10/100 cSt) en hogedruk-aardgas (2"–30", 1–65 bar, 5 meetstraten, 16 mastermeters, ATEX zone 1) | `[FEIT]` — [Rotork-case](https://www.rotork.com/en/casestudies/valve-actuation-at-the-worlds-largest-flow-metering-calibration-facility), [NFOGM-paper](https://nfogm.no/wp-content/uploads/2019/02/2007-13-EuroLoop-Metrological-concepts-for-efficient-calibrations-van-der-Beek-Netherlands-Measurement-institute.pdf) |
| Derde medium | Pagina "Air Calibration" bestaat op euroloop.nl; specificaties onbekend | `[AANNAME]` — verifiëren |
| Klanten | Meterfabrikanten (typetests, fabriekskalibratie) en eindgebruikers (raffinaderijen, terminals, pipeline-operators), wereldwijd | `[FEIT]` — Kiwa 2017; klantnamen `[NIET GEVONDEN]` |
| Accreditatie | ISO/IEC 17025:2017, RvA-registratie **K161** op naam van **EuroLoop Calibrations B.V.**, scope geldig 19-12-2024 t/m 01-01-2029; via RvA/ILAC wereldwijd erkend | `[FEIT]` — [rva.nl K161](https://www.rva.nl/en/alle-geaccrediteerden/k161/) |
| Omvang | ±35 medewerkers ("ruim 35", drie ploegen ma–vr); LinkedIn-klasse 11–50. Omzet `[NIET GEVONDEN]` | `[FEIT]` — [watertalent.nl](https://www.watertalent.nl/nl/euroloop) |
| Directie | Dick van Driel (Managing Director) | `[FEIT]` — LinkedIn, Ondernemen010 |
| Recente ontwikkeling | Haalbaarheidsonderzoek kalibratiecentrum voor waterstof-flowmeters (Rotterdams "Hydro Generation"-initiatief) | `[FEIT]` (datering onzeker) — [Ondernemen010](https://www.ondernemen010.nl/actueel/door-betrouwbaar-meten-van-waterstof-maken-we-een-internationale-markt-mogelijk/) |

## 1.2 De aangesloten bedrijven

### Juridische structuur: drie EuroLoop-entiteiten op één adres `[FEIT]`

| Entiteit | Registratie | Vermoedelijke rol |
|---|---|---|
| EuroLoop B.V. | Drimble-dossier 24369667; KvK 54624401 volgens Creditsafe (onderling strijdige bronnen — uittreksel opvragen) | `[AANNAME]` oorspronkelijke/facilitaire entiteit |
| EuroLoop Calibrations B.V. | KvK 68215738, opgericht 03-03-2017 (samenvallend met Kiwa-herstructurering); houder van de RvA-accreditatie | `[FEIT]` operationele, geaccrediteerde kalibratie-entiteit |
| EuroLoop Services B.V. | KvK 62038680, opgericht ±2014; SBI "overige keuring en controle" | `[AANNAME]` mogelijk de entiteit achter "MNR" |

Aandeelhoudersverhoudingen per B.V. en welke entiteit met klanten (en met ons) contracteert: `[NIET GEVONDEN]` → **vragenlijst**.

### Eigendom en partners

- **Kiwa** — sinds 1-2-2017 partner; "EuroLoop management and Kiwa as an independent third party control the company" — dus gezamenlijke zeggenschap ter borging van onafhankelijkheid, geen gewone samenwerking en geen geïntegreerde Kiwa-dochter. Exact belang `[NIET GEVONDEN]`. `[FEIT]` — [Kiwa 2017](https://www.kiwa.com/en/media/news/2017/euroloop-and-kiwa-united-in-worldwide-oil-and-gas-calibration-market/). Kiwa zelf is sinds 2021 onderdeel van SHV Holdings `[FEIT]`.
- **TNO** — oprichter (2009, geopend 2010 als "NMi EuroLoop"); uitgetreden bij de ontvlechting van 2017. `[FEIT]`. Let op: TNO is sinds 2024 weer 100% eigenaar van VSL, de herleidbaarheidsbron van EuroLoop. `[FEIT]`
- **KROHNE** — betrokken bij de oprichting, uitgetreden 2017; vermoedelijk nog klant. `[FEIT]` historie, `[AANNAME]` klantrol.
- **VSL / NMi** — metrologische keten (herleidbaarheid resp. certificering/naamhistorie), geen eigendomsband sinds 2017. `[FEIT]`/`[AANNAME]`.
- **MNR (meter maintenance & repair)** — intern gepositioneerd als "een apart bedrijf … niet je collega; er moet een goede werkorder gemaakt worden" `[UIT GESPREK]`. Publiek spoor: `[NIET GEVONDEN]` (geen KvK-inschrijving, vacature of LinkedIn onder die naam). Hypothese: interne unit of ondergebracht in EuroLoop Services B.V. → **kernvraag vragenlijst**.

### Bestaand softwarelandschap rond het proces `[FEIT — cruciale vondst]`

Minstens drie externe partijen hebben eerder software rond exact dit proces gebouwd:

1. **iHomer** — "administratief systeem dat kalibraties begeleidt van offerte, via planning en daadwerkelijke kalibratie, tot facturatie" ([case "Euroloop Calibration Flow"](https://www.ihomer.nl/cases/euroloop)).
2. **Bisbrick** — no-code/low-code "Flow web application" voor kalibratieprocesoptimalisatie ([project](https://www.bisbrick.com/en/project/euroloop-calibration-management)); ook de backend van het eerdere klantportaal-prototype (`euroloop-portal`, zie EUROLOOP_CONTEXT.md deel 3).
3. **Beyonder** — CVT (Calibration Verification Tool), online analysetool voor kalibratiedata ([case](https://beyonder.eu/en/cases/euroloop)).

Daarnaast: "My Euroloop"-klantportaal op euroloop.nl (inhoud onbekend) en het remote-witness-systeem **witness.euroloop.nl** (`[UIT GESPREK]`; online `[NIET GEVONDEN]`). Wat hiervan nog draait, wie wat onderhoudt en wat het nieuwe systeem vervangt versus koppelt, is **de belangrijkste onopgeloste systeemvraag** van dit traject.

## 1.3 Bedrijfsprocessen die om planning draaien

Kernproces volgens de klant zelf (`[UIT GESPREK]`, EUROLOOP_CONTEXT.md §2.1): **offerte → order → werkvoorbereiding (DCS) → planning → uitvoering → rapportage**, met planning expliciet benoemd als *"het hart van flow"*, ±3 kalibraties per dag, en de kalibratiedatum al tijdens sales afgesproken.

| Proces | Planningscomponent | Status |
|---|---|---|
| Loop-capaciteit | Slots per dag per loop; twee parallelle agenda's (gas/vloeistof) met gedeelde resources; volgorde-afhankelijke omsteltijden (diameterwissel, viscositeitswissel/spoelen, druk op- en afbouw) | `[UIT GESPREK]` 3/dag; omstellogica `[SECTOR-AANNAME]` |
| Personeel | Drie ploegen ma–vr `[FEIT]`; dedicated plannersrol bestaat(-de) ("Senior Planner" bij NMi EuroLoop, [salary.com](https://www.salary.com/research/company/nmi-euroloop/senior-planner-salary?cjid=18274140)); overige rollen (operators, monteurs, metrologen, tekenbevoegden 17025) `[SECTOR-AANNAME]` |
| Meterlogistiek | Aanvoer/afvoer van zware meters (tonnen, tot 30"), inslag → inbouw met spools → uitbouw → retour; shipping- en materiaalstatus zijn in het portal-prototype aparte statussen | `[FEIT]` portal-velden; procesdetails `[SECTOR-AANNAME]` |
| Witnesses | Klanten wonen kalibraties bij (on-site of remote); reis- en **hotelcoördinatie is gekoppeld aan de planning** ("mensen hebben soms al een hotel in de avond ervoor") | `[UIT GESPREK]` |
| MNR | Meter komt binnen "als bij de garage" → diagnose → reparatie → overdracht; meterdata wordt nu handmatig hertypt; reparatie kan herkalibratie vereisen (terug de loop-agenda in) | `[UIT GESPREK]`; herkalibratie-flow `[AANNAME]` |
| Onderhoud faciliteit | Herkalibratie mastermeters/provers, compressor-/kleponderhoud, RvA-audits blokkeren loop-capaciteit | `[SECTOR-AANNAME]` |
| Certificering | 17025-regime: review en geautoriseerde ondertekening vóór certificaatuitgifte; aparte wachtrij na de meetdag | `[SECTOR-AANNAME]` |

**Waarom standaardsoftware hier knelt** `[ANALYSE]`: gangbare kalibratiemanagement-pakketten (IndySoft, Fluke MET/TEAM, Beamex CMX) zijn gebouwd rond recall-cycli van instrumentenparken, niet rond capaciteitsplanning van één schaarse faciliteit met volgorde-afhankelijke omsteltijden, meterlogistiek én witness-/hotelcoördinatie. Dat verklaart waarom EuroLoop al drie keer maatwerk liet bouwen — en het is het commerciële argument voor dit traject.

## 1.4 Samenvatting fase 1

1. EuroLoop is een **klein (±35 fte), hooggespecialiseerd, internationaal opererend** kalibratie-instituut waarvan de omzet draait om schaarse loop-tijd; planning is letterlijk door de klant benoemd als het hart van het gewenste systeem.
2. "De aangesloten bedrijven" blijken een **groep van drie B.V.'s** plus de intern als apart bedrijf gepositioneerde unit **MNR**; de juridische en administratieve scheiding (facturatie, klantdossiers, planning-overdracht kalibratie↔reparatie) is publiek niet vast te stellen en moet via de vragenlijst.
3. Er is een **voorgeschiedenis van minstens drie softwaretrajecten** (iHomer, Bisbrick, Beyonder) rond hetzelfde proces; het lot daarvan bepaalt scope, migratie en integraties van ons aanbod.
4. De grootste kennisgaten: entiteitenstructuur/MNR, actueel systeemlandschap, capaciteits- en omstelregels, witness-/hotelproces, en alles rond certificering/koppeling met de procesautomatisering.
