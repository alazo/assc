from django.conf.urls import include, url

from django.contrib import admin
from assc import views
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'assc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeFEView.as_view(), name='home'),
    url(r'^index_fe$', views.HomeFEView.as_view(), name='index-fe'),
    url(r'^index_mp$', views.HomeMPView.as_view(), name='index-mp'),
    url(r'^admin/', include(admin.site.urls)),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
