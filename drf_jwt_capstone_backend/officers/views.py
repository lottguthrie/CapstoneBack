from functools import partial
from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework.serializers import Serializer
from .models import DailyReport, Officers
from .serializers import OfficersSerializer, DailyReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()




# Create your views here.
class AddOfficer(APIView):
    
    def post(self, request):
        serializer = OfficersSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Officer(APIView):

    def get_users(self):
        try:
            return Officers.objects.filter(is_active=True)
        except Officers.DoesNotExist:
            raise Http404

    def get_officer(self):

        officer=[]

        officers= self.get_users()
        for officer in officers:
            officer.append(Officers.objects.get(username= officer.username))
        return officer
            

    def get(self, request):
        officer = Officers.objects.all()
        serializer = OfficersSerializer(officer, many=True)
        return Response(serializer.data)



class GetAllOfficers(APIView):

    def get_officer(self, name):
        try:
            return Officers.objects.filter(username=name)
        except Officers.DoesNotExist:
            raise Http404

    def get(self, request, name):
        officer = self.get_officer(name)
        serializer = OfficersSerializer(officer, many= True)
        return Response(serializer.data)

class OfficerData(APIView):

    def get_officer(self, pk):
        try:
            return Officers.objects.get(pk=pk)
        except Officers.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        officer = self.get_officer(pk)
        serializer = OfficersSerializer(officer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        officer = self.get_officer(pk)
        serializer = OfficersSerializer(officer, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        officer = self.get_officer(pk)
        officer.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class AddDailyReport(APIView):

    def post(self, request):
        serializer = DailyReport(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GetDailyReport(APIView):

    def get_officer(self, name):
        try:
            return DailyReport.objects.filter(username=name)

        except Officers.DoesNotExist:
            raise Http404

    def get(self, request, name):
        all_officers=  self.get_officer(name)
        serializer= DailyReportSerializer(all_officers, many = True)
        return Response(serializer.data)


class EditDailyReport(APIView):

    def get_officer_daily_report(self, pk):
        try:
            return DailyReport.objects.get(pk=pk)
        except DailyReport.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        officer = self.get_officer_daily_report(pk)
        serializer = DailyReportSerializer(officer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        officer = self.get_officer_daily_report(pk)
        serializer = DailyReportSerializer(officer, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        officer = self.get_officer_daily_report(pk)
        officer.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)