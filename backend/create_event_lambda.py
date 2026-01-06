import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
sns = boto3.client('sns', region_name='eu-north-1')

table = dynamodb.Table('Eventstable')

SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:484907499616:EventAnnouncements"

def lambda_handler(event, context):

    if event["httpMethod"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": ""
        }

    body = json.loads(event.get('body', '{}'))

    event_item = {
        "eventId": body.get("eventId", str(uuid.uuid4())),
        "title": body["title"],
        "description": body["description"],
        "eventDate": body["eventDate"],
        "createdBy": body.get("createdBy", "admin"),
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=event_item)

    message = (
        f"New Event Created:\n\n"
        f"Title: {event_item['title']}\n"
        f"Date: {event_item['eventDate']}\n"
        f"Description: {event_item['description']}"
    )

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=f"New Event: {event_item['title']}"
    )

    return {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps({
            "message": "Event created successfully",
            "event": event_item
        })
    }
