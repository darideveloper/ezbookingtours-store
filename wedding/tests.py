import json
from wedding import models
from django.test import TestCase
from datetime import datetime

API_BASE = "/wedding"

class TestViewIndex (TestCase):
    
    def test_get (self):
        """ Test index view """
        
        # Make request
        response = self.client.get(f'{API_BASE}/')
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertContains (response, "Running")
        
class TestViewValidateVipCode (TestCase):
        
    def setUp (self):
        
        self.api_endpoint = f'{API_BASE}/validate-vip-code/'
        
        # Create VipCodes
        self.vip_code = "12345"
        models.VipCode.objects.create(value=self.vip_code, enabled=True)
        
    def test_valid (self):
        """ Test validate vip code view """
        
        # Make request
        response = self.client.post(
            self.api_endpoint, 
            json.dumps ({"vip-code": self.vip_code}),
            content_type="application/json"
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "success",
            "message": "valid vip code"
        })
    
    def test_invalid (self):
        """ Test validate vip code view """
        
        # Make request
        response = self.client.post(
            self.api_endpoint, 
            json.dumps ({"vip-code": "1234567"}),
            content_type="application/json"
        )
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "error",
            "message": "invalid vip code"
        })
        
    def test_missing_vip_code (self):
        """ Test validate vip code view """
        
        # Make request
        response = self.client.post(
            self.api_endpoint,
            json.dumps ({}),
            content_type="application/json"
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "error",
            "message": "vip-code missing"
        })
        
class TestViewBuy (TestCase):
    
    def setUp (self):
        
        self.api_endpoint = f"{API_BASE}/buy/" 
        
        # Create sample data
        self.sample_data = {        
            "name": "John",
            "last-name": "Doe",
            "vip-code": "123456",
            "price": 100,
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
        
        self.vip_code = "12345"
        models.VipCode.objects.create(value=self.vip_code, enabled=True)
    
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
        self.assertEqual(response.json()["message"], "stripe link generated")
        self.assertIn("checkout.stripe.com/c/pay/", response.json()["redirect"])
        
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
    
    def test_eror_stripe_data (self):
        """ Test buy with incorrect stripe data """
        
        incomplete_data = self.sample_data.copy()
        incomplete_data["stripe-data"]["sample"].pop("amount")
        
        response = self.client.post(
            self.api_endpoint, 
            json.dumps (incomplete_data),
            content_type="application/json"
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "error")
        self.assertEqual(response.json()["message"], "error generating stripe link")
        
    def test_vip_sucess (self):
        
        # Replace vip code from sample data
        self.sample_data["vip-code"] = self.vip_code
        
        response = self.client.post(
            self.api_endpoint, 
            json.dumps (self.sample_data),
            content_type="application/json"
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(response.json()["message"], "sale saved")
        self.assertIn("success", response.json()["redirect"])
           
class TestViewTransports (TestCase):
    
    def setUp (self):
        
        self.api_endpoint = f"{API_BASE}/transports/"
        
    def test_get (self):
        """ Test get transports """
        
        # Create models
        transport_1 = models.Transport.objects.create(
            key="sample 1",
            name="Sample transport 1",
            price=100,
            by_default=True
        )
        
        transport_2 = models.Transport.objects.create(
            key="sample 2",
            name="Sample transport 2",
            price=100,
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
                "price": transport.price,
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
            extra_price = 100.51,
        )
        
        hotel_2 = models.Hotel.objects.create(
            name = "Sample hotel 2",
            extra_price = 100.01,
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
                "extra_price": str(hotel.extra_price),
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
        
class TestViewFreedates (TestCase):
    
    def setUp (self):
        self.api_endpoint = f"{API_BASE}/free-dates/"
        
    def test_get (self):
        """ Test get free dates """
        
        # Create models
        arrival_category = models.FreeDaysCategory.objects.create(
            name="arrival"
        )
        departure_category = models.FreeDaysCategory.objects.create(
            name="departure"
        )
        
        arrival_date_1 = datetime(2021, 1, 1)
        arrival_date_2 = datetime(2021, 1, 2)
        departure_date_1 = datetime(2021, 1, 1)
        departure_date_2 = datetime(2021, 1, 2)

        models.FreeDays.objects.create(
            date=arrival_date_1,
            category=arrival_category
        )
        models.FreeDays.objects.create(
            date=arrival_date_2,
            category=arrival_category
        )
        models.FreeDays.objects.create(
            date=departure_date_1,
            category=departure_category
        )
        models.FreeDays.objects.create(
            date=departure_date_2,
            category=departure_category
        )
        
        response = self.client.get(
            self.api_endpoint
        )

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(response.json()["message"], "free dates found")
        self.assertEqual(response.json()["data"], {
            "arrival": [arrival_date_1.strftime("%Y-%m-%d"), arrival_date_2.strftime("%Y-%m-%d")],
            "departure": [departure_date_2.strftime("%Y-%m-%d"), departure_date_1.strftime("%Y-%m-%d")]
        })
        
    def test_no_models (self):
        """ Test get hotels without models """
        
        response = self.client.get(
            self.api_endpoint
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "error")
        self.assertEqual(response.json()["message"], "error getting free dates")
        self.assertEqual(response.json()["data"], {})
        
class TestSuccessView (TestCase):
    
    def setUp(self):
        
        self.api_endpoint = f"{API_BASE}/success/x/?from=https://www.darideveloper.com"
        
        # Create sale
        self.sale = models.Sale.objects.create(
            name="John",
            last_name="Doe",
            price=100,
            vip_code="12345"
        )
        
    def test_invalid_sale (self):
        """ Try to acreedit invalid sale id """
        
        response = self.client.get(
            self.api_endpoint.replace("x", "100")
        )
        
        # Check response
        self.assertEqual(response.status_code, 302)
        
        # Validate model
        self.sale.refresh_from_db()
        self.assertEqual(self.sale.is_paid, False)
        
    def test_valid_sale (self):
        """ Acreedit valid sale id """
        
        response = self.client.get(
            self.api_endpoint.replace("x", "1")
        )
        
        # Check response
        self.assertEqual(response.status_code, 302)
        
        # Validate model
        self.sale.refresh_from_db()
        self.assertEqual(self.sale.is_paid, False)