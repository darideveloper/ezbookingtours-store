# EzBookingTours Store — Booking & Admin Dashboard

Django admin dashboard and booking API for the Cancun Concierge DMC ecosystem. It started as a checkout widget backend for the EZBookingTours WordPress store and evolved into the central system managing all booking modules: airport transfers, weddings, celebrations and tours.

## Tech Stack

- **Django 4.2** — modular monolith (12 apps, one per client/event vertical)
- **Django Unfold** — modern admin interface
- **PostgreSQL** — database
- **Stripe** — payments via external proxy service
- **SMTP** — voucher and confirmation emails

## Features

- 12 booking modules: store, riviera_maya, wedding, will_ryan, rohan_karisma, driven_mastermind, andrea_scott, tony_thoa, digitalrealty, seema_rohan, rhea_peeyush, loris
- JSON API endpoints for hotels, transports and free dates consumed by landing pages
- Sale/booking capture with payment state tracking (Stripe, cash or free)
- Voucher and confirmation emails per event with branded HTML templates
- VIP codes and free-date management
- Embeddable checkout widget for WordPress (original store)
- Django Unfold admin with per-app sections, search and filters

## Setup

```sh
pip install -r requirements.txt
cp .env.example .env   # configure DB, SMTP, Stripe proxy
python manage.py migrate
python manage.py runserver
```

---

## Contact

Developed by [Dari Developer](https://darideveloper.com)

- 🌐 [darideveloper.com](https://darideveloper.com)
- 💬 [WhatsApp](https://api.whatsapp.com/send?phone=5214493402622)
- 📂 [View project in portfolio](https://darideveloper.com/portafolio/cancunconcierge)

---

# EzBookingTours Store — Panel de administración y reservas

Dashboard de administración y API de reservas en Django para el ecosistema de Cancun Concierge DMC. Comenzó como backend de un widget de checkout para la tienda WordPress de EZBookingTours y evolucionó hasta convertirse en el sistema central que gestiona todos los módulos de reserva: traslados aeroportuarios, bodas, celebraciones y tours.

## Tech Stack

- **Django 4.2** — monolito modular (12 apps, una por cliente/vertical)
- **Django Unfold** — interfaz de administración moderna
- **PostgreSQL** — base de datos
- **Stripe** — pagos mediante servicio proxy externo
- **SMTP** — correos de confirmación y vouchers

## Features

- 12 módulos de reserva: store, riviera_maya, wedding, will_ryan, rohan_karisma, driven_mastermind, andrea_scott, tony_thoa, digitalrealty, seema_rohan, rhea_peeyush, loris
- Endpoints JSON para hoteles, transportes y fechas libres consumidos por las landing pages
- Captura de ventas/reservas con estado de pago (Stripe, efectivo o gratis)
- Correos de confirmación y vouchers por evento con plantillas HTML personalizadas
- Gestión de códigos VIP y fechas de cortesía
- Widget de checkout embebible para WordPress (tienda original)
- Admin Django Unfold con secciones por app, búsqueda y filtros

## Setup

```sh
pip install -r requirements.txt
cp .env.example .env   # configurar DB, SMTP, proxy Stripe
python manage.py migrate
python manage.py runserver
```

---

## Contacto

Desarrollado por [Dari Developer](https://darideveloper.com)

- 🌐 [darideveloper.com](https://darideveloper.com)
- 💬 [WhatsApp](https://api.whatsapp.com/send?phone=5214493402622)
- 📂 [Ver proyecto en el portafolio](https://darideveloper.com/portafolio/cancunconcierge)
