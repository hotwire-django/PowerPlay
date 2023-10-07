from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import TemplateView

from app import views, views_guestbook, views_demos

urlpatterns = [
    path('', lambda request: redirect("home")),
    path('home/', TemplateView.as_view(template_name='home.html'), name="home"),

    path('about_gb', TemplateView.as_view(template_name='partials/systems_gb.html'), name="about_gb"),
    path('about_gbp', TemplateView.as_view(template_name='partials/systems_gbp.html'), name="about_gbp"),
    path('about_gbc', TemplateView.as_view(template_name='partials/systems_gbc.html'), name="about_gbc"),

    path('game/', views.game_list, name="game_list"),
    path('game/detail/<slug:slug>/', views.game_detail, name="game_detail"),
    path('game/edit/<slug:slug>/', views.game_edit, name="game_edit"),

    path('game/edit/title/<slug:slug>/', views.edit_title, name="edit_title"),

    path('guestbook/', views_guestbook.guestbook_list, name="guestbook"),
    path('guestbook/remove/<uuid:pk>/', views_guestbook.guestbook_remove_entry, name="guestbook_remove_entry"),
    path('guestbook/stream/', views_guestbook.guestbook_stream, name="guestbook_stream"),

    # Demo Pages
    path('add_stylesheet/', TemplateView.as_view(template_name='samples/add_stylesheet.html'), name="add_stylesheet"),
    path('game/slow/', views_demos.game_list_slow, name="game_list_slow"),

    path('infinite_scroller/', TemplateView.as_view(template_name='infinite_scroller.html'), name="infinite_scroller"),
    path('scroll_frame/<int:page>', views_demos.scroll_frame, name="scroll_frame"),

    path('sse_test', TemplateView.as_view(template_name='sse_demo.html'), name="sse_demo"),
    path('sse', views_demos.sse, name="sse"),

    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
