# Online Store Backend API (Django): 
___
## General description
___
The project is an online store in the field of fishing and tourism from fishing rods, spinning rods and reels to motor boats and tents and much more. The project supports the main functionality, the presence of a showcase with a description of the product, carts, and a user’s personal account.
## Start
___
Clone the repo: ***git clone*** **https://github.com/Petrarko44/online-store**

Use a virtual environment that you prefere.

Install the required packages:
```shell
pip install -r requirements.txt
```
Apply migrations:
```shell
python manage.py migrate
```
Create an admin user:
```shell
python manage.py createsuperuser
```
Run the server:
```shell
python manage.py runserver
```
## Endpoints ##

```http request

        'auth'/
        POST: 'token/login/'        
        GET/POST: 'users/'                  | list users, create user
        PUT/PATCH/DELETE: 'users/me/'       | update/delete auth user
        

        'goods/' 
        GET: 'goods'                        | get all products
        POST: 'goods'                       | create new product
        GET/PATCH/DELETE: 'goods/{id}'      | get/change a product
        GET: 'type'                         | get all types
        POST: 'type'                        | create new type
        GET/PATCH/DELETE:  'type/{id}'      | get/change a type
        GET: 'category'                     | get all categories
        POST: 'category'                    | create new category
        GET/PATCH/DELETE:  'category/{id}'  | get/change a category
        GET: 'subcategory'                  | get all subcategories
        POST: subcategory'                  | create new subcategory
        GET/PATCH/DELETE: 'subcategory/{id}'| get/change a subcategory
        GET: 'brand'                        | get all brands
        POST: 'brand'                       | create new brand
        GET/PATCH/DELETE: 'brand/{id}'      | get/change a brand

        'orders/'
        GET: 'orders'                       | get all orders
        POST: 'orders'                      | create new order
        GET/PATCH/DELETE:  'orders/{id}'    | get/change a order
        GET: 'orders_item'                  | get all orders item
        POST: 'orders_item'                 | create new order item
        GET/PATCH/DELETE: 'orders_item/{id}'| get/change a order item

        'carts/'
        GET: 'cart'                         | get all carts
        POST: 'cart'                        | create new cart
        GET/PATCH/DELETE: 'cart/{id}'       | get/change a cart
        
        