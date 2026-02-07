from django.db import models


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    transport_type = models.CharField(
        max_length=150, verbose_name="Tipo de transporte", default=""
    )
    name = models.CharField(max_length=150, verbose_name="Nombre")
    last_name = models.CharField(max_length=150, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo", default="")
    passengers = models.IntegerField(verbose_name="Pasajeros", default=1)
    price = models.IntegerField(verbose_name="Precio", default=0)
    arriving = models.TextField(verbose_name="Info de Llegada", default="")
    departing = models.TextField(verbose_name="Info de Salida", default="")
    transport_vehicule = models.CharField(
        max_length=150, verbose_name="Vehiculo de transporte", default=""
    )
    sale_done = models.BooleanField(
        verbose_name="Venta realizada",
        default=False,
    )

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.transport_type}"

    class Meta:
        verbose_name = "Venta (Digital Realty)"
        verbose_name_plural = "Ventas (Digital Realty)"
