---
id: fr/domain/technical
type: domain
target_lang: fr
name: Documents techniques (francais)
description: Terminologie et regles pour les documents techniques traduits en francais
term_mappings:
  "manual": "manuel"
  "specification": "specification"
  "datasheet": "fiche technique"
  "user guide": "guide utilisateur"
  "installation guide": "guide d'installation"
  "maintenance": "maintenance"
  "troubleshooting": "depannage"
  "spare parts": "pieces detachees"
  "component": "composant"
  "assembly": "assemblage"
  "welding": "soudure"
  "tolerance": "tolerance"
  "standard": "norme"
  "certification": "certification"
  "compliance": "conformite"
  "testing": "essai"
  "quality control": "controle qualite"
  "calibration": "etalonnage"
  "dimension": "dimension"
  "weight": "poids"
  "temperature": "temperature"
  "pressure": "pression"
  "voltage": "tension"
  "current": "courant"
  "frequency": "frequence"
  "software": "logiciel"
  "hardware": "materiel"
  "firmware": "micrologiciel"
  "database": "base de donnees"
  "server": "serveur"
  "network": "reseau"
  "API": "API"
  "debugging": "debogage"
  "deployment": "deploiement"
  "release": "version"
  "ground": "terre"
  "phase": "phase"
  "neutral": "neutre"
  "circuit breaker": "disjoncteur"
  "fuse": "fusible"
  "conductor": "conducteur"
  "insulation": "isolation"
  "enclosure": "boitier"
  "guard": "protecteur"
  "interlock": "verrouillage"
  "emergency stop": "arret d'urgence"
  "lockout/tagout": "consignation"
  "hazard": "danger"
  "risk": "risque"
  "personal protective equipment": "equipement de protection individuelle"
  "safety data sheet": "fiche de donnees de securite"
  "threshold": "seuil"
  "rated value": "valeur nominale"
  "maximum allowable": "maximum admissible"
  "working load limit": "limite de charge d'utilisation"
  "yield strength": "limite d'elasticite"
  "tensile strength": "resistance a la traction"
  "fatigue": "fatigue"
  "creep": "fluage"
  "corrosion": "corrosion"
  "erosion": "erosion"
  "wear": "usure"
  "lubrication": "lubrification"
  "coolant": "liquide de refroidissement"
  "hydraulic": "hydraulique"
  "pneumatic": "pneumatique"
  "actuator": "actionneur"
  "sensor": "capteur"
  "transducer": "transducteur"
  "controller": "automate"
  "programmable logic controller": "automate programmable industriel"
  "human-machine interface": "interface homme-machine"
  "servo motor": "servomoteur"
  "gear": "engrenage"
  "bearing": "roulement"
  "shaft": "arbre"
  "pulley": "poulie"
  "belt": "courroie"
  "chain": "chaine"
  "valve": "vanne"
  "pump": "pompe"
  "cylinder": "verin"
  "piston": "piston"
  "seal": "joint d'etancheite"
  "gasket": "joint"
  "fastener": "fixation"
  "nut": "ecrou"
  "bolt": "boulon"
  "screw": "vis"
  "washer": "rondelle"
  "pin": "goupille"
  "key": "came"
  "spring": "ressort"
  "damper": "amortisseur"
  "actuator": "actionneur"
  "solenoid": "electrovanne"
  "transformer": "transformateur"
  "rectifier": "redresseur"
  "inverter": "onduleur"
  "motor": "moteur"
  "generator": "generatrice"
  "alternator": "alternateur"
  "load": "charge"
  "power supply": "alimentation electrique"
  "output": "sortie"
  "input": "entree"
  "feedback": "retour"
  "setpoint": "consigne"
  "closed loop": "boucle fermee"
  "open loop": "boucle ouverte"
  "algorithm": "algorithme"
  "protocol": "protocole"
  "interface": "interface"
  "bandwidth": "bande passante"
  "latency": "latence"
  "throughput": "debit"
  "redundancy": "redondance"
  "fail-safe": "securite integree"
  "fault tolerance": "tolerance aux pannes"
  "mean time between failures": "duree moyenne de bon fonctionnement"
  "mean time to repair": "duree moyenne de reparation"
  "availability": "disponibilite"
  "reliability": "fiabilite"
  "maintainability": "maintenabilite"
---
# =============================================================================
# MODELE DE LECTURE / READER MODEL
# =============================================================================

Ce modele decrit comment lire et interpreter un document technique source en
vue de sa traduction en francais. Il identifie les marqueurs de registre,
les elements normatifs contraignants et les pieges terminologiques specifiques
au domaine technique.

## 1. Identification du type de document technique

Avant toute traduction, determiner la sous-categorie du document source parmi
les suivantes :

| Type de document          | Marqueurs francais               | Registre   |
|---------------------------|----------------------------------|------------|
| Manuel d'utilisation      | "Appuyez sur", "Branchez"        | Imperatif  |
| Notice d'installation     | "Fixer", "Raccorder"             | Imperatif  |
| Fiche technique           | "Caracteristiques"               | Indicatif  |
| Sp\'ecification technique | "Le systeme doit..."             | Obligation |
| Rapport d'essai           | "Il a ete constate que..."       | Passe compose |
| Norme (NF/ISO/EN)         | "Doit", "Il convient de"         | Modale     |
| Certificat de conformite  | "Est declare conforme a"         | Present    |
| Brevet                     | "Est caracterise en ce que"      | Juridico-technique |

## 2. Registres de traduction selon le public cible

| Public cible               | Registre                         | Exigences                             |
|----------------------------|----------------------------------|---------------------------------------|
| Ingenieur / Technicien     | Technique precis, jargon assume  | Conserver le vocabulaire specialise   |
| Operateur / Utilisateur    | Vulgarise, imperatif simple      | Phrases courtes, evitement du jargon  |
| Service apres-vente        | Technique + maintenance          | Termes de diagnostic normalises        |
| Autorite de certification  | Normatif, juridico-technique     | Citations exactes des normes           |
| Public general             | Simplifie, securite en tete      | Eviter tout terme non explique         |

## 3. Marqueurs de contenu normatif

Dans les textes techniques, certains enonces ont force obligatoire.
Les distinguer des enonces purement informatifs est essentiel :

| Marqueur source          | Traduction francaise       | Valeur           |
|--------------------------|----------------------------|------------------|
| "shall"                  | "doit"                     | Obligation absolue |
| "shall not"              | "ne doit pas"              | Interdiction      |
| "must"                   | "doit" / "il est necessaire de" | Obligation forte |
| "must not"               | "il est interdit de"       | Interdiction      |
| "should"                 | "il convient de"           | Recommandation    |
| "should not"             | "il est deconseille de"    | Deconseil         |
| "may"                    | "peut" / "il est possible de" | Permission      |
| "need not"               | "il n'est pas necessaire de" | Absence d'obligation |
| "it is recommended"      | "il est recommande de"     | Recommandation    |
| "it is required"         | "il est requis de"         | Obligation        |

## 4. Pieges terminologiques techniques

| Terme anglais           | Traduction erronee possible | Traduction correcte (contexte technique) |
|-------------------------|-----------------------------|------------------------------------------|
| "control"               | "controler" (verifier)      | "commander" (pilotage)                   |
| "monitor"               | "moniteur" (ecran)          | "surveiller" / "superviser"              |
| "performance"           | "performance" (spectacle)   | "performances" (rendement)              |
| "sensitive"             | "sensitif" (physiologique)  | "sensible"                               |
| "actual"                | "actuel"                     | "reel" / "effectif"                      |
| "eventually"            | "eventuellement"            | "a terme" / "finalement"                 |
| "currently"             | "couramment"                | "actuellement"                           |
| "deception"             | "deception" (delusion)      | "tromperie" / "illusion"                |
| "library" (software)    | "librairie"                 | "bibliotheque"                           |
| "default"               | "defaut" (panne)            | "par defaut" / "valeur par defaut"       |
| "revision"              | "revision" (controle)       | "version" / "mise a jour" (d'un document)|
| "instruction"           | "instruction" (ordre unique)| "instructions" (pluriel)                 |

# =============================================================================
# CADRE DECISIONNEL / DECISION FRAMEWORK
# =============================================================================

Chaque tableau ci-dessous presente une decision de traduction recurrente dans
les documents techniques. La colonne "Decision" indique le parti a prendre.

## Table 1 : Unites de mesure et symboles

| Contexte                                      | Regle                                                    | Decision                                  |
|-----------------------------------------------|----------------------------------------------------------|-------------------------------------------|
| Valeur numerique + symbole d'unite            | Conserver le symbole normalise (SI)                      | 12 V, 230 V, 50 Hz, 10 A                  |
| Valeur numerique + nom d'unite                | Traduire le nom, conserver la valeur                     | 12 volts, 230 volts, 50 hertz, 10 amperes |
| Unite non-SI (inch, foot, psi, BTU)           | Conserver l'original, ajouter conversion SI entre parentheses | 12 in (304,8 mm)                    |
| Temperature en degres Fahrenheit              | Conserver + ajouter Celsius                              | 212 degF (100 degC)                        |
| Pression en psi                               | Conserver + ajouter kPa/MPa                              | 150 psi (1,03 MPa)                        |
| Force en lbf                                  | Conserver + ajouter N                                    | 100 lbf (444,8 N)                         |
| Couple en ft-lbf                              | Conserver + ajouter N.m                                  | 50 ft-lbf (67,8 N.m)                      |

## Table 2 : Nombres, formats numeriques et decimaux

| Contexte                             | Regle                                      | Decision                     |
|--------------------------------------|--------------------------------------------|------------------------------|
| Separateur decimal (. -> ,)          | Remplacer le point par la virgule          | 3.14 -> 3,14                |
| Separateur de milliers (, -> espace) | Remplacer la virgule par espace ins\'ecable | 1,234 -> 1 234             |
| Pourcentage dans un texte technique  | Espace avant le signe %                    | 15,5 % (pas 15.5%)          |
| Tolerance                           | Symbole +/- ou plage                       | +/- 0,1 mm ou de 9,9 a 10,1 |
| Fraction (1/2, 3/4)                 | Conserver la fraction ou ecrire en clair    | 1/2 ou "un demi"            |
| Nombre negatif                      | Signe moins ou parentheses                  | -25 degC ou (25)             |
| Grand nombre (>9999)                | Espace ins\'ecable tous les 3 chiffres      | 12 345,67                   |

## Table 3 : Instructions et voix verbale

| Contexte source                    | Traduction recommandee                    | Justification                                |
|------------------------------------|-------------------------------------------|----------------------------------------------|
| "Press the START button"           | "Appuyez sur le bouton MARCHE"            | Imperatif pour instruction directe           |
| "Do not operate without guard"     | "Ne pas utiliser sans protecteur"         | Infinitif pour avertissement                 |
| "The system shall be grounded"     | "Le systeme doit etre mis a la terre"     | "Doit" pour obligation technique             |
| "It is recommended to calibrate"   | "Il est recommande d'etalonner"           | Tour impersonnel pour recommandation          |
| "The component is made of steel"   | "Le composant est en acier"               | Present passif pour description               |
| "Once assembled, check alignment"  | "Apres assemblage, verifier l'alignement" | Infinitif apres une etape                    |
| "If alarm sounds, stop immediately"| "Si l'alarme retentit, arreter immediatement" | Conditionnel + imperatif              |
| "Disconnect power before servicing"| "Debrancher l'alimentation avant toute intervention" | Ordre chronologique logique       |

## Table 4 : Termes electrotechniques

| Anglais                     | Francais                     | Contexte                                   |
|-----------------------------|------------------------------|--------------------------------------------|
| "power supply"              | "alimentation"               | Generale                                   |
| "mains supply"              | "alimentation secteur"       | Reseau electrique public                   |
| "power distribution"        | "distribution electrique"    | Reseau interne                             |
| "earthing" / "grounding"    | "mise a la terre"            | Protection                                 |
| "overcurrent protection"    | "protection contre les surintensites" | Disjoncteur                           |
| "short circuit"             | "court-circuit"              | Defaut electrique                          |
| "earth fault"              | "defaut a la terre"          | Defaut d'isolation                         |
| "residual current device"   | "dispositif differentiel residuel" | DDR                                   |
| "arc flash"                | "arc electrique"             | Danger electrique                          |
| "insulation resistance"     | "resistance d'isolement"     | Mesure                                     |
| "dielectric strength"       | "rigidite dielectrique"      | Tenue aux tensions                         |
| "EMC"                      | "CEM (compatibilite electromagnetique)" | Norme                                 |
| "screening" / "shielding"   | "blindage"                   | Protection electromagnetique               |

## Table 5 : Termes mecaniques

| Anglais                     | Francais                     | Contexte                                   |
|-----------------------------|------------------------------|--------------------------------------------|
| "housing"                   | "boitier" / "corps"          | Enveloppe exterieure                       |
| "chassis"                   | "chassis"                   | Structure porteuse                         |
| "frame"                     | "cadre" / "bat"             | Support                                    |
| "flange"                    | "bride"                      | Raccord                                    |
| "coupling"                  | "accouplement"               | Liaison d'arbres                           |
| "bushing"                   | "baguette" / "douille"       | Piece d'usure                              |
| "thread"                    | "filetage"                   | Pas de vis                                 |
| "pitch"                     | "pas"                        | Vis, engrenage                             |
| "torque"                    | "couple"                     | Serrage                                    |
| "tightening torque"         | "couple de serrage"          | Valeur                                     |
| "pretension"               | "precontrainte"              | Ressort, boulon                            |
| "clearance"                 | "jeu"                        | Espace entre pieces                        |
| "interference fit"          | "ajustement serre"           | Assemblage force                           |
| "clearance fit"             | "ajustement libre"           | Assemblage libre                           |
| "surface finish"            | "etat de surface"            | Rugosite                                   |
| "roughness"                 | "rugosite"                   | Ra                                         |

## Table 6 : Termes logiciels et informatiques

| Anglais                     | Francais                     | Contexte                                   |
|-----------------------------|------------------------------|--------------------------------------------|
| "framework"                 | "cadriciel"                  | Recommande par la DGLFLF (mais "framework" courant) |
| "middleware"                | "intergiciel"                | Terme officiel francais                     |
| "cloud"                     | "nuage" / "informatique en nuage" | ou "cloud" (courant)                   |
| "on-premises"              | "sur site"                   | Oppose a "cloud"                           |
| "endpoint"                  | "point d'acces" / "terminal" | Reseau                                     |
| "payload"                   | "charge utile"               | Transmission de donnees                    |
| "queue"                     | "file d'attente"             | Structure de donnees                       |
| "thread" (programming)      | "fil d'execution"            | Programmation concurrente                  |
| "token" (auth)              | "jeton"                      | Authentification                           |
| "sandbox"                   | "bac a sable"                | Environnement isole                        |
| "container"                 | "conteneur"                  | Virtualisation                             |
| "orchestration"             | "orchestration"              | Gestion de conteneurs                      |
| "pipeline" (CI/CD)          | "chaîne de deploiement"      | Integration continue                       |
| "staging"                   | "preproduction"              | Environnement                      |
| "rollback"                  | "retour arriere"             | Annulation de version                      |

## Table 7 : Termes de securite

| Anglais                     | Francais                     | Contexte                                   |
|-----------------------------|------------------------------|--------------------------------------------|
| "safety"                    | "securite"                   | Protection des personnes                   |
| "security"                  | "surete" / "securite"        | Protection contre actes malveillants       |
| "hazard"                    | "danger"                     | Source potentielle de dommage              |
| "risk"                      | "risque"                     | Combinaison gravite x probabilite          |
| "residual risk"             | "risque residuel"            | Apres mesures de reduction                 |
| "risk assessment"           | "evaluation des risques"     | Processus                                  |
| "risk reduction"            | "reduction du risque"        | Mesures                                    |
| "safety function"           | "fonction de securite"       | Fonction critique                          |
| "safety integrity level"    | "niveau d'integrite de securite" | SIL                                    |
| "performance level"         | "niveau de performance"      | PL (ISO 13849)                             |
| "category" (safety)         | "categorie"                  | Architecture (ISO 13849-1)                 |
| "redundancy"                | "redondance"                 | Double canal                               |
| "diversity"                 | "diversite"                  | Technologies differentes                   |
| "diagnostic coverage"       | "taux de couverture de diagnostic" | DC                                    |
| "safe state"                | "etat de securite"           | Etat apres arret d'urgence                 |
| "fault exclusion"           | "exclusion de defaut"        | ISO 13849-1                                |
| "common cause failure"      | "defaut de cause commune"    | CCF                                        |
| "systematic failure"        | "defaut systematique"        | Defaut lie a la conception                 |
| "random hardware failure"   | "defaut aleatoire de materiel" | Defaut physique                           |

## Table 8 : Symboles et abreviations normalises

| Symbole/Abrev. | Signification anglaise    | Signification francaise       | Regle                                  |
|----------------|---------------------------|-------------------------------|----------------------------------------|
| dia / phi      | diameter                   | diametre                      | Remplacer par le symbole ø ou "diam."  |
| mm             | millimeter                 | millimetre                    | Conserver (normalise)                  |
| rpm            | revolutions per minute     | tr/min                        | Traduire (tours par minute)            |
| psi            | pounds per square inch     | livres par pouce carre        | Conserver + conversion SI              |
| gpm            | gallons per minute         | gallons par minute            | Conserver + conversion SI              |
| cfm            | cubic feet per minute      | pieds cubes par minute        | Conserver + conversion SI              |
| AWG            | American Wire Gauge        | calibre americain des fils    | Conserver + equivalent mm2             |
| NPT            | National Pipe Thread       | filetage conique americain    | Conserver + equivalent metrique        |
| UNC/UNF        | Unified Coarse/Fine Thread | filetage unifie gros/fin      | Conserver                               |
| BSP            | British Standard Pipe      | filetage britannique          | Conserver                               |
| IP             | Ingress Protection         | Indice de Protection          | Conserver (IP54, IP65, etc.)           |
| IK             | Impact Protection          | Indice de Resistance aux Chocs| Conserver (IK07, IK10, etc.)           |

## Table 9 : Verbes techniques recurrents

| Anglais          | Francais           | Contexte                                    |
|------------------|--------------------|---------------------------------------------|
| "to install"      | "installer"        | Mise en place                                |
| "to mount"        | "monter"           | Fixation sur support                         |
| "to assemble"     | "assembler"        | Mise en ensemble de plusieurs pieces         |
| "to connect"      | "raccorder"        | Liaison electrique, fluidique                |
| "to wire"         | "cabler"           | Connexion electrique                         |
| "to route"        | "acheminer"        | Passage de cables, tuyaux                    |
| "to fasten"       | "fixer"            | Serrage, vissage                             |
| "to tighten"      | "serrer"           | Avec un outil, a un couple donne             |
| "to loosen"       | "desserrer"        | Relacher                                     |
| "to remove"       | "retirer"          | Enlever                                      |
| "to disassemble"  | "demonter"         | Separation des parties                       |
| "to replace"      | "remplacer"        | Substitution par une piece neuve             |
| "to adjust"       | "regler"           | Mise a la valeur desiree                     |
| "to calibrate"    | "etalonner"        | Verification / correction d'un instrument    |
| "to verify"       | "verifier"         | Controle                                     |
| "to inspect"      | "inspecter"        | Examen visuel ou instrumental                |
| "to test"         | "tester / essayer" | Mise a l'epreuve                             |
| "to operate"      | "exploiter"        | Faire fonctionner                            |
| "to shutdown"     | "mettre a l'arret" | Arret planifie                               |
| "to trip"         | "declencher"       | Arret par dispositif de protection           |
| "to reset"        | "reinitialiser"    | Remise a l'etat initial                      |

## Table 10 : Couleurs normalisees

| Anglais     | Francais                  | Code normalise (NF C 15-100 / CEI 60446) |
|-------------|---------------------------|------------------------------------------|
| green-yellow| vert-jaune                | Conducteur de protection (PE)            |
| blue        | bleu                      | Conducteur neutre (N)                    |
| brown       | marron                    | Conducteur de phase (L1)                 |
| black       | noir                      | Conducteur de phase (L2)                 |
| grey        | gris                      | Conducteur de phase (L3)                 |
| red         | rouge                     | Courant continu positif / commande       |
| white       | blanc                     | Courant continu negatif / commande       |
| orange      | orange                    | Commande speciale ou reserve              |

## Table 11 : Mentions de certification et marquage

| Mention source           | Traduction francaise         | Remarque                                    |
|--------------------------|------------------------------|---------------------------------------------|
| "CE marked"              | "marque CE"                  | A conserver tel quel                        |
| "CE compliant"           | "conforme CE"                |                                             |
| "UL listed"              | "homologue UL"               | Conserver le sigle UL                       |
| "FCC compliance"         | "conformite FCC"             | Conserver le sigle FCC + equivalence CFR    |
| "RoHS compliant"         | "conforme RoHS"              | Directive 2011/65/UE                        |
| "REACH compliant"        | "conforme REACH"             | Reglement europ\'een                         |
| "ATEX certified"         | "certifie ATEX"              | Atmospheres explosibles                     |
| "IECEx certified"        | "certifie IECEx"             | Schema international                        |
| "CE marking of conformity" | "marquage CE de conformite" |                                             |
| "Notified Body"          | "Organisme notifie"          | Abreviation : ON                            |
| "EC type examination"    | "examen CE de type"          | Module B                                    |
| "Declaration of Conformity" | "Declaration UE de conformite" | Document obligatoire                     |

## Table 12 : Termes de maintenance et fiabilite

| Anglais                        | Francais                               |
|--------------------------------|----------------------------------------|
| "preventive maintenance"       | "maintenance preventive"               |
| "predictive maintenance"       | "maintenance predictive"               |
| "corrective maintenance"       | "maintenance corrective"               |
| "condition-based maintenance"  | "maintenance conditionnelle"           |
| "scheduled maintenance"        | "maintenance programmee"               |
| "unscheduled maintenance"      | "maintenance non programmee"           |
| "planned downtime"             | "arret planifie"                       |
| "unplanned downtime"           | "arret non planifie"                   |
| "overhaul"                     | "revision generale"                    |
| "refurbishment"                | "remise en etat"                       |
| "retrofit"                     | "modernisation"                        |
| "life cycle"                   | "cycle de vie"                         |
| "useful life"                  | "duree de vie utile"                   |
| "residual useful life"         | "duree de vie residuelle"              |
| "failure mode"                 | "mode de defaillance"                  |
| "failure rate"                 | "taux de defaillance"                  |
| "FMEA"                         | "AMDEC (Analyse des Modes de Defaillance et de leurs Criticites)" |
| "FMECA"                        | "AMDEC (Analyse des Modes de Defaillance, de leurs Effets et de leur Criticite)" |
| "root cause analysis"          | "analyse des causes racines"           |
| "Weibull distribution"         | "loi de Weibull"                       |
| "bathtub curve"               | "courbe en baignoire"                  |

## Table 13 : Termes de qualite et essais

| Anglais                          | Francais                           |
|----------------------------------|------------------------------------|
| "quality assurance"              | "assurance qualite"                |
| "quality management system"      | "systeme de management de la qualite" |
| "quality plan"                   | "plan qualite"                     |
| "acceptance criteria"            | "criteres d'acceptation"           |
| "inspection and testing"         | "controle et essais"               |
| "non-destructive testing"        | "controle non destructif"          |
| "destructive testing"            | "essai destructif"                 |
| "type test"                      | "essai de type"                    |
| "routine test"                   | "essai individuel" / "essai de routine" |
| "sampling test"                  | "essai par echantillonnage"        |
| "production test"                | "essai en production"              |
| "factory acceptance test"        | "essai de reception en usine"      |
| "site acceptance test"           | "essai de reception sur site"      |
| "type approval"                  | "agrement de type"                 |
| "first article inspection"       | "inspection premiere piece"        |
| "capability study"               | "etude de capabilite"              |
| "control plan"                   | "plan de controle"                 |
| "statistical process control"    | "maitrise statistique des procedes" |

## Table 14 : Termes environnementaux et REACH

| Anglais                              | Francais                               |
|--------------------------------------|----------------------------------------|
| "environmental management system"    | "systeme de management environnemental"|
| "environmental impact assessment"    | "evaluation d'impact sur l'environnement" |
| "life cycle assessment"             | "analyse du cycle de vie"              |
| "carbon footprint"                   | "empreinte carbone"                    |
| "greenhouse gas emissions"           | "emissions de gaz a effet de serre"    |
| "volatile organic compounds"         | "composes organiques volatils"         |
| "hazardous substance"               | "substance dangereuse"                 |
| "substance of very high concern"     | "substance extremement preoccupante"   |
| "restriction of hazardous substances"| "restriction des substances dangereuses" |
| "per- and polyfluoroalkyl substances"| "substances per- et polyfluoroalkyles" |
| "end-of-life treatment"             | "traitement en fin de vie"             |
| "recyclability"                     | "recyclabilite"                        |
| "extended producer responsibility"   | "responsabilite elargie du producteur" |
| "waste electrical and electronic equipment" | "dechets d'equipements electriques et electroniques" |

# =============================================================================
# NORMES ET STANDARDS
# =============================================================================

## Normes francaises (NF)

L'AFNOR (Association Francaise de Normalisation) est l'organisme national de
normalisation. Les normes NF sont reconnues d'application volontaire, sauf
lorsqu'elles sont rendues obligatoires par arret\'e ministeriel.

| Domaine               | Normes principales                  | Equivalent EN/ISO               |
|------------------------|-------------------------------------|----------------------------------|
| Construction electrique | NF C 15-100                         | Installation electrique          |
| Mecanique              | NF E 00-000 series                  | ISO 286 (tolerances)             |
| Dessin technique       | NF E 04-000 series                  | ISO 128, ISO 129                 |
| Soudure                | NF A 80-000 series                  | EN 287, EN 288, ISO 9606         |
| Qualite                | NF EN ISO 9001                      | ISO 9001                         |
| Environnement          | NF EN ISO 14001                     | ISO 14001                        |
| Securite machines      | NF EN ISO 12100                     | ISO 12100                        |
| Compatibilite EM       | NF EN 61000 series                  | IEC 61000                        |
| Appareillage           | NF EN 60947 series                  | IEC 60947                        |
| Canalisations          | NF EN 10255                         | EN 10255                         |
| Essais non destructifs | NF EN ISO 9712                      | ISO 9712                         |
| Management de l'energie | NF EN ISO 50001                    | ISO 50001                        |
| Securite de l'information | NF EN ISO 27001                  | ISO 27001                        |

## NF C 15-100 : Installations electriques

Norme fondamentale pour les installations electriques basse tension en France.
Equivaut a la CEI 60364 et a la HD 60364 (harmonisation europeenne).

Points specifiques a la norme francaise :
- Schemas de liaison a la terre : TT (reseau public), TN (neutre relie a la terre), IT (neutre isole)
- Section minimale des conducteurs : 1,5 mm2 eclairage, 2,5 mm2 prises
- Protection differentielle : 30 mA pour les circuits terminaux
- Zones de securite dans les pieces d'eau
- Nombre de prises par circuit : 8 max en 1,5 mm2, 12 max en 2,5 mm2

## Marquage CE et Directives europeennes

Le marquage CE n'est pas une marque de qualite mais une declaration du fabricant
attestant la conformite aux directives europeennes applicables.

| Directive              | Sigle  | Domaine                               |
|------------------------|--------|---------------------------------------|
| 2014/35/UE              | BT     | Basse tension                          |
| 2006/42/CE              | MD     | Machines                               |
| 2014/30/UE              | CEM    | Compatibilite electromagnetique        |
| 2014/53/UE              | RED    | Equipements radio                      |
| 2014/68/UE              | DESP   | Equipements sous pression              |
| 2014/34/UE              | ATEX   | Atmospheres explosibles                |
| 2009/125/CE             | ERP    | Conception ecologique                  |
| 93/42/CEE modifiee      | MDD    | Dispositifs medicaux                   |
| 2016/425                | PPE    | Equipements de protection individuelle |

## Niveaux de securite (Safety Integrity Levels)

| Norme                   | Domaine                | Niveaux / Categories                    |
|--------------------------|------------------------|-----------------------------------------|
| IEC 61508                | Generale (securite fonctionnelle) | SIL 1 a SIL 4                |
| ISO 13849-1              | Machines               | Categories B, 1, 2, 3, 4 + PL a a e    |
| IEC 62061                | Machines (electriques)  | SIL 1 a SIL 3                           |
| ISO 26262                | Automobile             | ASIL A a ASIL D                         |
| IEC 61511                | Procedes industriels   | SIL 1 a SIL 4                           |
| IEC 62304                | Logiciel medical       | Classe A, B, C                          |
| EN 50126 / 50128 / 50129 | Ferroviaire            | SIL 0 a SIL 4                           |

## Unites SI et equivalents

| Grandeur           | Unite SI             | Symboles courants et conversions                      |
|--------------------|----------------------|-------------------------------------------------------|
| Longueur           | metre (m)            | 1 in = 25,4 mm, 1 ft = 0,3048 m, 1 yd = 0,9144 m    |
| Masse              | kilogramme (kg)      | 1 lb = 0,4536 kg, 1 oz = 28,35 g                     |
| Temps              | seconde (s)          | h, min, s                                             |
| Courant electrique | ampere (A)           | mA, A, kA                                            |
| Temperature        | kelvin (K)           | K = degC + 273,15 ; degC = (degF - 32) / 1,8        |
| Quantite de matiere| mole (mol)           |                                                        |
| Intensite lumineuse| candela (cd)         |                                                        |
| Pression           | pascal (Pa)          | 1 bar = 100 000 Pa, 1 psi = 6 894,76 Pa              |
| Energie            | joule (J)            | 1 kWh = 3,6 MJ, 1 cal = 4,1868 J, 1 BTU = 1 055 J   |
| Puissance          | watt (W)             | 1 ch (cheval-vapeur) = 735,5 W, 1 hp = 745,7 W      |
| Force              | newton (N)           | 1 kgf = 9,80665 N, 1 lbf = 4,44822 N                 |
| Frequence          | hertz (Hz)           |                                                        |
| Tension electrique | volt (V)             |                                                        |
| Resistance         | ohm (Ω)              |                                                        |
| Capacite           | farad (F)            |                                                        |
| Inductance         | henry (H)            |                                                        |
| Flux lumineux      | lumen (lm)           |                                                        |
| Eclairement        | lux (lx)             |                                                        |
| Activite radioactive| becquerel (Bq)      |                                                        |
| Dose absorbee      | gray (Gy)            |                                                        |

## Regles de redaction technique en francais

1. **Nom des boutons et commandes** : en lettres capitales entre guillemets ou
   entre crochets : "Appuyez sur le bouton [MARCHE]".

2. **Avertissements de securite** : suivre la hierarchie suivante :
   - DANGER : risque de mort ou de blessure grave immediat
   - AVERTISSEMENT : risque de mort ou de blessure grave potentiel
   - ATTENTION : risque de blessure leger ou moyen
   - AVIS : risque de dommage materiel

3. **Numerotation des notes** : appels de note en exposant, notes en bas de
   page ou en fin de document.

4. **Tableaux** : titres en gras, en-tetes en majuscules non gras, alignement
   des colonnes numeriques a droite.

5. **Figures et illustrations** : titre sous la figure (Figure 1 - ...),
   reference dans le texte avec majuscule.

6. **Procedures** : utiliser des listes numerotees avec des imperatifs.
   Chaque etape commence par un verbe a l'imperatif.

7. **Abreviations** : definir a la premiere occurrence dans le texte ou
   dans un glossaire en debut de document.

8. **Termes etrangers** : les termes anglais couramment adoptes en francais
   (software, hardware, bypass) peuvent etre conserves si leur usage est
   generalise dans la profession. Dans le doute, utiliser le terme francais.

9. **Ecriture inclusive** : dans les documents techniques, privilegier les
   formes epicenes ou la double flexion courte ("les operateurs et operateurs")
   uniquement si le contexte RH l'exige. Par defaut, utiliser le masculin
   generique.

10. **Dates** : format francais jj/mm/aaaa (ou jj mois aaaa dans le texte).
    Ne pas utiliser le format ISO 8601 (aaaa-mm-jj) sauf dans les metadonnees.
