"""miko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from . import postView
from . import accountView
import account.views
import post.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^post/sell/do/', post.views.postItem),
    url(r'^post/sell/', postView.sell, name='sell'),

    url(r'^account/register/do/', account.views.registerAccount),
    url(r'^account/login/do/', account.views.loginAccount),
    url(r'^account/logout/', accountView.logout, name='logout'),

    url(r'^account/register/', accountView.register, name='register'),
    url(r'^account/login/', accountView.login, name='login'),

    url(r'^account/', accountView.index, name='profile'),
    url(r'^$', postView.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
