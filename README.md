# Coding Exercise
Implement a Restful task list API as well as run this application in container.

### Run Service
```shell script
docker-compose up #--build
```

### DB Migration
```shell script
docker exec -it $(docker ps | grep coding_exercise_flask | awk '{print $1}') bash -c "flask db migrate;flask db upgrade"
```

### Unit Test
```shell script
docker exec -it $(docker ps | grep coding_exercise_flask | awk '{print $1}') bash -c "python -m unittest test/test_module.py"
```

### Api
Nginx container expose on port 80
```http request
http://localhost/tasks
```