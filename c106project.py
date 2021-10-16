import plotly.express as px 
import csv
import numpy as piya

#   Sleep affected by the amount of coffee consumption thus correlated 
with open("data106pt3.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Coffee in ml",y = "sleep in hours")
    fig.show()   


#   Finding Correlation between coffee consumption and hours slept
def getDataSource(dath_path):
    coffee =[]
    sleep = []

    with open(dath_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x" :coffee , "y" : sleep}

def findCorrelation(datasource):
    correlation = piya.corrcoef(datasource["x"],datasource["y"])
    print("correlation between coffee consumed and hours of sleep# is :  \n-->",correlation[0,1])

def setup():
    data_path = "data106pt3.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()  