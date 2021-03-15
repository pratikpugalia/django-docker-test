from django.conf.urls import url 
from companyData import views 
 
urlpatterns = [ 
    url(r'^api/companies$', views.companyData_list),
    url(r'^api/companies/data$', views.companyData_detail),
]
