# Plan pour ajouter les pages et corriger les liens

## Objectifs
- Créer les pages manquantes : Contact, FAQ, Livraison, Inscription.
- Mettre à jour `base.html` pour lier correctement ces pages.

## Étapes
1. Ajouter les fonctions de vue `contact`, `faq`, `shipping` et `register` dans `shop/views.py`.
2. Ajouter les URLs correspondantes dans `shop/urls.py`.
3. Créer les templates HTML minimaux dans `templates/shop/` pour ces vues.
4. Mettre à jour `templates/base.html` pour remplacer les `#` par les URLs.
