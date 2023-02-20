from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
from app1.forms import *

#FUNCTION BASE VIEW --> FBV
#CLASS BASE VIEW -->CBV


#fbv to returning string as response
def fbv_string(request):
    return HttpResponse('This is a FBV string')

#cbv to returning  string as response
class Cbvstring(View):
    def get(self,request):
        return HttpResponse('this is a CBV string')
    



#fbv to  render html files as response in template view
def fbv_htmlpage(request):
    d={'name':'siva'}
    return render(request,'fbv_htmlpage.html',d)

# cbv to render html files as response in template view
class cbv_htmlpage(View):
    def get(self,request):
       d={'name':'pavan'} 
       return render(request,'cbv_htmlpage.html',d)
    



#fbv handling the django forms
def fbv_forms(request):
    SFO=studentform()
    d={'sfo':SFO}
    if request.method=='POST':
        SFD=studentform(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))

    return render(request,'fbv_forms.html',d)

#cbv  handling the django forms
class cbv_forms(View):
    def get(self,request):
        SFO=studentform()
        d={'sfo':SFO}
        return render(request,'cbv_forms.html',d)
    
    def post(self,request):
        SFD=studentform(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))