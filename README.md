# Todo App

A simple Todo App built with Django, HTML, CSS, and JavaScript. This application allows users to manage their tasks by adding, editing, and deleting todos.

## Features

- **Add Todo**: Users can add new tasks to their todo list.
- **Edit Todo**: Users can update the details of their existing tasks.
- **Delete Todo**: Users can remove tasks from their todo list.
- **Responsive Design**: The app is designed to be responsive and works on both desktop and mobile devices.
- **User Authentication**: Users can register, log in, and log out to manage their own todo lists (optional feature).
  
## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default with Django, can be changed to PostgreSQL, MySQL, etc.)
- **Environment Management**: Python-dotenv

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python  3.11.9
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**:

   git clone https://github.com/yourusername/todoapp.git
   cd todoapp

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

pip install -r requirements.txt

Set up environment variables:


Apply migrations:
python manage.py migrate
Create a superuser (optional, for admin access):
python manage.py createsuperuser

Run the development server:
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to see the app in action.

