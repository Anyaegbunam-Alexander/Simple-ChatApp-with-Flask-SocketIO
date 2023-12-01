from chatapp import create_app, socketio, db

app = create_app()

with app.app_context():
    db.create_all()

socketio.run(app)
