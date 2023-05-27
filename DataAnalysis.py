from CustomException import CustomException, errorOccurred
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os

class DataAnalysis:
    '''
        This class is responsible for data analysis step. This class needs collection object from mongo client on which data analysis will be performed.
    '''

    def __init__(self, collection):
        self.collection = collection
    
    def getAllDocuments(self):
        # fetches all the data for collection
        try:
            allDocs = self.collection.find()
            print("Documents Fetched Successfully!")
            return allDocs
        except Exception as e:
            return CustomException(e)
    
    def calculateAverage(self, search_field, search_value, average_field):
        # calculate the average value for given average_field after filtering on the basis of search_field and search_value
        try:
            filterStep = {'$match': {search_field: search_value}}
            averageStep = {'$group' : {'_id' : None, f'average_{average_field}' : {'$avg' : f'${average_field}'}}}
            data = list(self.collection.aggregate([filterStep, averageStep]))
            if data:
                print("Average Calculated Successfully!")
                return data[0][f'average_{average_field}']
            return f"Data not found for {search_value}"
        except Exception as e:
            return CustomException(e)
    
    def convertDocumentsToCsv(self, documents):
        # create the csv file for the fetched documents from collection
        try:
            file_name = 'sample_collection.csv'
            fields = list(documents[0].keys())
            with open(file_name, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                writer.writeheader()
                for document in documents:
                    writer.writerow(document)
        except Exception as e:
            return CustomException(e)
    
    def getEducationData(self, listDocs):
        # get the education type count data
        try:
            data = {}
            for doc in listDocs:
                education = doc['education']
                if education['degree'] not in data:
                    data[education['degree']] = 0
                data[education['degree']] += 1
            return data
        except Exception as e:
            return CustomException(e)
    
    def getCountryData(self, listDocs):
        # get the countries count data
        try:
            data = {}
            for doc in listDocs:
                country = doc['country']
                if country not in data:
                    data[country] = 0
                data[country] += 1
            return data
        except Exception as e:
            return CustomException(e)
    
    def getGenderData(self, listDocs):
        # get the gender count data
        try:
            data = {}
            for doc in listDocs:
                gender = doc['gender']
                if gender not in data:
                    data[gender] = 0
                data[gender] += 1
            return data
        except Exception as e:
            return CustomException(e)
    
    def ageCriteriaData(self, listDocs, age_divider):
        # get the count of age below or above given age_divider arguement
        try:
            data = {f'age_below_{age_divider}': 0, f'age_above_{age_divider}': 0}
            for doc in listDocs:
                age = doc['age']
                if age <= age_divider:
                    data[f'age_below_{age_divider}'] += 1
                else:
                    data[f'age_above_{age_divider}'] += 1
            return data
        except Exception as e:
            return CustomException(e)
    
    def barGraph(self, title, data):
        # plot the bar graph for given dictionary data
        x_data = data.keys()
        y_data = data.values()
        fig, ax = plt.subplots()
        ax.bar(x_data, y_data, align='center', alpha=0.5)
        ax.set_ylabel('Count')
        ax.set_xlabel(title)
        ax.set_xticks(np.arange(len(x_data)))
        ax.set_xticklabels(x_data)
        plt.tight_layout()
        plt.savefig(f"eda_graphs/{title}_bar_plot.png")
        plt.show()
    
    def pieChart(self, title, data):
        # plot the pie chart for given dictionary data
        x_data = data.keys()
        y_data = data.values()
        fig, ax = plt.subplots()
        ax.pie(y_data, labels=x_data, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        ax.set_title(title)
        plt.tight_layout()
        plt.savefig(f"eda_graphs/{title}_pie_chart.png")
        plt.show()
    
    def plotGraphs(self, data_to_plot):
        # plot the bar and pie charts for multiple data dictionaries given
        for title,data in data_to_plot.items():
            print("\n" + "*"*5 + f" Plotting for {title} " + "*"*5)
            self.barGraph(title=title, data=data)
            self.pieChart(title=title, data=data)

    def eda(self):
        # generates the data and plot graphs for various fields
        try:
            allDocs = list(self.getAllDocuments())
            self.convertDocumentsToCsv(allDocs)
            df = pd.read_csv("sample_collection.csv")
            print("Documents Description: ")
            print(df.describe())

            educationData = self.getEducationData(listDocs=allDocs)
            countryData = self.getCountryData(listDocs=allDocs)
            genderData = self.getGenderData(listDocs=allDocs)
            ageData = self.ageCriteriaData(listDocs=allDocs, age_divider=30)
            dataToPlot = {}
            if not errorOccurred(educationData):
                dataToPlot['education'] = educationData
            if not errorOccurred(countryData):
                dataToPlot['country'] = countryData
            if not errorOccurred(genderData):
                dataToPlot['gender'] = genderData
            if not errorOccurred(ageData):
                dataToPlot['age'] = ageData
            self.plotGraphs(data_to_plot=dataToPlot)
            print("EDA Done Successfully!")
        except Exception as e:
            return CustomException(e)
