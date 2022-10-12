"""befit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from befit_app import views as befit_app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', befit_app_views.home),
    path('articles/', befit_app_views.articles, name='articles'),
    path('home', befit_app_views.home, name='home'),
    path('add_food', befit_app_views.add_food, name='add_food'),
    path('personal_page', befit_app_views.personal_page, name='personal_page'),
    path('articles/<int:article_id>', befit_app_views.article, name='article'),
    path('articles/<str:article_id>', befit_app_views.article, name='article'),
   
    
]

urlpatterns += [ 
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)