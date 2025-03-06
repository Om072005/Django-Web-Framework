from django.core.management.base import BaseCommand
from restaurant.models import Menu

class Command(BaseCommand):
    help = 'Populates the menu with sample data'
    
    def handle(self, *args, **options):
        if Menu.objects.count() > 0:
            self.stdout.write(self.style.WARNING('Menu items already exist! No items added.'))
            return
            
        menu_items = [
            {'title': 'Greek Salad', 'price': 12.99, 'inventory': 100},
            {'title': 'Bruschetta', 'price': 8.99, 'inventory': 80},
            {'title': 'Grilled Fish', 'price': 21.99, 'inventory': 50},
            {'title': 'Pasta Carbonara', 'price': 15.99, 'inventory': 60},
            {'title': 'Lemon Dessert', 'price': 7.99, 'inventory': 90}
        ]
        
        menu_objects = [Menu(**item) for item in menu_items]
        Menu.objects.bulk_create(menu_objects)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(menu_items)} menu items'))
