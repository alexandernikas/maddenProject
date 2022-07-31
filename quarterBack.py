import requests
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import utils as tl

def quarterBack():

    st.title('Why Your Quarterback Sucks')
    st.image('https://www.nj.com/resizer/ld18wd-x7snOdx7E4cn1a3StHwM=/1280x0/smart/arc-anglerfish-arc2-prod-advancelocal.s3.amazonaws.com/public/3Y5PYCDTIRFJDO7P3BAELRV5PI.jpg')
    data = requests.get('https://ratings-api.ea.com/v2/entities/m23-ratings?filter=iteration:launch-ratings%20AND%20position:(QB)&sort=overall_rating:DESC,firstName:ASC&limit=50&offset=0').json()
    
    df = pd.DataFrame()
    tl.clean(data, df)
    player = st.sidebar.selectbox('Select player', df.index)
    insult = player + np.random.choice(tl.insult) + ". Here are a few things " + player + " is bad at:"
    st.subheader(insult)
    tl.badAt(player, df)