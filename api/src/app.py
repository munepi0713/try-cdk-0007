import json

def get_data(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "GetData"})}


def create_data(event, context):
    print(event)
    print(context)

    # This return data is similar to one for API Gateway integration,
    # though no format regulation about a return value from Lambda handler
    # for StepFunction integration.
    return {"statusCode": 200, "body": json.dumps({"message": "CreateData"})}
