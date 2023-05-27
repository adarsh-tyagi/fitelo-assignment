from CustomException import CustomException

class DataManipulation:
    '''
        This class is responsible for Data Manipulation tasks. This class needs collection object from mongo client on which data manipulations (CRUD) 
        operations will be performed.
    '''
    
    def __init__(self, collection):
        self.collection = collection

    def insertDocuments(self, data_list):
        # insert multiple documents, pass list of dictionaries as arguement
        try: 
            self.collection.insert_many(data_list)
            print("Documents Inserted Successfully!")
        except Exception as e:
            return CustomException(e)
        
    def findDocuments(self, field_name, operator, value, ascending=True):
        # search for the documents on the particular field's value, pass the field name, operator ($gt, $lt, ...), value and sorting order as True or False
        # By default sorting order will be True (ASCENDING)
        try:
            query = {field_name : {operator : value}}
            sortingOrder = 1 if ascending else -1
            documents = self.collection.find(query).sort(field_name, sortingOrder)
            print("Documents Fetched Successfully!")
            return documents
        except Exception as e:
            return CustomException(e)
        
    def updateDocuments(self, search_key, search_value, update_key, update_value):
        # update the documents, pass the search key, search value on which documents get filtered and required update field and value
        try:
            query = {search_key: search_value}
            newData = {"$set": {update_key : update_value}}
            self.collection.update_many(query, newData)
            print("Documents Updated Successfully!")
        except Exception as e:
            return CustomException(e)
    
    def deleteDocuments(self, search_key, search_value):
        # delete the multiple documents matching the passed search key and value
        try:
            query = {search_key : search_value}
            self.collection.delete_many(query)
            print("Documents Deleted Successfully!")
        except Exception as e:
            return CustomException(e)
