from bson.objectid import ObjectId


class Product(object):
    """A class for storing Project related information"""

    def __init__(self, product_id=None, title=None, description=None, price=0.0, date=None):
        if product_id is None:
            self._id = ObjectId()
        else:
            self._id = product_id
        self.title = title
        self.description = description
        self.price = price
        self.date = date

    def get_as_json(self):
        """ Method returns the JSON representation of the Project object, which can be saved to MongoDB """
        return self.__dict__

    @staticmethod    
    def build_from_json(json_data):
        """ Method used to build Project objects from JSON data returned from MongoDB """
        if json_data is not None:
            try:                            
                return Product(json_data.get('_id', None),
                    json_data['title'],
                    json_data['description'],
                    json_data['price'],
                    json_data['date'])
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e.message))
        else:
            raise Exception("No data to create Project from!")
