#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Webtron deploys websites in aws.
Webtron automates the process of deploying
static websites in s3 with cloudfront,
DNS with Route53 and
certificates from ACM
"""


import boto3
import click

from bucket import BucketManager


session = boto3.Session(profile_name='pyauto')
bucket_manager = BucketManager(session)



@click.group()
def cli():
    """This script deploys websites in AWS."""
    pass


@cli.command("list_buckets")
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command("list_bucket_objects")
@click.argument("bucket")
def list_bucket_objects(bucket):
    """List bucket objects from a bucket"""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command("setup_bucket")
@click.argument("bucket")
def setup_bucket(bucket):
    """Create and configure s3 bucket"""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)


    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET"""
    bucket_manager.sync(pathname, bucket)
    

if __name__ == "__main__":
    cli()