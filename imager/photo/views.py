import os
from PIL import Image

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, UpdateView

from .forms import upload

# Create your views here.
class input(View):
    template_name = 'input.html'
    form_class = upload
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})

    '''
    if request.method == 'POST':
    
        form = upload(request.POST)
        
        if form.is_valid():
        
            return input('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = upload()
    return render(request, 'input.html', {'form':form})
    '''
    #return HttpResponse('contact view')