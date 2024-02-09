from django.urls import path

from . import views
from .views import ItemDetailView, ItemListView

app_name = "item"

urlpatterns = [
    path("<int:item_id>/", ItemDetailView.as_view(), name="item-detail"),
    # path('', views.items, name='items'),
    path("", ItemListView.as_view(), name="items"),
    path("new/", views.new, name="new"),
    # path('<int:pk>/', views.detail, name='detail'),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
]
