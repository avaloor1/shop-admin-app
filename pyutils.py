import streamlit as st

def logoff_options():
    if "authenticated" in st.session_state and st.session_state.authenticated:
        logoff_col = st.columns([8, 1])[1]
        with logoff_col:
            if st.button("🔒 Logoff"):
                for key in st.session_state.keys():
                    del st.session_state[key]
                    st.switch_page("main_app.py")               

def logoff():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.switch_page("main_app.py")
