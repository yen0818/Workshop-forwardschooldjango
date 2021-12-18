from combine import views
from django.urls import path
 
app_name = 'combine'
 
urlpatterns=[
    path('', views.HomePageView.as_view(), name='home'),
    path('getnum/',views.Api.getNums, name='get-num'),
    path('getavg/',views.Api.getAvg, name='get-avg'),
    path('getgraph/',views.Api.getGraph, name='get-graph'),
    path('getdata/',views.Api.getData, name='get-data'),
    path('get-seaborn-graph/',views.Api.getSeabornGraph, name='get-seaborn-graph'),
    path('chart/',views.HomeView.as_view(), name='home-view'),
    path('chart-api/',views.ChartData.as_view(), name='chart-api'),
    path('plotly-chart/',views.PlotlyChartView.as_view(), name='plotly-chart'),
    path('book-table/',views.BookTableView.as_view(), name='book-table'),
    path('user-table/',views.UserTableView.as_view(), name='user-table')
]