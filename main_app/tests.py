from django.test import TestCase
from django.urls import reverse
from .models import CompanyData
from django.core.files.uploadedfile import SimpleUploadedFile
import csv
import os

class CompanyDataTestCase(TestCase):
    def setUp(self):
        CompanyData.objects.create(
            company_name="ITSPE",
            address="Gachchibowli_Hyderabad",
            city="Hyderabad",
            state="Telangana",
            zip_code="500032",
            website="https://www.itspe.co.in/"
        )

    def test_company_data_creation(self):
        company = CompanyData.objects.get(company_name="ITSPE")
        self.assertEqual(company.city, "Hyderabad")

    def test_upload_csv(self):
        test_csv_data = [
            ["company_name", "address", "city", "state", "zip_code", "website"],
            ["Another Company", "456 Another St", "Another City", "AC", "67890", "http://anothercompany.com"]
        ]

        test_csv_path = 'test_data.csv'
        with open(test_csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(test_csv_data)

        with open(test_csv_path, 'rb') as file:
            response = self.client.post(reverse('upload'), {'file': SimpleUploadedFile('test_data.csv', file.read(), content_type='text/csv')})
        
        os.remove(test_csv_path)  # Clean up the test file after use

        self.assertEqual(response.status_code, 302)
        self.assertTrue(CompanyData.objects.filter(company_name="Another Company").exists())

    def test_query_api(self):
        response = self.client.get(reverse('query_company_data'), {'city': 'Hyderabad'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
