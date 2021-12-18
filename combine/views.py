from django.shortcuts import render
from django.http import HttpResponse
from forward.settings import MEDIA_ROOT
from django.views.generic import TemplateView
 
# Create your views here.
 
import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg') #Agg is a non-interactive backend, only save to files
import matplotlib.pyplot as plt
import seaborn as sb
 
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'combine/index.html', context=None)
 
class Api(TemplateView):
    # Create your views here.
    def getNums(request):
        n = np.array([2,3,4])
        name1 = "name-1" + str(n[1])
        return HttpResponse('{"name":'+name1+',"age":31,"city":"New York"}')
 
    def getAvg(request):
        s1=request.GET.get("val","")
        print (s1)
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)
 
        return HttpResponse(str(np.average(ar)))
 
    def getGraph(request):
        x = np.arange(0,2 * np.pi, 0.01) # starts from 0, ends till 6.28 and adds by 0.01
        s = np.cos(x)**2 # ** is the operator for "power of".
        plt.plot(x,s)
 
        plt.xlabel('xlabel(X)')
        plt.ylabel('ylabel(y)')
        plt.title('Basic Graph!')
        plt.grid(True)
 
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response
 
    def getData(request):
        samp = np.random.randint(100,600,size=(4,5)) #size means the array size
        df = pd.DataFrame(samp, index=['alex','danny','lina','david'],columns=['Jan','Feb','Mar','Apr','May'])
        return HttpResponse(df.to_html(index=True, classes='table table-bordered'))
 
    def getSeabornGraph(request):
        file_path = MEDIA_ROOT+"/titanic_train.csv"
        df = pd.read_csv(file_path)
        graph = sb.factorplot(x='Survived',hue='Sex',data=df, col='Pclass',kind='count') #passenger class
        
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        return response
 
# Chapter 4: CHART.JS (Involves Javascript)
 
from rest_framework.views import APIView #Using the APIView class is pretty much the same as using a regular View class
from rest_framework.response import Response
 
class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'combine/charts.html')
 
class ChartData(APIView):
 
    def get(self, request, format=None):
        labels=['January','February',"March","April","May","June","July"]
        chartLabel="My Data"
        chartData=[0,10,5,2,20,30,45]
        data = {
            "labels":labels,
            "chartLabel":chartLabel, 
            "chartdata":chartData, 
        }
        return Response(data)
 
 
# Chapter 5: Plot.ly (Involves Javascript)
from plotly.offline import plot
import plotly.graph_objs as go
 
class PlotlyChartView(TemplateView):
    def get(self, request, *args, **kwargs):
        x_data=[0,1,2,3]
        y_data=[x**2 for x in x_data]
        plot_div = plot([go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines',
            name='My Plotly Chart',
            opacity=0.8,
            marker_color='green'
        )], output_type='div')
 
        return render(request, 'combine/plotly.html', context={'plot_div':plot_div})
 
# Part 6: DJANGO-TABLES (Does not involves Javascript) #An app for creating HTML tables
import django_tables2 as tables
from book.models import Book
from hello_world.models import User, UserProfileInfo
 
# Table Class
class BookTable(tables.Table):
    class Meta:
        model = Book
 
# View
class BookTableView(tables.SingleTableView):
    table_class=BookTable
    queryset=Book.objects.all()
    template_name="combine/table.html"
 
# Table Class
class UserTable(tables.Table):
    class Meta:
        model = UserProfileInfo
 
# View
class UserTableView(tables.SingleTableView):
    table_class=UserTable
    queryset=UserProfileInfo.objects.all() #ORM Object Relation Mapping
    template_name="combine/table.html"