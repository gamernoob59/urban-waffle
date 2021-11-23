import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
import pandas as pd

df=pd.read_csv("sp.csv")
data=df["math score"].tolist()

data_mean=statistics.mean(data)
data_sd=statistics.stdev(data)

#print("hello")
#print(data_sd)
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

def show_fig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([data],["math score"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()
    fig1=ff.create_distplot([data],["reading score"],show_hist=False)
    fig1.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig1.show()
    fig2=ff.create_distplot([data],["writing score"],show_hist=False)
    fig2.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig2.show()

def randomMeanSet(counter):
    dataset=[]
    for i in range (0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def sd():
    meanList=[]
    for i in range (0,1000):
        setOfMeans=randomMeanSet(100)
        meanList.append(setOfMeans)
    stddev=statistics.stdev(meanList)
    print("The standard deviation is: ",stddev)

def setup():
    meanList=[]
    for i in range (0,1000):
        setOfMeans=randomMeanSet(100)
        meanList.append(setOfMeans)
    show_fig(meanList)
    themean=statistics.mean(meanList)
    print("The mean is: ",themean)

setup()
totalMean=statistics.mean(data)
print("The total mean is: "+totalMean)
sd()
