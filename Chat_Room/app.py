from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] == 'dfnvaolofafo'
app.secret_key = 'foannbaoeap'
socketio = SocketIO(app)

rooms = {} #store info about rooms (we store our data here in RAM )
def  generate_unique_code(length): 
    #take length of string which we need to generate as a name for our room
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:   #check if this room is already exist
            break
    return code



@app.route("/", methods=['POST', 'GET'])
def home():
    #session.clear()
    if request.method =='POST':
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)  #change default none to false if we didn't get anything
        create = request.form.get("create", False)
        if not name:
            return render_template("home.html" , error='Please enter a name' , code = code , name = name)
        if join != False and not code:
            return render_template("home.html" , error = "Please enter a room code",code = code , name = name)
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members":0 , "messages":[] }
        elif code not in rooms:
            return render_template("home.html", error = "Room does not exist",code = code , name = name)
        #session is used to store data on server
        session['room'] = room 
        session['name'] = name
        return redirect(url_for("room"))
    
    return render_template("home.html")


@app.route("/room")  
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))
    return render_template("room.html" , code=room, messages=rooms[room]["messages"])

#show my entered message to all members of the room
@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    content = {
        "name": session.get("name"),
        "message": data["data"],
    }
    send(content , to=room)
    rooms[room]["messages"].append(content)
    # print(f"{session.get('name')} said: {data['data']}")

#join an existing room
@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({"name": name, "message":"has entered the room"} , to=room)
    rooms[room]["members"] += 1
    # print(f"{name} joined room {room}")

#leaving a room
@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)
    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    send({"name": name, "message":"has left the room"} , to=room)
    # print(f"{name} has left the room {room}")

if __name__ == "__main__":
    socketio.run(app, debug=True)
 