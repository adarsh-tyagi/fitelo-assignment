from Database import Database
from DataManipulation import DataManipulation
from DataAnalysis import DataAnalysis
from DataAggregation import DataAggregation
from CustomException import errorOccurred
from dbData import dataToInsert

def dataManipulation(collection):
    manipulation = DataManipulation(collection=collection)

    # Insert the documents
    res = manipulation.insertDocuments(dataToInsert)
    if errorOccurred(res):
        return
    print("Data After Insertion:")
    print(list(collection.find()))
    print("\n")

    # Perform a query to find all documents where the "age" field is greater than or equal to 30 and sort them in descending order
    res = manipulation.findDocuments(
        field_name="age", operator="$gt", value=30, ascending=False)
    if errorOccurred(res):
        return
    print(list(res))
    print("\n")

    # Update the documents where the "gender" field is "Male" and set the value of the "status" field to "Active".
    res = manipulation.updateDocuments(
        search_key="gender", search_value="Male", update_key="status", update_value="Active")
    if errorOccurred(res):
        return
    print("Data After Updation:")
    print(list(collection.find()))
    print("\n")

    # Delete all documents where the "country" field is "United States"
    res = manipulation.deleteDocuments(search_key="country", search_value="United States")
    if errorOccurred(res):
        return
    print("Data After Deletion:")
    print(list(collection.find()))

def dataAnalysis(collection):
    analysis = DataAnalysis(collection=collection)

    # Retrieve all documents from the "sample_collection" in the "sample_db" database
    res = analysis.getAllDocuments()
    if errorOccurred(res):
        return
    print(list(res))

    # Generate relevant insights from the dataset using Python
    # Use the matplotlib library to create visualizations (e.g., bar plots, scatter plots, etc.) to represent the data patterns and relationships
    res = analysis.eda()
    if errorOccurred(res):
        return

    # Python function to calculate the average age of females in the dataset and return the result
    res = analysis.calculateAverage(search_field="gender", search_value="Female", average_field="age")
    if errorOccurred(res):
        return
    print("Average age of Females:")
    print(f"{res} years")

def dataAggregation(collection):
    aggregation = DataAggregation(collection=collection)

    # Group the documents by the "country" field and calculate the average age in each country.
    # Sort the results in descending order of the average age.
    # Limit the output to the top 5 countries with the highest average age
    res = aggregation.groupAndGetTopAverage(group_field="country", average_field="age", limit=5, ascending=False)
    if errorOccurred(res):
        return
    print("Top 5 Countries with maximum average age: ")
    print(list(res))

def main():
    # Create sample_database and sample_collection in the mongodb
    print("\n" + "-"*75)
    print("Starting Database and Collection Creation Step ===>")
    print("-"*75)
    db = Database()
    collection = db.createMongoDbAndCollection('sample_database', 'sample_collection')
    if errorOccurred(collection):
        return
    
    # 1. MongoDB Data Manipulation
    print("\n" + "-"*75)
    print("Starting Data Manipulation Step ===>")
    print("-"*75)
    dataManipulation(collection=collection)
    
    # 2. Python Data Analysis
    print("\n" + "-"*75)
    print("Starting Data Analysis Step ===>")
    print("-"*75)
    dataAnalysis(collection=collection)

    # 3. MongoDB Aggregation
    print("\n" + "-"*75)
    print("Starting Data Aggregation Step ===>")
    print("-"*75)
    dataAggregation(collection=collection)


if __name__ == "__main__":
    print("*"*50)
    main()
    print("\n" + "*"*22 + " END " + "*"*22)