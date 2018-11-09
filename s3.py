import boto3
import pandas as pd
import os
import gzip
import io


s3 = boto3.client('s3', os.environ['S3_REGION'])

csv_obj = s3.get_object(Bucket=os.environ['S3_BUCKET'], Key=os.environ['S3_KEY'])
body = csv_obj['Body']
compressed = io.BytesIO(body.read())
decompressed = gzip.GzipFile(fileobj=compressed)

df = pd.read_csv(decompressed)
df
