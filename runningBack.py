import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import utils as tl

def runningBack():

    st.title('Why Your Running Back Sucks')
    st.image('https://chorus.stimg.co/20313863/3QApfumble11VIKEcg012510.jpg?fit=crop&crop=faces')
    data = requests.get('https://ratings-api.ea.com/v2/entities/m22-ratings?filter=iteration:week-17%20AND%20position:(HB)&sort=overall_rating:DESC,firstName:ASC&limit=50&offset=0').json()
    df = pd.DataFrame()
    tl.clean(data, df)
    player = st.sidebar.selectbox('Select player', df.index)
    insult = player + np.random.choice(tl.insult) + ". Here are a few things " + player + " is bad at:"
    st.subheader(insult)
    tl.badAt(player, df)