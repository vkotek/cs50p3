# cs50p3 - Pizzeria

## Setup
pip install -r requirements.txt
python manage.py loaddata data.json


## Overview

- Build using [Materialize]() - A modern responsive front-end framework based on Material Design
- Using rest_framework to manage backend API calls

### Structure
- eshop - Primary app holding all models except user
- user - Views for user management (authentication, registration, etc)
- api - Back-end API for AJAX calls from the front-end
- kitchen - Kitchen view to manage all orders
  
### Entity Relationship Diagram
![](images/ERD.png)

### Process Flow - Add item to Cart
![](images/process_flow.png)

### User Management
- Username is automatically populated with email value on backend

### Order Management
- Items added to cart are created in OrderLine but without an order ID
- Once order is submitted, a Order record is created and the order id for OrderLine items for given user are populated

### Extras
- The 'Special' pizza allows 5 toppings
- Up to 5 paid toppings can be added to any sub
