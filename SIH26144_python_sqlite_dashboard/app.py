import streamlit as st
from core.ui import inject_css
from core.runtime import init_state, restart_demo


st.set_page_config(page_title="Microbarometer", page_icon=":material/air:", layout="wide", initial_sidebar_state="expanded")
inject_css()
init_state()

with st.sidebar:
    st.markdown("## Microbarometer")
    if st.button("↻ Restart demonstration", use_container_width=True):
        restart_demo()
        st.rerun()

monitoring = st.Page("pages/1_Live_Dashboard.py", title="Live Dashboard", icon=":material/dashboard:", default=True)
events = st.Page("pages/3_Events.py", title="Events", icon=":material/warning:")
system = st.Page("pages/4_System.py", title="System", icon=":material/settings:")
prototype = st.Page("pages/5_Prototype.py", title="Prototype", icon=":material/view_in_ar:")
calibration = st.Page("pages/7_Calibration.py", title="Calibration", icon=":material/tune:")
about = st.Page("pages/6_About.py", title="About", icon=":material/info:")

pg = st.navigation([monitoring, events, system, prototype, calibration, about])
pg.run()
