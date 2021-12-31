from functools import partial
from django.contrib.auth import get_user_model
from django.http.response import Http404
from drf_jwt_capstone_backend import supervisors
from rest_framework.serializers import Serializer
from .models import SupervisorReport, Supervisors
from .serializers import SupervisorsSerializer, SupervisorReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()




# Create your views here.
class AddSupervisor(APIView):
    
    def post(self, request):
        serializer = SupervisorsSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Supervisor(APIView):

    def get_users(self):
        try:
            return Supervisors.objects.filter(is_active=True)
        except Supervisors.DoesNotExist:
            raise Http404

    def get_supervisor(self):

        supervisor=[]

        supervisors= self.get_users()
        for supervisor in supervisors:
            supervisor.append(Supervisors.objects.get(last_name= supervisor.last_name))
        return supervisor
            

    def get(self, request):
        supervisor = Supervisors.objects.all()
        serializer = SupervisorsSerializer(supervisor, many=True)
        return Response(serializer.data)



class GetAllSupervisors(APIView):

    def get_supervisor(self, name):
        try:
            return Supervisors.objects.filter(last_name=name)
        except Supervisors.DoesNotExist:
            raise Http404

    def get(self, request, name):
        supervisor = self.get_supervisor(name)
        serializer = SupervisorsSerializer(supervisor, many= True)
        return Response(serializer.data)

class SupervisorData(APIView):

    def get_supervisor(self, pk):
        try:
            return Supervisors.objects.get(pk=pk)
        except Supervisors.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supervisor = self.get_supervisor(pk)
        serializer = SupervisorsSerializer(supervisor)
        return Response(serializer.data)
    
    def put(self, request, pk):
        supervisor = self.get_supervisor(pk)
        serializer = SupervisorsSerializer(supervisor, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        supervisor = self.get_supervisor(pk)
        supervisor.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class AddSupervisorReport(APIView):

    def post(self, request):
        serializer = SupervisorReport(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GetSupervisorReport(APIView):

    def get_supervisor(self, name):
        try:
            return SupervisorReport.objects.filter(last_name=name)

        except Supervisors.DoesNotExist:
            raise Http404

    def get(self, request, name):
        all_supervisor=  self.get_supervisor(name)
        serializer= SupervisorReportSerializer(all_supervisor, many = True)
        return Response(serializer.data)


class EditSupervisorReport(APIView):

    def get_supervisor_report(self, pk):
        try:
            return SupervisorReport.objects.get(pk=pk)
        except SupervisorReport.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supervisor = self.get_supervisor_report(pk)
        serializer = SupervisorReportSerializer(supervisor)
        return Response(serializer.data)
    
    def put(self, request, pk):
        supervisor = self.get_supervisor_report(pk)
        serializer = SupervisorReportSerializer(supervisor, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        supervisor = self.get_supervisor_report(pk)
        supervisor.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)