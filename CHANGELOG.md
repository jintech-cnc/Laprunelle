# Corrections et modernisation — La prunelle E-boutique

## Bugs corrigés

- **Menu mobile inexistant** : sur téléphone, aucun moyen d'accéder à la navigation
  (le menu desktop était `hidden md:flex` sans bouton hamburger). Ajouté un vrai
  menu mobile avec bouton et panneau déroulant.
- **`django.contrib.admin` absent** de `INSTALLED_APPS` alors que `shop/admin.py`
  l'importait et que `/admin/` était commenté dans les URLs. L'admin Django est
  maintenant activé et les modèles `Category`/`Product` y sont enregistrés.
- **Inscription factice** : la page `/register/` affichait juste du texte, sans
  formulaire. Elle crée maintenant un vrai compte utilisateur (et connecte
  automatiquement l'utilisateur).
- **Aucune page de connexion** : `add_product` est protégée par
  `@user_passes_test`, qui redirigeait vers `/accounts/login/` (page 404 car
  inexistante). Une vraie page `/login/` a été créée et `LOGIN_URL` configuré.
- **Panier sans fin** : le bouton "Passer la commande" pointait vers `#`. Il
  génère maintenant un message de commande pré-rempli envoyé via WhatsApp
  (comme sur vos autres projets). **Pensez à remplacer `WHATSAPP_NUMBER`** dans
  `templates/base.html` par le vrai numéro de la boutique.
- **Liens morts** : "Collections", "Nouveautés", "À propos" et les liens du
  pied de page pointaient vers `#`. Ils sont maintenant fonctionnels
  ("Nouveautés" filtre réellement les articles marqués `is_new`).
- **Champ `icon` de `Category` jamais utilisé** : les icônes FontAwesome
  définies sur chaque catégorie apparaissent maintenant dans les boutons de
  filtre.
- **Formulaire newsletter** qui rechargeait la page sans rien faire : il
  affiche maintenant une confirmation (toujours pas connecté à un vrai
  service d'emailing — à brancher si besoin, ex. Mailchimp/Brevo).

## Ajouts

- Icône de recherche fonctionnelle (filtre les articles par nom/catégorie).
- Page "À propos".
- `requirements.txt`.
- **Tableau de bord "Gérer la boutique"** (`/gestion/`) : liste de tous les
  articles avec boutons Modifier/Supprimer, sans jamais passer par
  `/admin/`. Le lien "Publier" du menu a été renommé "Gérer la boutique" et
  pointe désormais vers ce tableau de bord.
- **Slug automatique** : le champ technique "slug" a été retiré du
  formulaire d'ajout/modification d'article ; il est généré tout seul à
  partir du nom (et rendu unique automatiquement en cas de doublon).
- Formulaire d'ajout/modification avec des libellés en français clair
  ("Nom de l'article", "Lien de la photo"...) et des indications d'aide.

## À faire côté configuration avant mise en production

1. `pip install -r requirements.txt`
2. `python manage.py migrate` (nécessaire : `django.contrib.admin` vient
   d'être activé, et le champ `slug` de `Product` a changé)
3. `python manage.py createsuperuser`
4. Remplacer `WHATSAPP_NUMBER` dans `templates/base.html`
5. Mettre `DEBUG = False` et renseigner `ALLOWED_HOSTS` avant le déploiement
6. Remplacer `SECRET_KEY` par une valeur secrète propre à la production
