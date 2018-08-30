import csv
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
l=[]
m=[]
n=[]
def dash_view(request):
    csv_file = open('Top Lanes.csv', 'r')
    x = csv.reader(csv_file, delimiter=',')
    d=str(request.GET.get("d")).replace("-","/")
    f = str(request.GET.get("start"))
    t = str(request.GET.get("end"))
    c = f + "->" + t
    filtered = [row for row in x if row[1] == d and row[0] == c]
    for i in filtered:
        o = i[2].split(" ")
        l.append(o[0])
        m.append(float(i[3]))
        n.append(float(i[4]))

    context={}
    return render(request,"dash.html",context)
# Create your views here.
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):
        usernames =(l,m,n)
        return Response(usernames)
