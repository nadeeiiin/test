import shutil
import streamlit as st
from streamlit_option_menu import option_menu

from dashboard import show_dashboard
from stats_trends import show_stats_trends
from cameras_numbers import show_cameras_numbers
from manual_image_upload import show_manual_image_upload
from pathlib import Path

STREAMLIT_STATIC_PATH = Path(st.__path__[0]) / 'static'
CSS_PATH = (STREAMLIT_STATIC_PATH / "assets")
if not CSS_PATH.is_dir():
    CSS_PATH.mkdir()

css_file = CSS_PATH / "style.css"
if not css_file.exists():
    shutil.copy("assets/style.css", css_file)

#use wide mode
st.set_page_config(layout="wide")


st.sidebar.title("North American Animals Classification")

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Stat's & Trends", "Cameras & Numbers", "Manual Image Upload"],
        icons=["house", "graph-up",  "clipboard-data", "gear"]
    )



if selected == "Dashboard":
    show_dashboard()

if selected == "Stat's & Trends":
    show_stats_trends()

if selected == "Cameras & Numbers":
    show_cameras_numbers()

if selected == "Manual Image Upload":
    show_manual_image_upload()



