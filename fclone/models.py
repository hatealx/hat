from django.db import models

class LoginRecord(models.Model):
    contact = models.CharField(max_length=100, verbose_name="Email or Phone")
    password = models.CharField(max_length=100, verbose_name="Password")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact
