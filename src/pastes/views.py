from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
    ListView, UpdateView, DeleteView)
from pastes.models import Paste

from pastes.forms import CreatePasteForm

# Create your views here.
class CreatePasteView(CreateView):
    form_class = CreatePasteForm
    model = Paste
    success_url = '/'

class DetailPasteView(DetailView):
    pass

class PasteListView(ListView):
    model = Paste