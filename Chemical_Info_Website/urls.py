"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Chemical_Info_Website.views import index, chemical_list, chemical_addition

urlpatterns = [
    path('Chemical_Info_Website/smiles/<str:smiles>/', chemical_list, name='BP_get'),
    path('Chemical_Info_Website/add_chemical', chemical_addition, name='adding_chem'),
    path('Chemical_Info_Website/chemweb', index, name='index'),
]
