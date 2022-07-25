from os import stat
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer

for i in range(0,10):
    pass


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        ser = PuppySerializer(puppy)
        return Response(ser.data)

    # delete a single puppy
    elif request.method == 'DELETE':
        puppy.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        

        
    # update details of a single puppy
    elif request.method == 'PUT':
        data = request.data
        ser = PuppySerializer(puppy, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET', 'POST'])
def get_post_puppies(request):    # use to get all puppies and to add new puppy.
    # get all puppies
    if request.method == 'GET':                        # test done - for with and without data - passed.
        # if Puppy.objects.all() == 'QuerySet []':
        #     # print("signal ---", Puppy.objects.all())
        #     return Response(status=status.HTTP_204_NO_CONTENT)

        # else:
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
        # return Response({})

    # insert a new record for a puppy
    elif request.method == 'POST':
        data = {'name' : request.data.get('name'),
        'age' : int(request.data.get('age')),
        'breed' : request.data.get('breed'),
        'color' : request.data.get('color')}
        print(data)
        ser = PuppySerializer(data = data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        