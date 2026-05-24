---
id: fr/rules/base
type: rules
target_lang: fr
name: Règles de traduction vers le français
description: Règles de base pour la traduction de documents vers le français
---

## Format des nombres

- Séparateur de décimales : virgule (1 234,56)
- Séparateur de milliers : espace insécable (1 234 567)
- Pourcentage : espace avant le signe (15,5 %)
- Nombres négatifs : signe moins ou parenthèses (−1 234,56)

## Monnaie

- Symbole après le montant : 100 €, 1 234,56 $
- Espace insécable entre le montant et le symbole
- Termes français : euro, dollar, livre sterling, yen
- Monnaie française historique : franc (ancienne monnaie)

## Date et heure

- Format : JJ/MM/AAAA (18/05/2026)
- Format long : le 18 mai 2026
- Jours de la semaine : lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche
- Mois : janvier, février, mars, avril, mai, juin, juillet, août, septembre, octobre, novembre, décembre
- Heure : 14 h 30 (format 24h)

## Adresses

- Ordre français : numéro + rue + code postal + ville
- Exemple : 37, rue du Ponceau, 75002 Paris
- Départements : numéro + nom (75 - Paris, 13 - Marseille)

## Noms propres

- Conserver les noms propres étrangers dans leur orthographe d'origine
- Noms de lieux français : utiliser l'orthographe officielle française
- Noms d'entreprises : conserver la dénomination sociale exacte

## Ponctuation

- Guillemets français : « texte » (avec espaces insécables)
- Guillemets anglais acceptés dans les contextes informels : "texte"
- Espace avant les deux-points : :
- Espace avant le point-virgule : ;
- Espace avant le point d'exclamation : !
- Espace avant le point d'interrogation : ?
- Tiret cadratin pour les incises : —
- Apostrophe : ’ (Unicode U+2019)

## Mise en forme

- Conserver la structure : titres, listes, tableaux
- Titres : capitalisation selon les règles françaises (première lettre en majuscule, reste en minuscule sauf noms propres)
- Listes : utiliser des tirets (-) ou des numéros (1., 2., 3.)
- Tableaux : conserver l'alignement et la structure

## Grammaire

- Accord en genre et en nombre : adjectifs, participes passés
- Utiliser la voix active autant que possible
- Accord du verbe avec le sujet
- Utiliser le subjonctif après les expressions de volonté, de doute, de nécessité
- Pronoms : accord en genre et en nombre

## Registre

- Documents formels : vouvoiement, phrases complètes
- Documents juridiques : registre soutenu, formules consacrées
- Documents administratifs : style administratif français standard
- Documents commerciaux : registre professionnel, courtois

## Marques OCR

- Format d'inférence : `[inféré : texte original"original", description, raison]`
- Exemple : `[inféré : "pas age"original", basé sur le contexte, probablement "passage"]`
- Signaler les caractères douteux avec `[caractère incertain : X]`
- Signaler les textes tronqués avec `[texte incomplet]`

## Philosophie de traduction : fidélité, élégance, adaptation

1. **Fidélité** : sens exact du texte source, aucune omission ni ajout
2. **Élégance** : style naturel et fluide en français, éviter le « franglais »
3. **Adaptation** : adapter les références culturelles quand nécessaire

Ordre de priorité : fidélité > élégance > adaptation

## Stratégies pour le langage créatif

### Jeux de mots et calembours
- Les jeux de mots intraduisibles : conserver l'original + annotation explicative
- Les jeux de mots adaptables : créer un équivalent français
- Exemple : « Ship from China » → « Livraison depuis la Chine » (pas de jeu de mots en français, adapter le sens)

### Traduction de slogans
- Privilégier l'impact marketing sur la traduction littérale
- Adapter au marché français : culture, humour, références
- Exemple : « Just Do It » → « Just Do It » (garder l'anglais si la marque est internationale)

### Localisation de noms de marques
- Vérifier les connotations en français
- Adapter la phonétique si nécessaire
- Exemple : « Chevrolet Nova » → vérifier que « nova » n'a pas de connotation négative

## Langage non standard

### Dialectes et régionalismes
- Français de France vs français canadien vs français belge vs français suisse
- Adapter au marché cible principal
- Signaler les variantes régionales importantes

### Argot et langage familier
- Documents formels : registre soutenu, éviter l'argot
- Documents informels : conserver le ton si approprié
- Internet et réseaux sociaux : adapter les expressions

### Jargon technique
- Conserver la terminologie technique standard
- Utiliser les termes normalisés (ISO, AFNOR)
- Expliquer les acronymes à la première occurrence

## Problèmes de qualité source

### Erreurs OCR
- Corriger les erreurs évidentes (ex : « l » → « I », « 0 » → « O »)
- Signaler les corrections avec `[inféré : ...]`
- Conserver le texte original si la correction est incertaine

### Texte incomplet ou tronqué
- Signaler avec `[texte incomplet]`
- Ne pas inventer de contenu manquant
- Traduire ce qui est disponible

### Documents multilingues
- Identifier les langues présentes
- Traduire chaque section dans la langue cible
- Conserver les citations dans la langue d'origine si approprié
