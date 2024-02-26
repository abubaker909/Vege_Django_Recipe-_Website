
# Django Receipes App

This is a Django web application for managing and displaying receipes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to [http://localhost:8000/](http://localhost:8000/) to view the app.

## Usage

- Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) using the superuser credentials.
- Add, update, and delete receipes through the admin panel.
- View all receipes at [http://localhost:8000/getAll/](http://localhost:8000/getAll/).
- View details of a single receipe at [http://localhost:8000/getOne/<id>/](http://localhost:8000/getOne/<id>/).

## Features

- Create, update, and delete receipes.
- Upload and display receipe images.
- Admin panel for easy management.
- ...

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
