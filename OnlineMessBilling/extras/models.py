from django.db import models

# Create your models here.

class ExtraItem(models.Model):

	item_name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6,decimal_places=2,default=0)

	def __str__(self):
		return self.item_name