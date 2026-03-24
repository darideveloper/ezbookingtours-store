import json
from seema_rohan import models
from django.test import TestCase
from datetime import datetime
from decimal import Decimal

API_BASE = "/seema-rohan"

class TestViewIndex (TestCase):
    
    def test_get (self):
        """ Test index view """
        
        # Make request
        response = self.client.get(f'{API_BASE}/')
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertContains (response, "Running")
        
class TestViewBuy (TestCase):
    
    def setUp (self):
        
        self.api_endpoint = f"{API_BASE}/buy/" 
        
        # Create sample data
        self.sample_data = {        
            "name": "John",
            "last-name": "Doe",
            "from-host": "https://www.darideveloper.com/",
            "stripe-data": {
                "sample": {
                    "amount": 1,
                    "description": "sample product",
                    "image_url": "https://www.darideveloper.com/imgs/logo.png",
                    "price": 100
                }
            },
            "phone": "1234567890",
            "email": "sample@gmail.com"
        }
    
    def test_success (self):
        """ Test buy view """
                
        # Make request
        response = self.client.post(
            self.api_endpoint, 
            json.dumps (self.sample_data),
            content_type="application/json"
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(response.json()["message"], "sale saved")
        self.assertEqual(response.json()["redirect"], "https://www.darideveloper.com/?thanks=true")

        # Check that sale is NOT paid initially
        sale = models.Sale.objects.latest('id')
        self.assertFalse(sale.is_paid)
        
    def test_missing_data (self):
        """ Test buy view without submiting full data """
        
        incomplete_data = self.sample_data.copy()
        incomplete_data.pop("name")
        
        response = self.client.post(
            self.api_endpoint, 
            json.dumps (incomplete_data),
            content_type="application/json"
        )
        
         # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "error")
        self.assertEqual(response.json()["message"], "missing data")

    def test_hotel_name_saving(self):
        """ Test that custom hotel name is saved when hotel is 'other' """
        
        payload = {
            "name": "test",
            "last-name": "test",
            "price": 0,
            "vip-code": "",
            "stripe-data": {
                "Airport - Hotel Transfer": {
                    "amount": 1,
                    "description": "Name: test, Last name: test, Passengers: 1, Email: test@gmail.com, Phone: t122133, Hotel: other, Hotel Name: test naother, Arriving date: 2026-01-01, Arriving time: 02:00, Airline: test, Flight: test",
                    "price": 0,
                    "image_url": "http://localhost:5173/imgs/logo.png"
                }
            },
            "from-host": "http://localhost:5173/?thanks=true",
            "phone": "t122133",
            "email": "test@gmail.com"
        }
        
        response = self.client.post(
            self.api_endpoint, 
            json.dumps(payload),
            content_type="application/json"
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        
        sale = models.Sale.objects.latest('id')
        self.assertEqual(sale.hotel_name, "test naother")
        self.assertIsNone(sale.hotel)
           
class TestViewTransports (TestCase):
    
    def setUp (self):
        
        self.api_endpoint = f"{API_BASE}/transports/"
        
    def test_get (self):
        """ Test get transports """
        
        # Create models
        transport_1 = models.Transport.objects.create(
            key="sample 1",
            name="Sample transport 1",
            price=Decimal("100.00"),
            by_default=True
        )
        
        transport_2 = models.Transport.objects.create(
            key="sample 2",
            name="Sample transport 2",
            price=Decimal("100.00"),
            by_default=True
        )
                
        response = self.client.get(
            self.api_endpoint
        )
        
        # Format data from models
        data = []
        for transport in [transport_1, transport_2]:
            data.append({
                "id": transport.id,
                "key": transport.key,
                "name": transport.name,
                "price": "{:.2f}".format(transport.price),
                "by_default": transport.by_default
            })
            
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(response.json()["message"], "transports found")
        self.assertEqual(response.json()["data"], data)
        
    def test_no_models (self):
        """ Test get transports without models """
        
        response = self.client.get(
            self.api_endpoint
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "error")
        self.assertEqual(response.json()["message"], "transports not found")
        self.assertEqual(response.json()["data"], [])
        
class TestViewHotels (TestCase):
    
    def setUp (self):
        self.api_endpoint = f"{API_BASE}/hotels/"
        
    def test_get (self):
        """ Test get hotels """
        
        # Create models
        hotel_1 = models.Hotel.objects.create(
            name = "Sample hotel 1",
            extra_price = Decimal("100.51"),
        )
        
        hotel_2 = models.Hotel.objects.create(
            name = "Sample hotel 2",
            extra_price = Decimal("100.01"),
        )
                
        response = self.client.get(
            self.api_endpoint
        )
        
        # Format data from models
        data = []
        for hotel in [hotel_1, hotel_2]:
                        
            data.append({
                "id": hotel.id,
                "name": hotel.name,
                "extra_price": "{:.2f}".format(hotel.extra_price),
            })
            
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(response.json()["message"], "hotels found")
        self.assertEqual(response.json()["data"], data)
        
    def test_no_models (self):
        """ Test get hotels without models """
        
        response = self.client.get(
            self.api_endpoint
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "error")
        self.assertEqual(response.json()["message"], "hotels not found")
        self.assertEqual(response.json()["data"], [])
