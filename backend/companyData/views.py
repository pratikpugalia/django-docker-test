from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from companyData.models import CompanyData
from companyData.serializers import CompanyDataSerializer
from companyData.serializers import CompanySerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def companyData_list(request):
    companyData = CompanyData.objects.values('company').distinct()

    company_serializer = CompanySerializer(companyData, many=True)
    company_list = []
    for item in company_serializer.data:
        company_list.append(item['company'])
    return JsonResponse(company_list, safe=False)
 
 
@api_view(['POST'])
def companyData_detail(request):
    companyList = JSONParser().parse(request)
    print(companyList)
    
    try: 
        companyData = CompanyData.objects.filter(company__in=companyList) 
    except CompanyData.DoesNotExist: 
        return JsonResponse({'message': 'The Company Data does not exist'}, status=status.HTTP_404_NOT_FOUND) 


    companyData_serializer = CompanyDataSerializer(companyData, many=True)
            

    return JsonResponse(companyData_serializer.data, safe=False)
    
