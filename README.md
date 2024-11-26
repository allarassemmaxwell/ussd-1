# Django USSD System

[![CI/CD Workflow Status](https://github.com/allarassemmaxwell/ussd-1/blob/main/.github/workflows/ci_cd.yml/badge.svg)](https://github.com/allarassemmaxwell/ussd-1/blob/main/.github/workflows/ci_cd.yml)

This is a Django-based application that provides a USSD interface using Africa's Talking API. The app allows users to interact with a menu and make payments, check balances, or perform other actions via a USSD interface.

Requirements

Python 3.x
Docker (for running the app in a containerized environment)
Docker Compose (optional, for managing multi-container environments)
Setup Instructions

1. Clone the repository

```
git clone https://github.com/allarassemmaxwell/olepaipai-backend.git
cd olepaipai-backend
```

2. Build and start Docker containers
Ensure Docker and Docker Compose are installed, then build and run the containers.

```
docker-compose up --build

```

This will build the Docker image and start the containers for your Django app, PostgreSQL (if you're using it), and any other services defined in docker-compose.yml.

3. Configure Environment Variables
Create a .env file in the root directory (next to docker-compose.yml) and include the following variables:

```
USSD_USERNAME=sandbox
USSD_API_KEY=your_africastalking_api_key
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=your_allowed_hosts
DATABASE_URL=postgres://user:password@db:5432/dbname

```

Replace sandbox and your_africastalking_api_key with your Africa’s Talking credentials.
Set the DJANGO_SECRET_KEY to a secret value (you can generate one online).
Ensure the database URL is configured if you're using PostgreSQL.
4. Running the Application
Once the containers are up, the Django app should be available at the following address:
```
http://localhost:8000
```
5. Running Django Admin
To access Django admin, create a superuser in your container:
```
docker-compose exec web python manage.py createsuperuser

```
Follow the prompts to set the username, email, and password.

6. Testing the USSD Menu
To test the USSD functionality, you’ll need to use a service like Ngrok to expose your local server, or configure your production server to handle incoming requests to the /ussd/ endpoint.

7. Stopping the Containers
When you're done, stop the containers by running:
```
docker-compose down

```

Technologies Used

Django
Africa’s Talking API (for USSD functionality)
Docker
PostgreSQL (optional for database)
Gunicorn (for serving the application in production)