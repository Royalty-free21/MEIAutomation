from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
)
from constructs import Construct

class InfraStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Simple VPC
        vpc = ec2.Vpc(self, "MyVPC", max_azs=2)

        # Simple S3 Bucket
        bucket = s3.Bucket(self, "MyAppBucket")
