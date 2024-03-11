from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
    ListView, UpdateView, DeleteView)
from pastes.models import Paste, User

from pastes.forms import CreatePasteForm, UpdatePasteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class CreatePasteView(LoginRequiredMixin, CreateView):
    form_class = CreatePasteForm
    model = Paste
    success_url = "/"

class DetailPasteView(LoginRequiredMixin, DetailView):
    model = Paste

    # def get_context_data(self, **kwargs):
    #     args = super().get_context_data(**kwargs)
    #     args['paste_title'] = self.title
    #     return args

class PasteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("account_login")
    model = Paste

class PasteUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UpdatePasteForm
    model = Paste
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"view-type": "update"})
        return context

class PasteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paste
    success_url = "/"

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User