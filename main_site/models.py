from django.conf import settings
from django.db import models
from django.utils import timezone

class Question(models.Model):
    asker = models.TextField()
    title = models.TextField()
    content = models.TextField()
    time = models.DateTimeField()
    seen = models.BooleanField()
    response = models.TextField(default=None,blank=True,null=True)
    id = models.AutoField(primary_key=True)

    def submit(self):
        self.time = timezone.now()
        self.seen = False
        self.save()

    def __str__(self):
        return self.title