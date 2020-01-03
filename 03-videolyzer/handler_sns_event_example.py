# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:389938739438:handleLabelDetectionTopic:c79dfb02-ba1b-4adc-8427-54b49db98425', 'Sns': {'Type': 'Notification', 'MessageId': 'cf66e799-3838-5940-b0b7-b1101164cd71', 'TopicArn': 'arn:aws:sns:us-east-1:389938739438:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"4423a72b817e55ed47957517b4bef3f4f11e3de31fb513ab9de026e32a116704","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1578051355926,"Video":{"S3ObjectName":"kaushik_pexels.mp4","S3Bucket":"kaushikvideolyzervideos12345"}}', 'Timestamp': '2020-01-03T11:35:56.055Z', 'SignatureVersion': '1', 'Signature': 'na1aGRk8MfM1OzRd/EzvwpFI9Mz0LMXYrEy8V0FohPUfuJgp82CCR46qbd0/7oYZ6tsBrPThw7PxJ8ITd/hdJYy2AQZJNhtt65tKPa9/S01qOD/FlkyKHoi6Vyanw62MxxYxZx1oSmMCH0A0wOIshvsqRP3699eHu9vTucL125gAwlJTPFRUQz9Aif9FEgh4QONYeCrz6uUv0JWMLflpJDwbmrVULFKQ62r8HwBnqphwZI6GbJT265YYxvvDIoTeDdMVeekk4z7y2LUw+K7GuPZKS3asgeyfLuzTAoakhQ3TT/CXxkRqVDQa957T0zrH5aWoZIN3j798gahySRkodw==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:389938739438:handleLabelDetectionTopic:c79dfb02-ba1b-4adc-8427-54b49db98425', 'MessageAttributes': {}}}]}
event
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Type']
event['Records'][0]['Sns']['Message']
type( event['Records'][0]['Sns']['Message'])
import json
#jon.loads( event['Records'][0]['Sns']['Message'])
json.loads( event['Records'][0]['Sns']['Message'])
