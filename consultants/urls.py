from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # <-- c’est ici que le nom 'dashboard' est défini
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




