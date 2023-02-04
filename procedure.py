import pandas as pd
import streamlit

from database import *


def my_procedure():
    list_of_track = [i[0] for i in view_only_track_names()]
    selected_track = streamlit.selectbox("Select Order Number", list_of_track)
    res = show_progress(selected_track)
    df = pd.DataFrame(res, columns=['Deliverystatus'])
    streamlit.write('Your order progress is {}'.format(df['Deliverystatus'][0]))
