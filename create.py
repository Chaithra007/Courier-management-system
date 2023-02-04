import streamlit as st
from database import add_data, add_customer_data, add_hub_data, add_courier_data, add_track_data, add_shipping_data, \
    add_payment_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        Admin_id = st.text_input("Admin ID:")
        First_name = st.text_input("First Name:")
        Last_name = st.text_input("Last Name:")
    with col2:
        Email = st.text_input("Email")
        Address = st.text_input("Address:")

    if st.button("Add Admin Details"):
        add_data(Admin_id, First_name, Last_name, Email, Address)
        st.success("Successfully added Admin: {}".format(First_name))


def create_customer():
    col1, col2 = st.columns(2)
    with col1:
        Customer_id = st.text_input("Customer ID:")
        First_name = st.text_input("First Name:")
        Last_name = st.text_input("Last Name:")
    with col2:
        Email = st.text_input("Email")
        Phone = st.text_input("Phone")
        Dob = st.text_input("Date of Birth")
        Age = st.text_input("Age")
        AdminID = st.text_input("AdminID")

    if st.button("Add Customer Details"):
        add_customer_data(Customer_id, First_name, Last_name, Email, Phone, Dob, Age, AdminID)
        st.success("Successfully added Customer: {}".format(First_name))


def create_hub():
    col1, col2 = st.columns(2)
    with col1:
        Hub_id = st.text_input("Hub ID:")
        Name = st.text_input("Name:")
        Location = st.text_input("Location:")
    with col2:
        Phone = st.text_input("Phone")
        AdminID = st.text_input("AdminID")

    if st.button("Add Hub Details"):
        add_hub_data(Hub_id, Name, Location, Phone, AdminID)
        st.success("Successfully added Hub: {}".format(Name))


def create_courier():
    col1, col2 = st.columns(2)
    with col1:
        Courier_id = st.text_input("Courier ID:")
        Courier_type = st.selectbox("Courier_type", ["Express service", "OverNight service", "On demand service"])
    with col2:
        Destianation = st.text_input("Destination:")
        CustomerID = st.text_input("CustomerID")

    if st.button("Add Courier Details"):
        add_courier_data(Courier_id, Courier_type, Destianation, CustomerID)
        st.success("Successfully added Hub: {}".format(Courier_id))


def create_track():
    col1, col2 = st.columns(2)
    with col1:
        Order_no = st.text_input("Order_NO:")
        Order_received = st.selectbox("Order_received", ["Yes", "No"])
        Order_picked = st.selectbox("Order_picked", ["Yes", "No"])
    with col2:
        Out_for_delivery = st.selectbox("Out_for_delivery", ["Yes", "No"])
        Reached_destination = st.selectbox("Reached_destination", ["Yes", "No"])
        AdminID = st.text_input("AdminID:")

    if st.button("Add Track Details"):
        add_track_data(Order_no, Order_received, Order_picked, Out_for_delivery, Reached_destination, AdminID)
        st.success("Successfully added Track details of order number: {}".format(Order_no))


def create_shipping():
    col1, col2 = st.columns(2)
    with col1:
        Item_No = st.text_input("Item_No:")
        Weight = st.text_input("Weight:")
    with col2:
        Final_delivery_date = st.date_input("Final_delivery_date:")
        customer_ID = st.text_input("customer_ID:")
        Hub_ID = st.text_input("Hub_ID:")

    if st.button("Add Track Details"):
        add_shipping_data(Item_No, Weight, Final_delivery_date, customer_ID, Hub_ID)
        st.success("Successfully added shipping details of item number: {}".format(Item_No))


def create_payment():
    col1, col2 = st.columns(2)
    with col1:
        Transaction_ID = st.text_input("Transaction_ID:")
        Mode = st.selectbox("Mode", ["UPI", "NEFT", "Cash_on_delivery"])
    with col2:
        Item_No = st.text_input("Item_No:")
        Customer_ID = st.text_input("Cusotmer_ID")

    if st.button("Add Payment Details"):
        add_payment_data(Item_No, Transaction_ID, Mode, Customer_ID)
        st.success("Successfully added payment details with transaction ID: {}".format(Transaction_ID))
