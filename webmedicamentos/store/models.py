from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    idusuario=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    contrasena=models.CharField(max_length=20)
    
    
class cliente(models.Model):
    
    idcliente=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    telefono=models.CharField(max_length=15)
    dirección=models.CharField(max_length=30)
    idusuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
    
   
class categoria(models.Model):
    idcategoria=models.IntegerField(primary_key=True)
    descripcion=models.CharField(max_length=50)
    
class producto(models.Model):
     idproducto=models.IntegerField(primary_key=True)
     precio=models.floatField()
     stock=models.IntegerField()
     idcategoria=models.ForeignKey(categoria,on_delete=models.CASCADE)

class proveedor(models.Model):
     idproveedor=models.IntegerField(primary_key=True)
     nombre=models.CharField(max_length=40)
     telefono=models.CharField(max_length=40)

class orden_pedido(models.Model):
    
    idproducto=models.ForeignKey(producto,on_delete=models.CASCADE)
    idproveedor=models.ForeignKey(proveedor,on_delete=models.CASCADE)
    fecha=models.DateIntegerField()
    cantidad=models.IntegerField()

class factura(models.Model):
     num_factura=models.AutoField(primary_key=True)
     fecha=models.DateIntegerField()
     idusuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
     idcliente=models.ForeignKey(cliente,on_delete=models.CASCADE)
     iduproducto=models.IntegerField()
     cantidad=models.IntegerField()
     precio_total=models.floatField()