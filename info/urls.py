from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('location/', views.location, name = 'location'),
    path('members/', views.members, name = 'members'),
    path('professor/<str:profname>/', views.professor, name = 'professor'),
    path('publictaions/<str:category>/', views.publictaions, name = 'publictaions'),
    path('conferences/', views.conferences, name = 'conferences'),
    path('patents/', views.patents, name = 'patents'),
    path('project/', views.project, name = 'project'),
    path('research/', views.research, name = 'research'),
    path('album/', views.album, name = 'album'),
    path('members/<int:pk>/', views.members_detail, name = 'member_detail'),
    
]