import os

class Aws_S3_config():
    ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    REGION_NAME = os.environ.get('AWS_REGION_NAME') # 'eu-central-1' 


class Google_config():
    API_KEY = 'AIzaSyCs9_ayHgvpR2CfIZU6jpj1hrYX0Y2YYwQ'
    STATIC_IMAGE_URL = "https://maps.googleapis.com/maps/api/staticmap?zoom=11&size=400x400&maptype=terrain&path=color:0xff0000ff|weight:2|enc:{polyline}&key={key}"

class Mapbox_config():
    STATIC_IMAGE_URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/path-3+F34815-1({urlpath})/auto/500x300?access_token={key}"
    API_KEY = os.environ.get('MAPBOX_SECRET_KEY')