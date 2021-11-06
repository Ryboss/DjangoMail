from django.shortcuts import render
from .forms import UserForm
import smtplib
import email.message
# Create your views here.
def index(request):
    submitbutton = request.POST.get("submit")

    name = ''
    phone = ''
    message = ''
    emailvalue = ''
    form = UserForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        phone = form.cleaned_data.get("phone")
        message = form.cleaned_data.get("message")
        emailvalue = form.cleaned_data.get("email")

    context = {
        'form': form,
        'name': name,
        'phone':phone,
        'submitbutton': submitbutton,
        'emailvalue':emailvalue,
        'message': message
    
    }
    email_content = f"""
    <html>
    <meta charset = "UTF-8">

    <body>
    <p>Name recipient {context['name']}</p>
    <p>Phone recipient {context['phone']}</p>
    <p>Message {context['message']}</p>
    </body>
    </html>"""
    msg = email.message.Message()
    msg['From'] = 'Your gmail'
    msg['To'] = context['emailvalue']
    password = 'Your password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    s.sendmail(msg['From'], msg['To'], msg.as_string())
    return render(request,'send/index.html', context)