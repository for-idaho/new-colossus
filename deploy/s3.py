import boto3


def put(key, body, bucket_name, content_type='text/html'):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).put_object(
        Key=key, Body=body, ContentType=content_type)


def create_bucket(bucket_name, index_data, error_data):
    """Create an AWS s3 Bucket

    bucket_name -- the name of the bucket. Must be unique
    index_data -- binary data for the index file
    error_data -- binary data for the error file
    """

    client = boto3.client('s3')
    client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    })

    index_file_name = "index.html"
    error_file_name = "error.html"

    put(index_file_name, index_data, bucket_name)
    put(error_file_name, error_data, bucket_name)

    _make_bucket_public_readable(bucket_name)
    client.put_bucket_website(Bucket=bucket_name,
                              WebsiteConfiguration=_webconfig(
                                  error_file_name, index_file_name))

    return "{}.s3-website.us-east-2.amazonaws.com".format(bucket_name)


def _make_bucket_public_readable(bucket_name):
    bucket_policy = boto3.resource('s3').BucketPolicy(bucket_name)
    policy_string = '{{\
    "Version":"2012-10-17",\
    "Statement":[{{\
      "Sid":"PublicReadGetObject",\
      "Effect":"Allow",\
      "Principal": "*",\
      "Action":["s3:GetObject"],\
      "Resource":["arn:aws:s3:::{}/*"]\
      }}]\
    }}'.format(bucket_name)

    response = bucket_policy.put(Policy=policy_string)


def _webconfig(err, index):
    return {
        'ErrorDocument': {
            'Key': err
        },
        'IndexDocument': {
            'Suffix': index
        }
    }
