from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.MainDashboardView,name='mainDashboardView'),
    path('/getchartdata',views.ChartData.as_view(), name='getChartData'),

]
