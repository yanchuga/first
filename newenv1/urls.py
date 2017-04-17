"""newenv1 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from students import views as myapp_views

urlpatterns = [
    #students url
    url(r'^$', myapp_views.students_list, name='home'),
    url(r'^students/add/$', myapp_views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', myapp_views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', myapp_views.students_delete, name='students_delete'),
    #groups url
    url(r'^groups/$', myapp_views.groups_list, name='groups'),
    url(r'^groups/add/$', myapp_views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', myapp_views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', myapp_views.groups_delete, name='groups_delete'),
    url(r'^admin/', admin.site.urls),
]