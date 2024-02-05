from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:movie_id>/',views.mshow,name="mshow"),
    path('addmovie/',views.addm,name="addm"),
    path('update/<int:id>/',views.updatem,name="updatem"),
    path('delete/<int:id>/',views.deletem,name="deletem"),
]
