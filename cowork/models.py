from django.db import models

# Create your models here.


class Tenants(models.Model):
    id = models.AutoField()
    tenant_type = models.CharField(max_length=255)             
    phone = models.CharField(max_length=15)                  
    email = models.CharField(max_length=255)                  

class Individuals(models.Model):
    id = models.AutoField()
    tenant_id = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    surname = models.CharField(max_lenght=255)
    name = models.CharField(max_lenght=255)
    patronymic = models.CharField(max_lenght=255)
    passport_series = models.IntegerField(max_length=4)
    passport_number = models.IntegerField(max_length=6)

class Entits(models.Model):
    id = models.AutoField()
    tenant_id = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    company_name = models.TextField()
    inn = models.IntegerField(max_length=10)
    ogrn = models.IntegerField(max_length=13)
    address= models.TextField()

class Individual_entrepreneurs(models.Model):
    id = models.AutoField()
    tenant_id = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    surname = models.CharField(max_lenght=255)
    name = models.CharField(max_lenght=255)
    patronymic = models.CharField(max_lenght=255)
    address = models.TextField()
    inn = models.IntegerField(max_length=12)
    ogrnip = models.IntegerField(max_length=15)

class Premises(models.Model):
    id = models.AutoField()
    premise_type = models.ForeignKey('Premises_types', on_delete=models.CASCADE)
    square = models.IntegerField()
    number_of_workplfces = models.IntegerField()
    address = models.TextField()

class Premises_types(models.Model):
    id = models.AutoField()
    type = models.CharField(max_length=255)

class Rates(models.Model):
    id = models.AutoField()
    premise_type = models.ForeignKey('Premises_types', on_delete=models.CASCADE)
    rental_time = models.CharField(max_length=255)
    fixed_or_non_fixed = models.BooleanField(default=False)
    price = models.IntegerField()

class Additional_services(models.Model):
    id = models.AutoField()
    name = models.CharField(max_lenght=255)
    description = models.TextField()
    price = models.IntegerField()

class Discount_cards(models.Model):
    id = models.AutoField()
    tenant_id = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    discount = models.IntegerField()

class Deals(models.Model):
    id = models.AutoField()
    tenant_id = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    rate_id = models.ForeignKey('Rates', on_delete=models.CASCADE)
    premise_id = models.ForeignKey('Premises', on_delete=models.CASCADE)
    additional_services = models.ForeignKey('Additional_services', on_delete=models.CASCADE)
    start_of_lease = models.DateField()         #доп опции в скобках ???
    end_of_lease = models.DateField()
    date_of_signing_the_deal = models.DateField()
    discount = models.ForeignKey('Discount_cards', on_delete=models.CASCADE)
    total_price = models.IntegerField()