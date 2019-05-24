from django.conf import settings
from django.db import models
from django.utils import timezone

class Question(models.Model):
    asker = models.TextField()
    title = models.TextField()
    cat = models.TextField()
    order = models.IntegerField()
    content = models.TextField()
    time = models.DateTimeField()
    seen = models.BooleanField()
    response = models.TextField(default=None,blank=True,null=True)
    id = models.AutoField(primary_key=True)

    def submit(self):
        self.time = timezone.now()
        self.seen = False
        self.save()
    
    def reply(self,res):
        # unseen when reply is empty
        self.seen = res != ""
        self.response = res
        self.save()

    def __str__(self):
        return self.title

class Project(models.Model):
    pass

class Author(models.Model):
    name = models.CharField(max_length=4)
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    subject = models.CharField(max_length=50)
    Project = models.OneToOneField(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
