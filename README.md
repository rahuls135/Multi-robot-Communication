# Microservice
## Steps
1. Install python3
2. Install pip3
3. ```pip install -r requirements.txt```
4. ```flask --app services/app run```

Flask service is now runnning.

## Example Usage:

Run the given client file

```python3 client.py```

Using curl

### GET

Get all Tasks

```curl http://127.0.0.1:5000/tasks```

Get Task by ID

```curl http://127.0.0.1:5000/tasks/1```

### POST

Post task. Required to create JSON.

```curl -X POST -H "Content-Type: application/json" -d '{"title":"Task 1", "description":"Description of Task 1"}' http://127.0.0.1:5000/tasks```

### PUT

Update Task by ID

```curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Task 1", "description":"Updated description of Task 1"}' http://127.0.0.1:5000/tasks/1```
### DELETE

Del Task by ID

```curl -X DELETE http://127.0.0.1:5000/tasks/1```
