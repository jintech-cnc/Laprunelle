from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

INPUT_CLASS = 'w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-black focus:outline-none'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': INPUT_CLASS}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.setdefault('class', INPUT_CLASS)


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': INPUT_CLASS}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': INPUT_CLASS}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Le champ "slug" est retiré du formulaire : il est généré
        # automatiquement à partir du nom de l'article (voir Product.save()).
        fields = [
            'name', 'category', 'description', 'price',
            'image', 'image_url', 'is_new', 'is_popular', 'is_on_sale',
            'discount_percentage', 'sizes'
        ]
        labels = {
            'name': "Nom de l'article",
            'category': "Catégorie",
            'description': "Description",
            'price': "Prix (€)",
            'image': "Photo (Upload local)",
            'image_url': "Ou lien photo externe",
            'is_new': "Nouveauté",
            'is_popular': "Coup de cœur",
            'is_on_sale': "En promotion",
            'discount_percentage': "Réduction (%)",
            'sizes': "Tailles disponibles",
        }
        help_texts = {
            'image': "Sélectionnez une photo depuis votre appareil.",
            'image_url': "Ou collez un lien URL externe.",
            'sizes': "Séparez les tailles par une virgule, par exemple : XS,S,M,L,XL",
            'discount_percentage': "Uniquement utile si \"En promotion\" est coché.",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Ex : Robe Été Fleurie'}),
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': INPUT_CLASS, 'placeholder': "Décrivez l'article en quelques phrases"}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS, 'placeholder': '0.00'}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS}),
            'image_url': forms.URLInput(attrs={'class': INPUT_CLASS, 'placeholder': 'https://...'}),
            'discount_percentage': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'sizes': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'XS,S,M,L,XL'}),
        }
