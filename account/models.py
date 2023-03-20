from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender = (
    ('MALE','MALE'),('FEMALE','FEMLE')
)

marital_status = (
    ('SINGLE', 'SINGLE'), ('MARRIED','MARRIED'),
)
state_of_origin = (
    ('abia', 'abia'), ('adamawa','adamawa'),('akwa-ibom','akwa-ibom'),
)

class profile (models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20)
    DoB = models.DateField()
    gender = models.CharField(max_length=12,choices=gender)
    state_of_origin= models.CharField(max_length=10,choices=state_of_origin,default='')
    lga_of_origin = models.CharField(max_length=100,default='')
    scheme_name = models.CharField(max_length=10,blank=True,null=True,default='')
    phone_number = models.CharField(max_length=11)
    year_of_application = models.CharField(max_length=4)
    profile_pics = models.ImageField(upload_to='profile_pics', default='')
    address = models.TextField(max_length=200)
    marital_status = models.CharField(max_length=15,choices=marital_status)


    def __str__(self) -> str:
        return f'{self.User}'
