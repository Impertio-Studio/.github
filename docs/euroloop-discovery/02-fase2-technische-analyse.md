# Fase 2 — Technische analyse `euroloop-app`

> **Repository:** [Impertio-Studio/euroloop-app](https://github.com/Impertio-Studio/euroloop-app) (fork van `impertio-frappe-react-template`) · analyse op commit `657e481` (shallow clone) · **Datum:** 25-08-2026
> **Belangrijkste kwalificatie vooraf:** dit is **geen wildgegroeid productiesysteem maar een bewust gebouwde demonstrator** ("This is a demo, not a delivery" — USER_STORIES.md). Het *wildgegroeide systeem* dat vervangen moet worden is het **echte werkproces bij EuroLoop**: Excel-offertes + de mailbox als planningssysteem. De app modelleert dat probleem en het beoogde antwoord erop.

## 2.1 Architectuur, stack en structuur

- **Ontkoppelde architectuur:** Frappe ≥15 backend (Python, MariaDB) + React 19 SPA (Vite 8, TypeScript strict, Tailwind 4, shadcn/radix, frappe-react-sdk/SWR, Redux Toolkit voor UI-state). Same-origin-opzet (Vite-proxy in dev, Frappe of nginx serveert de build in prod), cookie-sessies + CSRF-endpoint (`euroloop/api/csrf.py`).
- **Template-erfenis:** upstream-sync-workflow haalt template-fixes binnen als PR; theming via één seam (`theme.css` + `app.config.ts`, nog onaangepast — demo draait op template-branding). Volledige offline/Capacitor-laag (SQLite + outbox-sync, `frontend/src/sync|db|data|platform`) aanwezig maar **door de demo niet gebruikt** en alleen geconfigureerd voor het template-doctype `Example Task`.
- **Status "HALF-MIGRATED"** (letterlijk in `frontend/src/main.tsx:41-52`): echte Frappe-auth en 20+ echte doctypes bestaan, maar de schermen lezen het **hele dossier in één call** (`euroloop.api.data.bundle`, ~110 KB op demogrootte) en schrijven via server-side transitiefuncties (`euroloop/api/workflow.py`, 477 regels). De docs (README/DEMO.md, 08-08) lopen achter op de code (doctypes 11-08).
- **AI-assistent** (na de docs toegevoegd): read-only, tool-using assistent (`euroloop/api/ai.py`, Anthropic SDK, achtergrondjob met `frappe.set_user`), incl. een `correspondentie`-tool die de maildraad als kennisbron ontsluit.
- **CI/CD:** alleen release- en upstream-sync-workflows; **geen** test/lint/typecheck-gate.

## 2.2 Functionaliteit — en hoe "mail als planningstool" is gemodelleerd

Twaalf domeinschermen (proces, dashboard, klanten, offertes, werkvoorbereiding/DCS, planning, kalibraties, meters, MNR, certificaten, beheer + AI-widget). Kernpunten:

- **Planning:** weekbord ma–vr per loop met `slots_per_day` uit loopconfiguratie, drag-and-drop vanuit een backlog, bewaking van "afgesproken datum vs. geplande datum" (drift rood zichtbaar), witnesses & hotelboekingen als registratiepaneel, shipping-/materiaalstatus per kaart. **Geen server-side capaciteitsbewaking**: plan-acties bestaan alleen client-side; dubbelboeking wordt niet door de database geweigerd.
- **Mail:** doctypes `EuroLoop Mail Thread` (gekoppeld aan klant/offerte/DCS/kalibratie) + `Mail Message` met `flag` (datum/scope/witness/logistiek), `handled` en `determines` (welke DCS-velden een bericht bepaalde). Het `CorrespondencePanel` hangt bewust **op het record** (offerte, DCS, planning, kalibratie, klant, MNR) in plaats van in een aparte inbox — het ontwerp-antwoord op "de planner staat niet op de threads".
- **De eerlijkheidsregel als asset:** alles gesimuleerds is in de UI gelabeld (`SimulatedNotice`): *"Er is geen koppeling met een mailbox — deze berichten zijn verzonnen."* Er is **nul serverlogica rond mail**: geen mailbox-koppeling, geen ingest, geen verzending, geen automatische flagging (flags zijn met de hand in de seed gezet), leesstatus per browser (localStorage) i.p.v. per gebruiker.
- **Niet gebouwd** (selectie uit USER_STORIES-gaps): offerte-PDF, klant aanmaken, DCS-revisies, werkorder naar de vloer (veld bestaat, scherm niet), operator-dagstaat, pre-run checklist, zoeken (globaal én in correspondentie), gecombineerde tijdlijn, branding. De demodata-reset is door de backend-migratie feitelijk stuk (`resetDemo` → `notPorted`).

## 2.3 Datamodel

18 domein-doctypes + 2 AI- + 2 template-doctypes. De keten offerte → DCS → kalibratie → certificaat is server-side werkend gemodelleerd (win → DCS + flowpoint-generatie uit norm; release → kalibratie + hotelboekingen; resultaten per flowpoint; release → certificaatnummer). Portal-vocabulaire (flowpoints, Qmin/Qmax/Qt, spools U1–U3/D1–D2, regulation, drie adresblokken) is trouw overgenomen.

**Impliciet gebleven entiteiten** (geen eigen doctype): order/opdracht (frontend-projectie), werkorder (één boolean), certificaat (één stringveld, geen document/PDF/revocatie), planning-slot/capaciteitskalender, prijstabelversie (hardcoded constante), norm→methode-mapping (CSV-strings), zending, factuur, gebruikersrollen. **MNR is een losstaand eiland**: alleen gekoppeld aan meter+klant, met `requires_recalibration` als vlag zonder vervolgflow, zonder link naar de mailthreads en zonder eigen planning.

Modelzwaktes voor productie: geen enkele controller-validatie (alle `.py` leeg), nummers niet uniek en race-gevoelig gegenereerd, statussen als vrije Selects (direct save omzeilt elke overgang), geen `is_submittable`/bevriezing van gecertificeerde meetdata, denormalisatie zonder bewaking, taalmix NL/EN.

## 2.4 Technische staat

| Component | Oordeel | Kern |
|---|---|---|
| Frontend-toolchain (tsconfig strict, eslint, vitest, 13 testbestanden) | **Herbruikbaar** | Modern en streng; tests dekken vooral demo-materiaal |
| Sync-engine + offline-DB | **Herbruikbaar** | Doordacht patroon (idempotentie, optimistic locking, dead-letter); dekt nu alléén `Example Task`; SQLCipher-passphrase is een **dev-placeholder** |
| Storage-laag (S3 presigned) | **Herbruikbaar** | Correct authz-patroon; uploadlimieten en echte-bucket-test ontbreken |
| `api/workflow.py` | **Aanpassen** | Juiste plek, maar read-permissiegat, nummer-race, `simulate_run` als productie-endpoint, 0 tests |
| `api/data.py` bundle + provider | **Vervangen (op termijn)** | Bewuste demo-seam; full-dossier-fetch en N+1 schalen niet |
| Doctype-schema | **Aanpassen** | Zelfverklaard "demo scaffold: expected to change after the workshop day" |
| Rollen/permissies | **Nieuwbouw** | Álle doctypes alleen `System Manager`; de zes demo-rollen (Sales, Werkvoorbereider, Planner, Operator, MNR Monteur, Manager) bestaan alleen als frontend-switcher — in een echte uitrol ziet iedereen alles, inclusief prijzen |
| Backend-tests/CI | **Nieuwbouw** | Backend-dekking is feitelijk 0 op security-kritieke code |
| Schermen + procesderivatie (`lib/process.ts`) | **Aanpassen** | De UX-kern en de waarde van de demo; datalaag moet omgehangen |
| Demo-tuig (seed 1.113 regels, providers, `euroloop/demo/`) | **Verwijderen/dev-only** | Uitstekend demomateriaal, hoort niet in productie |

## 2.5 Pijnpunten die de "wildgroei" verklaren (knelpunt-kandidaten)

Uit gesprek + repo-documentatie, genummerd als kandidaat-knelpunten voor het rode-draad-register:

- **K1** — De e-mailthread is het feitelijke systeem van registratie voor de jobspecificatie; de DCS wordt er met de hand uit gedestilleerd. `[UIT GESPREK]`
- **K2** — Meterdata wordt bij overdracht naar MNR opnieuw ingetikt ("je moet nog een keer weer gaan zitten te tikken" — het scherpst benoemde pijnpunt). `[UIT GESPREK]`
- **K3** — Hetzelfde hertypen één stap eerder: mailthread → DCS. `[UIT GESPREK]`
- **K4** — De redenering achter DCS-velden ("waarom 5 punten?") is een jaar later onvindbaar. `[UIT GESPREK/ANALYSE]`
- **K5** — De planner staat niet op de threads die hem het meest aangaan; het mailverkeer neemt juist toe ná het inplannen (toegang, levering, reizen, datumwijzigingen). `[ANALYSE repo — verifiëren]`
- **K6** — Een datumwijzigingsverzoek kan verzuipen in een thread (demo-scenario is hier omheen gebouwd). `[AANNAME]`
- **K7** — Offertes en klantdata leven in Excel; prijs komt uit een maattabel; documenten zijn sjablonen met "puntje puntje euro". `[UIT GESPREK]`
- **K8** — Commerciële datumafspraak (bij sales) en operationele planning zijn losgekoppeld. `[UIT GESPREK/ANALYSE]`
- **K9** — Witness-/hotelcoördinatie hangt aan de planning maar is handwerk. `[UIT GESPREK]`
- **K10** — MNR-overdracht verloopt informeel; werkorder-discipline moet door de directie worden afgedwongen. `[UIT GESPREK]`
- **K11** — Fysieke fit-check (past de meter in de lijn) gebeurt laat en ad hoc. `[AANNAME]`
- **K12** — Offreren is bijna volledig mechanisch maar kost handwerk. `[ANALYSE]`
- **K13** — Bijlagen (datasheets) verdwijnen in mailboxen. `[AANNAME]`
- **K14** — Dit terrein is al eerder betreden: het Bisbrick-klantportaal probeerde exact de intake-per-mail te vervangen en is kennelijk gestrand; waarom is onbekend. `[FEIT dat het bestond; lot onbekend]`

**Wildgroei-mechanisme** `[ANALYSE]`: elke processtap maakt zijn eigen kopie van dezelfde data (Excel → mail → DCS → MNR), de mailthread is de enige plek waar de klantintentie compleet staat, en na de handover "bezit" niemand het record. Mail is dáárom het planningssysteem geworden: het was de enige plek waar alles samenkwam.

## 2.6 Samenvatting fase 2

1. De repo is een **hoogwaardige demonstrator + productie-aanzet** op een degelijke template — een requirements-instrument dat bewust markeert wat verzonnen is, geen half product.
2. **Herbruikbaar:** architectuurfundament, schermen/UX, procesderivatie, domeinvocabulaire, sync/storage-patronen. **Nieuwbouw:** rollen/permissies, mail-integratie (de kern!), planning-server-side, certificering/PDF, MNR-flow, backend-tests, facturatie.
3. De **afstand tussen "mail-UI op de juiste plek" (klaar) en "werkende mail-als-planningstool"** (mailboxkoppeling, job-matching, flag-detectie, rechten/AVG) is de grootste openstaande bouwopgave — en de haalbaarheidsvraag ("hoe vindt een mail zijn job?") is door de demo bewust ontweken.
4. Vrijwel alle domeinregels in de app zijn **onbevestigde aannames** (rollen, prijsdrivers, normen, uitvoeringsproces, certificaat, 3 slots/dag) — precies de lijst die de vragenlijst moet afwerken.
