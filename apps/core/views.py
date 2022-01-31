from django.http import response
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = "core/Dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'active'
        return context


