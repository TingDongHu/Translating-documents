---
id: fr/rules/scoring-rubric
type: scoring
target_lang: fr
name: Grille d'evaluation qualitative
description: Grille d'evaluation a 6 dimensions pour la traduction vers le francais
---

# Grille d'evaluation qualitative pour la traduction vers le francais

## Apercu des dimensions

| Dimension | Poids | Description |
|-----------|-------|-------------|
| 1. Exactitude numerique | 30 % | Virgule decimale, separateurs, formats date/heure, devises |
| 2. Cohérence terminologique | 20 % | Uniformite du vocabulaire, respect du glossaire |
| 3. Fidelite semantique | 25 % | Sens exact, nuances, registre, pas de hors-sujet |
| 4. Conformite au format | 10 % | Structure, mise en page, balises, tableaux |
| 5. Complétude | 10 % | Aucun segment omis, ni tronque, ni duplique |
| 6. Qualite des inferences/OCR | 5 % | Pertinence des restaurations, signalement des incertitudes |

**Seuil de reussite : 70/100** (moyenne ponderee)

**Zero-tolerance :** toute violation grave d'une regle zero-tolerance entraine une note plafonnee a 60/100 sur la dimension concernee ET un plafond global de 60/100 si la violation concerne les dimensions 1, 2 ou 3.

---

## Dimension 1 : Exactitude numerique (poids 30 %)

Regles zero-tolerance dans cette dimension :
- Point decimal utilise a la place de la virgule decimale → 0/100 sur la dimension
- Format de date americain (MM/DD/AAAA) utilise a la place du format francais → 0/100
- Symbole monetaire place avant le montant (100 € ecrit $100) → penalite severe
- Format 12h (AM/PM) utilise sans conversion en 24h → penalite severe

### Bareme

| Note | Qualite | Description |
|------|---------|-------------|
| **100** | Parfait | Tous les nombres, dates, montants, pourcentages et unites sont correctement formates selon les regles francaises. Aucune erreur numerique. Separateurs decimaux (virgule), separateurs de milliers (espace), formats de date (JJ/MM/AAAA), heures (24h), symboles monetaires (position apres le montant), pourcentages (espace avant %). |
| **90** | Excellent | Au plus 1 erreur mineure dans tout le document. Exemple : espace manquant entre nombre et unite (10 km ecrit 10km). Aucune violation zero-tolerance. |
| **80** | Bon | 2-3 erreurs mineures, ou 1 erreur moderee. Exemple : format de date ISO (2026-05-18) utilise dans un contexte non technique ; espace de milliers omis sur un nombre a 4 chiffres. Aucune violation zero-tolerance. |
| **70** | Satisfaisant | 4-6 erreurs mineures, ou 2 erreurs moderees. Exemple : plusieurs espaces de milliers manquants ; usage incoherent de la virgule decimale (parfois point, parfois virgule). |
| **60** | Insuffisant | 7-10 erreurs, ou 1 erreur grave. Exemple : format americain utilise pour les dates (MM/DD/AAAA) ; heure en format 12h avec AM/PM ; point decimal systematique. Note plafonnee si violation zero-tolerance. |
| **<50** | Rejet | Plus de 10 erreurs, ou 2+ violations zero-tolerance. Exemple : tout le document utilise le point decimal ; les dates sont en format americain ; les montants sont en format anglo-saxon. Travail a reprendre integralement. |

---

## Dimension 2 : Cohérence terminologique (poids 20 %)

Regles zero-tolerance dans cette dimension :
- Traduction differente d'un meme terme technique dans le meme document → 0/100 si systematique
- Non-respect d'un glossaire ou d'une terminologie client fournie → note plafonnee a 60

### Bareme

| Note | Qualite | Description |
|------|---------|-------------|
| **100** | Parfait | Terminologie parfaitement cohérente dans tout le document. Chaque terme source est traduit par le meme equivalent francais partout. Respect integral du glossaire et de la terminologie client. Aucune variation non justifiee. |
| **90** | Excellent | Au plus 1 terme traduit de deux manieres differentes (variation non justifiee). Le glossaire client est respecte a 100 %. Les acronymes sont definis a la premiere occurrence et utilises de maniere cohérente. |
| **80** | Bon | 2-3 variations non justifiees. Glossaire respecte avec 1 ecart mineur. Les acronymes sont globalement cohérents avec une exception. |
| **70** | Satisfaisant | 4-5 variations, ou 2 ecarts au glossaire. Certains termes techniques sont traduits de maniere incoherente, sans compromettre la comprehension. Les acronymes presentent 2-3 incoherences. |
| **60** | Insuffisant | 6-10 variations. Ecarts significatifs par rapport au glossaire client. Incoherence dans la traduction des termes cles. Note plafonnee si violation zero-tolerance. |
| **<50** | Rejet | Plus de 10 variations. Terminologie chaotique. Absence de coherence dans la traduction des termes techniques. Glossaire ignore. Travail a reprendre integralement. |

---

## Dimension 3 : Fidelite semantique (poids 25 %)

Regles zero-tolerance dans cette dimension :
- Contresens majeur (sens oppose au texte source) → 0/100 sur la dimension
- Omission d'un paragraphe entier ou d'une section → 0/100
- Contresens sur un element cle (date, montant, nom propre, consigne) → penalite severe

### Bareme

| Note | Qualite | Description |
|------|---------|-------------|
| **100** | Parfait | Le sens du texte source est rendu integralement et avec exactitude. Toutes les nuances sont preservees. Aucun contresens, aucun faux-sens, aucune omission. Le registre du texte source est parfaitement respecte. Les references culturelles sont correctement adaptees. |
| **90** | Excellent | Un faux-sens mineur (exemple : mot precise traduit par "exact" au lieu de "precis"). Nuances globalement preservees. Registre respecte. Aucune omission significative. Les references culturelles sont correctement traitees. |
| **80** | Bon | 2-3 faux-sens mineurs, ou 1 omission mineure (phrase ou bout de phrase). Nuances partiellement preservees. Registre globalement respecte avec un ecart. Les references culturelles sont traitees de maniere acceptable. |
| **70** | Satisfaisant | 4-6 faux-sens ou omissions mineures. Quelques nuances perdues. Registre parfois deviant du texte source. References culturelles partiellement traitees. La comprehension globale du document reste correcte. |
| **60** | Insuffisant | 1 contresens significatif, ou faux-sens multiples (7+), ou omissions notables. Nuances frequemment perdues. Registre non respecte. References culturelles ignorees ou mal traitees. Note plafonnee si violation zero-tolerance. |
| **<50** | Rejet | Contresens majeurs rendant le texte incompréhensible ou trompeur. Omissions de sections entieres. Sens deforme. Registre inapproprie. Travail a reprendre integralement. |

---

## Dimension 4 : Conformite au format (poids 10 %)

Regles zero-tolerance dans cette dimension :
- Non-respect des regles de ponctuation francaise (espaces avant les doubles signes, guillemets non conformes) → 0/100 si systematique
- Structure du document source completement ignoree → 0/100

### Bareme

| Note | Qualite | Description |
|------|---------|-------------|
| **100** | Parfait | Toutes les regles typographiques francaises sont respectees : espaces insécables avant les doubles signes (: ; ! ?), guillemets francais « », apostrophes typographiques, tirets cadratins, capitalisation des titres selon les regles francaises. La structure du document source est parfaitement reproduite : titres, sous-titres, listes, tableaux, paragraphes. |
| **90** | Excellent | 1-2 ecarts typographiques mineurs. Exemple : guillemets anglais utilises une fois dans une citation interne. Structure du document source respectee a 100 %. |
| **80** | Bon | 3-5 ecarts typographiques, ou 1 erreur de structure (titre mal hierarchise, liste non reproduite). Guillemets globalement conformes avec quelques exceptions. |
| **70** | Satisfaisant | 6-10 ecarts typographiques, ou 2-3 erreurs de structure. Espaces insécables parfois omises. Guillemets francais et anglais melanges sans raison. Tableaux partiellement reproduits. |
| **60** | Insuffisant | 11-20 ecarts, ou erreurs de structure significatives. Ponctuation francaise non respectee de maniere systematique. Structure du document source partiellement ignoree. Note plafonnee si violation zero-tolerance. |
| **<50** | Rejet | Plus de 20 ecarts. Ponctuation anglo-saxonne utilisee dans tout le document (guillemets anglais " ", espaces avant doubles signes absentes, apostrophes droites). Structure du document source ignoree. Travail a reprendre integralement. |

---

## Dimension 5 : Complétude (poids 10 %)

Regles zero-tolerance dans cette dimension :
- Section entiere non traduite → 0/100 sur la dimension
- Page entiere sautee → 0/100

### Bareme

| Note | Qualite | Description |
|------|---------|-------------|
| **100** | Parfait | 100 % du document source est traduit. Aucun segment, aucune phrase, aucun mot n'est omis. Aucune partie n'est laissee non traduite. Aucune duplication ou traduction double. Tous les elements du document source sont presents dans le document cible. |
| **90** | Excellent | Au plus 1 phrase courte oubliee. 99-100 % de couverture. Aucune section entiere omise. Aucune page sautee. Peut contenir une duplication mineure. |
| **80** | Bon | 2-3 phrases omises, ou 1 paragraphe court. 97-99 % de couverture. Peut contenir 2-3 duplications. Aucune section ou page entiere omise. |
| **70** | Satisfaisant | 4-6 phrases omises, ou 1-2 paragraphes. 95-97 % de couverture. Peut contenir quelques duplications. Des segments non traduits apparaissent (mots ou bouts de phrases). |
| **60** | Insuffisant | 7-15 phrases omises, ou plusieurs paragraphes. 90-95 % de couverture. Duplications notables. Segments non traduits significatifs. Note plafonnee si violation zero-tolerance. |
| **<50** | Rejet | Moins de 90 % du document traduit. Sections entieres ou pages manquantes. Travail abandonne en cours. Nombreuses duplications. Travail a reprendre integralement. |

---

## Dimension 6 : Qualite des inferences / OCR (poids 5 %)

Regles zero-tolerance dans cette dimension :
- Texte restaure invente sans fondement dans le contexte → 0/100 sur la dimension
- Absence totale de signalement alors que le document source presente des defauts OCR evidents → 0/100

### Bareme

| Note | Qualite | Description |
|------|---------|-------------|
| **100** | Parfait | Tous les artefacts OCR sont correctement identifies et traites. Les restaurations sont pertinentes, correctement formatees en `[restaure: ...]` et justifiees. Les caracteres douteux sont signales. Les textes tronques sont marques. Aucune information n'est invente(e). Le niveau de certitude est correctement indique pour chaque restauration. |
| **90** | Excellent | 1-2 restaurations dont la justification pourrait etre plus precise. Tous les artefacts sont identifies. Format correct. Aucune invention. Signalement adequat. |
| **80** | Bon | 3-4 restaurations imparfaitement formulees ou justifiees. 1 artefact non identifie. Format globalement correct. Restaurations basees sur le contexte. |
| **70** | Satisfaisant | 5-6 restaurations problematiques, ou format incoherent (melange de styles de signalement). 2-3 artefacts non identifies. Certaines restaurations manquent de justification contextuelle. |
| **60** | Insuffisant | 7-10 restaurations mal formulees ou injustifiees. Plusieurs artefacts OCR non traites. Restaurations inventees sans base contextuelle. Note plafonnee si violation zero-tolerance. |
| **<50** | Rejet | Artefacts OCR ignores ou mal traites de maniere systematique. Restaurations inventees sans lien avec le texte source. Absence de signalement des defauts OCR. Travail a reprendre integralement. |

---

## Regles globales et plafonnement

### Violations zero-tolerance

Les violations suivantes sont considerees comme zero-tolerance et entrainent un **plafonnement a 60/100** sur la dimension concernee ET un **plafonnement de la note globale a 60/100** (quelle que soit la moyenne ponderee) :

| Dimension | Violation zero-tolerance |
|-----------|--------------------------|
| 1. Exactitude numerique | Point decimal a la place de la virgule (usage systematique) |
| 1. Exactitude numerique | Format de date americain (MM/DD/AAAA) dans tout le document |
| 1. Exactitude numerique | Format 12h (AM/PM) utilise sans conversion |
| 2. Cohérence terminologique | Traduction systematiquement incoherente d'un meme terme technique |
| 2. Cohérence terminologique | Non-respect du glossaire client fourni |
| 3. Fidelite semantique | Contresens majeur modifiant le sens du document |
| 3. Fidelite semantique | Omission d'une section ou page entiere |
| 4. Conformite au format | Non-respect systematique de la ponctuation francaise |
| 4. Conformite au format | Structure du document source ignoree |
| 5. Complétude | Section ou page entiere non traduite |
| 6. Inferences/OCR | Restauration inventee sans fondement contextuel |

### Violations zero-tolerance enregistrables (toutes dimensions)

Les violations suivantes, bien que n'apparaissant pas dans les barèmes specifiques ci-dessus, sont considerees comme zero-tolerance en vertu des regles generales de traduction vers le francais :

| Violation | Impact |
|-----------|--------|
| Melange vous/tu dans un document formel | Plafond global a 60/100 |
| Symbole monetaire place avant le montant (ex. €100) | Plafond dimension 1 a 60/100 |
| Absence d'espace avant les doubles signes (: ; ! ?) si systematique | Plafond dimension 4 a 60/100 |
| Guillemets anglais " " utilises systematiquement sans guillemets francais | Plafond dimension 4 a 60/100 |
| Noms propres francais sans leurs accents (Ecole → Ecole, Etat → Etat) | Plafond dimension 4 a 60/100 si systematique |

### Calcul de la note globale

```
Note globale = (Note_D1 × 0,30) + (Note_D2 × 0,20) + (Note_D3 × 0,25) + (Note_D4 × 0,10) + (Note_D5 × 0,10) + (Note_D6 × 0,05)
```

**Plafonnement :** si une violation zero-tolerance est detectee et confirmee, la note globale est plafonnee a 60/100. Dans ce cas, la note est indiquee comme "60 (plafonne)" quelle que soit la moyenne ponderee calculee.

### Decision finale

| Note globale | Decision |
|-------------|----------|
| 90-100 | Accepte - Qualite excellente |
| 80-89 | Accepte - Qualite bonne |
| 70-79 | Accepte sous reserve - Corrections mineures requises |
| 60-69 | Refuse - Corrections majeures requises (revision obligatoire) |
| < 60 ou plafonne | Refuse - Travail a reprendre integralement |

### Procedure d'evaluation

1. Verifier les violations zero-tolerance en premier (tout le document).
2. Si une violation zero-tolerance est confirmee, appliquer le plafonnement.
3. Evaluer chaque dimension independamment en utilisant le bareme correspondant.
4. Calculer la moyenne ponderee.
5. Appliquer le plafonnement eventuel.
6. Rendre la decision finale.

---

## Annexes

### Annexe A : Exemples de violations zero-tolerance

**Exemple 1 : Point decimal (violation D1)**
- Source : "The temperature is 37.5 degrees."
- Traduit comme : "La temperature est de 37.5 degres." (au lieu de 37,5)
- Verdict : Zero-tolerance → D1 = 60 max, note globale plafonnee a 60

**Exemple 2 : Date americaine (violation D1)**
- Source : "Meeting on 05/18/2026"
- Traduit comme : "Reunion le 05/18/2026" (au lieu de 18/05/2026)
- Verdict : Zero-tolerance → D1 = 60 max, note globale plafonnee a 60

**Exemple 3 : Melange vous/tu (violation transversale)**
- Document formel melangeant "nous vous informons" et "comme tu le sais"
- Verdict : Zero-tolerance → note globale plafonnee a 60

**Exemple 4 : Montant errone (violation D1)**
- Source : "The price is $100.50"
- Traduit comme : "Le prix est de 100,50 $US" (correct) OU "Le prix est de $100.50" (incorrect)
- Verdict si incorrect : Zero-tolerance → D1 = 60 max

**Exemple 5 : Section non traduite (violation D5)**
- Un paragraphe entier du document source reste en anglais dans le document cible
- Verdict : Zero-tolerance → D5 = 60 max

### Annexe B : Guide rapide des formats corrects

| Element | Anglais (source) | Francais (cible) |
|---------|-------------------|-------------------|
| Virgule decimale | 3.14 | 3,14 |
| Milliers | 1,234,567 | 1 234 567 |
| Date | 05/18/2026 | 18/05/2026 |
| Heure | 2:30 PM | 14 h 30 |
| Monnaie | $100.50 | 100,50 $ / 100,50 USD |
| Pourcentage | 15.5% | 15,5 % |
| Guillemets | "texte" | « texte » |
| Apostrophe | ' | ' (typographique) |
| Tiret d'incise | - text - | — texte — |
| Deux-points | text: | texte : (espace avant) |
| Point d'interrogation | text? | texte ? (espace avant) |
| Point d'exclamation | text! | texte ! (espace avant) |

### Annexe C : Niveaux de gravite des erreurs

| Gravite | Definition | Impact |
|---------|------------|--------|
| Critique | Violation zero-tolerance, contresens, omission majeure | Plafonnement global ou 0 sur la dimension |
| Grave | Erreur affectant la comprehension ou la qualite du document | -20 a -30 points sur la dimension |
| Moderee | Erreur visible mais ne compromettant pas la comprehension | -10 a -20 points sur la dimension |
| Mineure | Erreur de detail, ecart typographique leger | -5 a -10 points sur la dimension |
| Cosmétique | Imperfection sans impact sur le sens ou la qualite | -1 a -5 points sur la dimension |
