from django.core.management.base import BaseCommand, CommandError

from users.utils import import_data_from_csv


class Command(BaseCommand):
    help = 'Describe what your command does here'

    def handle(self, *args, **options):
        import_data_from_csv("dataset.csv")
