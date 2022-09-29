from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Postes


class SinglePostView(DetailView):
    model = Postes
    template_name = 'blog/single-post.html'
