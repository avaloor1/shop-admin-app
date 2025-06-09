import streamlit as st
#print("Session state keys at app start:", list(st.session_state.keys()))
from sqlalchemy import create_engine, text
import bcrypt
from pyutils import logoff_options

# Load Snowflake credentials
account = st.secrets["credentials"]["account"]
user = st.secrets["credentials"]["user"]
warehouse = st.secrets["credentials"]["warehouse"]
database = st.secrets["credentials"]["database"]
schema = st.secrets["credentials"]["schema"]
private_key_b64 = st.secrets["credentials"]["private_key"]

# SQLAlchemy connection
engine = create_engine(
    f"snowflake://{user}@{account}/{database}/{schema}?warehouse={warehouse}",
    connect_args={"private_key": private_key_b64}
)

def check_login(username, password):
    with engine.begin() as conn:
        result = conn.execute(text("SELECT PASSWORD_HASH FROM USER_ACCOUNTS WHERE USERNAME = :username"), {"username": username}).fetchone()
    return result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8'))


st.title("🛒 Shop Admin Login")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("signin_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Sign In"):
            if check_login(username, password):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid credentials")

if st.session_state.authenticated:
    st.success("✅ Login successful.")
    st.page_link("pages/1_Data_Management.py", label="📊 Go to Data Management")
    # Enable logoff button
    logoff_options()


