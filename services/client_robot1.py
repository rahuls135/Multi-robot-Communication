import requests
import time

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
    # Updates Robot1, Gets Robot2

    # Retrieve status of robot2
    print("Status of robot2:")
    print(get_robot_status('robot2'))

    # Retrieve position of robot1
    print("\nPosition of robot1:")
    print(get_robot_attribute('robot1', 'pos'))

    # Update status of robot1
    print("\nUpdating status of robot1... pos: [1,2,3] and holding tower")
    update_data = {'pos': [1, 2, 3], 'holding_tower': 1, 'in_middle': 0}
    update_robot_status('robot1', update_data)

     # Update position of robot1
    print("\n robot1 now in middle...")
    update_robot_attribute('robot1', 'in_middle', 1)


    # Retrieve updated status of robot1
    print("\nUpdated status of robot2:")
    print(get_robot_status('robot2'))

    print("Is robot2 holding the tower?")
    print("yes" if get_robot_status('robot2')['holding_tower'] else "no")

    while (True):
        pass

if __name__ == '__main__':
    main()