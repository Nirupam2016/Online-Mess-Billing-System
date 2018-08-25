from django import forms
from django.contrib.auth.models import User

from authentication.views import *
from authentication.models import Userprofile
from extras.models import ExtraItem

reg = Userprofile.objects.all()
items = ExtraItem.objects.all()

list1 = [('-','---SELECT---')]
list2 = [('-','---SELECT---')]



for item in items:
	list2.append((item.item_name,item.item_name))

for r in reg:
	u = User.objects.filter(username = r.user)
	if not is_member(u.first()):
		list1.append((r.regNum,r.regNum))

class AddTransactionForm(forms.Form):

	regnum = forms.CharField(
		
        required = True,
        label = 'Registration No.',
        max_length = 32,
        widget = forms.Select(
        	choices = list1,
            attrs={
            "class": "form-control",
            }
        )
    )
	item = forms.CharField(
		
        required = True,
        label = 'Item',
        max_length = 32,
        widget = forms.Select(
        	choices = list2,
            attrs={
            "class": "form-control",
            }
        )
    )
