# Fitelo: Python + MongoDB

### Introduction:
This project is using Python and MongoDB. To use MongoDB with Python, pyMongo library is used and tasks like Data Manipulation, Data Analysis and MongoDB's Data Aggregation are done.

## Code Structure:
#### dbData.py :
This file contains the list of dictionaries to be inserted in collection (table). Each dictionary has data like name, age, gender, country, interests and education.

#### .env :
This file contains the variable **uri** with a value which will be the mongo atlas uri. Create this file before running the project. This uri is necesaary for creating database and collections.
**NOTE :**  ***I have not added my .env file because it is having my mongodb credentials***

#### Database.py :
This file contains the Database class. The class has a method named **"createMongoDbAndCollection"** which read the mongo uri from .env file to creates the database and new collection inside that database. If collections already exists then it will remove that and create new one.

#### DataManipulation.py :
This file contains the class responsible for performing the Manipulation task. This class takes the collection and contains methods named insertDocuments, findDocuments, updateDocuments and deleteDocuments.

#### DataAnalysis.py : 
This file contains the class responsible for performing data analysis and eda task. It takes collection and perform methods like getAllDocuments, calculateAverage for a given data fields, eda and also plots bar and pie charts for fields present in dbData file like age, gender, country, education.

#### DataAggregation.py : 
This file contains the class responsible for performing MongoDB's aggregation method. It has a method groupAndGetTopAverage which groups the documents and perform the specifiled field value average on the grouped data.

#### CustomException.py : 
This file contains the exception handler class which will wraps the any type of exception occurred at any point and has a method to get that particular error message.

#### main.py : 
This file is the starting point of execution for the project. This file contains the main method which will start the tasks execution like database and collection creation in mongodb, data insertion, data manipulation, analysis, eda and aggregation.

## Folders:
#### eda_graphs : 
This folder stores the bar graphs and pie charts generated for features like age, gender, education and country during Data Analysis. 

## Steps to run:
- Install all the required libraries mentioned in requirements.txt file using command:  **pip install -r requirements.txt**
- Run main.py file using command: **python main.py**



