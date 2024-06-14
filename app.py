from flask import Flask, render_template, jsonify
import threading
import time

app = Flask(__name__)

# Shared state to store the style information
style_info = {
    "color": "blue",
    "fontSize": "20px",
    "fontWeight": "normal"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change_style', methods=['POST'])
def change_style():
    global style_info
    # Initial style change
    new_style = {
        "color": "red",
        "fontSize": "24px",
        "fontWeight": "bold"
    }
    style_info = new_style

    # Start the background task to change the style after 3 seconds
    threading.Thread(target=delayed_style_change).start()

    return jsonify(new_style)

@app.route('/get_current_style', methods=['GET'])
def get_current_style():
    return jsonify(style_info)

def delayed_style_change():
    time.sleep(3)  # Wait for 3 seconds
    global style_info
    # New style after delay
    style_info = {
        "color": "green",
        "fontSize": "28px",
        "fontWeight": "bold"
    }

if __name__ == '__main__':
    app.run(debug=True)
