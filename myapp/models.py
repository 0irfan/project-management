from django.db import models


# Create your models here.
class ProjectInformation(models.Model):
    start_date=models.DateField()
    End_date=models.DateField()
    CURRENCIES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('Pak','pakistan rupees')
        #Add more as you needed
    )
    Total_cost=models.DecimalField(max_digits=20,decimal_places=2)
    currencey=models.CharField(max_length=3,choices=CURRENCIES)
    Resource_Name=models.CharField(max_length=20)
    Resource_position=models.CharField(max_length=50)
    Total_cost_resources=models.DecimalField(max_digits=20,decimal_places=2)
    option_period=models.IntegerField()
    project_description=models.CharField(max_length=500)

class Deliverable(models.Model):
    Activity=models.CharField(max_length=500)
    Activity_description=models.CharField(max_length=1000)

class projectAuthority(models.Model):
    Contact_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    fax_number=models.IntegerField()
    work_address=models.CharField(max_length=255)
 

        


