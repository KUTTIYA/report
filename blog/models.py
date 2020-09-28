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

class delivery_note(models.Model):
    no = models.CharField(verbose_name='Delivery Note no.',max_length=10)
    
    def __str__(self):
		    return self.no

class truck_list_report(models.Model):
    list_no = models.CharField(verbose_name='No.', max_length=5)
    delivery_note_no = models.ForeignKey(delivery_note, on_delete=models.CASCADE)
    remark = models.TextField(verbose_name='Remark', null=True)
    destination = models.CharField(verbose_name='Destination',max_length=200)
    delivery_date = models.DateField(verbose_name='Delivery Date',max_length=200)
    
    def __str__(self):
		    return self.list_no

class truck_header_report(models.Model):
    truck_control_no = models.CharField(verbose_name='Truck Control No.', max_length=5)
    truck_no = models.ForeignKey(truck, on_delete=models.CASCADE)
    name = models.ForeignKey(employee, on_delete=models.CASCADE)
    promised_date = models.DateField()
    list_id = models.ForeignKey(truck_list_report, on_delete=models.CASCADE)

    def __str__(self):
		    return self.truck_control_no

class master_package(models.Model):
    package_no = models.CharField(max_length=10)
    package_name = models.CharField(max_length=50)

    def __str__(self):
		    return self.package_name

class dn_list(models.Model):
    list_no = models.IntegerField(verbose_name='No.')
    order_no = models.CharField(verbose_name='Order No.', max_length=5)
    package_no = models.ManyToManyField(master_package,verbose_name='Package Code')
    order = models.IntegerField(verbose_name='Order')
    actual = models.IntegerField(verbose_name='Actual')
    remark = models.TextField(verbose_name='Remark', max_length=200)

    def __str__(self):
		    return str (self.pk)

class dn_header(models.Model):
    dn_no = models.CharField(max_length=5)
    delivery_date = models.DateField(verbose_name='Delivery Date')
    driver_name = models.ForeignKey(employee, on_delete=models.CASCADE)
    promised_date =  models.DateField(verbose_name='Promised Date')
    dn_list = models.ManyToManyField(dn_list)
    def __str__(self):
		    return self.dn_no







    