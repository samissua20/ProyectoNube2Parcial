import json
import boto3
import random as rd
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
  table = dynamodb.Table('animedb')

  batch_keys = {
    table.name: {
        'Keys': [{"ID": str(rd.randint(20,299))} for i in range(4)]
    }
    
  }

  data = dynamodb.batch_get_item(RequestItems=batch_keys)

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response