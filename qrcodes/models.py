from django.db import models

# Create your models here.
class QRCodes(models.Model):
    name=models.CharField(max_length=35)
    upi_id=models.CharField(max_length=35)
    qrcode=models.ImageField(upload_to='qr_codes')
    time=models.DateTimeField(auto_now_add=True)