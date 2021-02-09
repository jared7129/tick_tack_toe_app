from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewGameForm, PlayForm
from .models import Game


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        form = NewGameForm(request.POST)
        if form.is_valid():
            game = form.create()
            game.play_auto()
            game.save()
            return redirect(game)
    else:
        form = NewGameForm()
    return render(request, "list.html", {'form': form})


@require_http_methods(["GET", "POST"])
def tictactoe(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = PlayForm(request.POST)
        if form.is_valid():
            game.play(form.cleaned_data['index'])
            game.play_auto()
            game.save()

            return redirect(game)
        else:
            pass

    return render(request, "detail.html", {
        'game': game
    })
