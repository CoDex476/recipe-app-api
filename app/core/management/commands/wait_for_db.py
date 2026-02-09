"""
django management command to wait for the database to be available.
"""

import time

from psycopg2 import OperationalError as psycopg2Error

from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except Exception as e:
                self.stdout.write(f"Database unavailable, waiting 1 second... {e}")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
