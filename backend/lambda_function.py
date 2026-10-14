
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
        "body": json.dumps({
            "service": "StudentHub API",
            "status": "success",
            "message": "AWS Lambda дұрыс жұмыс істеп тұр!"
        }, ensure_ascii=False)
    }
