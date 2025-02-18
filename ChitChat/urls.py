from django.urls import path, include
from ChitChat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # authentication section
    path("auth/login/", LoginView.as_view
         (template_name="chat/login.html"), name="login-user"),
    path("auth/logout/", auth_views.LogoutView.as_view(), name="logout-user"),
]