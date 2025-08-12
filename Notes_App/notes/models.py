from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title