from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('submit', views.submit_questions, name='submit_questions'),
    path('view', views.view_questions, name='view_questions'),
    path('api/super/view', views.super_view_questions,
         name='super_view_questions'),
    path('agenda', views.view_agenda, name='view_agenda'),
    path('paper', views.view_paper, name='view_paper'),
    path('api/response/<int:id>', views.response_questions,
         name='response_questions'),
    path('api/slide/generate', views.generate_slide, name='generate_slide'),
    path('api/slide/view', views.view_slide, name='view_slide'),
    path('project', views.view_project, name='view_project'),
    path('m1/burnside', views.burn_side, name='burn_side')
]
