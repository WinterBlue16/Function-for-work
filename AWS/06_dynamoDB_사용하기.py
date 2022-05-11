import boto3

# 1. create table
dynamodb = boto3.resource("dynamodb")

table = dynamodb.create_table(
    TableName='Country',
    # partion key, sort key setting
    KeySchema=[ 
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'continent',
                'KeyType': 'RANGE'
            }
        ],
        # key type setting # don't need to definition of non-key attribute
        AttributeDefinitions=[ 
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'continent',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

table.wait_until_exists()
print(table.item_count)

table_name = "Country"
key_dict = {"name":"Korea", "continent": "Asia"}
data = {"name": "China", "continent": "Asia", "population": 1402, "language": "chinese"}

# create new data
def put_item(table_name: str, data: dict):
    table = dynamodb.Table(table_name)
    print(table.creation_date_time)

    table.put_item(Item=data)
    print("새로운 데이터를 추가하였습니다.")
    return None

# put_item('Country', data)


def get_item(table_name: str, partion_key: str, sort_key: str):
    table = dynamodb.Table(table_name)

    response = table.get_item(Key={"name": partion_key, "continent": sort_key})
    print(response)
    item = response["Item"]
    print(item)


# get_item(table_name, 'Japan', 'Asia')


def update_item(table_name: str, key_dict:dict, column_name: str, value: int):
    table = dynamodb.Table(table_name)
    
    table.update_item(
        Key=key_dict,
        UpdateExpression='SET {} = :vall'.format(column_name),
        ExpressionAttributeValues={
            ':vall': value
        }
    )
    print('데이터가 업데이트되었습니다.')

# update_item(table_name,key_dict, 'population', 234)