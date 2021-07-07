import unittest
from flask_testing import TestCase
import json

from app.app import create_app, db
from app.models import Tasks


class TestModule(TestCase):
    def create_app(self):
        return create_app('test')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_list_tasks(self):
        task = Tasks("name")
        db.session.add(task)
        db.session.commit()

        response = self.client.get("http://127.0.0.1:8080/tasks")
        self.assertEquals(response.status_code, 200)

        test_result = {
            "result": [
                {"id": 1, "name": "name", "status": 0}
            ]
        }
        self.assertEquals(json.loads(response.data), test_result)

    def test_create_task(self):
        response = self.client.post(
            "http://127.0.0.1:8080/task",
            json={
                "name": "買晚餐"
            }
        )
        self.assertEquals(response.status_code, 201)

        test_result = {
            "result": {
                "id": 1,
                "name": "買晚餐",
                "status": 0
            }
        }
        self.assertEquals(json.loads(response.data), test_result)

    def test_update_task(self):
        task = Tasks("買早餐")
        db.session.add(task)
        db.session.commit()

        response = self.client.put(
            "http://127.0.0.1:8080/task/1",
            json={
                "name": "買早餐",
                "status": 1
            }
        )
        self.assertEquals(response.status_code, 200)

        test_result = {
            "id": 1,
            "name": "買早餐",
            "status": 1
        }
        self.assertEquals(json.loads(response.data), test_result)

    def test_delete_task(self):
        task = Tasks("買早餐")
        db.session.add(task)
        db.session.commit()

        response = self.client.delete("http://127.0.0.1:8080/task/1")
        self.assertEquals(response.status_code, 200)

        self.assertEquals(Tasks.query.get(1), None)


if __name__ == '__main__':
    unittest.main()
