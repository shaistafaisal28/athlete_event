# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 08:53:56 2023

@author: tosha
"""


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

file = r'C:\Users\tosha\Downloads/athlete_events.csv'
st.header ('Olympic History Dashboard')
heading ('Created by Shaista Khan')


df = pd.read_csv('athlete_events.csv')

#colum 1
selected_team = col1.selectbox('Select you Country', Team)


#column 4
# of participations total
data['ID'].count()

#find count of medals :
medal_count = df.groupby('Medal')['Name'].count().sort_values(ascending=False).head(10)

# of gold Medals
Medal['Gold'].unique()

# of silver medals
medal['silver'].unique()

# of Bronze Medals
medal['Bronze'].unique()
#colum 3
#number of Medals over years for each medals type (G,S,B) -  Single line chart

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Number of Medals', dpi=100):
    
    # size of the figure 
    plt.figure(figsize=(15,4), dpi=dpi)
    
    plt.plot(x, y, color='tab:blue')
    
    # set title, axis labels
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.title(title)
    # alt way of doing this 
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    
    plt.show()
    
plot_df(df, x=df['Date'], y=df['Number of Medals'], title='Number of medals over the years')


#Horizontal Bar chart by # of Medals recieved by each Athlete, sorted by the 
#most & top 5 only
# creating a bar chart 
fig = plt.bar(x=medal.index, height=Name.values)
# adding supplementary formatting 
plt.title('Medals by Athlete')
plt.xlabel('Medals')
plt.ylabel('Name')
plt.show()

#Highlight table by number of medals recieved in each sports sorted by the most
#and top 5 only
medal.groupby('Medals')['sports'].count()

#colum 3
#Number of medals over age Histogram chart, 10 Years bin
details = plt.hist(data['medal','Age'].values, bins=10)
details

#pie Chart summary by number  of madels by gender 
plt.rcParams['figure.figsize'] = [12, 8]
details = plt.pie(data['Medals', 'Sex'].values, bins=10)
details


#vertical Bar chart by #of Medals recieved in each season.

details = plt.bar(data['Medals', 'Season'].values, bins=10)
details




