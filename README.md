# Microservice
## Steps
1. Install python3
2. Install pip3
3. ```pip install -r requirements.txt```
4. ```flask --app services/service run```

Flask service is now runnning.

# Example Usage:

This program can either be ran using the given client files, or using curl.

## Option 1: Client Files
Run the given client file(s)

```python3 client_robot1.py```

```python3 client_robot2.py```

## Option 2: Using curl

Note: {robotID} is either robot1 or robot2

### GET

Get Robot Status by ID

```curl <SERVER_IP>:<SERVER_PORT>/get_robot_status/{robotID}```

```curl <SERVER_PORT>:<SERVER_PORT>/get_robot_status/{robotID}```

### PUT

Update Robot Status by ID

```curl -X PUT -H "Content-Type: application/json" -d {\"position\":[4,3,1],\"holding_tower\":1,\"in_middle\":1} <SERVER_ID>:<SERVER_PORT>/update_robot/{ID}```

### POST

Due to the nature of this program, POST actions are not supported.

### DELETE

Due to the nature of this program, DELETE actions are not supported.
