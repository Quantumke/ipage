from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from .forms import ContactDetails, ProspectusForm
from .models import contactus
# Create your views here.

def home(request):
    context= RequestContext(request)
    return render_to_response('index.html',{}, context_instance=context )

def contactsave(request):
    context=RequestContext(request)
    if request.method=='POST':
        form = ContactDetails(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            message=form.cleaned_data['message']
            to='info@i254.co.ke'
            template_html = 'email/admin_mail.html'
            html_content = render_to_string(template_html, {})
            # form.save()
            mail = EmailMultiAlternatives(
                subject="New Enquiry",
                body="There's a new application.",
                from_email=email,
                to=[to],
                headers={"Reply-To": "no-reply-support@i254.co.ke"},

            )
            mail.attach_alternative(html_content.format(**locals()), "text/html")
            mail.send()
            admin_template = 'email/feedback_response.html'
            template_content = render_to_string(admin_template, {})
            client_reciept = EmailMultiAlternatives(
                subject="Thank you for your feedback",
                body="We have recieved your feedback and we will get back to you shortly.",
                from_email=to,
                to=[email],
                headers={"Reply-To": "no-reply-support@i254.co.ke"},

            )
            client_reciept.attach_alternative(template_content.format(**locals()), "text/html")

            client_reciept.send()

            # print '*******It worked*********'
            return  HttpResponseRedirect('/')

    return render_to_response('index.html', {}, context_instance=context)


def prospectsave(request):
    context=RequestContext(request)
    if request.method=='POST':
        form= ProspectusForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            package = form.cleaned_data['package']
            description=form.cleaned_data['description']
            to = 'info@i254.co.ke'
            template_html = 'email/admin_prospects.html'
            html_content = render_to_string(template_html, {})
            # form.save()
            mail = EmailMultiAlternatives(
                subject="New Prospect",
                body="There's a new application.",
                from_email=email,
                to=[to],
                headers={"Reply-To": "no-reply-support@i254.co.ke"},

            )
            mail.attach_alternative(html_content.format(**locals()), "text/html")

            mail.send()
            template_reciept = 'email/prospect_response.html'
            html_reciept = render_to_string(template_reciept, {})
            email_reciept = EmailMultiAlternatives(
                subject="Thank you for your request",
                body="Please tell us more, for us to serve you better.",
                from_email=to,
                to=[email],
                headers={"Reply-To": "no-reply-support@i254.co.ke"},

            )
            email_reciept.attach_alternative(html_reciept.format(**locals()), "text/html")

            email_reciept.send()
            return HttpResponseRedirect('/')
    return render_to_response('index.html', {}, context_instance=context)

