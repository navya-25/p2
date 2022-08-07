from django.urls import path
from . import views
app_name='cars'
urlpatterns=[
    path('list/',views.list,name='list'),
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('rental_review/',views.rental_review,name='rental_review')


]