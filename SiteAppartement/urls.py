from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
import annonces.views
import authentication.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',annonces.views.home,name='home'),
    path('annonces/<int:annonce_id>',annonces.views.annonce_detail,name='annonce-detail'),
    path('publierAnnonce/', annonces.views.publier_annonce, name='publier-annonce'),
    path('login/',LoginView.as_view(
        template_name = "authentication/login.html",
        next_page = settings.LOGIN_REDIRECT_URL,
    ),name='login'),
    path('logout/',LogoutView.as_view(
    ),name='logout'),
    path('signup/',authentication.views.signup,name='signup'),
    path('password-change/',PasswordChangeView.as_view(
        template_name = "authentication/password_change_form.html"
    ),name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(
        template_name = "authentication/password_change_done.html"
    ),name ='password_change_done'),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
