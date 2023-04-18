from django.urls import path
from . import views
from .views import homePageView, loginView, addNoteView


urlpatterns = [
    path('', homePageView, name='home'),
    path('login/', loginView, name='login'),
    path('add/', addNoteView, name='add_note'),
    path('users/<str:username>/notes/', views.userNotesView, name='user_notes'),
]

