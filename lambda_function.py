import boto3
import random
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")
bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"fact": "No facts available in DynamoDB."})
        }

    fact = random.choice(items)["FactText"]

    messages = [
        {
            "role": "user",
            "content": f"Take this cloud computing fact and make it fun and engaging in 1-2 sentences max: {fact}"
        }
    ]

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 100,
        "messages": messages,
        "temperature": 0.7
    }

    try:
        resp = bedrock.invoke_model(
            modelId="us.anthropic.claude-3-5-haiku-20241022-v1:0",
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )

        result = json.loads(resp["body"].read())
        witty_fact = ""

        if "content" in result and result["content"]:
            for block in result["content"]:
                if block.get("type") == "text":
                    witty_fact = block["text"].strip()
                    break

        if not witty_fact or len(witty_fact) > 300:
            witty_fact = fact

    except Exception as e:
        print(f"Bedrock error: {e}")
        witty_fact = fact

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({"fact": witty_fact})
    }