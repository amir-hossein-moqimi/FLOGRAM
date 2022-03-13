from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.sitemaps import StaticViewsSitemap
from django.contrib.sitemaps.views import sitemap

app_name = 'FLOGRAM'

sitemaps = {
    'static' : StaticViewsSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name="aboutUs"),
    path('', views.home, name="homePage"),
    path('accounts/', include('accounts.urls'), name="accounts"),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
urlpatterns += staticfiles_urlpatterns()