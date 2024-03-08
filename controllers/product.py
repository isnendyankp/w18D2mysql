from flask import Blueprint, render_template
from connectors.mysql_connector import Session

from models.product import Product
from sqlalchemy import select

product_routes = Blueprint('product_routes',__name__)

@product_routes.route("/product", methods=['GET'])
def product_home():

    # Initialize Response Data
    response_data = dict()

    # Fetch all Products
    session = Session()

    # try except

    try:
        product_query = select(Product)
    except :

    return render_template("products/product_home.html")
