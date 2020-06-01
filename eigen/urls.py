from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from enumerator import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.TableView.as_view(), name='table'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
