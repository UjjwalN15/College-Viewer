import csv
from django.core.management.base import BaseCommand
from base.models import College

class Command(BaseCommand):
    help = 'Import colleges from CSV file into the database'

    def handle(self, *args, **kwargs):
        # Path to the CSV file
        csv_file_path = r'C:\Users\prajw\OneDrive\Desktop\Python Programming\Project\Colleges\Data.csv'  # Update this path

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                College.objects.update_or_create(
                    name=row['College'],
                    defaults={
                        'location': row['Location'],
                        'university': row['University'],
                        'course_offered': row['Course Offered'],
                        'ownership_type': row['Ownership Type'],
                        'phone_number': row['Phone Number'],
                        'email': row['Email'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Colleges data imported successfully!'))
