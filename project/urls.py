# project/urls.py
from django.contrib import admin
from django.urls import path, include
from CV_Gen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name='accept'),
    path('<int:id>/', views.resume, name='resume'),
    path('list/', views.list_profiles, name='list_profiles'),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('preview/', views.preview_pdf, name='preview_pdf'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
