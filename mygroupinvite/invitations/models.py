from django.db import models

class Invitation(models.Model):
    roll_number = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    whatsapp_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
