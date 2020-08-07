from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BookMark

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from django.views.generic.detail import DetailView

from django.views.generic.edit import UpdateView

from django.views.generic.edit import DeleteView
# Create your views here.
class BookMarkListView(ListView):
    model = BookMark
    paginate_by = 6

class BookMarkCreateView(CreateView):
    model = BookMark
    fields = ['site_name', 'url']
    success_url = reverse_lazy("bookmark:list")
    template_name_suffix = '_create'

class BookMarkDetailView(DetailView):
    model=BookMark

class BookMarkUpdateView(UpdateView):
    model = BookMark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy("bookmark:list")

class BookMarkDeleteView(DeleteView):
    model=BookMark
    success_url = reverse_lazy('bookmark:list')