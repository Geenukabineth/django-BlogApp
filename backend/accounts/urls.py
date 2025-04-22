from django.urls import path
from . import views


urlpatterns = [
    path("", views.product_list, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("login/base/create/", views.create_product, name="create_product"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/<int:id>/edit/", views.update, name="update"),
    path("product/<int:id>/delete/", views.delete, name="delete"),
    path("login/base/", views.base, name="base"),
]
