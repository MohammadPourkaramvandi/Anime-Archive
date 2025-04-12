from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.AnimeItemsCreateView.as_view(), name="create_url"),
    path('', views.AnimeItemsListView.as_view(), name="list_url"),
    path('<int:pk>/edit/', views.AnimeItemsUpdateView.as_view(), name='update_url'),
]
