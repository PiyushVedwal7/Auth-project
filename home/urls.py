
# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name="logout"),
    path('pdf/', views.pdf, name="pdf"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('recipes/', views.recipes, name="recipes"),
    path('update/<int:id>/', views.update, name="update_recipe"),
    path('delete/<int:id>/', views.delete, name="delete_recipe"),
]
