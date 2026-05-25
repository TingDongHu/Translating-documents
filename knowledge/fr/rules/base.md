---
id: fr/rules/base
type: rules
target_lang: fr
name: Regles de traduction vers le francais
description: Regles de base pour la traduction de documents vers le francais
---

# Regles de traduction vers le francais

## 1. Format des nombres

### 1.1 Separateur decimal
- La virgule est le seul separateur decimal autorise en francais.
- Exemple correct : 3,14 / 0,75 / 123,45
- Exemple accepte (variante belge/suisse) : 3·14 (point median, usage restreint)
- Erreur grave (zero-tolerance) : utiliser le point comme separateur decimal (3.14) est une faute de typographie francaise. Ne JAMAIS ecrire 3.14 dans un texte francais.

### 1.2 Separateur de milliers
- Espace insécable (ou simple espace si l'espace insécable n'est pas techniquement possible) pour separer les milliers.
- Exemple correct : 1 234 567 / 12 345 / 1 000
- Exemple accepte (variante) : 1'234 (apostrophe, usage suisse)
- Jamais de point comme separateur de milliers en francais moderne.
- Les nombres a quatre chiffres (1000-9999) peuvent s'ecrire sans separateur (1234) ou avec espace (1 234) selon le contexte.

### 1.3 Nombres negatifs
- Signe moins (−, U+2212) colle au nombre, ou entre parentheses en contexte comptable.
- Exemple correct : −1 234,56 / (1 234,56) pour les bilans
- Ne pas utiliser le trait d'union (-) comme signe moins en typographie soignee.

### 1.4 Pourcentages
- Espace insécable avant le signe %.
- Exemple correct : 15,5 % / 100 % / une augmentation de 3 %
- Exemple incorrect : 15.5% / 15,5% (sans espace)
- Dans certains contextes techniques (tableaux, figures), le pourcentage peut etre colle a la valeur, mais la norme exige l'espace.

### 1.5 Fractions et nombres decimaux
- Les fractions simples s'ecrivent en toutes lettres : 1/2 → un demi, 3/4 → trois quarts.
- En contexte technique, conserver la forme fractionnaire (1/2, 3/4).
- Les decimaux utilisent toujours la virgule, jamais le point.

### 1.6 Nombres en toutes lettres
- De 0 a 16 : zero, un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize, quatorze, quinze, seize
- 17-19 : dix-sept, dix-huit, dix-neuf
- 20-99 avec trait d'union (vingt et un → vingt-et-un, rectifications de 1990)
- 100-999 : deux cents, deux cent un (pas d'accord de "cent" devant un autre nombre)
- 1000 et plus : mille est invariable (pas de "s")
- Les rectifications orthographiques de 1990 recommandent le trait d'union pour tous les numeraux composés.

### 1.7 Unités de mesure
- Espace insécable entre le nombre et l'unite.
- Exemple correct : 10 km / 5 kg / 100 ml
- Exemple incorrect : 10km / 5kg
- Unites ISO avec symboles normalises : km, m, cm, mm, kg, g, mg, l, ml, h, min, s
- Temperature : 25 °C (espace avant °C)

### 1.8 Nombres ordinaux
- 1er / 1re (premier / premiere)
- 2e / 2de (deuxieme / seconde) — pas "2eme" ni "2nd" en francais standard
- 3e (troisieme), 4e (quatrieme), etc.
- L'exposant (1^er, 1^re) est facultatif ; 1er est acceptable.

### 1.9 Plages numeriques
- Trait d'union ou "a" pour exprimer une plage.
- Exemple : 10-15 / de 10 a 15 / pages 10-15
- Jamais d'espace avant et apres le trait d'union dans les plages.

---

## 2. Monnaie

### 2.1 Position du symbole
- Le symbole monetaire se place APRES le montant, separe par une espace insécable.
- Exemple correct : 100,00 € / 50 $ / 25 £ / 1 200 ¥
- Exemple incorrect : €100 / $50 / £25
- Exception : les tableaux financiers et certains contextes internationaux peuvent utiliser le code ISO avant le montant.

### 2.2 Codes ISO
- Utiliser les codes ISO 4217 en contexte technique ou international.
- EUR, USD, GBP, JPY, CHF, CAD, AUD, CNY
- Exemple : 100,00 EUR / 50,00 USD
- En contexte general, preferer les symboles (€, $, £) aux codes.

### 2.3 Noms des devises en francais
- euro (masculin, sans majuscule) — pluriel : euros
- dollar (masculin) — dollar americain, dollar canadien, dollar australien
- livre sterling (feminin)
- yen (masculin, invariable)
- franc suisse (masculin) — anciennement franc francais
- yuan / renminbi (masculin)

### 2.4 Centimes et subdivisions
- Les centimes s'indiquent apres la virgule : 100,50 € (cent euros et cinquante centimes)
- Format : 0,01 € minimum (un centime)
- Subdivisions : centime (euro), cent (dollar), penny/pence (livre), sen (yen)

### 2.5 Devises historiques
- franc francais (FRF) : ancienne devise de la France (remplacee par l'euro en 2002)
- Taux de conversion fixe : 1 EUR = 6,55957 FRF
- Indiquer "ancienne devise" ou "AF" (anciens francs) en contexte historique
- ecu : unite de compte europeenne avant l'euro

### 2.6 Grands montants
- Les grands montants s'ecrivent avec les mots million / milliard / billion.
- Exemple : 1,5 million d'euros / 2,3 milliards de dollars
- Attention aux faux amis : billion francais = 10^12 (pas 10^9 comme en anglais US)
- Mille milliards = billion (francais) = trillion (anglais US)

### 2.7 Contexte financier
- Parents : (1 234,56) pour les montants negatifs
- Soldes : signe + ou - devant le montant : +1 000,00 € / −500,00 €
- Taux d'interet : 3,5 % (avec espace avant %)
- TVA : TVA a 20 % / TTC (toutes taxes comprises) / HT (hors taxes)

---

## 3. Date et heure

### 3.1 Format de date court
- Ordre : jour / mois / annee (JJ/MM/AAAA)
- Exemple correct : 18/05/2026
- Exemple incorrect : 05/18/2026 (format americain) — zero-tolerance
- Variante ISO (contexte technique) : 2026-05-18 (AAAA-MM-JJ)
- Variante francaise complete : 18/05/2026 — pas de zero devant le jour en contexte usuel (18/5/2026 acceptable)

### 3.2 Format de date long
- Article + jour + mois + annee
- Exemple : le 18 mai 2026 / le 1er janvier 2026
- Premier du mois : le 1er janvier (pas "le 1 janvier" en francais soigne)
- Devant les mois commenceant par une voyelle : le 2 avril / le 3 aout

### 3.3 Mois de l'annee
- janvier, fevrier, mars, avril, mai, juin, juillet, aout, septembre, octobre, novembre, decembre
- Les noms de mois sont en minuscule en francais (sauf debut de phrase).
- Abreviations : janv., fevr., mars, avr., mai, juin, juil., aout, sept., oct., nov., dec.
- Attention : aout prend un accent circonflexe (reforme 1990 : aout sans accent possible).

### 3.4 Jours de la semaine
- lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche
- Toujours en minuscule sauf debut de phrase.
- Abreviations : lun., mar., mer., jeu., ven., sam., dim.

### 3.5 Siecles et annees
- Siecle en chiffres romains : XXI^e siecle / 21^e siecle (les deux acceptes)
- Annees : en 2026 / l'annee 2026 / en 2025-2026
- Decennies : les annees 1990 / les annees quatre-vingt-dix
- Avant JC / apres JC : -500 (ou 500 av. J.-C.) / 2026 apr. J.-C.

### 3.6 Format de l'heure
- Format 24h obligatoire en francais.
- Exemple correct : 14 h 30 / 9 h 15 / 23 h 45
- Exemple incorrect : 2:30 PM / 2:30 p.m. — zero-tolerance en contexte formel
- Heures pleines : 14 h (pas 14:00 ni 14h00 en francais soigne)
- Minutes : 14 h 30 (avec espace entre h et les minutes)
- Secondes : 14 h 30 min 15 s (contexte technique)

### 3.7 Durees
- Heures encadrees par des lettres : 2 h 30 min / 1 h 45
- Format decimal : 2,5 h (contexte technique)
- Duree en jours : 3 jours / 72 heures
- Chronometrage : 1 h 23 min 45 s

### 3.8 Fuseaux horaires et references temporelles
- Heure legale : heure d'hiver (UTC+1) / heure d'ete (UTC+2, du dernier dimanche de mars au dernier dimanche d'octobre)
- Abreviation : HEC (Heure de l'Europe Centrale) / CEST (Central European Summer Time)
- Indiquer le fuseau en contexte international : 14 h 30 UTC+1 / 14 h 30 (heure de Paris)

### 3.9 Periodes et saisons
- Printemps, ete, automne, hiver (masculins sauf automne qui est masculin)
- Trimestre : T1, T2, T3, T4 ou 1^er trimestre, 2^e trimestre
- Semestre : S1 (janvier-juin), S2 (juillet-decembre)
- Annee fiscale / scolaire : 2025-2026 (avec trait d'union)

### 3.10 Mentions temporelles
- Aujourd'hui, hier, demain, avant-hier, apres-demain
- Cette semaine, la semaine prochaine, la semaine derniere
- Ce mois-ci, le mois prochain, le mois dernier
- Cette annee, l'annee prochaine, l'annee derniere

---

## 4. Adresses

### 4.1 Format general francais
- Ordre strict : [numero] + [voie] → [code postal] → [ville] → [pays]
- Exemple : 37, rue du Ponceau, 75002 Paris, France
- Chaque element sur une ligne separee dans les en-tetes de lettre.

### 4.2 Types de voies et abreviations
- rue (r.), avenue (av.), boulevard (bd), place (pl.), impasse (imp.), allee (all.)
- chemin (chem.), route (rte), cours (c.), square (sq.)
- Exemple : 25, bd Saint-Germain, 75005 Paris

### 4.3 Code postal
- Code a 5 chiffres en France metropolitaine.
- Premier chiffre = numero du departement (75 = Paris, 13 = Bouches-du-Rhone, 69 = Rhone).
- Codes speciaux : 97100 (Guadeloupe), 97200 (Martinique), 97300 (Guyane), 97400 (La Reunion), 97500 (Saint-Pierre-et-Miquelon), 97600 (Mayotte), 98000 (Monaco).
- Code postal et ville sur la meme ligne, separe par un espace.

### 4.4 Format international
- Avant l'expediteur : mention "Exp. :" ou "Expediteur :"
- Pour les envois internationaux : ajouter le nom du pays en MAJUSCULES sur la derniere ligne.
- Exemple international :
  Mme Sophie Martin
  15, rue de la Paix
  75002 Paris
  FRANCE

### 4.5 Adresses pour les autres pays francophones
- Belgique : code postal a 4 chiffres (1000 Bruxelles)
- Suisse : code postal a 4 chiffres (1200 Geneve, 1000 Lausanne)
- Canada : [numero] [voie], [ville] ([province]) [code postal], Canada
  Exemple : 123, rue Sainte-Catherine, Montreal (Quebec) H2X 1K9, Canada
- Code postal canadien : format A#A #A#

### 4.6 Elements d'adresse
- Boite postale : BP 123 (ou Boite postale 123)
- Cedex : 75002 Paris Cedex 02 (pour les entreprises)
- Lieu-dit : Lieu-dit Les Chataigniers, 24300 La Chapelle-Montmoreau
- Residence : Residence Les Fleurs, Batiment B, 2e etage, Appartement 45

### 4.7 Noms de lieux
- Departements : nom precedente du numero — 75 Paris, 13 Bouches-du-Rhone, 69 Rhone
- Regions : Auvergne-Rhone-Alpes, Bourgogne-Franche-Comte, Bretagne, Centre-Val de Loire, Corse, Grand Est, Hauts-de-France, Ile-de-France, Normandie, Nouvelle-Aquitaine, Occitanie, Pays de la Loire, Provence-Alpes-Cote d'Azur
- Villes : conserver les accents — Montreal, Quebec, Geneve, Bruxelles

---

## 5. Noms propres

### 5.1 Conservation des accents
- Les noms propres francais conservent TOUS leurs accents, diacritiques et signes speciaux, y compris en majuscules.
- Regle academique : les majuscules doivent porter les accents (Etat, Ecole, Ile-de-France, Eglise).
- Caracteres concernes : E, E, E, E, C, I, I, O, U, U, A, A, AE, OE
- Exemple : ECOLE (pas ECOLE) / ETAT (pas ETAT)
- Meme en contexte de saisie informatique, preferer les majuscules accentuees.

### 5.2 Noms propres etrangers
- Conserver l'orthographe originale des noms propres etrangers.
- Exemple : Shakespeare (pas "Chekspir"), Beethoven, Nietzsche, Dostoevsky
- Translitteration du cyrillique : utiliser la norme ISO 9 ou la translitteration usuelle en francais.
- Exemple : Tchekhov (pas Chekhov) / Dostoievski (pas Dostoevsky)
- Noms asiatiques : conserver l'ordre original (nom de famille + prenom) si culturellement approprie.

### 5.3 Noms de lieux etrangers
- Utiliser l'exonyme francais lorsqu'il existe de maniere etablie.
- Exemple : Londres (pas London) / New York (pas Nouvelle-York) / Munich (pas Munchen) / Rome (pas Roma) / Pekin (pas Beijing)
- Pour les exonymes moins connus, conserver le nom local.
- Noms de pays : la France, l'Espagne, l'Italie, le Bresil, le Japon, les Etats-Unis, le Royaume-Uni

### 5.4 Entreprises et formes juridiques
- Conserver la denomination sociale exacte (y compris la ponctuation et les majuscules originales).
- Formes juridiques francaises :
  - SARL (Societe a Responsabilite Limitee)
  - SAS (Societe par Actions Simplifiee)
  - SA (Societe Anonyme)
  - SNC (Societe en Nom Collectif)
  - SCA (Societe en Commandite par Actions)
  - EURL (Entreprise Unipersonnelle a Responsabilite Limitee)
  - SASU (Societe par Actions Simplifiee Unipersonnelle)
  - Association loi 1901
  - GIE (Groupement d'Interet Economique)
- Formes juridiques etrangeres : conserver l'abreviation originale (LLC, GmbH, Ltd, Inc., SpA, AB, SA/NV)

### 5.5 Marques et noms commerciaux
- Conserver l'orthographe officielle des marques.
- Ne pas traduire les noms de marque (sauf exception notoire historique).
- Verifier les noms de produits : certains ont des noms officiels en francais.
- Exemple : Google (pas traduit), Mercedes-Benz (nom conserve)
- Articles definis : le Mercedes (la marque) / la Mercedes (la voiture)

### 5.6 Titres d'oeuvres
- Titres d'oeuvres (livres, films, tableaux) : majuscule au premier mot et aux noms propres en francais.
- Exemple : "Le grand Meaulnes" / "A la recherche du temps perdu" / "Les miserables"
- Titres d'oeuvres etrangeres : conserver le titre original. Si traduit, indiquer entre parentheses.
- Exemple : "Hamlet" ou "Hamlet" (trad. "Hamlet, prince de Danemark")

### 5.7 Personnalites et titres
- Monsieur (M.), Madame (Mme), Mademoiselle (Mlle) — usage feminin : Mme, pas "Mme"
- Docteur (Dr), Professeur (Pr), Maître (Me) pour les avocats
- Titres nobiliaires : le comte, la duchesse, le vicomte, le marquis
- Titres presidentiels : M. le President, Mme la Presidente, Son Excellence

### 5.8 Noms de rues et lieux
- Les noms de rues, places et monuments prennent une majuscule au premier mot significatif.
- Exemple : rue de la Paix (pas "Rue de la Paix") / place de la Concorde / avenue des Champs-Elysees
- Batiments : le Louvre, la Tour Eiffel, l'Arc de Triomphe, le Pantheon
- Les mots generiques (rue, place, allee) restent en minuscule.

---

## 6. Ponctuation

### 6.1 Guillemets
- Guillemets francais obligatoires : « » (U+00AB et U+00BB).
- Espace insécable entre le guillemet et le texte : « texte »
- Espace insécable apres le guillemet ouvrant et avant le guillemet fermant.
- Guillemets anglais " " acceptes uniquement dans les citations internes (guillemet dans un guillemet).
- Pas d'espace avec les guillemets anglais.

### 6.2 Espaces avant la double ponctuation
- Espace insécable (ou espace fine insécable) AVANT :
  - Les deux-points ( : )
  - Le point-virgule ( ; )
  - Le point d'exclamation ( ! )
  - Le point d'interrogation ( ? )
- Cette regle est specifique au francais et essentielle a la typographie correcte.
- Apres ces signes, espace normale (sauf pour le point-virgule qui garde une espace fine).

### 6.3 Espaces apres la ponctuation simple
- Apres un point (.) : espace normale.
- Apres une virgule (,) : espace normale.
- Apres des points de suspension (...) : espace normale (ou pas d'espace si fin de mot).
- Le point n'est pas precede d'une espace en francais.

### 6.4 Tiret cadratin (—)
- Tiret cadratin (em dash, U+2014) pour les incises et les dialogues.
- Espaces insécables avant et apres : phrase — incise — suite.
- Alternative en contexte moins formel : tiret moyen (en dash, U+2013) avec espaces.
- Dans les dialogues, chaque changement d'interlocuteur commence par un tiret cadratin.

### 6.5 Apostrophe et traits d'union
- Apostrophe courbe ’ (U+2019) de preference, ou droite (') si contrainte technique.
- Pas d'espace avant ou apres l'apostrophe.
- Trait d'union (-) pour les mots composes : arc-en-ciel, chef-d'oeuvre, grand-mere
- Trait d'union dans les numeraux : vingt-et-un, cent-vingt-trois
- Trait d'union dans les prenoms composes : Jean-Pierre, Marie-Claire
- Trait d'union apres "ce" : ce-matins (familier) ; "cet" sans trait d'union

### 6.6 Points de suspension
- Trois points (...), pas plus.
- Espace apres les points de suspension si la phrase continue.
- Pas d'espace avant si le mot est tronque : "Je..."
- Utilisation : suspension de la pensee, omission, hesitation.

### 6.7 Parentheses et crochets
- Pas d'espace avant la parenthese ouvrante.
- Pas d'espace avant le crochet ouvrant.
- Espace apres la parenthese ou le crochet fermant (sauf si suivi d'une autre ponctuation).
- Parentheses dans les phrases : (comme ceci) avec espace avant la parenthese fermante en fin de phrase avant le point.

### 6.8 Virgule
- Pas de virgule avant "et" (pas d'Oxford comma en francais).
- Exemple : J'ai achete du pain, du fromage et du vin. (pas "du pain, du fromage, et du vin")
- Virgule apres un complement en debut de phrase : Ce matin, je suis alle au marche.
- Virgule encadrant une incise : Le chien, qui etait fatigue, dormait.

### 6.9 Ponctuation des listes
- Elements de liste en minuscule, termines par un point-virgule, sauf le dernier qui prend un point.
- Ou : elements en minuscule sans ponctuation finale.
- Elements de liste complets (phrases entieres) : chaque element commence par une majuscule et se termine par un point.

### 6.10 Abreviations et initiales
- Point apres chaque abreviation coupée a la premiere syllabe : M., Mme, Mlle, Dr, Pr
- Pas de point pour les sigles : SNCF, EDF, ONU, OTAN, UE, USA
- Sigles qui se prononcent comme des mots : ONU (o-nu), OTAN (o-tan), UNESCO
- Sigles epeles : SNCF (es-en-ce-eff), USA (u-es-a)

---

## 7. Mise en forme

### 7.1 Capitalisation des titres
- Regle francaise : majuscule au premier mot du titre et aux noms propres.
- Exemple : "Les mysteres de Paris" (pas "Les Mysteres de Paris")
- Exemple : "Le rouge et le noir" / "Du cote de chez Swann"
- Exception : les titres d'oeuvres contemporaines peuvent suivre les conventions de l'editeur.
- Regle pour les en-tetes et sections : majuscule uniquement sur le premier mot.

### 7.2 Titres de parties
- Chapitre 1, Section 2, Partie III (chiffres arabes ou romains).
- "Premiere partie" / "Deuxieme chapitre" (epellation possible).
- Sous-titres : separe par deux-points ou point-virgule.
- Les mots "chapitre", "section", "partie" s'ecrivent en minuscule ou prennent une majuscule selon le style editorial.

### 7.3 Listes a puces
- Utiliser des tirets (-) ou des puces (*).
- Chaque element commence par une minuscule (sauf si phrase complete).
- Elements courts : pas de ponctuation finale.
- Elements longs (phrases) : point final.
- Elements en phrases incompletes : point-virgule entre elements, point au dernier.

### 7.4 Listes numerotees
- Utiliser 1., 2., 3. ou a), b), c) ou (1), (2), (3).
- Style cohérent dans tout le document.
- Pour les listes hierarchiques : I. / A. / 1. / a) / i.

### 7.5 Tableaux
- Conserver la structure : alignement, colonnes, en-têtes.
- En-tetes de colonne : majuscule au premier mot seulement.
- Nombres dans les tableaux : alignes a droite, decimaux alignes sur la virgule.
- Texte dans les tableaux : aligne a gauche.
- Titre du tableau : "Tableau 1 :" avant le titre (majuscule a Tableau).

### 7.6 Légendes d'illustrations
- "Figure 1 :" ou "Fig. 1 :" suivi de la legende.
- Legende en minuscule apres le numero (sauf noms propres).
- Point final si la legende est une phrase complete.

### 7.7 Notes de bas de page
- Appel de note : chiffre en exposant avant la ponctuation.
- Si la note porte sur un mot precis, l'appel se place apres ce mot.
- Si la note porte sur une phrase entiere, l'appel se place apres le point final.
- Contenu de la note : majuscule au premier mot, point final.

### 7.8 Soulignements et styles
- Eviter le soulignement (reserve aux liens hypertextes).
- Italique pour les titres d'oeuvres, mots etrangers, et citations courtes.
- Gras pour les titres et mots importants (usage modere en francais).
- Les guillemets remplacent l'italique quand celui-ci n'est pas disponible.

### 7.9 Citations
- Citations courtes (moins de 3 lignes) : entre guillemets francais avec espace insécable.
- Citations longues : en retrait, sans guillemets, en caractere plus petit.
- Citation dans une citation : guillemets anglais " " a l'interieur des guillemets francais.
- Appel de source apres la citation, entre parentheses ou en note.

### 7.10 Numerotation des pages et sections
- Pages : p. 12 / pp. 12-15 / page 12 / pages 12-15
- Paragraphes : § 12 / §§ 12-14
- Articles (juridique) : art. 12 / articles 12 a 15

---

## 8. Grammaire

### 8.1 Ordre des mots (SVO)
- Structure canonique : Sujet + Verbe + Objet.
- Exemple : Le chat (sujet) mange (verbe) la souris (objet).
- Inversion sujet-verbe dans les questions formelles : "Quand viendrez-vous ?" (pas "Quand vous viendrez ?")
- Inversion dans les incises : "dit-il", "repondit-elle"

### 8.2 Genre des mots (masculin / feminin)
- Tout nom en francais a un genre : masculin ou feminin.
- Exemples courants sujets a erreur :
  - Un arbre (masc.), une fleur (fém.)
  - Le probleme (masc.), la solution (fém.)
  - Un travail (masc.), une tache (fém.)
  - Le sable (masc.), la mer (fém.)
  - Un espoir (masc.), une esperance (fém.)
- Accord de l'adjectif et du participe passe avec le genre du nom.
- Exemple : un grand arbre / une grande maison

### 8.3 Nombre et accords
- Singulier et pluriel : regle generale -s au pluriel.
- Noms en -au, -eau, -eu, -oeu : -x au pluriel (chateau → chateaux, cheveu → cheveux)
- Noms en -ou : -s (trou → trous) sauf bijou, caillou, chou, genou, hibou, joujou, pou → -x
- Noms en -al : -aux (cheval → chevaux) sauf bal, carnaval, festival, recital, regal → -s
- Noms en -ail : -ails sauf bail → baux, email → emaux, soupirail → soupiraux, travail → travaux, vitrail → vitraux
- Noms composes : regle variable (consulter le dictionnaire)

### 8.4 Conjugaison : temps de l'indicatif
- Present : actions en cours, etats, verites generales.
  - Exemple : Je parle, tu parles, il/elle/on parle, nous parlons, vous parlez, ils/elles parlent
- Imparfait : actions passees continues, descriptions, habitudes.
  - Exemple : Je parlais, il parlait, nous parlions
- Passé composé : actions passees ponctuelles, resultats.
  - Exemple : J'ai parle, il a parle, nous avons parle
- Plus-que-parfait : action anterieure a une autre action passee.
  - Exemple : J'avais parle, il avait parle
- Futur simple : actions futures.
  - Exemple : Je parlerai, tu parleras
- Futur anterieur : action future anterieure a une autre action future.
  - Exemple : J'aurai parle, il aura parle

### 8.5 Passe compose vs imparfait
- Imparfait : actions d'arriere-plan, descriptions, habitudes, duree non delimitee.
  - Exemple : "Il faisait beau quand je suis sorti." (description du decor)
  - Exemple : "Quand j'etais enfant, je jouais au tennis." (habitude)
- Passé compose : actions de premier plan, evenements ponctuels, changement d'etat.
  - Exemple : "J'ai ouvert la porte et je suis entre." (action ponctuelle)
  - Exemple : "Il a soudainement compris." (changement soudain)
- Regle : ne pas melanger les deux sans raison stylistique.

### 8.6 Subjonctif
- Declencheurs courants du subjonctif :
  - Volonte : il faut que, je veux que, j'aimerais que
  - Doute : je doute que, il est possible que, il se peut que
  - Sentiment : je suis content que, je regrette que, il est dommage que
  - Necessite : il est necessaire que, il est important que
  - Conjonctions : bien que, quoique, avant que, pour que, afin que, sans que
  - Superlatif : le meilleur que, le seul que, le premier que
- Exemple : "Il faut que tu viennes." (pas "tu viens")
- Exemple : "Bien qu'il soit tard..." (pas "il est tard")
- Apres "penser que" et "croire que" : indicatif a la forme affirmative, subjonctif a la forme negative.
  - "Je pense qu'il vient." / "Je ne pense pas qu'il vienne."

### 8.7 Conditionnel
- Conditionnel present : actions hypothetiques, politesse, incertitude.
  - Exemple : "Si j'avais le temps, je viendrais."
  - Exemple : "Je voudrais un cafe, s'il vous plait." (politesse)
  - Exemple : "Il serait a Paris." (incertitude / oui-dire)
- Conditionnel passe : hypothese non realisee dans le passe.
  - Exemple : "Si j'avais su, je serais venu."
  - Exemple : "Il aurait du partir plus tot."

### 8.8 Participe passe
- Accord avec etre : le participe s'accorde avec le sujet.
  - Exemple : "Elle est arrivee." / "Ils sont partis." / "Elles sont venues."
- Accord avec avoir : le participe s'accorde avec le COD si celui-ci est place avant le verbe.
  - Exemple : "Les lettres que j'ai ecrites." (COD "que" = lettres, place avant)
  - Exemple : "J'ai ecrit les lettres." (COD "les lettres" apres, pas d'accord)
- Verbes pronominaux : accord avec le sujet (sauf COD place apres).
  - Exemple : "Elle s'est lavee." / "Elles se sont lave les mains." (pas d'accord : "les mains" est COD apres)

### 8.9 Prepositions
- a / de / en / dans / par / pour / sur / avec / sans / chez / entre / sous
- Attention aux faux amis et usages specifiques :
  - "aller EN France" (pays feminin) / "aller AU Japon" (pays masculin)
  - "etre A Paris" / "venir DE Paris"
  - "penser A" (something) / "penser DE" (opinion)
  - "commencer A" / "fINIR de"
- Verbes avec preposition :
  - Decider de, parler de, reussir a, tenir a, consentir a, s'attendre a

### 8.10 Pronoms
- Pronoms personnels sujets : je, tu, il/elle/on, nous, vous, ils/elles
- Pronoms personnels COD : me, te, le/la, nous, vous, les
- Pronoms personnels COI : me, te, lui, nous, vous, leur
- Pronoms toniques : moi, toi, lui/elle, nous, vous, eux/elles
- Pronoms relatifs : qui (sujet), que (COD), dont (COI/complement du nom), ou (lieu/temps)
- Pronoms adverbiaux : en (de + nom), y (a + nom)

### 8.11 Negation
- Structure : ne + verbe + pas (ou autre mot negatif : rien, personne, jamais, plus, aucun)
- Exemple : "Je ne sais pas." / "Il n'a rien dit." / "Personne n'est venu."
- "ne" s'elide devant une voyelle : n'ai, n'est, n'ont
- En francais familier, "ne" peut etre omis, mais le francais ecrit formel exige "ne".
- Negation complexe : "ne...que" (restriction, = seulement) : "Je n'ai que cinq euros."

---

## 9. Registre et formality

### 9.1 Vous vs tu
- Vouvoiement (vous) : registre formel, professionnel, administratif, juridique.
  - Utilisation : inconnu, superieur, client, personne agee, contexte officiel.
- Tutoiement (tu) : familier, intime, enfant, Dieu, contexte informel.
- Zero-tolerance : un melange vous/tu dans le meme document formel est une faute grave.
- Ne JAMAIS tutoyer un client ou un superieur dans une correspondance professionnelle.
- En contexte administratif : le vouvoiement systematique du citoyen par l'administration.

### 9.2 Formules de politesse formelles
- Ouverture de lettre :
  - "Madame," / "Monsieur," / "Madame, Monsieur,"
  - "Cher Monsieur," / "Chere Madame," (plus familier)
  - "Monsieur le Directeur," / "Madame la Presidente," (avec titre)
- Corps : formules de politesse integrees :
  - "Je vous prie d'agreer, Madame, Monsieur, l'expression de mes salutations distinguees."
  - "Veuillez agreer, Madame, mes salutations les meilleures."
  - "Dans l'attente de votre reponse, je vous prie de croire, Monsieur, a l'assurance de mes sentiments les meilleurs."

### 9.3 Formules de cloture par registre
- Tres formel (administratif/juridique) :
  - "Je vous prie d'agreer, Madame/Monsieur, l'expression de ma consideration distinguee."
  - "Veuillez agreer, Madame/Monsieur, l'assurance de ma consideration respectueuse."
  - "Je vous prie d'agreer, Monsieur le Directeur, l'expression de mon profond respect."
- Formel (professionnel courant) :
  - "Je vous prie d'agreer, Madame, mes salutations distinguees."
  - "Veuillez agreer, Monsieur, l'expression de mes salutations distinguees."
  - "Cordialement." / "Bien cordialement."
- Semi-formel (interne, connu) :
  - "Bien cordialement," / "Cordialement,"
  - "Avec mes meilleures salutations,"
  - "Sincerement,"
- Informel (interne, collegues proches) :
  - "Amities," / "Bien a toi," / "A bientot,"

### 9.4 Registre administratif
- Phrases completes, syntaxe complexe mais correcte.
- Utilisation de "il convient de", "il y a lieu de", "il est rappele que".
- Formules impersonnelles : "il est decide que", "il est precise que".
- Verbes performatifs : "je soussigne atteste", "le conseil decide", "la direction informe".
- Reference aux textes juridiques : "conformement a l'article", "en application de la loi du".
- Pronoms impersonnels : "on" evite sauf si intentionnel ; preferer "il" impersonnel.

### 9.5 Registre juridique
- Terminologie specifique : "le requerant", "le defendeur", "le soussigne", "la partie civile"
- Formules rituelles : "Par devant Me [nom], notaire a [ville]",
- "A dure : comparu..." (passe simple juridique)
- "Fait a [lieu], le [date]"
- "Lu et approuve" / "Bon pour acceptation" / "Bon pour pouvoir"
- Conditionnel juridique : "le tribunal considere que...", "attendus que...",
- Numerotation des articles, alineas, paragraphes.

### 9.6 Registre commercial et marketing
- Ton professionnel mais accessible.
- "Nous vous remercions de votre confiance."
- "Dans l'attente de votre retour,"
- "N'hesitez pas a nous contacter pour toute question."
- Marketing : "Decouvrez notre nouvelle gamme" / "Profitez de nos offres exclusives"
- Eviter les superlatifs excessifs non etayes.
- Adapter le degre de formality a la cible (B2B vs B2C).

### 9.7 Registre technique et scientifique
- Terminologie precise, normalisee (ISO, AFNOR, nomenclature scientifique).
- Voix passive acceptable dans la description de processus.
- "Il a ete observe que" / "Les resultats montrent que"
- "Conformement a la norme NF EN ISO"
- Eviter les jugements de valeur non scientifiques.
- Citations et references bibliographiques en norme francaise.

### 9.8 Niveaux de langue
- Soutenu (litteraire) : vocabulaire riche, phrases complexes, subjonctif respecte.
  - Exemple : "Il ete fort regrettable que vous n'ayez pu vous joindre a nous."
- Courant (standard) : usage quotidien correct, formules standards.
  - Exemple : "C'est dommage que vous n'ayez pas pu venir."
- Familier : oral, abreviations, "ne" omis, vocabulaire relache.
  - Exemple : "Dommage que t'aies pas pu venir."
- Traduire TOUJOURS dans le registre correspondant a celui du texte source.
- Ne pas sur-traduire en registre plus soutenu que l'original.

### 9.9 Titres et formules d'appel
- "Monsieur" / "Madame" : toujours avec majuscule en debut de lettre.
- "M." / "Mme" / "Mlle" : abreviations avec point.
- Devant un nom propre : "Monsieur Dupont" / "Madame Martin"
- "Monsieur le Maire" / "Madame la Directrice" (accord feminin des titres)
- "Monseigneur" (eveque), "Votre Excellence" (ambassadeur), "Votre Honneur" (juge)

---

## 10. Artefacts OCR

### 10.1 Format standard pour les restaurations
- Utiliser le format : `[restaure: <texte original>, <description>, <raison>]`
- Exemple : `[restaure: "pas age", base sur le contexte, probablement "passage"]`
- Exemple : `[restaure: "l'0rganisation", caractere douteux, "l'Organisation"]`
- Le texte restaure apparait en premier, suivi de la justification.

### 10.2 Marques pour caracteres incertains
- Pour les caracteres dont la lecture est incertaine : `[caractere incertain : X]`
- Exemple : "Le texte contient un `[caractere incertain : O/0]` dans le mot."
- Si plusieurs caracteres sont incertains, les lister.

### 10.3 Textes tronques et lacunaires
- Texte tronque visible : `[restaure: ... , texte tronque apres "mot"]`
- Texte manquant complet : `[texte incomplet]`
- Texte illisible : `[illisible]`
- Ne jamais inventer de contenu pour combler une lacune non restaurable.

### 10.4 Confusions optiques courantes
- l → I (lettre L minuscule → I majuscule) : frequente en OCR
- 0 → O (zero → lettre O) : surtout dans les dates et nombres
- O → 0 : dans les codes et reference
- rn → m : confusion optique classique
- cl → d : dans certaines polices
- Toutes les corrections de confusions optiques doivent etre signalees.

### 10.5 Signes diacritiques ignores par l'OCR
- Accents manquants : `[restaure: ete → ete, accent circonflexe restitue]`
- Cedille omise : `[restaure: ca → ca, cedille restituee]`
- Trema ignore : `[restaure: Noël → Noel, trema restitue]`
- Si la restitution est evidente a 100 %, la faire sans annotation.

### 10.6 Ponctuation OCR defectueuse
- Guillemets anglais remplaces par des guillemets ouvrants/fermants courbes : corriger silencieusement.
- Apostrophe droite → apostrophe typographique : corriger silencieusement.
- Points de suspension en trois points separes → points de suspension : corriger silencieusement.
- Tiret standard → tiret cadratin si le contexte le justifie.

### 10.7 Mise en page OCR
- Sauts de page : indiquer `[saut de page]` entre crochets.
- Colonnes mal reconnues : restructurer le texte dans l'ordre de lecture logique.
- Notes de bas de page OCRisees comme du texte principal : les signaler et les repositionner.
- Tableaux OCRises en texte : `[tableau non reconnu, structure restituee]`

### 10.8 Restauration contextuelle
- Si le contexte permet de restituer un mot avec une certitude > 95 %, effectuer la correction et l'indiquer.
- Si la certitude est entre 75 % et 95 %, utiliser le format `[restaure: ...]`.
- Si la certitude est inferieure a 75 %, laisser le texte original et marquer `[caractere incertain]`.
- Ne jamais deviner au-dela de ce que le contexte permet d'etablir raisonnablement.

### 10.9 Documents numerises (PDF source)
- Signaler les particularites de la numerisation.
- `[document numerise, qualite : bonne/moyenne/mediocre]`
- Signaler les pages manquantes : `[page X manquante dans l'original]`
- Signaler les pages dans le desordre : `[pages dans le desordre, ordre restitue]`

---

## 11. Philosophie de traduction

### 11.1 Fidelite au texte source
- Le sens exact du texte source doit etre preserve, sans omission ni ajout.
- En cas d'ambiguite, choisir l'interpretation la plus probable dans le contexte.
- Les jeux de mots, doubles sens et references culturelles doivent etre identifies et traites.
- Priorite : fidelite semantique > fidelite stylistique > fidelite formelle.

### 11.2 Naturel en francais
- Le resultat doit sonner comme un texte originalement ecrit en francais.
- Eviter les calques syntaxiques de l'anglais (anglicismes de structure).
- Exemple d'anglicisme syntaxique : "C'est important de noter que..." → "Il est important de noter que..."
- Exemple : "En addition" → "De plus" ou "En outre" (pas "en addition")
- Exemple : "Base sur" → "Fonde sur" ou fonde sur (pas "base sur" bien que courant)
- Exemple : "Issue" → "probleme" ou "point" (pas "issue" dans le sens de probleme)

### 11.3 Evitement des anglicismes
- Anglicismes lexicaux a eviter (preferer les equivalents francais) :
  - Meeting → reunion
  - Deadline → date limite / echeance
  - Feedback → retour (d'information)
  - Email → courriel / mel (message electronique)
  - Newsletter → lettre d'information / bulletin
  - Briefing → seance d'information
  - Coaching → accompagnement / encadrement
  - Follow-up → suivi
  - Brainstorming → remue-meninges (rare) / seance de reflexion collective
  - Manager → responsable / gestionnaire / chef de service
  - Boss → patron / chef / superieur
  - IT → informatique / SI (systeme d'information)
  - Buzz → retentissement / engouement
  - Challenge → defi
  - Win-win → gagnant-gagnant
  - Best practices → bonnes pratiques
  - Overview → apercu / vue d'ensemble
  - Agenda → ordre du jour (reunion) / agenda (calendrier)
- Certains anglicismes sont acceptes par l'usage : parking, week-end, sandwich, basket
- En cas de doute, consulter le site de l'Academie francaise ou FranceTerme.

### 11.4 Académie française et recommandations officielles
- L'Academie francaise est l'autorite de reference pour la langue francaise.
- FranceTerme (sous l'autorite de la Delegation generale a la langue francaise et aux langues de France) publie des equivalents officiels aux termes etrangers.
- Le Journal officiel publie regulierement des listes de termes recommandes.
- Les rectifications orthographiques de 1990 sont recommandees (trait d'union dans les numeraux, accent circonflexe facultatif sur i/u, etc.).
- Sites de reference : academie-francaise.fr / franceterme.culture.fr / langue-francaise.culture.gouv.fr

### 11.5 Adaptation culturelle
- Adapter les references culturelles non comprises du public francophone cible.
- Exemple : "Thanksgiving" → "Action de graces" (ou explication : "fete de Thanksgiving")
- Exemple : "Baseball" → "baseball" (conserve, avec explication si necessaire)
- Exemple : "High school" → "lycee" (equivalence du systeme educatif)
- Exemple : "911" (services d'urgence US) → "le 911" (conserve avec explication) ou adapter au contexte : "les urgences"
- Ne pas sur-adapter : conserver les specificites culturelles etrangeres quand elles sont porteuses de sens.

### 11.6 Localisation pour les marches francophones
- Distinguer les variantes du francais selon le marche cible :
  - Francais de France (norme pour l'UE)
  - Francais du Canada (Quebec)
  - Francais de Belgique
  - Francais de Suisse
  - Francais d'Afrique
- Differences notables :
  - Belgique/Suisse : septante (70), nonante (90)
  - Quebec : fin de semaine (week-end), courriel (email), magasinage (shopping)
  - France : soixante-dix (70), quatre-vingt-dix (90)
- Pour un public europeen, utiliser la norme de France.

### 11.7 Traduction des sigles et acronymes
- SIGLES INTERNATIONAUX : a conserver si universellement reconnus.
  - Exemple : ONU (pas UN), OTAN (pas NATO), UE (pas EU), OMS (pas WHO)
- Sigles d'organisations etrangeres : conserver le sigle original avec traduction entre parentheses a la premiere occurrence.
  - Exemple : "La FAO (Organisation des Nations Unies pour l'alimentation et l'agriculture)"
- Acronymes techniques : conserver l'acronyme anglais si plus connu que l'equivalent francais.
  - Exemple : PDF, HTML, HTTP, GPS (conserver)

### 11.8 Traduction des citations
- Citations en langue etrangere : conserver dans la langue originale et traduire en note ou entre parentheses.
- Citations bibliques : utiliser la traduction officielle francaise (Bible de Jerusalem, Segond, etc.).
- Citations juridiques : conserver la formulation originale du droit etranger.
- Citations litteraires : utiliser la traduction de reference si elle existe.

### 11.9 Traduction des realia (elements specifiques a une culture)
- Realia culturels : conserver le terme original avec explication si necessaire.
- Exemple : "sushi" (conserve), "sauna" (conserve), "siesta" (conserve)
- Realia administratifs : chercher l'equivalent fonctionnel.
  - Exemple : "IRS" → "le fisc americain (IRS)"
  - Exemple : "Social Security Number" → "numero de securite sociale americain"
- Realia juridiques : expliquer plutot que de chercher un faux equivalent.

### 11.10 Priorites en cas de conflit
1. Corrections zero-tolerance (virgule decimale, date, vouvoiement)
2. Fidelite semantique
3. Grammaire et orthographe francaises correctes
4. Conformite aux regles typographiques francaises
5. Naturel et fluidite du francais
6. Respect du registre et du ton du document source
7. Adaptation culturelle appropriee

### 11.11 Questions ethiques en traduction
- Ne pas introduire de biais (genre, race, religion, politique) absents du texte source.
- Respecter la neutralite de ton du document original.
- Signaler les passages potentiellement problematiques au relecteur.
- Ne pas censurer ni edulcorer le propos de l'auteur original.
- En cas de dilemme ethique, documenter la decision et ses raisons.
