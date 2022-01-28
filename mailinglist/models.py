from django.db import models

# Create your models here.
class Contact(models.Model):
    """Подписка по email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "Адрес email"
        verbose_name_plural = "Адреса email подписчиков"

    def __str__(self):
        return self.email