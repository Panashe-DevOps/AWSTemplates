import json

def lambda_handler(event, context):
    
    print("Loading Function")
    
    print(event)
    
    counter = int(event['Details']['ContactData']['Attributes']['Value'])
    
    print(counter)
    
    ## {'ContactData': {'Attributes': {'Value': '0'
    counter = counter+1
    
    return {
        "Count":str(counter)
    }
