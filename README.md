Little Lemon API – Test Endpoints in Insomnia
---------------------------------------------

This project contains backend APIs for the Little Lemon restaurant app.  
Use the URLs below to test the API in Insomnia.

---------------------------------
Authentication Endpoints
---------------------------------

1️. Register a new user
  POST http://localhost:8000/auth/users/
  Body (JSON):
  {
    "username": "yourusername",
    "password": "yourpassword",
    "email": "you@example.com"
  }

2️. Login to get authentication token
  POST http://localhost:8000/auth/token/login/
  Body (JSON):
  {
    "username": "yourusername",
    "password": "yourpassword"
  }
  Response example:
  {
    "auth_token": "123abc456xyz"
  }
  
In Insomnia, copy the token.  
Go to the **Header** section:  
Key: `Authorization`  
Value: `Token 123abc456xyz`  
Replace `123abc456xyz` with the token you received.  
You can now test endpoints that require authentication.

3️. Alternative login endpoint
  POST http://localhost:8000/restaurant/api-token-auth/
  Body (JSON):
  {
    "username": "yourusername",
    "password": "yourpassword"
  }

---------------------------------
Menu Item Endpoints (No Auth Required)
---------------------------------

GET http://localhost:8000/restaurant/menu-items/
    - Get a list of all menu items

POST http://localhost:8000/restaurant/menu-items/
Body (JSON):
{
  "title": "Pizza Margherita",
  "price": 12.50,
  "inventory": 10
}

GET http://localhost:8000/restaurant/menu-items/<id>/
    - Get details of a single menu item by ID

PUT http://localhost:8000/restaurant/menu-items/<id>/
Body (JSON):
{
  "title": "Updated Pizza",
  "price": 13.00,
  "inventory": 15
}

DELETE http://localhost:8000/restaurant/menu-items/<id>/
    - Delete a menu item

---------------------------------
Booking Endpoints (Authentication Required)
---------------------------------

GET http://localhost:8000/restaurant/booking/tables/
    - Get all bookings

POST http://localhost:8000/restaurant/booking/tables/
Body (JSON):
{
  "name": "John Doe",
  "number_of_guests": 4,
  "booking_date": "2025-12-05T19:00:00Z"
}

GET http://localhost:8000/restaurant/booking/tables/<id>/
    - Get a single booking

PUT http://localhost:8000/restaurant/booking/tables/<id>/
Body (JSON):
{
  "name": "Jane Doe",
  "number_of_guests": 5,
  "booking_date": "2025-12-06T20:00:00Z"
}

DELETE http://localhost:8000/restaurant/booking/tables/<id>/
    - Delete a booking

---------------------------------
Homepage
---------------------------------

GET http://localhost:8000/restaurant/
    - Loads the homepage template

---------------------------------
Insomnia Notes
---------------------------------

1. Create a new workspace in Insomnia: **Little Lemon API**  
2. For endpoints requiring authentication:
3. Go to the **Header** section:  
  Key: `Authorization`  
  Value: `Token 123abc456xyz`  
  Replace `123abc456xyz` with the token you received.  
4. Test each endpoint using GET, POST, PUT, DELETE methods  
5. For POST/PUT requests, select **JSON** in the body tab  

