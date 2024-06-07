from django.test import TestCase
from .models import Customer, Order

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", code="JD123")

    def test_customer_creation(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(customer.code, "JD123")

class OrderTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="John Doe", code="JD123")
        Order.objects.create(customer=customer, item="Widget", amount=10.99)

    def test_order_creation(self):
        order = Order.objects.get(item="Widget")
        self.assertEqual(order.amount, 10.99)
