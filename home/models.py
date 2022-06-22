from django.db import models


class Contact(models.Model):
    Name = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=50)
    Subject = models.CharField(max_length=100, null=True)
    Message = models.TextField()
    Date = models.DateTimeField()

    def __str__(self):
        if self.Name:
            return self.Name
        return self.Email
