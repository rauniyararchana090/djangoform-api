from django.shortcuts import render, HttpResponse
import csv
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Airport
from .serializer import AirportSerializer 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import AirportFilter
from rest_framework.generics import ListAPIView
from .form import AirportForm
#from rest_framework import viewsets


 
# Create your views here.
def open():
    csv_file= open ('new_info.csv','r')
    csv_reader=csv.reader(csvfile)
    for line in csv_reader:
        next(csv_reader)
        x = Airport(iata=line[0], icao=line[1], name=line[2], location=line[3], gps=line[4])
        x.save()




def form(request):
    form= AirportForm()
    if request.method == 'POST':
        form = AirportForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 

    ap = AirportForm()
    return render(request,'search.html',{'form':ap})


def update(request, pk):
    data = Airport.objects.get(id=pk)
    form= AirportForm(instance=data) #previsous data
    if request.method == 'POST':
        form = AirportForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save() 
    context={
        'data':data,
        'form':form
    }
    return render(request,'update.html',context)

def delete(request,  pk):
    data = Airport.objects.get(id=pk)
    
    if request.method == 'POST':
        data.delete()

    context={
        'item':data
    }    
    return render(request,'delete.html',context)      

@api_view(['GET','POST'])
def airport_list(request):

    if request.method == 'GET':
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports,  many=True)
        #myFilter = AirportFilter() #for filtering
        return Response (serializer.data) 

    elif request.method =='POST':   
        #data= JSONParser().parse(request) 
        serializer = AirportSerializer(data=request.data)

        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view (['GET','PUT','DELETE'])
def airport_details(request,id):
    try:  
        airport= Airport.objects.get(id=id)

    except Airport.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AirportSerializer(airport)
        return Response (serializer.data) 

    elif request.method == 'PUT':
        #data= JSONParser().parse(request) 
        serializer = AirportSerializer(airport,data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST) 


    elif request.method == 'DELETE':
          airport.delete()
          return  Response (status=status.HTTP_204_NO_CONTENT)

class AirportListSearch(ListAPIView):
    airports = Airport.objects.all()
    serializer = AirportSerializer(airports)
    filter_backend=(SearchFilter,OrderingFilter)
    search_field = ('iata','icao','name','location','gps')

'''class AirportViewsset(viewsets.ModelViewsSet):
    serializer = AirportSerializer

    def get_queryset(self):
        airports = Airport.objects.all()
        return airports'''

     