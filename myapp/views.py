from django.shortcuts import render,redirect
from myapp.models import Appointment, ImageModel
from myapp.models import Contact
from myapp.forms import AppointmentForm, ImageUploadForm
from myapp.models import Member
from myapp.models import Login

# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
           username = request.POST['username'],
           password = request.POST['password']
        ).exists():
           return render(request, 'index.html')
        else:
           return render(request, 'login.html')
    else:
        return render(request, 'login.html')
       

       
def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    return render(request, 'doctors.html')

def myservice(request):
    return render(request, 'services.html')

def departments(request):
    return render(request, 'departments.html')

def success(request):
    return render(request, 'contactsuccess.html')

def asuccess(request):
    return render(request, 'appointmentsuccess.html')

def contact(request):
    if request.method == 'POST':

        contactus = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        contactus.save()
        return redirect('success')
    else:
        return render(request, 'contact.html')
    
def create_appointment(request):
    if request.method == 'POST':

        myappointment = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        myappointment.save()
        return redirect('asuccess')

    else:
        return render(request,'appointment.html')
    
def show(request):
    allappointments = Appointment.objects.all()
    return render(request, 'show.html', {'appointments': allappointments})

def contactshow(request):
    allcontacts = Contact.objects.all()
    return render(request, 'showcontact.html', {'contacts': allcontacts})

def delete (request,id):
    appoint = Appointment.objects.get(id = id)
    appoint.delete()
    return redirect('/show')

def deletecontact(request, id):
    contact = Contact.objects.get(id = id)
    contact.delete()
    return redirect('/showcontact')

def edit(request,id):
    editappointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {'appointment':editappointment})
    

def update (request,id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST,instance=updateinfo)  
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')
    
def register(request):
    
    if request.method == 'POST':
        members = Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request,'register.html')






def login(request):
   if request.method == 'POST':
       signin = Login(
           username = request.POST['username'],
           password = request.POST['password'],
       )
       signin.save()
       return redirect('/index')
   else:
       return render (request,'login.html')
       
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
