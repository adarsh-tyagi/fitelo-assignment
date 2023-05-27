from CustomException import CustomException

class DataAggregation:
    '''
        This class is responsible for data aggregation step. This class needs collection object from mongo client on which data aggregation operation will be
        performed.
    '''
    
    def __init__(self, collection):
        self.collection = collection

    def groupAndGetTopAverage(self, group_field, average_field, limit=5, ascending=True):
        # group the documents on group_field value, then calculate the average for average_field and return the top limit result in a required sorted order
        try:
            groupStep = {'$group' : {'_id' : f'${group_field}', f'average_{average_field}' : {'$avg' : f'${average_field}'}}}
            sortingOrder = 1 if ascending else -1
            sortStep = {'$sort' : {f'average_{average_field}' : sortingOrder}}
            limitStep = {'$limit' : limit}
            result = self.collection.aggregate([groupStep, sortStep, limitStep])
            print("Aggregation Calculation Done Successfully!")
            return result
        except Exception as e:
            return CustomException(e)

