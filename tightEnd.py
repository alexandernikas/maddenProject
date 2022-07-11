import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import utils as tl

def tightEnd():

    st.title('Why Your Tight End Sucks')
    st.image('https://assets2.cbsnewsstatic.com/hub/i/r/2018/11/26/ad4373b7-1ca8-4a3f-8360-df112e53e4e8/thumbnail/1200x630/b2a24a5dfbdd1b33c122ed165d43c33d/gettyimages-10652195741.jpg')
    data = requests.get('https://ratings-api.ea.com/v2/entities/m22-ratings?filter=iteration:week-17%20AND%20position:(TE)&sort=overall_rating:DESC,firstName:ASC&limit=50&offset=0').json()
    df = pd.DataFrame()
    tl.clean(data, df)
    player = st.sidebar.selectbox('Select player', df.index)
    insult = player + np.random.choice(tl.insult) + ". Here are a few things " + player + " is bad at:"
    st.subheader(insult)
    tl.badAt(player, df)