from flask_migrate import Migrate

from app.app import create_app, db

app = create_app('tasks')
migrates = Migrate(app, db)
