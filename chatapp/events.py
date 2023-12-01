from flask import request
from flask_login import current_user
from flask_socketio import emit

from .extensions import socketio

@socketio.on("connect")
def handle_connect():
    print("Client connected!")
    emit(current_user.username, broadcast=True)


@socketio.on("user_join")
def handle_user_join():
    print(f"User {current_user.username} joined!")
    emit("user_join", {"username": current_user.username}, broadcast=True)


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected!")
    emit(current_user.username, broadcast=True)

@socketio.on("user_left")
def handle_user_left():
    username = current_user.username
    print(f"User {username} left!")
    emit("user_left", {"username": username}, broadcast=True)


@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = current_user.username
    emit("chat", {"message": message, "username": username}, broadcast=True)
