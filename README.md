<div><a href='https://github.com/darideveloper/ezbookingtours-store/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/ezbookingtours-store.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://ezbookingtours.com/wp-content/uploads/2022/04/EZ-Booking-Tours-Logo.png' alt='EZBookingTours Store' height='80px'/>

# EZBookingTours Store

Visit at: **[ezbookingtours.com/tour/chichen-itza-tour-de-lujo-mexicanos-presentando-identificacion-oficial-vigente-con-fotografia](https://ezbookingtours.com/tour/chichen-itza-tour-de-lujo-mexicanos-presentando-identificacion-oficial-vigente-con-fotografia/)**

Django dashboard to create checkout widgets to be embedded in WordPress online store [EZBookingTours](https://ezbookingtours.com/)

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#relatedprojects'>Related Projects</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://developer.mozilla.org/en-US/docs/Web/HTML' target='_blank'> <img src='https://i.imgur.com/OitgDfl.jpeg' alt='HTML + CSS' title='HTML + CSS' height='50px'/> </a><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://requests.readthedocs.io/en/latest/' target='_blank'> <img src='https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png' alt='Requests' title='Requests' height='50px'/> </a><a href='https://stripe.com/' target='_blank'> <img src='https://cdn.svgporn.com/logos/stripe.svg' alt='Stripe' title='Stripe' height='50px'/> </a><a href='https://www.postgresql.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/postgresql.svg' alt='PostgreSQL' title='PostgreSQL' height='50px'/> </a><a href='https://getbootstrap.com/' target='_blank'> <img src='https://cdn.svgporn.com/logos/bootstrap.svg' alt='Bootstrap' title='Bootstrap' height='50px'/> </a><a href='https://docs.djangoproject.com/en/4.0/' target='_blank'> <img src='https://cdn.svgporn.com/logos/django.svg' alt='Django' title='Django' height='50px'/> </a><a href='https://www.w3schools.com/js/js_es6.asp' target='_blank'> <img src='https://cdn.svgporn.com/logos/javascript.svg' alt='JavaScript' title='JavaScript' height='50px'/> </a></div>

# Related projects

<div align='center'><a href='https://github.com/darideveloper/cancun-concierge' target='_blank'> <img src='https://github.com/darideveloper/cancun-concierge/raw/master/imgs/logo.png' alt='Cancun Concierge' title='Cancun Concierge' height='50px'/> </a><a href='https://github.com/darideveloper/rivieramayaairporttransfers' target='_blank'> <img src='https://rivieramayaairporttransfers.com/imgs/page-logo-trans.png' alt='Riviera Maya Airport Transfers' title='Riviera Maya Airport Transfers' height='50px'/> </a></div>

# Media

![widget](https://github.com/darideveloper/ezbookingtours-store/blob/master/screenshots/widget.gif?raw=true)

![admin](https://github.com/darideveloper/ezbookingtours-store/blob/master/screenshots/admin.gif?raw=true)

# Details

This project have been created in order to have a more detailed and custom checkout in the online store, with dynamic options not allowed by WordPress.

The models/tables created in the database are:

* Hotels
* Pick ups en hoteles
* Tiempo de tours
* Tours
* Ventas

When a buy page of the online store loads, the dynamic link of the widget its generated based in the page content, and immediately its embedded the iframe and hidden the old checkout.
After the widget/iframe collected the sale data, the user its redirect to a stripe checkout.

# Roadmap

* [x] Create models
* [x] Custom admin
* [x] 404 page
* [x] Widget
	* [x] Render with dynamic link
	* [x] Get info from models
	* [x] Embedded in WordPress
	* [x] Dynamic price
	* [x] Collect user data
	* [x] Show error screens where not found tour or time
* [x] Save sales in database
* [x] Loading spinner
* [x] Success page after payment
* [x] Submit email to client after sale
* [x] Connect to stripe checkout

