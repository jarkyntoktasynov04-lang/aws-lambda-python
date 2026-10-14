
import json

def lambda_handler(event, context):
    name = event.get("name", "Student")

    result = {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Сәлем, {name}!",
            "service": "AWS Lambda",
            "status": "success"
        }, ensure_ascii=False)
    }

    return result
