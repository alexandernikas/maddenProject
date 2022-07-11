import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import utils as tl

def wideReciever():

    st.title('Why Your Wide Reciever Sucks')
    st.image('https://www.nj.com/resizer/if3XII58zWn_tVtkkybt5WP-LSk=/1280x0/smart/arc-anglerfish-arc2-prod-advancelocal.s3.amazonaws.com/public/BY2RCRS3OBDTHKRPFYRK2U3YXM.JPG')
    data = requests.get('https://ratings-api.ea.com/v2/entities/m22-ratings?filter=iteration:week-17%20AND%20position:(WR)&sort=overall_rating:DESC,firstName:ASC&limit=50&offset=0').json()
    df = pd.DataFrame()
    tl.clean(data, df)
    player = st.sidebar.selectbox('Select player', df.index)
    insult = player + np.random.choice(tl.insult) + ". Here are a few things " + player + " is bad at:"
    st.subheader(insult)
    tl.badAt(player, df)