from dotenv import load_dotenv
from flask import Flask
from connectors.mysql_connector import connection
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from models.product import Product
from sqlalchemy import select

# Load Controller Files
from controllers.product import product_routes

load_dotenv()

# Create Flask App
app=Flask(__name__)

# Register Blueprint
app.register_blueprint(product_routes)

# Product Route
@app.route("/")
def hello_world():
    # Insert a Product Object

    ## SQL Way
    # Session = sessionmaker(connection)
    # with Session() as session:
    #     session.execute(text("INSERT INTO product (name, price, description) VALUES ('Steel Wallet', 145000, 'Created from synthetic steel. Water-proof.')"))
    #     session.commit()

    ## ORM Way
    ### Create Product Object First
    # NewProduct = Product( name='Plastic Wallet', price=12000, description='Made from recyled plastic bags' )
    # Session = sessionmaker(connection)
    # with Session() as session:
    #     session.add(NewProduct)
    #     session.commit()

    # Fetch all Products
    product_query = select(Product)
    Session = sessionmaker(connection)
    with Session() as session:
        result = session.execute(product_query)
        for row in result.scalars():
            print(f'ID: {row.id}, Name: {row.name}')

    return "<p>Insert Success</p>"