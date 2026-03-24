from django.db import models
from django.utils import timezone
from ezbookingtours_store.tools import parse_dt

class Sale (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, default='')
    last_name = models.CharField(max_length=150, verbose_name='Apellido', db_index=True, default='')
    sale_datetime = models.DateTimeField(verbose_name='Fecha de venta', db_index=True, default=timezone.now)
    is_paid = models.BooleanField(verbose_name='Pagado', default=False)
    phone = models.CharField(max_length=150, verbose_name='Teléfono', db_index=True, default='')
    email = models.EmailField(verbose_name='Email', default='')
    stripe_data = models.JSONField(verbose_name='Datos de Stripe', default=dict, blank=True, null=True)

    # Structured fields
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Hotel')
    transport_type = models.ForeignKey('Transport', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Tipo de transporte')
    hotel_name = models.CharField(max_length=150, default='', verbose_name='Nombre del hotel (Personalizado)')
    passengers = models.IntegerField(default=1, verbose_name='Pasajeros')
    
    # Arriving Details
    arriving_date = models.DateField(null=True, blank=True, verbose_name='Fecha de llegada')
    arriving_time = models.TimeField(null=True, blank=True, verbose_name='Hora de llegada')
    arriving_airline = models.CharField(max_length=150, default='', verbose_name='Aerolínea de llegada')
    arriving_flight = models.CharField(max_length=150, default='', verbose_name='Vuelo de llegada')
    
    # Departing Details
    departing_date = models.DateField(null=True, blank=True, verbose_name='Fecha de salida')
    departing_time = models.TimeField(null=True, blank=True, verbose_name='Hora de salida')
    departing_airline = models.CharField(max_length=150, default='', verbose_name='Aerolínea de salida')
    departing_flight = models.CharField(max_length=150, default='', verbose_name='Vuelo de salida')
    
    def __str__ (self):
        return f"{self.name} {self.last_name} - {self.transport_type or 'Sin transporte'} - {self.sale_datetime.date()}"
    
    @property
    def total_price(self):
        """
        Calculates the total price of the sale based on transport and hotel.
        """
        total = 0
        if self.transport_type:
            total += self.transport_type.price
        if self.hotel:
            total += self.hotel.extra_price
        return total

    @classmethod
    def from_payload(cls, json_body):
        """
        Creates (but does not save) a Sale instance from a raw payload.
        Returns (sale_instance, details_objs)
        """
        name = json_body.get("name", "")
        last_name = json_body.get("last-name", "")
        stripe_data = json_body.get("stripe-data", {})
        phone = json_body.get("phone", "")
        email = json_body.get("email", "")

        # Parse booking details from description
        stripe_data_key = list(stripe_data.keys())[0] if stripe_data else None
        description = stripe_data[stripe_data_key].get("description", "") if stripe_data_key else ""
        details_lines = description.split(",")
        
        booking_details = {
            "passengers": 1,
            "hotel_name": "",
            "arriving_date": None,
            "arriving_time": None,
            "arriving_airline": "",
            "arriving_flight": "",
            "departing_date": None,
            "departing_time": None,
            "departing_airline": "",
            "departing_flight": "",
        }
        
        airline_count = 0
        flight_count = 0
        details_objs = []

        # Field mapping for simple parsing
        SIMPLE_MAPPING = {
            "Passengers": ("passengers", int),
            "Arriving date": ("arriving_date", lambda v: parse_dt(v, ["%Y-%m-%d"])),
            "Arriving time": ("arriving_time", lambda v: parse_dt(v, ["%H:%M"])),
            "Departing date": ("departing_date", lambda v: parse_dt(v, ["%Y-%m-%d"])),
            "Departing time": ("departing_time", lambda v: parse_dt(v, ["%H:%M"])),
        }
        
        # Sequence mapping for duplicate labels
        SEQUENCE_MAPPING = {
            "Airline": ["arriving_airline", "departing_airline"],
            "Flight": ["arriving_flight", "departing_flight"],
        }
        counts = {"Airline": 0, "Flight": 0}

        for line in details_lines:
            line_split = line.split(":")
            if len(line_split) > 1:
                key = line_split[0].strip()
                value = ":".join(line_split[1:]).strip()
                details_objs.append({"name": key, "value": value})
                
                # Logic Implementation
                if key in SIMPLE_MAPPING:
                    attr, func = SIMPLE_MAPPING[key]
                    try: booking_details[attr] = func(value)
                    except: pass
                elif key in SEQUENCE_MAPPING:
                    idx = counts[key]
                    if idx < len(SEQUENCE_MAPPING[key]):
                        booking_details[SEQUENCE_MAPPING[key][idx]] = value
                        counts[key] += 1
                elif key == "Hotel" and value.lower() != "other":
                    booking_details["hotel_name"] = value
                elif key == "Hotel name":
                    booking_details["hotel_name"] = value

        hotel_obj = None
        hotel_name_custom = booking_details["hotel_name"]
        if hotel_name_custom:
            hotel_obj = Hotel.objects.filter(name=hotel_name_custom).first()
            if hotel_obj:
                hotel_name_custom = ""
            
        transport_obj = None
        if stripe_data_key:
            transport_obj = Transport.objects.filter(name=stripe_data_key).first()

        sale = cls(
            name=name,
            last_name=last_name,
            stripe_data=stripe_data,
            phone=phone,
            email=email,
            hotel=hotel_obj,
            transport_type=transport_obj,
            hotel_name=hotel_name_custom,
            passengers=booking_details["passengers"],
            arriving_date=booking_details["arriving_date"],
            arriving_time=booking_details["arriving_time"],
            arriving_airline=booking_details["arriving_airline"],
            arriving_flight=booking_details["arriving_flight"],
            departing_date=booking_details["departing_date"],
            departing_time=booking_details["departing_time"],
            departing_airline=booking_details["departing_airline"],
            departing_flight=booking_details["departing_flight"],
        )
        return sale, details_objs

    class Meta:
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"
        
class Hotel (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del hotel', db_index=True, default='', unique=True)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio extra', default=0)
    
    def __str__ (self):
        return f"{self.name} - {self.extra_price}"
    
    class Meta:
        verbose_name_plural = "Hotel"
        verbose_name = "Hotel"

class Transport (models.Model):
    key = models.CharField(max_length=150, verbose_name='Clave', db_index=True, help_text='Clave del transporte', default='', unique=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del transporte', default='', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', help_text='Precio del transporte', default=0.0)
    by_default = models.BooleanField(verbose_name='Por defecto', help_text='Transporte por defecto', default=False)
    
    def __str__ (self):
        if self.by_default:
            return f"{self.name} ({self.price}) (Por defecto)"
        return f"{self.name} ({self.price})"
    
    class Meta:
        verbose_name_plural = "Transportes"
        verbose_name = "Transporte"
