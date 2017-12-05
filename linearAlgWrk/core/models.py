from django.db import models
from django.utils import timezone
# Create your models here.

class Input(models.Model):
    input_str = models.TextField()
    queried_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.input_str
