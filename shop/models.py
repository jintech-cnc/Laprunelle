from django.db import models
from django.utils.text import slugify
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, help_text="Nom de l'icône FontAwesome (ex: fa-tshirt)")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_on_sale = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(default=0)
    sizes = models.CharField(max_length=50, default="XS,S,M,L,XL")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Le slug n'est plus demandé dans le formulaire : il est généré
        # automatiquement à partir du nom (et rendu unique si besoin).
        if not self.slug:
            base_slug = slugify(self.name) or "article"
            slug = base_slug
            counter = 2
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

        # Si une image est téléversée, on récupère son URL Cloudinary et on met à jour image_url
        if self.image:
            try:
                cloudinary_url = self.image.url
                if self.image_url != cloudinary_url:
                    Product.objects.filter(pk=self.pk).update(image_url=cloudinary_url)
                    self.image_url = cloudinary_url
            except Exception:
                pass

    @property
    def final_price(self):
        if self.is_on_sale:
            return self.price * (Decimal(100 - self.discount_percentage) / Decimal(100))
        return self.price
