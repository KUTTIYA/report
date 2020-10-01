from django.conf import settings
from django.db import models

class department(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    
    def __str__(self):
		    return self.name

class employee(models.Model):
    name = models.CharField(verbose_name='Name',max_length=50)
    surname = models.CharField(verbose_name='Surname',max_length=50)
    address = models.CharField(verbose_name='Address',max_length=100)
    telephone = models.CharField(verbose_name='Telephone',max_length=10)
    position = models.CharField(verbose_name='Position',max_length=50)
    department = models.OneToOneField(department, on_delete=models.CASCADE, verbose_name='Department')
   
    def __str__(self):
		    return self.name

class truck_type(models.Model):
    name = models.CharField(verbose_name='Type',max_length=50)
    
    def __str__(self):
		    return self.name

class truck(models.Model):
    truck_no = models.CharField(verbose_name='Truck no.',max_length=10)
    truck_type = models.ForeignKey(truck_type, on_delete=models.CASCADE, verbose_name='Type')
    
    def __str__(self):
		    return self.truck_no

class master_package(models.Model):
    package_no = models.CharField(max_length=10)
    package_name = models.CharField(max_length=50)

    def __str__(self):
		    return self.package_name

class dn_list_report(models.Model):
    list_no = models.CharField(verbose_name='No.',max_length=5)
    order_no = models.CharField(verbose_name='Order No.', max_length=5)
    package_no = models.ForeignKey(master_package,verbose_name='Package Code', on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name='Order')
    actual = models.IntegerField(verbose_name='Actual')
    remark = models.TextField(verbose_name='Remark', max_length=200)

    def __str__(self):
		    return self.list_no

class dn_header_report(models.Model):
    dn_no = models.CharField(max_length=20)
    delivery_date = models.DateField(verbose_name='Delivery Date')
    truck_no = models.ForeignKey(truck, on_delete=models.CASCADE)
    trip_no = models.CharField(max_length=10)
    driver_name = models.ForeignKey(employee, on_delete=models.CASCADE)
    promised_date =  models.DateField(verbose_name='Promised Date')
    dn_list = models.ManyToManyField(dn_list_report)

    def __str__(self):
		    return self.dn_no

class truck_list_report(models.Model):
    list_no = models.CharField(verbose_name='No.', max_length=5)
    delivery_note_no = models.ForeignKey(dn_header_report, verbose_name='Delivery Note no.' , on_delete=models.CASCADE)
    remark = models.TextField(verbose_name='Remark', null=True)
    destination = models.CharField(verbose_name='Destination',max_length=200)
    delivery_date = models.DateField(verbose_name='Delivery Date',max_length=200)
    
    def __str__(self):
		    return self.list_no

class truck_header_report(models.Model):

    truck_control_no = models.CharField(verbose_name='Truck Control No.', max_length=20)
    truck_no = models.ForeignKey(truck, on_delete=models.CASCADE)
    driver_name = models.ForeignKey(employee, on_delete=models.CASCADE)
    promised_date = models.DateField(verbose_name='Promised Date')
    list_id = models.ManyToManyField(truck_list_report)

    def __str__(self):
		    return self.truck_control_no

class po_header_report(models.Model):
    po_no = models.CharField(verbose_name='Purchase Order No.', max_length=20)
    
    def __str__(self):
		    return self.po_no

class supplier(models.Model):
    sup_no = models.CharField(verbose_name='Supplier No.', max_length=20)
    sup_name = models.CharField(verbose_name='Name', max_length=50)

    def __str__(self):
		    return self.sup_name

class replacement_list_report(models.Model):
    list_no = models.CharField(verbose_name='No.', max_length=5)
    dn_no = models.ForeignKey(dn_header_report, verbose_name='Ref. DN No.' , on_delete=models.CASCADE)
    po_no = models.ForeignKey(po_header_report, verbose_name='MST PO No.' , on_delete=models.CASCADE)
    sup_no = models.ForeignKey(supplier, verbose_name='Supplier Code' , on_delete=models.CASCADE)
    package_no = models.ForeignKey(master_package,verbose_name='Package Code', on_delete=models.CASCADE)
    replacement = models.IntegerField(verbose_name='Replacement Qty.')
    receive = models.IntegerField(verbose_name='Receive Qty.')
    remark = models.TextField(verbose_name='Remark', null=True)
    
    def __str__(self):
		    return self.list_no

class replacement_header_report(models.Model):
    replacement_no = models.CharField(max_length=20)
    replacement_date = models.DateField(verbose_name='Replacement Date')
    replacement_list = models.ManyToManyField(replacement_list_report)

    def __str__(self):
		    return self.replacement_no





    