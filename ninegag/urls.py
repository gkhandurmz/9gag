from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user/signup/', views.signup, name='signup'),
    path('user/login/', views.login, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('<slug:postslug>/', views.SpecificPost, name='spost'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('post/create', views.create, name='create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
