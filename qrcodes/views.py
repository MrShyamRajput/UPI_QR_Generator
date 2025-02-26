from django.shortcuts import render, HttpResponse
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from .models import QRCodes 
from django.contrib import messages

def generate_QR(request):
    if request.method == "POST":
        name = request.POST.get('name')
        upi_id = request.POST.get("upi_id")

        # Generate UPI Payment URL
        url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

        # Generate QR Code
        qr_code = qrcode.make(url)

        # Convert QR Code to Bytes
        buffer = BytesIO()
        qr_code.save(buffer, format="PNG")

        # Create Django file object
        file_name = f"qr_{name}.png"
        qr_image = ContentFile(buffer.getvalue(), name=file_name)

        # Saving in Database
        try:
            QRCodes.objects.create(name=name, upi_id=upi_id, qrcode=qr_image)
            messages.success(request, f"QR Code for {name} has been successfully generated!")
        except:
            messages.success(request, f"Error during generating QR.. , Try again!")

    dic={
        'qr_codes':QRCodes.objects.all().order_by('-id')
    }
    
    return render(request, "display.html",dic)
