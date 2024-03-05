from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
    ListView, UpdateView, DeleteView)
from pastes.models import Paste

from pastes.forms import CreatePasteForm, UpdatePasteForm

# Create your views here.
class CreatePasteView(CreateView):
    form_class = CreatePasteForm
    model = Paste
    success_url = "/"

class DetailPasteView(DetailView):
    model = Paste

    # def get_context_data(self, **kwargs):
    #     args = super().get_context_data(**kwargs)
    #     args['paste_title'] = self.title
    #     return args

class PasteListView(ListView):
    model = Paste

class PasteUpdateView(UpdateView):
    form_class = UpdatePasteForm
    model = Paste
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"view-type": "update"})
        return context

class PasteDeleteView(DeleteView):
    model = Paste
    success_url = "/"
