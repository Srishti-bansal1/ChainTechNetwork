from django.shortcuts import render

from ChainApp.dynamicData import DynamicData
from .models import ChainModel
from .serializer import ChainSerializer, DynamicSerializer
from rest_framework import response , viewsets ,status
from rest_framework.decorators import action , api_view
from rest_framework.response import Response

# Create your views here.

class ChainViewSet(viewsets.ModelViewSet):
    queryset = ChainModel.objects.all()
    serializer_class = ChainSerializer
    
    
    @action(detail=False, methods=["GET"],url_path='show')
    def getCustom(self, request):
        queryset = ChainModel.objects.all()
        serializer = ChainSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    @action(detail=False, methods=["POST"],url_path='add_create')
    def Add_created(self, request):
        dataReceived = request.data 
        serializer = ChainSerializer(data = request.data)
        
        if ChainModel.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    
    
@api_view(['GET'])   
def index(request):
    return render(request, 'ChainTemp.html', {'index': index})


class DynamicViewSet(viewsets.GenericViewSet):
    serializer_class = DynamicSerializer
    
    @action(detail=False, methods=["GET"],url_path='dynamic')
    def getCustom(self, request):
        dynamicData = DynamicData()
        serializer = DynamicSerializer(dynamicData) 
        print(serializer.data)
        return Response(serializer.data)
    
@api_view(['GET'])   
def form(request):
    return render(request, 'userDataForm.html', {'form': form})


