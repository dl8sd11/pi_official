from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('api/query',views.view_questions, name='view_questions'),
    path('api/submit',views.submit_questions, name='submit_questions'),
    path('api/view',views.view_questions,name='view_questions'),
    path('api/response/<int:id>',views.response_questions,name='response_questions'),
]