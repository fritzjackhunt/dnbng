from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        subject = f"Message from {contact_fname} {contact_lname}"
        body = f"""
        You received a message from your contact form.

        Name: {contact_fname} {contact_lname}
        Email: {contact_email}

        Message:
        {contact_message}
        """

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Must match your Gmail
            to=['info@dnbng.xyz'],
            reply_to=[contact_email],  # Reply goes to the user
        )
        email.send(fail_silently=False)

        return render(request, 'dnbng/index.html', {'contact_fname': contact_fname})

    return render(request, 'dnbng/index.html')
