from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Monster

# Create your views here.

def monster_library(request):
    """
    Display an individual :model:`monster.Monster`.

    **Context**

    ``monster``
        An instance of :model:`monster.Monster`.

    **Template:**

    :template:`monster/monster_library.html`
    """
     
    queryset = Monster.objects
    library = get_object_or_404(queryset)

    return render(
        request, "monster/monster_library.html",
        {"library": library},
        )
