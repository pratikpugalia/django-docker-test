import csv
import datetime
import os
from django.core.management import BaseCommand
from companyData.models import CompanyData

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        script_dir = os.path.dirname(__file__)
        path = "../../../static/sample_headcount.csv"
        abs_file_path = os.path.join(script_dir, path)
        with open(abs_file_path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            #print(reader)
            for row in reader:
                #print(row)
                companyData = CompanyData.objects.create(
                    company=row[0],
                    month=datetime.datetime.strptime(str(row[1]), "%Y-%m"),
                    headcount=row[2]
                )