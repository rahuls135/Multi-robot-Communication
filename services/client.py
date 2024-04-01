import requests

# Base URL of the microservice
BASE_URL = 'http://127.0.0.1:5000'

# Function to retrieve all tasks
def get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    return response.json()

# Function to create a new task
def create_task(title, description):
    data = {'title': title, 'description': description}
    response = requests.post(f'{BASE_URL}/tasks', json=data)
    return response.json()

# Function to retrieve a specific task by ID
def get_task(task_id):
    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    return response.json()

# Function to update a specific task by ID
def update_task(task_id, title, description):
    data = {'title': title, 'description': description}
    response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=data)
    return response.json()

# Function to delete a specific task by ID
def delete_task(task_id):
    response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
    return response.json()


# Example usage
if __name__ == '__main__':
    # Retrieve all tasks
    print("All tasks:")
    print(get_tasks())

    # Create a new task
    print("\nCreating a new task...")
    task = create_task("New Task", "Description of the new task")
    print("New Task created:", task)

    # Retrieve a specific task by ID
    print("\nRetrieving task with ID 1:")
    task = get_task(1)
    print("Task:", task)

    # Update a specific task by ID
    print("\nUpdating task with ID 1...")
    updated_task = update_task(1, "Updated Task", "Updated description")
    print("Updated Task:", updated_task)

    # Delete a specific task by ID
    print("\nDeleting task with ID 1...")
    response = delete_task(1)
    print(response)

    # Retrieve all tasks after deletion
    print("\nAll tasks after deletion:")
    print(get_tasks())
