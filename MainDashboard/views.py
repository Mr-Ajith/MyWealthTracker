from django.shortcuts import render
from Login.views import * 
from MainDashboard.models import *
from MainDashboard.utils.updateDB import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def MainDashboardView(request):
  if request.user.is_authenticated:
    updateDashboardDB(request)
    mainDashboardValues = MainDashboard.objects.get(userId=request.user.username) 
    context = {
        'fullName': request.user.get_full_name(),
        'mainDashboardValues': mainDashboardValues,
        'menuId': 0,
    }
    return render(request, 'DashboardTemplates/dashboard.html', context)
  else:
    return redirect(login)



class ChartData(APIView):
  def get(self, request, format=None):
 
    menuId = request.GET.get('menuId', None)
    mainDashboardValues = MainDashboard.objects.get(userId=request.user.username)
    if (menuId == '0'):
      labels = [
          'Savings',
          'Fixed Deposits',
          'Mutual Funds',
          'Stocks',
      ]
      chartLabel = ""
      chartdata = []
      chartdata.insert(0, mainDashboardValues.savings)
      chartdata.insert(1, mainDashboardValues.fixedDeposit)
      chartdata.insert(2, mainDashboardValues.mutualFund)
      chartdata.insert(3, mainDashboardValues.stock)
      data = {
          "labels": labels,
          "chartLabel": chartLabel,
          "chartdata": chartdata,
          "menuId": menuId,
      }

    elif (menuId == '1'):
      savingsDashboardValues=SavingsDashboard.objects.get(userId=request.user.username)
      labels = [
          'Canara Bank',
          'Central Bank of India',
          'South Indian Bank',
      ]
      chartLabel = ""
      chartdata = []
      chartdata.insert(0, savingsDashboardValues.can)
      chartdata.insert(1, savingsDashboardValues.cbi)
      chartdata.insert(2, savingsDashboardValues.sib)
      data = {
          "labels": labels,
          "chartLabel": chartLabel,
          "chartdata": chartdata,
          "menuId": menuId,
      }
    else:
      labels = []
      chartLabel = ""
      chartdata = []
      data = {
          "labels": labels,
          "chartLabel": chartLabel,
          "chartdata": chartdata,
          "menuId": menuId,
      }
    return Response(data)
