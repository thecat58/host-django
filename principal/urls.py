from django.urls import path
from principal import views

urlpatterns = [
    path('',views.render_articles, name='articles')
]

