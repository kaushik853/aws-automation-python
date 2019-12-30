# coding: utf-8
import boto3
session = boto3.session.Session(profile_name='pyauto')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='kaushikvideoanalyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
from pathlib import Path
dir /Users/palkau/Downloads
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '/Users/palkau/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '/Users/palkau/Downloads/*.mp4')
dir
get_ipython().run_line_magic('ls', '/Users/palkau/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '/Users/palkau/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '/Users/palkau/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '/Users/palkau/Downloads/*.mp4')
from pathlib import Path
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('cd', '03-videolyzer/')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', 'C:\\\\Users\\\\palkau\\\\Downloads\\\\*.mp4')
get_ipython().run_line_magic('ls', 'C:\\Users\\palkau\\Downloads\\*.mp4')
get_ipython().run_line_magic('ls', 'C:\\Users\\palkau\\Downloads\\*.mp4')
pathname = 'C:\Users\palkau\Downloads\pexels_videos.mp4'
pathname='C:\Users\palkau\Downloads\pexels_videos.mp4'
pathname ='C:\Users\palkau\Downloads\pexels_videos.mp4'
pathname = 'C:\Users\palkau\Downloads\pexels_videos.mp4'
pathname = r'C:\Users\palkau\Downloads\pexels_videos.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
