from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 55)
    subject = models.CharField(max_length = 55)
    movingfrom = models.CharField(max_length = 55)
    movingto = models.CharField(max_length = 55)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self,name
