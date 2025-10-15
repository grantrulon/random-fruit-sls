import random
import json

def lambda_handler(event, context):
    # Returns a random fruit name
    possible_first_names = [
        "Emma",
        "Liam",
        "Sophia",
        "Noah",
        "Olivia",
        "Ethan",
        "Ava",
        "Mason",
        "Isabella",
        "Lucas",
        "Mia",
        "Alexander",
        "Charlotte",
        "James",
        "Amelia",
        "Benjamin",
        "Harper",
        "William",
        "Evelyn",
        "Michael",
        "Abigail",
        "Daniel",
        "Emily",
        "Henry",
        "Elizabeth",
        "Samuel",
        "Sofia",
        "David",
        "Grace",
        "Matthew"
    ]
    possible_last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Wilson",
        "Anderson",
        "Thomas",
        "Taylor",
        "Moore",
        "Jackson",
        "Martin",
        "Lee"
    ]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'data': f"{random.choice(possible_first_names)} {random.choice(possible_last_names)}"
        })
    }