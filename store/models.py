from django.db import models
from django.utils import timezone

class Tour (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del tour')
    location = models.CharField(default="Cancún", max_length=150, verbose_name='Lugar', db_index=True, help_text='Lugar donde se realiza el tour')
    adults_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Adultos', help_text='Precio de cada adulto en el tour')
    childs_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Niños', help_text='Precio de cada niño en el tour (solo si el tour admite niños)', null=True, blank=True)
    min_people = models.IntegerField(default=1, verbose_name='Minimo de personas', help_text='Minimo de personas para realizar el tour')
    duration = models.IntegerField(default=1, verbose_name='Duración', help_text='Duración del tour en horas')
    is_active = models.BooleanField(default=True, verbose_name='Activo', help_text='Si el tour esta activo o no')
    date_start = models.DateField(default=timezone.now, verbose_name='Fecha de inicio', help_text='Fecha de inicio del tour')
    date_end = models.DateField(default=timezone.now, verbose_name='Fecha de fin', help_text='Fecha de fin del tour')
    monday = models.BooleanField(default=True, verbose_name='Lunes', help_text='Si el tour se realiza los lunes')
    tuesday = models.BooleanField(default=True, verbose_name='Martes', help_text='Si el tour se realiza los martes')
    wednesday = models.BooleanField(default=True, verbose_name='Miercoles', help_text='Si el tour se realiza los miercoles')
    thursday = models.BooleanField(default=True, verbose_name='Jueves', help_text='Si el tour se realiza los jueves')
    friday = models.BooleanField(default=True, verbose_name='Viernes', help_text='Si el tour se realiza los viernes')
    saturnday = models.BooleanField(default=True, verbose_name='Sabado', help_text='Si el tour se realiza los sabados')
    sunday = models.BooleanField(default=True, verbose_name='Domingo', help_text='Si el tour se realiza los domingos')
    
    def __str__(self):
        return f"{self.name} - {self.location}"
    
    def Meta (self):
        verbose_name_plural = "Tours"
        verbose_name = "Tour"

class Hotel (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del hotel')
    address = models.CharField(max_length=250, verbose_name='Dirección', db_index=True, help_text='Dirección del hotel (opcional)', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def Meta (self):
        verbose_name_plural = "Hoteles"
        verbose_name = "Hotel"
        
class TourTime (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Tour', help_text='Tour al que pertenece el horario')
    time_start = models.TimeField(default=timezone.now, verbose_name='Hora de inicio', help_text='Hora de inicio del tour')
    duration = models.IntegerField(default=1, verbose_name='Duración', help_text='Duración del tour en horas')
    
    def __str__(self):
        tour_name = Tour.objects.get(id=self.tour_id.id).name
        tour_location = Tour.objects.get(id=self.tour_id.id).location
        return f"{tour_name} - {tour_location} - Hora de inicio: {self.time_start}"
    
    def Meta (self):
        verbose_name_plural = "Tiempo de tours"
        verbose_name = "Tiempo de tour"
        
class PickUp (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Hotel', help_text='Hotel al que pertenece el tour en el horario seleccionado')
    tour_time_id = models.ForeignKey(TourTime, on_delete=models.CASCADE, verbose_name='Tour Horario', help_text='Tour seleccionado con horario')
    time = models.TimeField(default=timezone.now, verbose_name='Hora de recogida', help_text='Hora de recogida del tour')
    
    def __str__(self):
        hotel_name = self.hotel_id.name
        tour_name = self.tour_time_id.tour_id.name
        tour_time = self.tour_time_id.time_start
        
        return f"Hotel: {hotel_name} - Tour: {tour_name} - Hora: {tour_time}"
    
    def Meta (self):
        verbose_name_plural = "Pick ups en hoteles"
        verbose_name = "Pick up en hotele"
        
class Sale (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    id_pick_up = models.ForeignKey(PickUp, on_delete=models.CASCADE, verbose_name='Tour Pick Up', help_text='Tour seleccionado con horario, hotel y pick up', )
    first_name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del cliente')
    last_name = models.CharField(max_length=150, verbose_name='Apellido', db_index=True, help_text='Apellido del cliente')
    email = models.EmailField(max_length=150, verbose_name='Email', db_index=True, help_text='Email del cliente')
    adults_num = models.IntegerField(default=1, verbose_name='Adultos', help_text='Numero de adultos')
    childs_num = models.IntegerField(default=0, verbose_name='Niños', help_text='Numero de niños')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total', help_text='Total de la venta')
    is_paid = models.BooleanField(default=False, verbose_name='Pagado', help_text='Si el tour esta pagado o no')
    tour_date = models.DateTimeField(default=timezone.now, verbose_name='Fecha tour', help_text='Fecha del tour')
    buy_date = models.DateTimeField(default=timezone.now, verbose_name='Fecha venta', help_text='Fecha de venta')
    
    def __str__(self):
        tour_name = self.id_pick_up.tour_time_id.tour_id.name
        hotel_name = self.id_pick_up.hotel_id.name
        tour_time = self.id_pick_up.tour_time_id.time_start
        return f"{self.first_name} {self.last_name} - Tour: {tour_name} - Hotel {hotel_name}, Hora {tour_time} - Total: {self.total} - Pagado: {self.is_paid}"
    
    def Meta (self):
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"
    