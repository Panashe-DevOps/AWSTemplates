import boto3


def lambda_handler(event, context):
    # TODO implement
    
    print(" loading function ")
    
    client = boto3.client("connect")
    
    response = client.start_outbound_voice_contact(DestinationPhoneNumber='+27639933142',
    ContactFlowId='5a0b6dd8-96d7-4486-b811-a5c51cae023e', InstanceId='f5fe2a0b-4c12-440b-b9bc-5088037a9cff', SourcePhoneNumber='+18449001233')
    
    #response = client.StartOutBoundVoiceContact(InstanceId='f5fe2a0b-4c12-440b-b9bc-5088037a9cff')
    
    print(response)
    
    return {"Okay":"200"}