import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
django.setup()

from shop.models import Category, Product

def seed_db():
    # Nettoyage
    Category.objects.all().delete()
    Product.objects.all().delete()

    # Création des catégories
    cat_femme = Category.objects.create(name="Femmes", slug="femmes", icon="fa-venus")
    cat_homme = Category.objects.create(name="Hommes", slug="hommes", icon="fa-mars")
    cat_accessoires = Category.objects.create(name="Accessoires", slug="accessoires", icon="fa-gem")

    # Produits Femmes
    Product.objects.create(
        name="Robe d'été Fleurie",
        slug="robe-ete-fleurie",
        category=cat_femme,
        description="Une robe légère et élégante, parfaite pour les journées ensoleillées. Fabriquée en coton 100% bio avec des motifs floraux délicats.",
        price=59.99,
        image_url="https://images.unsplash.com/photo-1572804013307-a9a111dc80c5?q=80&w=1000&auto=format&fit=crop",
        is_new=True,
        is_popular=True
    )

    Product.objects.create(
        name="Veste en Lin Beige",
        slug="veste-lin-beige",
        category=cat_femme,
        description="Veste structurée en lin naturel. Un incontournable pour un look sophistiqué mais décontracté.",
        price=89.00,
        image_url="https://images.unsplash.com/photo-1591047139829-d91aecb6caea?q=80&w=1000&auto=format&fit=crop",
        is_on_sale=True,
        discount_percentage=15
    )

    # Produits Hommes
    Product.objects.create(
        name="Chemise Oxford Blanche",
        slug="chemise-oxford-blanche",
        category=cat_homme,
        description="La chemise Oxford classique. Coupe ajustée, tissu résistant et respirant. Idéale pour le bureau ou une sortie.",
        price=45.00,
        image_url="https://images.unsplash.com/photo-1598033129183-c4f50c717658?q=80&w=1000&auto=format&fit=crop",
        is_popular=True
    )

    Product.objects.create(
        name="Manteau en Laine Anthracite",
        slug="manteau-laine-anthracite",
        category=cat_homme,
        description="Manteau élégant pour l'hiver. Laine de haute qualité offrant une chaleur optimale et une silhouette impeccable.",
        price=185.00,
        image_url="https://images.unsplash.com/photo-1539533113208-f6df8cc8b543?q=80&w=1000&auto=format&fit=crop",
        is_new=True
    )

    # Accessoires
    Product.objects.create(
        name="Sac à Main en Cuir",
        slug="sac-main-cuir-noir",
        category=cat_accessoires,
        description="Sac à main intemporel en cuir véritable. Finitions dorées et bandoulière amovible.",
        price=120.00,
        image_url="https://images.unsplash.com/photo-1584917765829-a83585fb9c31?q=80&w=1000&auto=format&fit=crop",
        is_popular=True
    )

    Product.objects.create(
        name="Lunettes de Soleil Vintage",
        slug="lunettes-soleil-vintage",
        category=cat_accessoires,
        description="Protection UV optimale avec un style rétro irrésistible. Monture légère et robuste.",
        price=35.00,
        image_url="https://images.unsplash.com/photo-1511499767390-a767b75d9918?q=80&w=1000&auto=format&fit=crop",
        is_on_sale=True,
        discount_percentage=20
    )

    print("Base de données initialisée avec succès !")

if __name__ == '__main__':
    seed_db()
