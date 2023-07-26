

from django.urls import path

from marketapp import views
app_name = 'marketapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('market/<int:market_id>/',views.details,name='details'),
    path('add/',views.add_market,name="add_market"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),

]