***Task Management System***
*Getting Started*

1. For sure having python installed is necessary. Please place project file in a directory.

2. Please setup project environment with virtualenv and pip:

py -m venv env

Mac OS / Linux: source env/bin/activate

Windows: .\env\Scripts\activate.bat

3. Change directory to project directory:

cd final_project\taskmanagement

4. Install requirements, migrate and run server on local host:

py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver

The server should be running on http://127.0.0.1:8000


**Overview**
This project is a small task management. It was built using Django and DRF and contains the following:

1. There are 2 users defined in this project which can be used for login:
user1:
username: admin
pass: Admin123

user2:
username: goli
pass:Gf123456

In order to add more users to login, we can type below command on cmd while we are in the project directory:

py manage.py createsuperuser

Then we should define a username, email & password. After that we can login with the new username & password in the system.

2. Each user can create, edit any delete any of his/her tasks.
3. Unauthenticated users can only see list of tasks and their details (not status) and they cannot edit/delete the task.
4. Each user can search on task title and description.
5. Each user can set his/her task status and see its history on task detail page.
6. All other mentioned requirements in the project description.
7. Link to my project on GitHub in order to clone from GitHub:
 https://github.com/goliF/final_project
8. I have done a part from Bonus Points and I have setup my project on pythonanywhere server:
 http://goli.pythonanywhere.com/


**Notes**
- I have defined separate API endpoints for create, list, update and delete as I wanted to personalized them and use Bootstrap, HTML & CSS... UI pages on each page.

- I have 2 models in addition to user model which are Task & Status. User can select a status for his/her task from a predefined values in a dropdown menu  and can see its history of status changes.in task detail page. This option is only visible for owner of the task.
