from django.urls import path
from . import views

urlpatterns = [
    path("", views.boot_rules_index, name="boot_rules_index"),
    path("<int:pk>/", views.boot_rules_detail, name="boot_rules_detail"),
    path("<category>/", views.boot_rules_category, name="boot_rules_category"),
]
