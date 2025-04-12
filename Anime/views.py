from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models

class AnimeItemsListView(generic.ListView):
    model = models.AnimeItems
    template_name = 'Anime/AnimeItems_list_view.html'
    context_object_name = 'AnimeItems'
    def get_queryset(self):
        return models.AnimeItems.objects.all().order_by('-id')

class AnimeItemsDetailView(generic.DetailView):
    model = models.AnimeItems
    template_name = 'Anime/AnimeItems_detail_view.html'
    
    
class AnimeItemsCreateView(generic.CreateView):
    model  = models.AnimeItems
    fields = ['title', 'seasone', 'episod', 'anime_picture']
    template_name = 'Anime/AnimeItems_create_view.html'
    success_url = "/"
    
class AnimeItemsUpdateView(generic.UpdateView):
    model  = models.AnimeItems
    fields = ['title', 'seasone', 'episod', 'anime_picture']
    template_name = 'Anime/AnimeItems_update_view.html'
    success_url = "/"
    
class AnimeItemsDeleteView(generic.DeleteView):
    model = models.AnimeItems
    template_name = 'Anime/AnimeItems_delete_view.html'
    success_url = reverse_lazy('AnimeItems_list_url')