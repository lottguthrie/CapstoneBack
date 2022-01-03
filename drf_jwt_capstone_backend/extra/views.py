from django.http import request
from django.http.response import Http404
from .models import Extra, OfficerRoles
from .serializers import ExtraSerializer, OfficerRolesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps 



class ExtraRegistration(APIView):
    
    def post(self, request):
        serializer = ExtraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllExtra(APIView):

    def get_extra(self, officer_id):
        try:
            return Extra.objects.filter(officer_id=officer_id)
        except Extra.DoesNotExist:
            raise Http404
    
    def get(self,request, officer_id):
        all_extras = self.get_extra(officer_id)
        serializer = ExtraSerializer(all_extras, many = True)
        return Response(serializer.data)


class ExtraData(APIView):

    def get_extra(self, officer_id):
        try:
            return Extra.objects.get(officer_id=officer_id)
        except Extra.DoesNotExist:
            raise Http404

    def get(self, request, officer_id):
        extra = self.get_extra(officer_id)
        serializer = ExtraSerializer(extra)
        return Response(serializer.data)

    def put(self, request, officer_id):
        extra = self.get_extra(officer_id)
        serializer = ExtraSerializer(extra, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, officer_id):
        extra = self.get_extra(officer_id)
        extra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class OfficerRolesRegistration(APIView):

    def post(self, request):
        serializer = OfficerRolesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AllOfficerRoles(APIView):

    def get(self, request):
        all_officer_roles = OfficerRoles.objects.all()
        serializer = OfficerRolesSerializer(all_officer_roles, many = True)
        return Response(serializer.data)



class OfficerRolesData(APIView):

    def get_officer_roles(self, last_name):
        try:
            return OfficerRoles.objects.get(name=last_name)
        except Extra.DoesNotExist:
            raise Http404

    def get(self, request, officer_id):
        officer_role = self.get_officer_roles(officer_id)
        serializer = OfficerRolesSerializer(officer_role)
        return Response(serializer.data)
    
    def put(self, request, officer_id):
        officer_role = self.get_officer_roles(officer_id)
        serializer = OfficerRolesSerializer(officer_role)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, officer_id):
        officer_role = self.get_officer_roles(officer_id)
        officer_role.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)