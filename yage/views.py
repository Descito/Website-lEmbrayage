from django.shortcuts import render
from .models import Prjt

# Create your views here.
def home(request):
	projects=Prjt.objects.all()
	return render(request, 'yage/home.html',{'projects':projects})