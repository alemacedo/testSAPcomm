import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    # Get the value_1 and value_2 parameters from the event object. The 
    # runtime converts the event object to a Python dictionary
    value_1=event['value_1']
    value_2=event['value_2']
    
    sum = do_sum(value_1, value_2)
    print(f"The sum is {sum}")
        
    logger.info(f"CloudWatch logs group: {context.log_group_name}")
    
    # return the calculated area as a JSON string
    data = {"sum": sum}
    return json.dumps(data)
    
def do_sum(value_1, value_2):
    return value_1+value_2