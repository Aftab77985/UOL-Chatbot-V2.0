from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name = 'homepage.html'

class ChatRoom(LoginRequiredMixin,TemplateView):
    template_name = 'chatroom.html'
    login_url  = 'login'