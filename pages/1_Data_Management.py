import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd

account = st.secrets["credentials"]["account"]
user = st.secrets["credentials"]["user"]
warehouse = st.secrets["credentials"]["warehouse"]
database = st.secrets["credentials"]["database"]
schema = st.secrets["credentials"]["schema"]
private_key_b64 = st.secrets["credentials"]["private_key"]

engine = create_engine(
    f"snowflake://{user}@{account}/{database}/{schema}?warehouse={warehouse}",
    connect_args={"private_key": private_key_b64}
)

st.title("📊 Shop Data Management")

table_name = st.selectbox("Select a table", ["SHOP_INVENTORY", "SHOP_TRANSACTIONS", "CUSTOMER_INFO"])

df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
st.dataframe(df)

if st.radio("Do you want to update a record?", ["No", "Yes"]) == "Yes":
    record_id_col = {
        "SHOP_INVENTORY": "ITEM_ID",
        "SHOP_TRANSACTIONS": "TRANSACTION_ID",
        "CUSTOMER_INFO": "CUSTOMER_ID"
    }[table_name]
    selected_id = st.selectbox("Select Record ID to Update", df[record_id_col].tolist())
    if selected_id:
        row = df[df[record_id_col] == selected_id].iloc[0]
        updates = {
            col: st.text_input(f"{col}", value=str(row[col]))
            for col in df.columns if col != record_id_col
        }
        if st.button("Save Changes"):
            set_clause = ", ".join([f"{col} = :{col}" for col in updates])
            updates["record_id"] = selected_id
            with engine.begin() as conn:
                conn.execute(text(f"UPDATE {table_name} SET {set_clause} WHERE {record_id_col} = :record_id"), updates)
            st.success("✅ Record updated successfully.")
            st.rerun()
