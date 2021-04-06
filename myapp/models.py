from django.db import models
class myapp(models.Model):
    eid = models.CharField(max_length=100)
    ename = models.CharField(max_length=100)
    eaddress = models.CharField(max_length=100)
    egender = models.CharField(max_length=100)
    ephoneno = models.CharField(max_length=100)
    



