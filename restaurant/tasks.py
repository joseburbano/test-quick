from celery import shared_task
from models import Restaurant
import pandas as pd
import boto3
from django.conf import settings

@shared_task
def generate_sales_report():
    restaurants = Restaurant.objects.all()
    data = [{"id": r.id, "name": r.name, "location": r.location} for r in restaurants]
    df = pd.DataFrame(data)
    file_name = "sales_report.csv"
    df.to_csv(file_name, index=False)

    # Simulate S3 Upload
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    s3.upload_file(file_name, settings.AWS_STORAGE_BUCKET_NAME, file_name)
    return f"Report uploaded to {settings.AWS_STORAGE_BUCKET_NAME}/{file_name}"