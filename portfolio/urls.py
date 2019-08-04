"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from .import views
# A1 from blog.views import blog_page
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls,name = '后台'),
    path('', views.home,name = '主站'),
    #和include为同一种操作类型 A1
 #   path('blog', blog_page),
    path('blog/', include('blog.urls')),
    path('ph/', include('ph.urls')),
    path('account/', include('account.urls')),
    path('strings/', include('strings.urls')),
    path('<int:gallery_id>/', views.gallery_text),
	path('todolist/', include('todo.urls')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
