from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('calendario/', views.calendario, name='calendario'),

    path('login/', views.login, name='login'),

    path('<int:pct_id>/', views.detail, name='detail'),

    path('<int:pct_id>/results/', views.results, name='results'),

    path('<int:pct_id>/vote/', views.vote, name='vote'),


]