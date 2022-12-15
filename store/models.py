from django.db import models
from datetime import datetime

class Tour (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del tour')
    adults_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Adultos', help_text='Precio de cada adulto en el tour')
    childs_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Niños', help_text='Precio de cada niño en el tour', null=True, blank=True)
    min_people = models.IntegerField(default=1, verbose_name='Minimo de personas', help_text='Minimo de personas para realizar el tour')
    is_active = models.BooleanField(default=True, verbose_name='Activo', help_text='Si el tour esta activo o no')
    date_start = models.DateField(default=datetime.now(), verbose_name='Fecha de inicio', help_text='Fecha de inicio del tour')
    date_end = models.DateField(default=datetime.now(), verbose_name='Fecha de fin', help_text='Fecha de fin del tour')
    monday = models.BooleanField(default=True, verbose_name='Lunes', help_text='Si el tour se realiza los lunes')
    tuesday = models.BooleanField(default=True, verbose_name='Martes', help_text='Si el tour se realiza los martes')
    wednesday = models.BooleanField(default=True, verbose_name='Miercoles', help_text='Si el tour se realiza los miercoles')
    thursday = models.BooleanField(default=True, verbose_name='Jueves', help_text='Si el tour se realiza los jueves')
    friday = models.BooleanField(default=True, verbose_name='Viernes', help_text='Si el tour se realiza los viernes')
    saturnday = models.BooleanField(default=True, verbose_name='Sabado', help_text='Si el tour se realiza los sabados')
    sunday = models.BooleanField(default=True, verbose_name='Domingo', help_text='Si el tour se realiza los domingos')
    
    def __str__(self):
        return f"{self.name} - Activo: {self.is_active} - Fecha inicio {self.date_start}"
    
    def Meta (self):
        verbose_name_plural = "Tours"
        verbose_name = "Tour"

class Hotels (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del hotel')
    address = models.CharField(max_length=250, verbose_name='Dirección', db_index=True, help_text='Dirección del hotel (opcional)', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def Meta (self):
        verbose_name_plural = "Hoteles"
        verbose_name = "Hotel"
        
class ToursTimes (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Tour', help_text='Tour al que pertenece el horario')
    time_start = models.TimeField(default=datetime.now(), verbose_name='Hora de inicio', help_text='Hora de inicio del tour')
    duration = models.IntegerField(default=1, verbose_name='Duración', help_text='Duración del tour en horas')
    
    def __str__(self):
        return f"{self.name} - Hora de inicio: {self.time_start}"
    
    def Meta (self):
        verbose_name_plural = "Tiempo de tours"
        verbose_name = "Tiempo de tour"
        
class PickUps (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE, verbose_name='Hotel', help_text='Hotel al que pertenece el tour en el horario seleccionado')
    tour_time_id = models.ForeignKey(ToursTimes, on_delete=models.CASCADE, verbose_name='Tour Horario', help_text='Tour seleccionado con horario')
    
    def __str__(self):
        hotel_name = Hotels.objects.get(id=self.hotel_id).name
        tour_name = Tour.objects.get(id=self.tour_time_id.tour_id.id).name
        tour_time = ToursTimes.objects.get(id=self.tour_time_id.id).time_start
        
        return f"Hotel: {hotel_name} - Tour: {tour_name} - Hora: {tour_time}"
    
    def Meta (self):
        verbose_name_plural = "Pick ups en hoteles"
        verbose_name = "Pick up en hotele"
        
class Sales (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True, editable=False, verbose_name='ID', db_index=True)
    id_pick_up = models.ForeignKey(PickUps, on_delete=models.CASCADE, verbose_name='Tour Pick Up', help_text='Tour seleccionado con horario, hotel y pick up', )
    first_name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del cliente')
    last_name = models.CharField(max_length=150, verbose_name='Apellido', db_index=True, help_text='Apellido del cliente')
    email = models.EmailField(max_length=150, verbose_name='Email', db_index=True, help_text='Email del cliente')
    adults_num = models.IntegerField(default=1, verbose_name='Adultos', help_text='Numero de adultos')
    childs_num = models.IntegerField(default=0, verbose_name='Niños', help_text='Numero de niños')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total', help_text='Total de la venta')
    is_paid = models.BooleanField(default=False, verbose_name='Pagado', help_text='Si el tour esta pagado o no')
    date = models.DateTimeField(default=datetime.now(), verbose_name='Fecha', help_text='Fecha del tour')
    
    def __str__(self):
        pick_up_row = PickUps.objects.get(id=self.id_pick_up)
        tour_name = pick_up_row.tour_time_id.tour_id.name
        hotel_name = pick_up_row.hotel_id.name
        tour_time = pick_up_row.tour_time_id.time_start
        return f"{self.first_name} {self.last_name} - Tour: {tour_name} - Hotel {hotel_name}, Hora {tour_time} - Total: {self.total} - Pagado: {self.is_paid}"
    
    def Meta (self):
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"
    