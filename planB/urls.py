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
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('upload/', upload_lesson, name='upload_lesson'),
#     path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
# ]
from django.urls import path
from app.views import LessonCreateView, LessonDetailView

urlpatterns = [
    path('upload/', LessonCreateView.as_view(), name='upload_lesson'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
]
