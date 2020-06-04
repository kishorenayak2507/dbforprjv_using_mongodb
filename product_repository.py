from pymongo import MongoClient
from bson.objectid import ObjectId
from product import Product


class ProductRepository(object):
    """ Repository implementing CRUD operations on products collection in MongoDB """

    def __init__(self):
        # initializing the MongoClient, this helps to 
        # access the MongoDB databases and collections 
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client['products']

    def create(self, product):
        if product is not None:
            self.database.products.insert(product.get_as_json())
        else:
            raise Exception("Nothing to save, because product parameter is None")

    def read(self, product_id=None):
        if product_id is None:
            return self.database.products.find({})
        else:
            return self.database.products.find({"_id": product_id})

    def update(self, product):
        if product is not None:
            # the save() method updates the document if this has an _id property 
            # which appears in the collection, otherwise it saves the data
            # as a new document in the collection
            self.database.products.save(product.get_as_json())
        else:
            raise Exception("Nothing to update, because product parameter is None")

    def delete(self, product):
        if product is not None:
            self.database.product.remove(product.get_as_json())
        else:
            raise Exception("Nothing to delete, because product parameter is None")
