from django.contrib import admin
from django.urls import path, include
from pybo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path

    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
