import streamlit as st
print("Session state keys before Sign In form:", list(st.session_state.keys()))


st.title("Sanity Test App")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    st.write("Welcome to Data Management")
else:
    st.write("Please log in")
