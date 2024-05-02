from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('picha/<int:pk>', views.picha, name='picha'),
    path('main', views.TagListView.as_view(), name="main"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)