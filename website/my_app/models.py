from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    description =models.TextField()
    date =models.DateTimeField()
    PRIORITY_CHOICES = (
        ("High","High"),
        ("Medium","Medium"),
        ("Low","Low")
    )
    priority =models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=name
    )


    def __str__(self):
        return self.name
