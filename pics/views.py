from typing import Any
from django.shortcuts import render
from .models import Picha, Tag
from django.views.generic import ListView
import json

# Create your views here.
def homepage(request):
    all_images = Picha.objects.all()

    return render(request, 'index.html', {'all_images':all_images})

def picha(request, pk):
    picha = Picha.objects.get(id=pk)
    return render(request, 'single_image.html',{'picha':picha})


class TagListView(ListView):
    model = Tag
    template_name = 're-use/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Tag.objects.values()))
        return context                                                                                                                                                                              