import json
import time
import random
import boto3


print('Loading function')


def lambda_handler(event, context):
    
    client = boto3.client('connect')
    
    response = client.start_outbound_voice_contact(
            DestinationPhoneNumber='+18448687238',
            ContactFlowId='13c94d97-93e2-4746-a495-28640beb5ba8',
            InstanceId='f5fe2a0b-4c12-440b-b9bc-5088037a9cff',
            SourcePhoneNumber='+18449001233')
        
    print(response)
    time.sleep(1)
            
    return {"Okay":"200"}
