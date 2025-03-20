ECOM - E-Commerce Django Application
Overview

ECOM is a feature-rich E-commerce application built using Django. The app supports user authentication, product browsing, registration, login, and profile management. It is designed to serve as a foundational template for developing more advanced e-commerce websites.
Features

    User Authentication: Users can register, log in, and manage their profile.
    Product Catalog: Browse through a list of products.
    Profile Management: Users can view and update their profile details.
    Responsive UI: The app's frontend adapts to different screen sizes for both desktop and mobile users.

Tech Stack

    Backend: Django
    Frontend: HTML, CSS, Bootstrap (optional for styling)
    Database: SQLite (default, can be configured to use other databases like PostgreSQL or MySQL)
    Authentication: Django's built-in authentication system
    Template Engine: Django Templates

Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.6 or higher
    Django 3.0 or higher
    pip (Python package manager)

Installation

Follow these steps to set up the project on your local machine.

    Clone the repository:

git clone https://github.com/yourusername/ECOM.git
cd ECOM

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

    On Windows:

venv\Scripts\activate

On MacOS/Linux:

    source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply migrations to set up the database:

python manage.py migrate

Create a superuser to access the Django admin panel (optional):

python manage.py createsuperuser

Follow the prompts to set up your admin credentials.

Run the development server:

    python manage.py runserver

    You can now access the application at http://127.0.0.1:8000.

Features in Detail
1. User Authentication

    Registration: Users can create an account with their email and password.
    Login: Registered users can log in to access the product catalog and manage their profile.
    Profile Management: After logging in, users can view and update their profile information.

2. Product Catalog

    The app displays a list of products fetched from the database.
    Products have details like name, description, price, and an image.
    Pagination is implemented to display products across multiple pages.

3. Admin Panel (Optional)

    The Django admin panel allows administrators to manage users, products, and other content.
    To access the admin panel, navigate to http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

Folder Structure

Here’s a high-level overview of the folder structure:

ECOM/
│
├── ecom/                    # Main application folder
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates for the application
│   │   └── product_list.html
│   │   └── register.html
│   │   └── login.html
│   │   └── profile.html
│   ├── models.py             # Database models for products and users
│   ├── views.py              # Views for handling requests and responses
│   └── forms.py              # Forms for user registration and profile editing
├── manage.py                # Django’s command-line utility
├── requirements.txt         # Python dependencies
├── db.sqlite3               # Default SQLite database
└── static/                  # Static files (CSS, JavaScript, images)

API Endpoints
1. Registration

    POST /register/
        Registers a new user by providing username, email, and password.

2. Login

    POST /login/
        Logs a user into the system by providing username and password.

3. Profile

    GET /profile/
        Displays the logged-in user's profile page.
    POST /profile/
        Allows the user to update their profile details.

4. Product List

    GET /products/
        Lists all products available in the catalog.

Running Tests

To ensure everything is functioning correctly, run the following command to execute tests:

python manage.py test

Deployment

To deploy this application, you can follow these general steps:

    Set up a production-ready web server like Gunicorn.
    Configure the application to use a production database (e.g., PostgreSQL).
    Set up NGINX or another reverse proxy server to serve static files.
    Ensure proper security measures, like enabling DEBUG = False in production and using secure cookies.

Contributing

Contributions are welcome! If you'd like to improve the project or fix a bug, please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a pull request.
