from flask import Flask, render_template, request, jsonify
from processInputQuery import getFinalAnswer

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/api/chat',methods=['POST'])
def chatbot():
    data = request.get_json()
    query = data.get('prompt')
    response = getFinalAnswer(query)
    return jsonify({"response":response})

# def calculate(msg):
#     return str(int(msg)**2)

# @socketio.on('message')
# def handle_message(msg):
#     print(f"Received message: {msg}")  # Log the message to the server console
#     ans = calculate(msg)
#     send(ans, broadcast=True)  # Broadcast the message to all connected clients

if __name__ == '__main__':
     app.run(host='127.0.0.1',port=4444)
