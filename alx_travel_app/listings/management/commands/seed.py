from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with fake data'
    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()
        # Create 10 fake users
        if User.objects.count() == 0:
            User.objects.create_superuser(username='admin', password='admin123')

        smaple_data = []
        for _ in range(10):
            smaple_data.append(Listing(
                title=fake.word(),
                description=fake.text(),
                price_per_night=fake.random_int(min=100, max=1000),
                location=fake.city(),
            ))
        Listing.objects.bulk_create(smaple_data)
        self.stdout.write(self.style.SUCCESS('Successfully populated database with fake data'))