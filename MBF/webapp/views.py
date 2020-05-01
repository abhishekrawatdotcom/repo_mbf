from django.shortcuts import render
from webapp import  forms
from django.http import  HttpResponseRedirect



def thank(request):
    return render(request,'thanks.html')


def myviews(request):
    form=forms.myform()
    if request.method=='POST':
        form=forms.myform(request.POST)
        if form.is_valid():
            print('validation success')
            form.save(commit=True)
        return HttpResponseRedirect('/bye')
    else:
        form=forms.myform()
    return  render(request,'welcome.html',{'form':form})







# Create your views here.
