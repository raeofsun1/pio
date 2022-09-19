
# Product IO

A simple working api with 22 endpoints, specifically designed for Product IO website.
With logical database django models using the inbuilt sqllite3 databse in django.




## Available endpoints
I am using a local host with 8000 port so all my endpoints would be starting with http://127.0.0.1:8000/

## User API endpoints

- UserList http://127.0.0.1:8000/user_list
- UserUpdate http://127.0.0.1:8000/user_update/<int:pk>/
- UserCreate http://127.0.0.1:8000/user_create/<int:pk>/
- UserDelete http://127.0.0.1:8000/user_delete/<int:pk>/
- UserOrder http://127.0.0.1:8000/order_user_list

## Seller API endpoints

- sellerList http://127.0.0.1:8000/seller_list
- sellerCreate http://127.0.0.1:8000/seller_create/<int:pk>/
- sellerDelete http://127.0.0.1:8000/seller_delete/<int:pk>/
- sellerOrder http://127.0.0.1:8000/seller_order_list

## Product API endpoints

- productList http://127.0.0.1:8000/product_list
- productCreate http://127.0.0.1:8000/product_create/<int:pk>/
- productDelete http://127.0.0.1:8000/product_delete/<int:pk>/

## ProductSeller API endpoints

- product_sellerList http://127.0.0.1:8000/product_seller_list
- product_sellerCreate http://127.0.0.1:8000/product_seller_create/<int:pk>/
- product_sellerDelete http://127.0.0.1:8000/product_seller_delete/<int:pk>/

## Order API endpoints

- orderList http://127.0.0.1:8000/order_list
- orderCreate http://127.0.0.1:8000/order_create/<int:pk>/
- orderDelete http://127.0.0.1:8000/order_delete/<int:pk>/

## Address API endpoints

- addressList http://127.0.0.1:8000/address_list
- addressCreate http://127.0.0.1:8000/address_create/<int:pk>/
- addressDelete http://127.0.0.1:8000/address_delete/<int:pk>/


## Installation

Install my-project with pip

```bash
  pip install requirements.txt
  python manage.py runserver
```
    
