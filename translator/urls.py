from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

# 이름공간(namespace)설정
app_name = "translator"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:property_id>',views.detail, name='detail'),
    path('<int:property_id>/en',views.detail, name='en'),
    path('<int:property_id>/ko-utf', views.detail, name='ko_utf'),
    path('upload', views.upload_file, name="upload_file"),
    path('google-translation', views.google_translation, name="google_translation"),
    path('encoding', views.encoding, name="encoding"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
