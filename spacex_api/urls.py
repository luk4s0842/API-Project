from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_launches, name='all_launches'),
    path('next', views.next_launches, name='next_launches'),
    path('previous', views.previous_launches, name='previous_launches'),
    path('<int:launch_id>', views.show_videos, name='show_videos'),
]
