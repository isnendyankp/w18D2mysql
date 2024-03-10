from flask import Blueprint, render_template, request
from connectors.mysql_connector import Session

from models.product import Product
from sqlalchemy import select

product_routes = Blueprint('product_routes',__name__)

# Get method for the product home page
@product_routes.route("/product", methods=['GET'])
def product_home():

    # Initialize Response Data
    response_data = dict()

    # Fetch all Products
    session = Session()

    # try except

    try:
        # create query
        product_query = select(Product)

        # execute query
        products = session.execute(product_query)

        # convert to list
        products = products.scalars()

        # add to response data dictionary 
        response_data['products'] = products

    
    except Exception as e:
        print(e)
        return "Error Processing Data"

    return render_template("products/product_home.html", response_data=response_data)

# Post method
@product_routes.route("/product", methods=['POST'])
def product_insert():

    # Create a new product object
    new_product = Product(
        name=request.form['name'],
        price=request.form['price'],
        description=request.form['description']
    )

    # Add session means add to the database
    session = Session()
    session.begin()

    try:

        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return "Error"