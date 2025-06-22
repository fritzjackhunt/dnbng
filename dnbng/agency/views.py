from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['compliance@veece.xyz'],
            fail_silently = False,
        )

        return render(request, 'dnbng/index.html', {'contact_fname' : contact_fname})

    else:
        return render(request, 'dnbng/index.html')