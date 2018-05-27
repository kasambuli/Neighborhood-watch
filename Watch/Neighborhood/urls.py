from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^accounts/profile/(\d+)', views.profile, name='profile'),
url(r'^profile/', views.update_profile, name='editProfile'),
url(r'^neighborhood/',views.neighborhood,name = 'neighborhood'),
url(r'^$',views.index,name ='index')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)