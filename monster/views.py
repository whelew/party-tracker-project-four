from django.shortcuts import render
from .models import Monster


def monster_library(request):
    """
    Display an individual :model:`monster.Monster`.

    **Context**

    ``monster``
        An instance of :model:`monster.Monster`.

    **Template:**

    :template:`monster/monster_library.html`
    """

    monsters = Monster.objects.all()

    return render(
        request, "monster/monster_library.html",
        {"monsters": monsters},
        )
