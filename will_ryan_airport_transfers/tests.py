from django.test import TestCase
from will_ryan_airport_transfers import models

API_BASE = "/will-ryan"

class TestViewHotels (TestCase):
    
    def setUp(self):
        
        self.hotel_1 = models.Hotel (name="Hotel 1", extra_price=10.0)
        self.hotel_1.save()
        self.hotel_2 = models.Hotel (name="Hotel 2", extra_price=20.0)
        self.hotel_2.save()
        
    def test_get (self):
        """ Test response fields """
        
        response = self.client.get(f"{API_BASE}/hotels/")
        self.assertEqual(response.status_code, 200)
        
        response_json = response.json()
        
        self.assertEqual(response_json[0]["fields"], {
            "name": self.hotel_2.name,
            "extra_price": self.hotel_2.extra_price
        })
        self.assertEqual(response_json[1]["fields"], {
            "name": self.hotel_1.name,
            "extra_price": self.hotel_1.extra_price
        })
        
class TestViewTransports (TestCase):
    
    def setUp (self):
        
        self.transport_1 = models.Transport (
            key="transport_1",
            name="Transport 1",
            price=10.0,
            por_defecto=True    
        )
        self.transport_1.save()
        self.transport_2 = models.Transport (
            key="transport_2",
            name="Transport 2",
            price=20.0,
            por_defecto=False
        )
        self.transport_2.save()
        
    def test_get (self):
        """ Test response fields """
        
        response = self.client.get(f"{API_BASE}/transports/")
        self.assertEqual(response.status_code, 200)
        
        response_json = response.json()
        
        self.assertEqual(response_json[0]["fields"], {
            "key": self.transport_1.key,
            "name": self.transport_1.name,
            "price": self.transport_1.price,
            "por_defecto": self.transport_1.por_defecto
        })
        
        self.assertEqual(response_json[1]["fields"], {
            "key": self.transport_2.key,
            "name": self.transport_2.name,
            "price": self.transport_2.price,
            "por_defecto": self.transport_2.por_defecto
        })