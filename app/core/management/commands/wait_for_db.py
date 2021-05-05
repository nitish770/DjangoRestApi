import time

from django.db.utils import OperationalError
from django.db import connections
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Command to pause execution till database is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database connection')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except:
                self.stdout.write('Waiting 1 sec')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Connection Successful"))
