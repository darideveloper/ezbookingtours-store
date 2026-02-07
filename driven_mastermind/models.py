from django.db import models


class Sale(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    client_email = models.EmailField(verbose_name="Correo del cliente")
    client_first_name = models.CharField(
        max_length=255, verbose_name="Nombre del cliente"
    )
    client_last_name = models.CharField(
        max_length=255, verbose_name="Apellido del cliente"
    )
    passenger_number = models.IntegerField(verbose_name="Número de pasajeros")
    hotel = models.CharField(max_length=255, verbose_name="Hotel")
    arriving_date = models.DateField(
        verbose_name="Fecha de llegada", null=True, blank=True
    )
    arriving_time = models.TimeField(
        verbose_name="Hora de llegada", null=True, blank=True
    )
    arriving_airline = models.CharField(
        max_length=255, verbose_name="Aerolínea de llegada", null=True, blank=True
    )
    arriving_flight = models.CharField(
        max_length=255, verbose_name="Vuelo de llegada", null=True, blank=True
    )
    departing_date = models.DateField(
        verbose_name="Fecha de salida", null=True, blank=True
    )
    departing_time = models.TimeField(
        verbose_name="Hora de salida", null=True, blank=True
    )
    departing_airline = models.CharField(
        max_length=255, verbose_name="Aerolínea de salida", null=True, blank=True
    )
    departing_flight = models.CharField(
        max_length=255, verbose_name="Vuelo de salida", null=True, blank=True
    )
    reservation_date_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha y hora de la reservación"
    )
    total_price = models.FloatField(verbose_name="Precio total")
    is_paid = models.BooleanField(verbose_name="Está pagado", default=False)
