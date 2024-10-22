from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('news/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('services/', include('services.urls')),
    path('control-panel/', include('control_panel.urls')),
    path('work/', include('work.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
