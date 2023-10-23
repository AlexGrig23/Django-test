# VNV Test task
Цeb application in Django according to the technical specifications

## Description
The application can be launched in 2 ways, using Docker or locally, but for this you will need to create a database.
The application has 2 pages Users and Groups. The application has 2 pages Users and Groups. 
It is also covered with tests and packaged in Docker containers
Credentials have been added to the .env.example file so that you can deploy the application in 3 clicks.

---
## Installation
**1. Clone the repository:**

   ```shell
   git clone 
   ```

  Create virtual env.

   ```shell
   python -m venv venv
   ```

**2. Create a `.env` file based on the `.env.example` file:**

   ```shell
   cd vnv_test
   ```

   ```shell
   cp .env.example .env
   ```
**3. If you want to run using Docker you must have a Docker desktop**
  
   ```shell
   docker compose build --no-cache
   ```
   
   After that, you must run next command, It builds the images if they are not located locally and starts the containers:

   ```shell
   docker compose up
   ```
   Starting development server at  http://127.0.1:8000/
  
	
**4 If you want to run locally without using docker**

   ```shell
   pip install -r requirements.txt
   ```
**5 You also need to create a PostgreSQL database and enter the credentials in the .env file.
 Additionally, you should update the 'HOST' in the Settings file (vnv_test/settings.py) to match your configuration.**

  ```shell
   cd vnv_test (root)
   ```

  ```shell
   python manage.py makemigrations
   ```

  ```shell
   python manage.py migrate
   ```

  ```shell
   python manage.py runserver
   ```
  Starting development server at  http://127.0.1:8000/

**6 Testing**

If you run using Docker

docker exec -it "CONTAINER ID" sh

```shell
python manage.py test
```

If you using virtual env. 

```shell
python manage.py test
```
