from django.db import models


class Sale(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    client_email = models.EmailField(verbose_name='Correo del cliente')
    client_first_name = models.CharField(verbose_name='Nombre del cliente')
    client_last_name = models.CharField(verbose_name='Apellido del cliente')
    passenger_number = models.IntegerField(verbose_name='Número de pasajeros')
    hotel = models.CharField(verbose_name='Hotel')
    arriving_date = models.DateField(verbose_name='Fecha de llegada')
    arriving_time = models.TimeField(verbose_name='Hora de llegada')
    arriving_airline = models.CharField(verbose_name='Aerolínea de llegada')
    arriving_flight = models.CharField(verbose_name='Vuelo de llegada')
    departing_date = models.DateField(verbose_name='Fecha de salida')
    departing_time = models.TimeField(verbose_name='Hora de salida')
    departing_airline = models.CharField(verbose_name='Aerolínea de salida')
    departing_flight = models.CharField(verbose_name='Vuelo de salida')
    reservation_date_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha y hora de la reservación'
    )
    total_price = models.FloatField(verbose_name='Precio total')
    is_paid = models.BooleanField(verbose_name='Está pagado', default=False)