import urllib.request
import json
import polyline
import boto3
from config import Google_config
from config import Aws_S3_config
from utils import reduce_precision


def get_session(resource):
    session = boto3.session.Session(
                        region_name=Aws_S3_config.REGION_NAME,
                        # endpoint_url=ENDPOINT_URL,
                        aws_access_key_id=Aws_S3_config.ACCESS_KEY,
                        aws_secret_access_key=Aws_S3_config.SECRET_ACCESS_KEY)

    session_object = session.resource('s3')
    return session_object


def get_bucket_object(bucket_name):
    s3_session = get_session('s3')
    bucket = s3_session.Bucket('bgtrailstracks')
    return bucket


def get_static_image_url(geojson_url):
    http_response = urllib.request.urlopen(geojson_url)
    json_data = json.load(http_response)
    points = json_data['features'][0]['geometry']['coordinates']
    coordinates = [(p[1], p[0]) for p in points]
    coordinates = reduce_precision(coordinates)
    p = polyline.encode(coordinates)
    img_url = Google_config.STATIC_IMAGE_URL.format(polyline=p, key=Google_config.API_KEY)
    return img_url


def upload_to_s3(upload_file, bucket_name=None, path=None):
    bucket = get_bucket_object()
    pass