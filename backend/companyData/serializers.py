from rest_framework import serializers 
from companyData.models import CompanyData
 
 
class CompanyDataSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CompanyData
        fields = ('company',
                  'month',
                  'headcount')

class CompanySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CompanyData
        fields = ('company',)
