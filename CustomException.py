class CustomException(Exception):
    def __init__(self, error_message):
        self.__message = error_message
    
    def getErrorMessage(self):
        return self.__message


def errorOccurred(data):
    if isinstance(data, CustomException):
        print(data.getErrorMessage())
        return True
    return False
