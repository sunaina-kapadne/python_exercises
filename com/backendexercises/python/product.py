from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Create the base class
Base = declarative_base()

# 2. Define the Product model
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"

# 3. Create the engine (SQLite in-memory database for simplicity)
engine = create_engine('sqlite:///:memory:', echo=True)

# 4. Create the table in the database
Base.metadata.create_all(engine)

# 5. Create a session
Session = sessionmaker(bind=engine)
session = Session()

# 6. Add sample data to the database
product1 = Product(name="Laptop", price=150.0)
product2 = Product(name="Headphones", price=50.0)
product3 = Product(name="Smartphone", price=200.0)

session.add_all([product1, product2, product3])
session.commit()

# 7. Query for products with a price greater than 100.0
expensive_products = session.query(Product).filter(Product.price > 100.0).all()

# 8. Print the result
for product in expensive_products:
    print(product)
