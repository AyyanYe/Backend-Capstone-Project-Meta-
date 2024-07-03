# Backend-Capstone-Project-Meta-Certification
# Cafe Management System

## Description
This Django project serves as a management system for a cafe, providing APIs for managing bookings and menu items.

## Features
- **Bookings:** Manage table bookings with customer details and booking times.
- **Menu:** CRUD operations for menu items, including listing and detailed views.

## Technologies Used
- Django
- Django REST Framework
- PostgreSQL (or your preferred database)
- JSON Web Token (JWT) Authentication

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Cafe
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Apply migrations:
   ```bash
   python manage.py migrate
4. Run the development server:
   ```bash
   python manage.py runserver
   
## API Endpoints

## Authentication
- Obtain JWT Token:
    POST /api-token-auth/
    Request Body: { "username": "your_username", "password": "your_password" }
### Booking APIs
- List all bookings:
    GET /restaurant/booking/
- Create a booking:
    POST /restaurant/booking/
    Request Body Example: { "table_number": 1, "customer_name": "John Doe", "booking_time": "2024-07-05T18:00:00Z" }
### Menu APIs
- List all menu items:
    GET /restaurant/menu/
    Retrieve a menu item:
    GET /restaurant/menu/<id>/
## Django URLs
- Admin Interface: /admin/
- REST API Root: /restaurant/
- JWT Authentication: /api-token-auth/
- User Authentication URLs: /auth/
