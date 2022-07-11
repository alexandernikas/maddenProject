import requests
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import string

#a little list of phrases
insult = [
' is an absolute bum'
,' is flat-out garbage'
,' is an embarrassment to the position'
,' makes my eyes bleed on Sunday'
,' makes Queen Elizabeth look like an All-Pro'
,' is a waste of cap space'
,' is a washed-up scrub'
,' is simply bad at football'
]

#to find json data link, navigate to the page you want to scrape, open the network tab and press F5 to refresh page. copy the lowest xhr response.
#pulls JSON objects from xhr response on the madden website
data = requests.get('https://ratings-api.ea.com/v2/entities/m22-ratings?filter=iteration:week-17%20AND%20position:(QB)&sort=overall_rating:DESC,firstName:ASC&limit=50&offset=0').json()

#create function to create new dataframe based on players' z scores for madden attributes
def zScore(df1, col, df2):
    
    #find average and standard deviation
    avg = np.average(df1[col])
    stdev = np.std(df1[col])

    #apply to dataframe column to find standard deviation from the mean
    df2[col] = (df1[col] - avg)/stdev

#create data cleaning function (this works for all the skill positions)
def clean(data, df):
    #passes JSON data to pandas df (mdn)
    mdn = pd.DataFrame(data['docs'])

    #set index
    mdn = mdn.set_index('fullNameForSearch')

    #drop columns with non-numeric data
    mdn = mdn.select_dtypes(include = 'number')

    #drop columns with all zero values
    mdn = mdn.loc[:, (mdn != 0).any(axis=0)]

    #drop columns containing 'diff' string (these columns aren't useful for analysis)
    for column in mdn.columns.tolist():
        if "_diff" in column:
            mdn = mdn.drop([column], axis = 1)
            
    #throw out a couple other columns we don't want to analyze
    mdn = mdn.drop(columns = ['teamId', 'jerseyNum', 'yearsPro','plyrPortrait','kickAccuracy_rating','kickPower_rating'])

    #apply function
    mdnZ = pd.DataFrame()
    for column in mdn.columns.tolist():
        df1 = mdn
        col = column
        df2 = mdnZ
        
        if column == "primaryKey":
            continue
        
        if column == "fullNameForSearch":
            continue

        zScore(df1, col, df2)

    #clean column names
    for column in mdnZ.columns.tolist():
        if column == "primaryKey":
            continue
        
        if column == "fullNameForSearch":
            continue
        
        newCol = ''
        
        for i, letter in enumerate(column):
            if i and letter.isupper():
                newCol += ' '

            newCol += letter
        
        if "_rating" in newCol:
            newCol = newCol.replace("_rating","")       
        
        newCol = string.capwords(newCol)
        
        mdnZ = mdnZ.rename(columns = {column : newCol})

    mdnZ['Age'] = mdnZ['Age']*(-1)

    
    for column in mdnZ.columns:
        df[column] = mdnZ[column]


COLOR = 'white'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR


def zGraph(df, col, player):
    #sort by col values
    df = df.sort_values(by = col)

    #set parameter for graph
    fig = plt.figure(figsize=(20, 8), facecolor = 'black')
    ax = fig.add_subplot(111)
    ax.set_facecolor('black')
    ax.set_ylabel('Z-Score')
    ax.bar(df.index,df[col], color='blue', alpha=0.75)
#    red_patch = mpatches.Patch(edgecolor='black', facecolor='black', color='red', label=player)
#    ax.legend(handles=[red_patch])

    # Plot the selected player bar separately
    ax.bar(player,df.loc[player,col], color='red')
    plt.xticks(df.index, df.index, rotation=70)
    st.write(col)
    st.pyplot(fig, ax)


def badAt(player, df):
    col1, col2 = st.columns(2)
    mini = df.loc[df.index == player]
    mini = mini.sort_values(by = player, axis = 1)
    mini = mini.iloc[:, : 4]
    for column in mini.columns[0:2]:
        df = df
        col = column
        player = player
        with col1:
           zGraph(df, col, player)
    for column in mini.columns[2:4]:
        df = df
        col = column
        player = player
        with col2:
            zGraph(df, col, player)
