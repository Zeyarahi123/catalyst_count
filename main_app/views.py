import csv
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CompanyData
from .forms import UploadFileForm


# Create your views here.

class UploadFileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'main_app/upload.html', {'form': form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            reader = csv.DictReader(file.read().decode('utf-8').splitlines())
            for row in reader:
                CompanyData.objects.create(**row)
            return redirect('success')
        return render(request, 'main_app/upload.html', {'form': form})

class SuccessView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'main_app/success.html')

