from django.urls import path
from . import views

urlpatterns =[
      path('create/',views.createorderview,name='addorder'),
      path('page/',views.Paginationshowview,name='pagination'),

]