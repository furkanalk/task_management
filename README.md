# bookstore_api that works with OAUTH2

**********************************************
# Authentication:
Register: ``` POST ```
```
localhost:8000/api/auth/register
```
```
{
    "username": "<username>",
    "email": "<email>",
    "password": "<password>"
    "role": "<role>"
}
```
Login: ``` POST ```
```
localhost:8000/api/auth/login
```
```
{
    "username": "<username>",
    "password": "<password>"
}
```
**********************************************
# Available commands for Authenticated Users:

Shows Users' their task: ``` GET ```
```
127.0.0.1:8000/api/mytask
```
Users can update their task status: ``` PUT ```
```
localhost:8000/api/mytask/status
```
```
{
    "status": "<status>"
}
```
> Status must be one of the following:
```
    idle',
    'to Do',
    'in Progress',
    'Done'
```
**********************************************
# Available commands for Admin Users:

Show all the Users: ``` GET ```
```
localhost:8000/api/users
```
Add a new User: ``` POST ```
```
localhost:8000/api/users/add
```
```
{
    "username": "<username>",
    "email": "<email>",
    "password": "<password>"
    "role": "<role>"
}
```
Get or delete a certain User: ``` GET ``` ``` DELETE ```
```
localhost:8000/api/users/<pk>
```
Update a certain User: ``` PUT ```
```
localhost:8000/api/users/<pk>
```
```
{
    "username": "<username>",
    "email": "<email>",
    "role": "<role>"
}
```
Add a new Task: ``` POST ```
```
localhost:8000/api/tasks/add
```
```
{
			"task_name": "<task-name>",
			"task_description": "<description>",
			"due_date": "<date>",
			"assignee": <id of the user>,
			"status": "<status>"
}
```
> Status must be one of the following:
```
    idle',
    'to Do',
    'in Progress',
    'Done'
```
Get or delete a certain task: ``` GET ``` ``` DELETE ```
```
localhost:8000/api/tasks/<pk>
```
Update a certain Task: ``` PUT ``` 
```
localhost:8000/api/books/<pk>
```
```
{
      id": <task-id>,
			"task_name": "<task-name>",
			"task_description": "<description>",
			"due_date": "<date>",
			"assignee": <id of the user>,
			"status": "<status>"
}
```
> Status must be one of the following:
```
    idle',
    'to Do',
    'in Progress',
    'Done'
```
