import boto3
from .serializers import DeviceSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
import os 
from dotenv import load_dotenv
load_dotenv()


print('===>'+os.environ.get('IS_OFFLINE'))

if os.environ.get('IS_OFFLINE'):
    dynamodb=boto3.resource("dynamodb", region_name='localhost', endpoint_url='http://localhost:7000')
else :
    dynamodb=boto3.resource("dynamodb")

table = dynamodb.Table('Device_Table')

class Create_Controller(APIView):

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        
        if not serializer.is_valid():
            return JsonResponse(data={serializer.errors},status=status.HTTP_400_BAD_REQUEST )

        data = serializer.validated_data
        result = table.get_item(Key={"id": data.get("id"),})
        
        item = result.get('Item')    
        if item:  
            return JsonResponse(data={'message': f'Item already exists with this id: {data.get("id")}.'},status=status.HTTP_409_CONFLICT)

        table.put_item(Item=data)
            
        return JsonResponse(data={'message': 'Item created successfully.'},status=status.HTTP_201_CREATED)


class Get_Controller(APIView):
    
    def get(self, request, pk):
        result=table.get_item(Key={"id": f"/devices/id{pk}",})
        if "Item" in result:
            serializer = DeviceSerializer(result["Item"])
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This item does not exist.'})

       
