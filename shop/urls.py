from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gestion/', views.manage_products, name='manage_products'),
    path('gestion/ajouter/', views.add_product, name='add_product'),
    path('gestion/<int:pk>/modifier/', views.edit_product, name='edit_product'),
    path('gestion/<int:pk>/supprimer/', views.delete_product, name='delete_product'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('shipping/', views.shipping, name='shipping'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('a-propos/', views.about, name='about'),
]
