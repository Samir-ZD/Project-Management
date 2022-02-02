from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class User(models.Model):
    # fix name and username logic in ADmin db
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    user_createdAT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Workspace(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace_name = models.CharField(max_length=255)
    workspace_desc = models.TextField(max_length=255)
    workspace_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.workspace_name + " | | " + self.workspace_desc + " | | " + str(self.workspace_created)


class Tasks(models.Model):
    Priority = (
        ('L', 'Low'),  # Blue
        ('M', 'Medium'),  # Yellow
        ('H', 'High'),  # Red
    )
    Status = (
        ('R', 'Running'),  # Blue
        ('S', 'Stuck'),  # Red
        ('D', 'Done'),  # Green
    )

    #Current_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Workspace_FK = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    Workspace_FK = models.OneToOneField(Workspace, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Priority = models.CharField(max_length=1, choices=Priority)
    Status = models.CharField(max_length=1, choices=Status)
    Deadline = models.DateField()

    def __str__(self):
        return self.Title + "  |   |  " + str(self.Workspace_FK.workspace_name)
