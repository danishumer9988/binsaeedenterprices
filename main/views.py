from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

def index(request):
    return render(request, 'main/index.html')

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        order_details = request.POST.get('order')

        # Send email to owner
        subject = f'New Order from {name}'
        message = f"""
        New Order Details:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        
        Order Details:
        {order_details}
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['binsaeedenterprices@gmail.com'],  # Owner's email
            fail_silently=False,
        )

        # Prepare WhatsApp message
        whatsapp_message = f"New Order from {name} ({phone}):\nEmail: {email}\nOrder Details: {order_details}"
        whatsapp_url = f"https://wa.me/923001234567?text={urllib.parse.quote(whatsapp_message)}"

        # Redirect to WhatsApp with the order details
        return redirect(whatsapp_url)

    return redirect('index')


def shipping_policy_view(request):
    return render(request, 'services/shipping-policy.html')

def returns_refunds_view(request):
    return render(request, 'services/returns-refunds.html')

def privacy_policy_view(request):
    return render(request, 'services/privacy-policy.html')