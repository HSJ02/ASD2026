from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),

    path('study/', views.study_page, name='study'),
    path('insight/', views.insight_page, name='insight'),
    path('dailylife/', views.dailylife_page, name='dailylife'),
    path('project/', views.project_page, name='project'),

    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]