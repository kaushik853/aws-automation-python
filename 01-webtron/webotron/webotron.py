import boto3
import click


session = boto3.Session(profile_name='pyauto')
s3 = session.resource('s3')


@click.group()
def cli():
    "This script deploys websites in AWS"
    pass
@cli.command("list_buckets")
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)
@cli.command("list_bucket_objects")
@click.argument("bucket")
def list_bucket_objects(bucket):
    "List bucket objects from a bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == "__main__":
    cli()
    
    