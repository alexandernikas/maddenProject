import streamlit as st
import pandas as pd
import utils as tl
import numpy as np
import matplotlib.pyplot as plt
import quarterBack as qb
import runningBack as rb
import wideReciever as wr
import tightEnd as te

#set page width
st.set_page_config(layout="wide")

pos = st.sidebar.selectbox('Select Position',['--','Quarterback','Running Back','Wide Reciever','Tight End'])
# atr = st.sidebar.selectbox('Select attribute', tl.mdnZ.columns.tolist())
# fxn = st.sidebar.selectbox('Select function', ['standard deviation','regression analysis'])

if pos == '--':
    st.sidebar.selectbox('Select Player:',['--'])
    st.title('Your Favorite Skill Position Player is Terrible')
    st.image('https://www.si.com/.image/t_share/MTg0OTA2NjA1MDczMDE1OTI4/aaron-rodgers.jpg')
    st.subheader("Why wait until the playoffs (or Week 9 if you root for a poverty franchise) to realize that your favorite NFL player is a fraud and a choke artist? I've cut out the middleman and quantified all the areas in which your favorite player is painfully subpar. Enjoy.")


if pos == 'Quarterback':
    qb.quarterBack()

if pos == 'Running Back':
    rb.runningBack()

if pos == 'Wide Reciever':
    wr.wideReciever()

if pos == 'Tight End':
    te.tightEnd()
# if fxn == 'standard deviation':
#     df = tl.mdnZ
#     col = atr
#     tl.zGraph(df, col)