from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import  PlayModel
from django.urls import reverse_lazy

class PlayView(CreateView):
  template_name = 'create.html'
  model = PlayModel
  fields = ('title','m_file')
  success_url = reverse_lazy('list')

class PlayViewList(ListView):
  template_name = 'list.html'
  model = PlayModel

class PlayViewDelete(DeleteView):
  template_name = 'delete.html'
  model = PlayModel
  success_url = reverse_lazy('list')

class PlayViewUpdate(UpdateView):
  template_name = 'update.html'
  model = PlayModel
  fields = ('title', )
  success_url = reverse_lazy('list')