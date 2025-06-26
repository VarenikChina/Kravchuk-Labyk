from django.core.management.base import BaseCommand
from products.models import Product, Category

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create categories
        led_category, _ = Category.objects.get_or_create(name='LED', description='LED products')
        neon_category, _ = Category.objects.get_or_create(name='NEON', description='Neon products')

        # Create products
        products = [
            {'name': 'LED Bulb', 'description': 'High quality LED bulb', 'price': 5.99, 'stock': 100, 'category': led_category},
            {'name': 'Neon Sign', 'description': 'Custom neon sign', 'price': 49.99, 'stock': 50, 'category': neon_category},
            {'name': 'LED Strip', 'description': 'Flexible LED strip', 'price': 12.99, 'stock': 200, 'category': led_category},
            {'name': 'Neon Light', 'description': 'Bright neon light', 'price': 29.99, 'stock': 75, 'category': neon_category},
            {'name': 'LED Panel', 'description': 'Energy efficient LED panel', 'price': 19.99, 'stock': 80, 'category': led_category},
            {'name': 'Neon Tube', 'description': 'Durable neon tube', 'price': 39.99, 'stock': 60, 'category': neon_category},
            {'name': 'LED Floodlight', 'description': 'Powerful LED floodlight', 'price': 24.99, 'stock': 90, 'category': led_category},
            {'name': 'Neon Art', 'description': 'Artistic neon piece', 'price': 59.99, 'stock': 30, 'category': neon_category},
            {'name': 'LED Spotlight', 'description': 'Focused LED spotlight', 'price': 14.99, 'stock': 110, 'category': led_category},
            {'name': 'Neon Glow', 'description': 'Glowing neon effect', 'price': 44.99, 'stock': 40, 'category': neon_category},
        ]

        for product in products:
            Product.objects.get_or_create(**product)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
