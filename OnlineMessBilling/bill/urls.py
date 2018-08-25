from django.urls import path,include

from . import views

urlpatterns = [

	path('',views.home),
	path('bill',views.bill),
	path('admin',views.admin_home),
	path('admin/add',views.add_transaction),
	path('admin/prev',views.transactions),
	path('admin/transaction_delete/<int:order_id>/', views.remove_order),
	
]