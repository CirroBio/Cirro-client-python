from cirro_api_client.v1.models import DiscussionInput

test = DiscussionInput.from_dict({
    'name': 'test',
    'description': 'dfd',
    'entity': {
        'type': 'DATASET',
        'id': '3'
    },
    'type': 'dfd',
    'projectId': 'sds'
})
print(test)
