from django.urls import path
from . import views
from .views import airport_list,airport_details,form,update,delete
#from .views import AirportViewsset
from rest_framework.routers import DefaultRouter


'''router = DefaultRouter()
router.register('viewsets',AirportViewsset)'''


urlpatterns = [
   # path('',views.search, name='search'),
    path('airport/',airport_list, name='airport'),
    path('detail/<int:id>',airport_details, name='details'),
    path('form/',form, name='AirportForm'),
    path('form/',form, name='AirportForm'),
    path('update/<str:pk>/',update,name='update'),
    path('delete/<str:pk>/',delete,name='delete'),

    #path('viewsset/',AirportViewsset, name='search'),
]