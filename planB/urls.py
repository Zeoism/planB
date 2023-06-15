"""planB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from app.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'app'  # Replace 'myapp' with the actual name of your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('upl/', LessonCreateView.as_view(), name='upload_lesson'),
    path('<int:lesson_id>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('account/', include('django.contrib.auth.urls')),
    path('class/<int:gid>/<int:cid>/', LessonClassView.as_view(), name='lesson_class_view'),
    #path('<int:lesson_id>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

