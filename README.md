# Coding Exercise
Implement a Restful task list API as well as run this application in container.

### Run Service
```shell script
docker-compose up #--build
```
*如果執行 `docker-compose dowm -v` 砍掉 volume 的話<br/>
要重啟 service 時有可能會因為 db 建的太慢造成 flask error<br/>
只要等 db container healthy 後再執行 `docker-compose up` 即可 

### DB Migration
```shell script
docker exec -it $(docker ps | grep tasks_api_flask | awk '{print $1}') bash -c "flask db migrate;flask db upgrade"
```

### Unit Test
```shell script
docker exec -it $(docker ps | grep tasks_api_flask | awk '{print $1}') bash -c "python -m unittest test/test_module.py"
```

### Api
Nginx container expose on port 80
```http request
http://localhost/tasks
```