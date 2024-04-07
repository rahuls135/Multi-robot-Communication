# Microservice
## Steps
1. Install python3
2. Install pip3
3. ```pip install -r requirements.txt```
4. ```flask --app services/service run```

Flask service is now runnning.

## Example Usage:

Run the given client file(s)

```python3 client_robot#.py```

Using curl

### GET

Get Robot Status by ID

```curl http://127.0.0.1:5000/get_robot_status/{ID}```
```curl http://127.0.0.1:5000/get_robot_status/{ID}```

### PUT

Update Robot Status by ID

```curl -X PUT -H "Content-Type: application/json" -d '{"pos":[7,8,9]], "holding_tower":1, "in_middle":1}' http://127.0.0.1:5000/update_robot_status/{ID}```


### POST

Due to the nature of this program, POST actions are not supported.

### DELETE

Due to the nature of this program, DELETE actions are not supported.