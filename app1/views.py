from django.shortcuts import render
from app1.stuforms import StudForm,SrchForm
from app1.models import stud
def view(request):
        return render(request,'menu.html')

def home(request):
        return render(request,'menu.html')
        
def register(request):
    title="New Student Registration"
    ack="Registered Successfully"
    form=StudForm(request.POST or None)
    if request.method == 'POST':
        form = StudForm(request.POST)

        if form.is_valid():
            form.save()
            # name=form.cleaned_data['s_name']
            # clas=form.cleaned_data['s_class']
            # addr=form.cleaned_data['s_addr']
            # school=form.cleaned_data['s_school']
            # mail=form.cleaned_data['s_email']
            # p=stud(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=mail)
            # p.save()
            return render(request,'ack.html',{"Ack":ack})
            
    return render(request,'register.html',{'form':form,"title":title})
def existing(request):
        title="All Registered Students"
        queryset=stud.objects.all()
        context={
                "title":title,
                "queryset":queryset,
                }
        return render(request,'existing.html',context)

def search(request):
        title="Search Student"
        form=SrchForm(request.POST or None)
        if form.is_valid():
                gn_name=form.cleaned_data['s_name']
                queryset=stud.objects.filter(s_name=gn_name)
                if len(queryset)==0:
                     return render(request,'ack.html',{"Ack":"student not found"})   
                context={
                "title":title,
                "queryset":queryset,
                }
                return render(request,'existing.html',context)

        return render(request,'search.html',{'form':form,"title":title})
def dropout(request):
        title="Remove Student"
        ack="Removed Successfully"
        form=SrchForm(request.POST or None)
        if form.is_valid():
                gn_name=form.cleaned_data['s_name']
                queryset=stud.objects.filter(s_name=gn_name)
                if len(queryset)==0:
                     return render(request,'ack.html',{"Ack":"student not found"})
                else:
                        queryset=stud.objects.filter(s_name=gn_name).delete()
                return render(request,'ack.html',{"Ack":ack})

        return render(request,'dropout.html',{'form':form,"title":title})
                


        

        
# Create your views here.
