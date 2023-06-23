from django.db import models

# Create your models here.
class Report(models.Model):
    latitude=models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)
    time=models.DateTimeField()
    incident=models.CharField(max_length=50)
    sy=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f" {self.incident}" 

