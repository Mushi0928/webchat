from flask import Flask, render_template
from flask_socketio import SocketIO , join_room , leave_room ,send ,emit
import eventlet

eventlet.monkey_patch()
app = Flask(__name__)
socketio = SocketIO(app,async_mode='eventlet')
socketio.init_app(app, cors_allowed_origins="*")
ROOMS = {}

@app.route('/')
def home():
    return render_template('/test/test.html')
    
@socketio.on('msg')
def message(msg):
    print(msg['text'])
    emit('msg',msg['text'],room = msg['room'])
    return
@socketio.on('connect')
def connect():
    print('connect')
    return
@socketio.on('join')
def on_join(data):
    join_room(data)
    print(data )
    emit('msg','weed',room=data)
    return
    

print('run')
socketio.run(app,debug=True,host="0.0.0.0",port=80)