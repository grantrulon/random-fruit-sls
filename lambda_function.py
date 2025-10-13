import random

def lambda_handler(event, context):
    # Returns a random fruit name
    possible_fruits = ["apple", "orange", "banana", "grape", "kiwi", "mango", "pear", "pineapple", "strawberry", "watermelon"]

    return {
        'statusCode': 200,
        'body': {
            "fruit": random.choice(possible_fruits)
        }
    }