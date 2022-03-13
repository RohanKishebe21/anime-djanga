
from django.conf import settings
from django.contrib import admin
from django.urls import path
from welcomeApp.views import aboutPage, initPage 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", initPage),
    path('about/', aboutPage, name ="about_path")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)