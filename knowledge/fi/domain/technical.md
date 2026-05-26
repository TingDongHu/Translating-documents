---
id: fi/domain/technical
type: domain
target_lang: fi
name: Domain: Technical (Finnish -- FI)
description: Finnish technical domain terminology and translation rules
---

# Finnish Technical Domain Translation

## Reader Model

### Target Reader Profile
- **Primary Reader**: Finnish software developers, engineers (insinöörit), IT professionals, technical writers
- **Secondary Reader**: System administrators, project managers, quality assurance specialists
- **Tertiary Reader**: End users, technical support staff, training personnel

### Reader Expectations
1. **IT Terminology Precision**: Finnish IT terminology must align with established Finnish computing terms (tietotekniikan termistö) from Teknologiateollisuus and the Finnish Terminology Centre (Termistokeskus TSK).
2. **Technical Clarity**: Instructions and documentation must be clear, unambiguous, and actionable.
3. **Consistent Terminology**: Technical terms must be used consistently throughout a document.
4. **Code and Commands**: Code snippets, command-line instructions, and configuration files remain in English.
5. **UI Localization**: User interface text should follow Finnish software localization conventions.

### Reader Expectation Matrix

| Expectation | Importance | Consequence if Unmet |
|-------------|------------|---------------------|
| Finnish IT terminology accuracy | Critical | Technical misunderstanding |
| Consistent terminology | High | Reader confusion |
| Clear instruction language | Critical | User errors |
| Code/commands in English | High | Inoperable instructions |
| Natural Finnish UI text | Medium | Poor user experience |
| Correct technical register | Medium | Unprofessional documentation |

---

## Decision Framework

### Table T1: Core IT Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Computer | tietokone | Computing device |
| Software | ohjelmisto | Programs and data |
| Hardware | laitteisto | Physical components |
| Operating system | käyttöjärjestelmä | OS |
| Server | palvelin | Network server |
| Client | asiakas / asiakasohjelma | Client machine/program |
| Database | tietokanta | Data store |
| Network | verkko | Interconnected systems |
| Internet | Internet / Internet-verkko | Global network |
| Website | verkkosivusto / verkkosivu | Web pages |
| Email | sähköposti | Electronic mail |
| File | tiedosto | Data file |
| Folder | kansio | Directory |
| Cloud | pilvi | Cloud computing |
| Cloud computing | pilvipalvelu / pilvilaskenta | Cloud services |
| Program | ohjelma | Software application |
| Application | sovellus | Software application |
| Mobile | mobiili / mobiilisovellus | Mobile device/app |
| Device | laite | Hardware device |
| Platform | alusta / käyttöjärjestelmä | Computing platform |
| Algorithm | algoritmi | Computation procedure |
| Protocol | protokolla | Communication rules |
| Interface | käyttöliittymä / rajapinta | UI or API |
| Application Programming Interface (API) | sovellusohjelmointirajapinta (API) | API |
| Database Management System (DBMS) | tietokannanhallintajärjestelmä (DBMS) | Database system |
| User Interface (UI) | käyttöliittymä (UI) | User-facing interface |
| User Experience (UX) | käyttäjäkokemus (UX) | User interaction quality |

### Table T2: Networking and Security Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Firewall | palomuuri / tulimuurisuoja | Network security barrier |
| Encryption | salaus | Data protection |
| Decryption | purku | Reversing encryption |
| Authentication | todennus / tunnistautuminen | Identity verification |
| Authorization | valtuutus / käyttöoikeus | Access permission |
| Password | salasana | Secret credential |
| Username | käyttäjätunnus | Account identifier |
| Access control | pääsynvalvonta | Permission management |
| Vulnerability | haavoittuvuus | Security weakness |
| Threat | uhka | Potential danger |
| Malware | haittaohjelma | Malicious software |
| Virus | tietokonevirus | Self-replicating malware |
| Ransomware | lunnasohjelma | Extortion malware |
| Phishing | tietoisku / phishing | Social engineering attack |
| Data breach | tietomurto | Unauthorized data access |
| Backup | varmuuskopio / backup | Data copy |
| Recovery | palautus | Data restoration |
| System administration | järjestelmänhallinto | IT system management |
| Virtual Private Network (VPN) | virtuaalinen yksityisverkko (VPN) | Encrypted network |

### Table T3: Software Development Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Programming | ohjelmointi | Code writing |
| Developer | kehittäjä / ohjelmoija | Software builder |
| Source code | lähdekoodi | Human-readable code |
| Compiler | kääntäjä | Code translator |
| Debugging | virheenjäljitys / debuggaus | Error fixing |
| Testing | testaus | Quality verification |
| Unit test | yksikkötesti | Component test |
| Integration test | integraatiotesti | System test |
| Deployment | käyttöönotto / julkaisu | Release to production |
| Version | versio | Software iteration |
| Update | päivitys | New version |
| Upgrade | päivitys / ylennys | Major version change |
| Patch | paikka / korjaus | Small fix |
| Release | julkaisu | Software distribution |
| Repository | tietovarasto / repository | Code storage |
| Branch | haara | Version branch |
| Merge | yhdistäminen | Combining code |
| Commit | toimitus / sitominen | Code save |
| Bug | virhe / ohjelmointivirhe | Code defect |
| Feature | ominaisuus | Software capability |
| Module | moduuli | Software component |
| Library | kirjasto | Reusable code |
| Framework | ohjelmistokehys / kehys | Development platform |

### Table T4: Cloud and Infrastructure Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Cloud service | pilvipalvelu | Remote computing service |
| Infrastructure as a Service (IaaS) | infrastruktuurina palveluna (IaaS) | Cloud infrastructure |
| Platform as a Service (PaaS) | alustana palveluna (PaaS) | Cloud platform |
| Software as a Service (SaaS) | ohjelmistona palveluna (SaaS) | Cloud applications |
| Container | säiliö | Application container |
| Microservice | mikropalvelu | Small service component |
| Scalability | skaalautuvuus | Growth capacity |
| Load balancing | kuorman tasapaino | Traffic distribution |
| Redundancy | varmuuskopio / redundantti | Backup/failover |
| Uptime | käyttöaika / toimintakelpoisuus | Availability |
| Downtime | keskeytys / käyttökelvottomuus | Service outage |
| Bandwidth | kaistakapasiteetti | Data throughput |
| Latency | viive / latenssi | Delay |
| Deployment | käyttöönotto | Service activation |
| Monitoring | valvonta | System observation |
| Logging | lokikirjaus | Record keeping |

### Table T5: Data and Analytics Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Data | tieto / tiedot | Information |
| Big data | big data / suuret tietomäärät | Large datasets |
| Data mining | tietojen louhinta | Pattern extraction |
| Machine learning | koneoppiminen | Automated learning |
| Artificial intelligence (AI) | tekoäly (AI) | Intelligent systems |
| Natural Language Processing (NLP) | luonnollisen kielen käsittely (NLP) | Text understanding |
| Neural network | hermoverkko | Learning architecture |
| Algorithm | algoritmi | Computation procedure |
| API | API / rajapinta | Integration point |
| Dashboard | hallintapaneeli / koontinäyttö | Data display |
| Analytics | analytiikka | Data analysis |
| Metadata | metatieto | Data about data |
| Data warehouse | tietovarasto | Central data store |
| Data lake | tietojärvi | Raw data storage |
| ETL | ETL (Extract, Transform, Load) | Data pipeline |

### Table T6: User Documentation Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| User manual | käyttöohje / käyttöopas | Usage guide |
| Installation | asennus | Setup process |
| Configuration | asetus / määritys | System setup |
| Settings | asetukset | Configuration options |
| Error message | virheilmoitus | Warning text |
| Warning | varoitus | Caution notice |
| Information | tiedote | Informational message |
| Dialog box | valintaikkuna | UI popup |
| Tooltip | työkalun vihje | Hover hint |
| Menu | valikko | Navigation list |
| Toolbar | työkalurivi | Button row |
| Sidebar | sivupalkki | Side panel |
| Checkbox | valintaruutu | Selection box |
| Drop-down list | avattava luettelo | Selection list |
| Button | painike | Clickable control |
| Tab | välilehti | Content tab |
| Scroll | vieritys | Content movement |
| Save | tallenna | Store changes |
| Cancel | peruuta | Abort action |
| OK | OK / hyväksy | Confirm action |

---

## Error Pattern Library

### EP-T1: Literal Translation of Technical Terms
- **Common Error**: Translating established English IT terms literally into Finnish.
- **Correct**: Use established Finnish IT terminology where it exists (e.g., `palvelin` for "server," not `palvelija`).
- **Rule**: Consult Finnish IT term databases (Termistokeskus TSK, Teknologiateollisuus) before creating new translations.

### EP-T2: Code and Commands Translation
- **Common Error**: Translating code snippets, command-line instructions, or configuration file content.
- **Correct**: Code, commands, and configuration remain in English. Only surrounding explanatory text is translated.
- **Rule**: NEVER translate code, commands, variable names, or configuration file content.

### EP-T3: Inconsistent Terminology
- **Common Error**: Using different Finnish translations for the same English term within a document.
- **Correct**: Establish a glossary at the start of a project and use terms consistently.
- **Rule**: Maintain terminology consistency throughout the entire document.

### EP-T4: UI Text Length Issues
- **Common Error**: Finnish translations that are too long for UI elements (buttons, menus).
- **Correct**: Finnish words are often longer than English; use abbreviations or rephrase where necessary.
- **Rule**: Test UI translations in context to ensure they fit the available space.

---

## Domain-Specific Reference

### Finnish IT Industry Context
Finland has a strong IT sector with companies like Nokia, Supercell, Rovio, and Wolt. Finnish IT terminology draws from:
- **Finnish computing tradition**: Many terms were coined in the 1960s-70s at Finnish universities.
- **Swedish influence**: Some terms overlap with Swedish IT terminology due to Finland's bilingual history.
- **International adoption**: English terms are widely used in spoken Finnish IT jargon.

### Finnish Terminology Resources
- **Termistokeskus TSK** (Finnish Terminology Centre): Terminology database and standards.
- **Teknologiateollisuus**: Industry-specific technical terms.
- **Finnish Wikipedia**: Established Finnish technical terminology.
- **Microsoft/Google/Apple Finnish localization**: Software terminology standards.

### Finnish IT Abbreviations
- `IT` = tietotekniikka (information technology)
- `AI` = tekoäly (artificial intelligence)
- `IoT` = esineiden internet (Internet of Things)
- `VR` = virtuaalitodellisuus (virtual reality)
- `AR` = lisätty todellisuus (augmented reality)
- `DevOps` = DevOps (no Finnish translation; used as-is)
- `UX` = käyttäjäkokemus (user experience)
- `CI/CD` = jatkuva integraatio/jatkuva toimitus (continuous integration/delivery)
