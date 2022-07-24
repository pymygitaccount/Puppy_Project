import json
from urllib import response
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer


# initialize the APIClient app
client = Client()           # requests    - object created for client

# class GetAllPuppiesTest(TestCase):                
class PuppiesTest(TestCase):                  # common class for all tests.
    """ Test module for GET all puppies API.
        Class for testing the various methods for Puppies APIs. """

    def setUp(self):
        self.casper = Puppy.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')
        self.rambo = Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')
        self.ricky = Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')

        self.rony = Puppy.objects.create(name='rony', age=1, breed='Gradane', color='Brown')


        self.valid_data = {'name':'rony', 'age':6, 'breed':'Labrador', 'color':'White'}
        self.invalid_data = {'name':'', 'age':6, 'breed':'Labrador', 'color':'Brown'}


    # # ------- For GET Request - all data
    # def test_get_all_pippies_data(self):
    #     # get API response.
    #     data_for_client_request = client.get(reverse('get_post_puppies'))
    #     print("Response:-",data_for_client_request.json)

    #     # get data from database.
    #     puppi = Puppy.objects.all()
    #     ser = PuppySerializer(puppi, many=True)
        
    #     # comparing both results- API response and data from datatabase.
    #     self.assertEqual(data_for_client_request.data, ser.data)
    #     self.assertEqual(data_for_client_request.status_code, status.HTTP_200_OK)


    # def test_get_all_puppies_when_no_data_in_database(self):
    #     client_api_request = client.get(reverse('get_post_puppies'))

    #     puppi = Puppy.objects.all()
    #     # print("signal ---", puppi)
    #     ser = PuppySerializer(puppi, many=True)

    #     self.assertEqual(client_api_request.data, ser.data )
    #     self.assertEqual(client_api_request.status_code, status.HTTP_200_OK)


    # # ------- For GET Request - single data - data available
    # def test_get_valid_single_puppy(self):
    #     # get client API request for single puppy
    #     response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}))
    #     print(response.json())

    #     # get single puppy data from database.
    #     puppy = Puppy.objects.get(pk = self.muffin.pk)
    #     ser = PuppySerializer(puppy)

    #     # comparing both field
    #     self.assertEqual(response.data, ser.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # # ------- For GET Request - single data - data not available -- invalid data
    # def test_get_invalid_single_puppy(self):
    #     client_response = client.get(reverse('get_delete_update_puppy', kwargs={'pk':30}))
    #     self.assertEqual(client_response.status_code, status.HTTP_404_NOT_FOUND)


    # ------- For POST Request - single data ( inserting valid puppy)
    # def test_create_valid_puppy(self):
    #     response = client.post(reverse('get_post_puppies'), data = json.dumps(self.valid_data), content_type = 'application/json')  
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # # ------- For POST Request - single data ( inserting invalid puppy)
    # def test_create_invalid_data(self):
    #     response = client.post(reverse('get_post_puppies'), data=json.dumps(self.invalid_data), content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # json.dumps()  - Convert Python objects into JSON strings, and print the values:

    # # ------- For PUT Request - Update single data ( inserting valid puppy)
    # def test_upadte_valid_puppy(self):
    #     client_seponse = client.put(reverse('get_delete_update_puppy', kwargs={'pk':self.rony.pk}), data = json.dumps(self.valid_data), content_type='application/json')
    #     self.assertEqual(client_seponse.status_code, status.HTTP_200_OK)


    # # ------- For DLETE Request - Delete single data single data 
    # def test_delete_single_puppy(self):
    #     client_response = client.delete(reverse('get_delete_update_puppy', kwargs={'pk':self.ricky.pk}))
    #     self.assertEqual(client_response.status_code, status.HTTP_204_NO_CONTENT)










