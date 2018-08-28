from django.db import models
from django.contrib.auth.models import User

from extras.models import *

# Create your models here.
class Transaction(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	regNum = models.CharField(max_length=10)
	item = models.ForeignKey(ExtraItem,on_delete=models.PROTECT)
	number = models.IntegerField(default = 1)
	price = models.DecimalField(default = 0.00, max_digits= 12, decimal_places=2)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.regNum} - {self.item} - {self.price} on {self.date}'


