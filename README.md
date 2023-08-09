# Task Management API

**********************************************
# Authentication: ``` OAUTH2 ```
Register: ``` POST ```
```
localhost:8000/auth/register
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
localhost:8000/auth/login
```
```
{
	"username": "<username>",
	"password": "<password>"
}
```
**********************************************
# Available commands for Authenticated Users:

Users can see their tasks: ``` GET ```
```
localhost:8000/mytask
```
Users can update their task status: ``` PUT ```
```
localhost:8000/mytask/status
```
```
{
	"status": "<status>"
}
```
> Status must be one of the following:
```
	'idle',
	'to Do',
	'in Progress',
	'Done'
```
**********************************************
# Available commands for Admin Users:

Show all the Users: ``` GET ```
```
localhost:8000/users
```
Add a new User: ``` POST ```
```
localhost:8000/users/add
```
```
{
	"username": "<username>",
    "email": "<email>",
    "password": "<password>",
	"role": "<role>"
}
```
Get or delete a certain User: ``` GET ``` ``` DELETE ```
```
localhost:8000/users/<pk>
```
Update a certain User: ``` PUT ```
```
localhost:8000/users/<pk>
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
localhost:8000/tasks/add
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
	'idle',
	'to Do',
	'in Progress',
	'Done'
```
Get or delete a certain task: ``` GET ``` ``` DELETE ```
```
localhost:8000/tasks/<pk>
```
Update a certain Task: ``` PUT ``` 
```
localhost:8000/tasks/<pk>
```
```
{
	"id": <task-id>,
	"task_name": "<task-name>",
	"task_description": "<description>",
	"due_date": "<date>",
	"assignee": <id of the user>,
	"status": "<status>"
}
```
> Status must be one of the following:
```
	'idle',
	'to Do',
	'in Progress',
	'Done'
```
