# Microservice
## Steps
1. Install python3
2. Install pip3
3. ```$ pip install -r requirements.txt```
4. ```$ flask --app services/service run```

Flask service is now runnning.

# Example Usage:
*Note: `{robotID}` is either "robot1" or "robot2"
*`<SERVER_IP>` is defaulted to 127.0.0.1 in Flask, but can be manually changed
*`<SERVER_PORT>` is defaulted to 5000 in Flask, but can be manually changed

First, run the server
`python3 server.py` is the easiest. Flask can also be used through the CLI to run server.

Server can either be invoked using the given client files, or using curl.

## Option 1: Client Files

Run the given client file(s)

```python3 client_robot1.py```

```python3 client_robot2.py```
`python3 client_robot#.py`

## Option 2: Using curl
### GET

Get Robot Status by ID
`$ curl http://<SERVER_IP>:<SERVER_PORT>/get_robot_status/{robotID}`

### PUT

Update Robot Status by ID
`curl -X PUT -H "Content-Type: application/json" -d {\"position\":[4,3,1],\"holding_tower\":1,\"in_middle\":1} http://<SERVER_IP>:<SERVER_PORT>/update_robot/{robotID}`


### POST

Due to the nature of this program, POST actions are not supported.

### DELETE

Due to the nature of this program, DELETE actions are not supported.
