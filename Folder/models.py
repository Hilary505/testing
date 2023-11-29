from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class personaldata(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    ward_number = models.IntegerField(default=(3))


    def __str__(self):
        return f"{self.name}:classroom{self.ward_number} on age{self.age}"

class  VCTroom(models.Model):
    topic = models.CharField(max_length=150)
    date = models.DateField(max_length=12,default=())
    start_time = models.TimeField(default=(2))
    VCTroom = models.ForeignKey(personaldata,on_delete=models.CASCADE ,default=(1))

    def __str__(self):
        return f"{self.topic}-{self.date}-{self.start_time} {self.VCTroom}"


