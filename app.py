
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from datetime import datetime
import pandas as pd

st.title("[DEMO: TATA ONLINE RETAIL STORE] TRANSACTION FORM")
st.markdown("Enter the details of the new transaction form below.")

conn = st.connection("gsheets", type=GSheetsConnection)

# fetch
df = conn.read(worksheet="TransactionData", usecols=list(range(8)), ttl=5)


# form 
with st.form(key='transaction_form'):
    
    invoice_no = st.text_input(label="Invoice")
    stock_code = st.text_input(label="StockCode")
    description = st.text_input(label="Description")
    quantity = st.number_input(label="Quantity")
    date_time = st.text_input(label="(yyyy/mm/dd HH:MM:SS)")
    # try:
    # # Sử dụng datetime.strptime
    #     date_time = datetime.strptime(date_time, "%d/%m/%Y %H:%M:%S")
    # except ValueError:
    #     st.error("Định dạng không hợp lệ. Vui lòng nhập theo định dạng dd/mm/yyyy HH:MM:SS.")
    unit_price = st.number_input(label="Price")
    customer_id = st.number_input(label="Customer ID")
    country = st.text_input(label="Country")
    gender = st.text_input(label="Gender")
    location = st.text_input(label="Location")
    age = st.number_input(label="Age")
    

    submitted = st.form_submit_button(label="Submit")
    if submitted: 
        transaction_data = pd.DataFrame(
            [
                {
                    "Invoice": invoice_no,
                    "StockCode": stock_code,
                    "Description": description,
                    "Quantity": quantity,
                    "InvoiceDate": datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S"),
                    "Price": unit_price,
                    "Customer ID": customer_id,
                    "Country": country,
                    "Gender": gender,
                    "Location": location,
                    "Age": age,
                }
                
            ]
        )
        
        updated_df = pd.concat([df, transaction_data], ignore_index=True)
        
        conn.update(worksheet='TransactionData', data=updated_df)
        
        st.success("Successfully submitted transaction form!") 

# st.dataframe(df)
