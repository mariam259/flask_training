# Flask Chat Room Application

This project is a simple chat room application built using Flask and Flask-SocketIO. It allows users to join chat rooms, send messages, and receive real-time updates.

**Features:**

* **Real-time messaging:** Users can send and receive messages in real time using WebSocket technology.
* **Chat rooms:** Users can join and create chat rooms to communicate with specific groups of people.
* **User interface:** A basic user interface is created using Ninja Templates, allowing users to enter or create chat rooms and interact with the chat.

**Technologies Used:**

* **Flask:** Python web framework for building the application.
* **Flask-SocketIO:** Extension for Flask that enables real-time, bidirectional communication.
* **Ninja Templates:** Template engine for creating the user interface.
* **Python:** Programming language for backend development.

**Project Structure:**

* `app.py`: Main application file containing Flask and SocketIO configurations, routes, and event handlers.
* `templates/`: Directory containing HTML templates for the home screen and chat room.
* `static/`: Directory for storing static assets for CSS styling.


**Explanation of Endpoints:**

* **`@app.route("/", methods=['POST', 'GET'])` (home route):**
    * Handles GET and POST requests for the home page.
    * Renders the "home.html" template.
    * Processes user input for name, and room code (join or create).
    * Validates user input (name and room code for joining).
    * Uses sessions to store the user's name and room information.
    * Redirects to the chat room (`/room`) upon successful validation.

* **`@app.route("/room")` (room route):**
    * Renders the "room.html" template for the chat room.
    * Retrieves room information and messages from the session and application data structure (`rooms`).
    * Requires a valid room code and user name in the session to access the chat room.

* **`@socketio.on("message")` (message event handler):**
    * Handles incoming messages sent by the user through the socket connection.
    * Retrieves the room information from the session.
    * Validates if the room exists.
    * Constructs a message object containing the user's name and message content.
    * Broadcasts the message to all members of the room using `send` with the room as the target.
    * Appends the message to the room's message history stored in `rooms`.

* **`@socketio.on("connect")` (connect event handler):**
    * Triggers when a user connects to the socket.
    * Retrieves room and user information from the session.
    * Validates if the room exists and the user information is present.
    * Joins the user to the specified room using `join_room`.
    * Broadcasts a message indicating the user has entered the room to all members of the room.
    * Increments the member count for the room.

* **`@socketio.on("disconnect")` (disconnect event handler):**
    * Triggers when a user disconnects from the socket.
    * Retrieves room and user information from the session.
    * Leaves the user from the room using `leave_room`.
    * Decrements the member count for the room.
    * If the room becomes empty (member count reaches 0), it's removed from the `rooms` data structure.
    * Broadcasts a message indicating the user has left the room to all remaining members of the room.
