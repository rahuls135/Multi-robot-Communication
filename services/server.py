from flask import Flask, jsonify, request
from server_config import HOST_URL, PORT

app = Flask(__name__)

# Initial statuses of two robots
robot_statuses = {
    'robot1': {
        'pos': [0, 0, 0],
        'holding_tower': 0,
        'in_middle': 0
    },
    'robot2': {
        'pos': [0, 0, 0],
        'holding_tower': 0,
        'in_middle': 0
    }
}

@app.route('/get_robot/<robot_id>', methods=['GET'])
def get_robot_status(robot_id):
    if robot_id not in robot_statuses:
        return jsonify({'error': 'Robot not found'}), 404
    return jsonify(robot_statuses[robot_id])


@app.route('/update_robot/<robot_id>', methods=['PUT'])
def update_robot_status(robot_id):
    if robot_id not in robot_statuses:
        return jsonify({'error': 'Robot not found'}), 404
    data = request.json
    robot_statuses[robot_id].update(data)
    return jsonify({'message': f'Status of {robot_id} updated successfully'})


@app.route('/get_robot/<robot_id>/<attribute>', methods=['GET'])
def get_robot_attribute(robot_id, attribute):
    if robot_id not in robot_statuses:
        return jsonify({'error': 'Robot not found'}), 404
    if attribute not in robot_statuses[robot_id]:
        return jsonify({'error': 'Attribute not found'}), 404
    return jsonify({attribute: robot_statuses[robot_id][attribute]})


if __name__ == '__main__':
    app.run(debug=True, host=HOST_URL, port=PORT)
