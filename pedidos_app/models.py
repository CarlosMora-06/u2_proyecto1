from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=80,unique=True)

    class meta:
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True)
    precio = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField()
    activo = models.BooleanField(default=False,null=True)
    creado = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=20)

    class meta:
        verbose_name_plural = "Productos"
        ordering = ["Nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.precio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    class meta:
        verbose_name_plural = "Clientes"
        ordering = ["Nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.email}"



class Pedido(models.Model):
    fechar = models.DateTimeField()
    pagado = models.BooleanField()

    #1 -N: Un cliente realiza muchos pedidos
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ["fechar"]

    def __str__(self):
        return f"{self.fechar} {self.cliente}"

class Item(models.Model):
    precio_initario = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Items"
        # ordering = [""]

        def __str__(self):
            return f"{self.precio_initario} {self.cantidad} {self.pedido} {self.producto}"