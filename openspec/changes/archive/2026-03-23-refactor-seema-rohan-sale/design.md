# Design: Refactor Seema Rohan Sale Model

The goal of this refactor is to provide a structured way to store booking information that is currently trapped inside the `stripe_data` JSONField and its `description` string.

## Proposed Model Changes

The `Sale` model in `seema_rohan/models.py` will be updated to include the following, ensuring all fields have descriptive `verbose_name` attributes for the Django Admin:

- **Relationships**:
  - `hotel`: `ForeignKey` to `Hotel` (null=True, blank=True, verbose_name='Hotel').
  - `transport_type`: `ForeignKey` to `Transport` (null=True, blank=True, verbose_name='Tipo de transporte').
- **Booking Info**:
  - `hotel_name`: `CharField` (max_length=150, default='', verbose_name='Nombre del hotel (Personalizado)').
  - `passengers`: `IntegerField` (default=1, verbose_name='Pasajeros').
- **Arriving Details**:
  - `arriving_date`: `DateField` (null=True, blank=True, verbose_name='Fecha de llegada').
  - `arriving_time`: `TimeField` (null=True, blank=True, verbose_name='Hora de llegada').
  - `arriving_airline`: `CharField` (max_length=150, default='', verbose_name='Aerolínea de llegada').
  - `arriving_flight`: `CharField` (max_length=150, default='', verbose_name='Vuelo de llegada').
- **Departing Details**:
  - `departing_date`: `DateField` (null=True, blank=True, verbose_name='Fecha de salida').
  - `departing_time`: `TimeField` (null=True, blank=True, verbose_name='Hora de salida').
  - `departing_airline`: `CharField` (max_length=150, default='', verbose_name='Aerolínea de salida').
  - `departing_flight`: `CharField` (max_length=150, default='', verbose_name='Vuelo de salida').

### Improved `__str__` Method
The `__str__` method will be updated to provide more context at a glance in the Admin:
```python
def __str__(self):
    return f"{self.name} {self.last_name} - {self.transport_type or 'Sin transporte'} - {self.sale_datetime.date()}"
```

## Implementation Plan

### 1. View Logic (`seema_rohan/views.py`)
Update `BuyView.post` to extract values from the `description` string. The string is comma-separated: `"Label: Value, Label: Value"`.

Key mappings:
- `Name` -> `name`
- `Last name` -> `last_name`
- `Passengers` -> `passengers`
- `Hotel` -> `hotel_name` (and attempt to look up the `Hotel` by name).
- `Hotel name` -> `hotel_name` (if custom).
- `Arriving date` -> `arriving_date`
- `Arriving time` -> `arriving_time`
- `Airline` (first occurrence) -> `arriving_airline`
- `Flight` (first occurrence) -> `arriving_flight`
- `Departing date` -> `departing_date`
- `Departing time` -> `departing_time`
- `Airline` (second occurrence) -> `departing_airline`
- `Flight` (second occurrence) -> `departing_flight`

### 2. Transport Lookup
The `stripe_data` keys contain the service name (e.g., "One Way (Arriving)", "Round Trip"). This will be matched against `Transport.name` to populate the `transport_type` ForeignKey.

### 3. Admin Configuration (`seema_rohan/admin.py`)
The `SaleAdmin` will be updated to display these new fields in the list view and use `fieldsets` to organize the detailed view into "Customer", "Transport", "Arrival", and "Departure" sections.
