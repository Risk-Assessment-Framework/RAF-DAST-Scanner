from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

logged_events = []

@app.route('/log_event', methods=['POST'])
def log_event():
    """
    - timestamp
    - source_ip
    - event_type
    - description
    """
    data = request.get_json()
    timestamp = datetime.fromisoformat(data['timestamp'])
    source_ip = data['source_ip']
    event_type = data['event_type']
    description = data['description']

    event = {
        'timestamp': timestamp,
        'source_ip': source_ip,
        'event_type': event_type,
        'description': description
    }
    logged_events.append(event)

    return jsonify({'status': 'success'})

@app.route('/get_events', methods=['GET'])
def get_events():
    """
    - start_time
    - end_time
    - event_type
    """
    start_time_str = request.args.get('start_time')
    end_time_str = request.args.get('end_time')
    event_type = request.args.get('event_type')

    if start_time_str is not None:
        start_time = datetime.fromisoformat(start_time_str)
    else:
        start_time = datetime.min
    if end_time_str is not None:
        end_time = datetime.fromisoformat(end_time_str)
    else:
        end_time = datetime.max

    filtered_events = []
    for event in logged_events:
        if start_time <= event['timestamp'] <= end_time:
            if event_type is None or event['event_type'] == event_type:
                filtered_events.append(event)

    return jsonify({'events': filtered_events})

if __name__ == '__main__':
    app.run()
