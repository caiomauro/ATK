# Agent Toolkit (ATK)

Agent Toolkit (ATK) is a web-based toolbox designed for the Geek Squad, enabling them to create drives and download front desk software efficiently.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

```bash
pip install django
pip install djangorestframework
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install psycopg2-binary
pip install psycopg
```

## Description

ATK is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The tool is integrated with various modules and functionalities, including user authentication, forum post creation, and deletion. Users with staff privileges can manage posts effectively.

## Features
User authentication and authorization
Creation and deletion of forum posts
User-specific functionalities

## Usage
After installing the required dependencies, you can run the ATK application by executing the following command:

```bash
python manage.py runserver
```

Once the server is running, you can access the ATK application by visiting the following URL in your web browser:

```
http://127.0.0.1:8000/
```

## License
This project is licensed under the MIT license.
