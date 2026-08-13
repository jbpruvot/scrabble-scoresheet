# Feuille de score — Scrabble

Feuille de score Scrabble interactive et installable (PWA), pour 2 à 4 joueurs.

- Grille de 15 tours par défaut (extensible avec « + Ajouter un tour »)
- Calcul automatique des totaux au fur et à mesure (les valeurs négatives déduisent le score)
- Noms des joueurs modifiables, 2 par défaut : **CAT** et **JB**
- Sauvegarde automatique dans le navigateur (localStorage)
- Installable sur mobile/tablette via « Ajouter à l'écran d'accueil »
- Fonctionne hors-ligne une fois installée (service worker)

## Installer sur une tablette

1. Ouvrir l'URL du site (GitHub Pages) dans le navigateur de la tablette.
2. **iPad (Safari)** : bouton Partager → *Sur l'écran d'accueil*.
   **Android (Chrome)** : menu ⋮ → *Installer l'application* (ou *Ajouter à l'écran d'accueil*).
3. L'icône apparaît sur l'écran d'accueil et s'ouvre en plein écran, comme une app native.

## Développement local

Fichiers statiques uniquement, aucune dépendance : ouvrir `index.html` dans un navigateur, ou servir le dossier avec n'importe quel serveur statique.

`gen_icons.py` régénère les icônes (`icons/`) à partir de Pillow — à relancer uniquement si le design change.
