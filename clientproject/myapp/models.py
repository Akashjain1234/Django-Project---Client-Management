from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    Created_by = models.CharField(max_length=100)
    Created_at = models.DateTimeField()

    def __str__(self):
        return self.name
    

class User(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    





