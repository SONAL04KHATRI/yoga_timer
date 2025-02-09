from flask import Flask, render_template, request, jsonify
import time
import threading

app = Flask(__name__)

# Timer variables
time_left = 0
running = False

def countdown():
    global time_left, running
    while running and time_left > 0:
        time.sleep(1)
        time_left -= 1
    running = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_timer():
    global time_left, running
    data = request.get_json()
    time_left = int(data['minutes']) * 60
    running = True
    threading.Thread(target=countdown).start()
    return jsonify({'message': 'Timer started', 'time_left': time_left})

@app.route('/pause', methods=['POST'])
def pause_timer():
    global running
    running = False
    return jsonify({'message': 'Timer paused', 'time_left': time_left})

@app.route('/reset', methods=['POST'])
def reset_timer():
    global time_left, running
    running = False
    time_left = 0
    return jsonify({'message': 'Timer reset'})

if __name__ == '__main__':
    app.run(debug=True)
