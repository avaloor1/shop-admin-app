# 🛒 Shop Admin App

**Streamlit + Snowflake app** for:
- Admin login via Snowflake keypad
- Viewing & editing fields in SHOP_INVENTORY, SHOP_TRANSACTIONS, CUSTOMER_INFO

## Table Setup
Run these in Snowflake:

```sql
CREATE TABLE IF NOT EXISTS SHOP_INVENTORY (...);
INSERT ...
CREATE TABLE IF NOT EXISTS SHOP_TRANSACTIONS (...);
CREATE TABLE IF NOT EXISTS CUSTOMER_INFO (...);
