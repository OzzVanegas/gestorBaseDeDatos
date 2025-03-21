from django.db import models

# Create your models here.

# Transaction Type Model
class TransactionType(models.Model):  
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

# Property Type Model
class PropertyType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

# State/Department Model
class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# City Model
class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# District Model
class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# TyprOwner Model
class TyprOwner(models.Model):
    id = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=50)

    def __str__(self):
        return self.Type


# Owner Model
class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    owner_type = models.ForeignKey(TyprOwner, on_delete=models.CASCADE)  # Relacionamos Owner con TyprOwner

    def __str__(self):
        return self.name


# Property Model
class Property(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.IntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    price_per_sq_mt = models.DecimalField(max_digits=10, decimal_places=10)
    stratum = models.CharField(max_length=9)
    address = models.CharField(max_length=45, default="Unknown")
    floor = models.CharField(max_length=20, null=True, blank=True)
    rooms = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=45, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    # Foreign Keys
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)  
    district = models.ForeignKey(District, on_delete=models.CASCADE)  
    def __str__(self):
        return self.name


    def delete(self, using=None, keep_parents=False):
        if hasattr(self, 'image') and self.image:
            self.image.storage.delete(self.image.name)
        super().delete()
