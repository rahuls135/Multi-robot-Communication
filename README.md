# Sharing Robot Status
## Steps
1. Install python3
2. Install pip3
3. `$ pip3 install -r requirements.txt`
4. Choose 1:
Run via Python3: `$ python3 env/services/sevice.py`
Run via Flask: `$ flask --app env/services/server run`

Server is now runnning.

## Usage
> Hey! This part is required for multiple device connection (2+ computers)!

In services/server_config.py, change `<HOST_URL>` to server device IP. Change `<PORT>` at discretion.

*`<HOST_URL>` is defaulted to 127.0.0.1 in Flask.

*`<PORT>` is defaulted to 5000 in Flask.

-----
Server can either be invoked using the given client files, or using `curl`.

### Option 1: Client Files

Run the given client file(s)

`python3 env/services/client_robot1.py`

`python3 env/services/client_robot2.py`

*These files are still in development. Only a basic functionality is given.

### Option 2: Using curl
*Note: `{robotID}` is either "robot1" or "robot2"
#### GET

Get Robot Status by ID
`$ curl http://<HOST_URL>:<PORT>/get_robot/{robotID}`

#### PUT

Update Robot Status by ID
`$ curl -X PUT -H "Content-Type: application/json" -d {\"position\":[4,3,1],\"holding_tower\":1,\"in_middle\":1} http://<HOST_URL>:<PORT>/update_robot/{robotID}`


#### POST

Due to the nature of this program, POST actions are not supported.

#### DELETE

Due to the nature of this program, DELETE actions are not supported.