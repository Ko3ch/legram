from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name = 'gram-home'),
    url(r'profile/(\d+)/$', views.profile, name='gram-profile'),
    url(r'profile/update_profile/', views.update_profile, name = 'gram-profile-update'),
    url(r'new_post/', views.new_image_post, name = 'gram-post'),
    url(r'search/', views.search_results, name='gram-search'),
    url(r'image/(\d+)/$', views.post_by_id, name='gram-single_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)