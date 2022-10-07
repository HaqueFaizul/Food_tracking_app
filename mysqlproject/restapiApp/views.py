from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerialize
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class EmployeeShow(APIView):
    def get(self,request):
        empobj=Employee.objects.all()
        empseriobj=EmployeeSerialize(empobj,many=True)
        return Response(empseriobj.data)
    def post(self,request):
        empseriobj=EmployeeSerialize(data=request.data)
        if (empseriobj.is_valid()):
            empseriobj.save()
            return Response(empseriobj.data,status.HTTP_201_CREATED)
        else:
            return Response(empseriobj.errors,status.HTTP_400_BAD_REQUEST)

class EmployeeUpdateDelete(APIView):
    def get(self,request,eid):
        empobj = Employee.objects.get(id=eid)
        empseriobj = EmployeeSerialize(empobj)
        return Response(empseriobj.data)
    def put(self,request,eid):
        empobj=Employee.objects.get(id=eid)
        empseriobj = EmployeeSerialize(empobj,data=request.data)
        if (empseriobj.is_valid()):
            empseriobj.save()
            return Response(empseriobj.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(empseriobj.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self,request,eid):
        empobj=Employee.objects.get(id=eid)
        empobj.delete()
        return Response(status.HTTP_200_OK)
