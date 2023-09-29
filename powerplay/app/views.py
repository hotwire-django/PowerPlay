from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from app.models import Game
from app.forms import GameEditForm, GameEditTitleForm

import time


def home(request):
    return render("")


def game_list_slow(request):
    time.sleep(3)
    p = Paginator(Game.objects.all(), 7)
    page = p.page(1)
    return render(request, "game_list.html", {"page": page})


def game_list(request):
    games = Game.objects.all().order_by("-review_score")
    if query := request.GET.get("q"):
        games = games.filter(title__icontains=query)
    p = Paginator(games, 5)
    page = p.page(request.GET.get("page", 1))
    return render(request, "game_list.html", {"page": page})


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, "game_detail.html", {"game": game})


def game_edit(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == "POST":
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, "Your changes have been saved.")
            return redirect("game_detail", slug)
    else:
        form = GameEditForm(instance=game)

    return render(
        request, "game_edit.html", {"form": form}, status=422 if form.errors else 200
    )


def edit_title(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == "POST":
        form = GameEditTitleForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return render(request, "partials/edit_title.html", {"game": game})
    else:
        form = GameEditTitleForm(instance=game)

    return render(request, "partials/edit_title.html", {"form": form})
