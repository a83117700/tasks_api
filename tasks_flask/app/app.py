from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app(database='tasks'):
    app = Flask(__name__)
    if database == 'tasks':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@db:3306/{}'.format(database)
    if database == 'test':
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.db")
        app.config['WTF_CSRF_ENABLED'] = False

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .models import Tasks

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Tasks.query.all()
        response = [{
            'id': task.id,
            'name': task.name,
            'status': int(task.status)
        } for task in tasks]
        return jsonify({'result': response})

    @app.route('/task', methods=['POST'])
    def create_task():
        name = request.json.get('name')
        task = Tasks(name)
        db.session.add(task)
        db.session.commit()

        response = {
            'id': task.id,
            'name': task.name,
            'status': int(task.status)
        }
        return jsonify({'result': response}), 201

    @app.route('/task/<id>', methods=['PUT'])
    def update_task(id):
        Tasks.query.filter_by(id=id).update({
            'name': request.json.get('name'),
            'status': request.json.get('status'),
        })
        db.session.commit()
        task = Tasks.query.get(id)
        return jsonify({
            'id': task.id,
            'name': task.name,
            'status': int(task.status)
        })

    @app.route('/task/<id>', methods=['DELETE'])
    def delete_task(id):
        task = Tasks.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return Response(status=200)

    return app