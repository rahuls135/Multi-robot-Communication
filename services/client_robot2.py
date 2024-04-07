import requests

# Base URL of the Flask API
BASE_URL = 'http://127.0.0.1:5000'

# Function to retrieve status of a robot
def get_robot_status(robot_id):
    response = requests.get(f'{BASE_URL}/robot/{robot_id}')
    return response.json()

# Function to retrieve status of a specific attribute of a robot
def get_robot_attribute(robot_id, attribute):
    response = requests.get(f'{BASE_URL}/robot/{robot_id}/{attribute}')
    return response.json()

# Function to update status of a robot
def update_robot_status(robot_id, data):
    response = requests.put(f'{BASE_URL}/robot/{robot_id}', json=data)
    return response.json()

# Function to update status of a robot
def update_robot_attribute(robot_id, attribute, value):
    data = {attribute: value}
    response = requests.put(f'{BASE_URL}/robot/{robot_id}', json=data)
    return response.json()

def main():
    # Updates Robot2, Gets Robot1

    # Retrieve status of robot1
    print("Status of robot1:")
    print(get_robot_status('robot1'))

    # Update status of robot1
    print("\nUpdating status of robot2... pos: [1,2,1] and in middle")
    update_data = {'pos': [1, 2, 3], 'in_middle': 0}
    update_robot_status('robot1', update_data)

    #  # Update position of robot2
    # print("\n robot2 now in middle...")
    # update_robot_attribute('robot2', 'in_middle', 1)


    # Retrieve updated status of robot2
    print("\nUpdated status of robot2:")
    print(get_robot_status('robot2'))

    print("Is robot1 holding the tower?")
    print("yes" if get_robot_status('robot1')['holding_tower'] else "no")

    while (True):
        pass
    
if __name__ == '__main__':
    main()