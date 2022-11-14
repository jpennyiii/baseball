from django.db import models
from django.utils import timezone
import datetime
class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_at=models.DateTimeField(auto_now=True)
		
	class Meta:
		abstract = True
		
class Position(BaseModel):
	description = models.CharField(max_length=100)

class Person(BaseModel):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	height = models.DecimalField(max_digits=10, decimal_places=5,null=True)
	weight = models.DecimalField(max_digits=10, decimal_places=5,null=True)

class Club(BaseModel):
	name = models.CharField(max_length=100)
	coach = models.ForeignKey(Person, on_delete=models.CASCADE)
	latitude=models.DecimalField(max_digits=22,decimal_places=16,null=True,blank=True)
	latitude=models.DecimalField(max_digits=22,decimal_places=16,null=True,blank=True)
	
class Play(BaseModel):
	player = models.ForeignKey(Person, on_delete=models.CASCADE)
	team = models.ForeignKey(Club, on_delete=models.CASCADE)
	latitude=models.DecimalField(max_digits=22,decimal_places=16,null=True,blank=True)
	latitude=models.DecimalField(max_digits=22,decimal_places=16,null=True,blank=True)

	
# 
# latitude=models.DecimalField(max_digits=22,decimal_places=16,null=True,blank=True)
# isActive=models.BooleanField(default=False, verbose_name="Zoning Fee")
# birthdate=models.DateField(default=timezone.now, blank=True)
# coach = models.ForeignKey(Person, on_delete=models.CASCADE)

# Create your models here.
