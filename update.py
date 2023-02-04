import datetime

import pandas as pd
import streamlit as st
from database import *


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Admin ID', 'First Name', 'Last Name', 'Email', 'Address'])
    with st.expander("Current Admin Details"):
        st.dataframe(df)
    list_of_admin = [i[0] for i in view_only_names()]
    selected_admin = st.selectbox("Admin to Edit", list_of_admin)
    selected_result = get_admin(selected_admin)
    # st.write(selected_result)
    if selected_result:
        admin_id = selected_result[0][0]
        first_name = selected_result[0][1]
        last_name = selected_result[0][2]
        email = selected_result[0][3]
        address = selected_result[0][4]

        col1, col2 = st.columns(2)
        with col1:
            new_admin_id = st.text_input("AdminID:", admin_id)
            new_first_name = st.text_input("First Name:", first_name)
            new_last_name = st.text_input("Last Name:", last_name)
        with col2:
            new_email = st.text_input("Email:", email)
            new_address = st.text_input("Address:", address)
        if st.button("Update Admin Details"):
            edit_admin_data(new_admin_id, new_first_name, new_last_name, new_email, new_address, admin_id)
            st.success("Successfully updated")

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Admin ID', 'First Name', 'Last Name', 'Email', 'Address'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_customer():
    result = view_all_customer_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Customer_id', 'First_name', 'Last_name', 'Email', 'Phone', ' Dob', 'Age', 'AdminID'])
    with st.expander("Current Customer Details"):
        st.dataframe(df)
    list_of_customer = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Customer to Edit", list_of_customer)
    selected_result = get_customer(selected_customer)
    # st.write(selected_result)
    if selected_result:
        customer_id = selected_result[0][0]
        first_name = selected_result[0][1]
        last_name = selected_result[0][2]
        email = selected_result[0][3]
        Phone = selected_result[0][4]
        Dob = selected_result[0][5]
        Age = selected_result[0][6]
        Admin = selected_result[0][7]

        col1, col2 = st.columns(2)
        with col1:
            new_customer_id = st.text_input("AdminID:", customer_id)
            new_first_name = st.text_input("First Name:", first_name)
            new_last_name = st.text_input("Last Name:", last_name)
        with col2:
            new_email = st.text_input("Email:", email)
            new_phone = st.text_input("Phone:", Phone)
            new_Dob = st.text_input("DOB:", Dob)
            new_Age = st.text_input("Age:", Age)
            new_Admin = st.text_input("Admin:", Admin)
        if st.button("Update Customer Details"):
            edit_customer_data(new_customer_id, new_first_name, new_last_name, new_email, new_phone, new_Dob, new_Age,
                               new_Admin, customer_id)
            st.success("Successfully updated")

    result2 = view_all_customer_data()
    df2 = pd.DataFrame(result2,
                       columns=['Customer_id', 'First_name', 'Last_name', 'Email', 'Phone', ' Dob', 'Age', 'AdminID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_hub():
    result = view_all_hub_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Hub_id', 'Name', 'Location', 'Phone', 'AdminID'])
    with st.expander("Current Hub Details"):
        st.dataframe(df)
    list_of_hub = [i[0] for i in view_only_hub_names()]
    selected_hub = st.selectbox("Hub to Edit", list_of_hub)
    selected_result = get_hub(selected_hub)
    # st.write(selected_result)
    if selected_result:
        hub_id = selected_result[0][0]
        name = selected_result[0][1]
        Location = selected_result[0][2]
        Phone = selected_result[0][3]
        Admin = selected_result[0][4]

        col1, col2 = st.columns(2)
        with col1:
            new_hub_id = st.text_input("HubID:", hub_id)
            new_name = st.text_input("Name:", name)
            new_Location = st.text_input("Location:", Location)
        with col2:
            new_phone = st.text_input("Email:", Phone)
            new_admin = st.text_input("AdminID:", Admin)
        if st.button("Update  Hub Details"):
            edit_hub_data(new_hub_id, new_name, new_Location, new_phone, new_admin, hub_id)
            st.success("Successfully updated")

    result2 = view_all_hub_data()
    df2 = pd.DataFrame(result2, columns=['HUB ID', 'First Name', 'Last Name', 'Email', 'AdminID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_courier():
    result = view_all_courier_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Courier_ID', 'Courier_Type', 'Courier_Destination', 'customer_ID'])
    with st.expander("Current Courier Details"):
        st.dataframe(df)
    list_of_courier = [i[0] for i in view_only_courier_names()]
    selected_courier = st.selectbox("Courier to Edit", list_of_courier)
    selected_result = get_courier(selected_courier)
    # st.write(selected_result)
    if selected_result:
        Courier_id = selected_result[0][0]
        Courier_type = selected_result[0][1]
        Destination = selected_result[0][2]
        CustomerID = selected_result[0][3]

        col1, col2 = st.columns(2)
        with col1:
            new_Courier_id = st.text_input("CourierID:", Courier_id)
            new_Courier_type = st.selectbox("Courier_type",
                                            ["Express service", "OverNight service", "On demand service"])

        with col2:
            new_Destination = st.text_input("Destination :", Destination)
            new_CustomerID = st.text_input("CustomerID", CustomerID)
        if st.button("Update courier Details"):
            edit_courier_data(new_Courier_id, new_Courier_type, new_Destination, new_CustomerID, Courier_id)
            st.success("Successfully updated")

    result2 = view_all_courier_data()
    df2 = pd.DataFrame(result2, columns=['Courier_ID', 'Courier_Type', 'Courier_Destination', 'customer_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_track():
    result = view_all_track_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Order_No', 'Order_received', 'Order_picked', 'Out_for_delivery', 'Reached_destination',
                               'AdminID'])
    with st.expander("Current Track Details"):
        st.dataframe(df)
    list_of_track = [i[0] for i in view_only_track_names()]
    selected_track = st.selectbox("Track to Edit", list_of_track)
    selected_result = get_track(selected_track)
    # st.write(selected_result)
    if selected_result:
        Order_No = selected_result[0][0]
        Order_received = selected_result[0][1]
        Order_picked = selected_result[0][2]
        Out_for_delivery = selected_result[0][3]
        Reached_destination = selected_result[0][4]
        AdminID = selected_result[0][5]

        col1, col2 = st.columns(2)
        with col1:
            new_Order_No = st.text_input("Order_No:", Order_No)
            if Order_received == "Yes":
                new_Order_received = st.selectbox("Order_received", ["Yes", "No"], index=0)
            if Order_received == "No":
                new_Order_received = st.selectbox("Order_received", ["Yes", "No"], index=1)
            if Order_picked == "Yes":
                new_Order_picked = st.selectbox("Order_picked", ["Yes", "No"], index=0)
            if Order_picked == "No":
                new_Order_picked = st.selectbox("Order_picked", ["Yes", "No"], index=1)

        with col2:
            if Out_for_delivery == "Yes":
                new_Out_for_delivery = st.selectbox("Out_for_delivery", ["Yes", "No"], index=0)
            if Out_for_delivery == "No":
                new_Out_for_delivery = st.selectbox("Out_for_delivery", ["Yes", "No"], index=1)
            if Reached_destination == "Yes":
                new_Reached_destination = st.selectbox("Reached_destination", ["Yes", "No"], index=0)
            if Reached_destination == "No":
                new_Reached_destination = st.selectbox("Reached_destination", ["Yes", "No"], index=1)

            new_AdminID = st.text_input("AdminID:", AdminID)
        if st.button("Update track Details"):
            edit_track_data(new_Order_No, new_Order_received, new_Order_picked, new_Out_for_delivery,
                            new_Reached_destination, new_AdminID, Order_No)
            st.success("Successfully updated")

    result2 = view_all_track_data()
    df2 = pd.DataFrame(result2,
                       columns=['Order_No', 'Order_received', 'Order_picked', 'Out_for_delivery', 'Reached_destination',
                                'AdminID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_shipping():
    result = view_all_shipping_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Item_No', ' Weight', 'Final_delivery_date', 'customer_ID','Hub_id'])
    with st.expander("Current Shipping Details"):
        st.dataframe(df)
    list_of_shipping = [i[0] for i in view_only_shipping_names()]
    selected_shipping = st.selectbox("Shipping to Edit", list_of_shipping)
    selected_result = get_shipping(selected_shipping)
    # st.write(selected_result)
    if selected_result:
        Item_No = selected_result[0][0]
        Weight = selected_result[0][1]
        Final_delivery_date = selected_result[0][2]
        customer_ID = selected_result[0][3]
        hubid=selected_result[0][4]
        col1, col2 = st.columns(2)
        with col1:
            new_Item_No = st.text_input("Item_No:", Item_No)
            new_Weight = st.text_input("Weight:", Weight)

        with col2:
            new_Final_delivery_date = st.date_input("Final_delivery_date", Final_delivery_date)

            new_customer_ID = st.text_input("Customer_ID :", customer_ID)
            new_hubid=st.text_input("Hub_ID",hubid)
        if st.button("Update courier Details"):
            edit_shipping_data(new_Item_No, new_Weight, new_Final_delivery_date, new_customer_ID,new_hubid, Item_No)
            st.success("Successfully updated")

    result2 = view_all_shipping_data()
    df2 = pd.DataFrame(result2, columns=['Item_No', ' Weight', 'Final_delivery_date', 'customer_ID','hubid'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_payment():
    result = view_all_payment_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Transaction_ID', 'Mode', 'Item_No','price'])
    with st.expander("Current Payment Details"):
        st.dataframe(df)
    list_of_payment = [i[0] for i in view_only_payment_names()]
    selected_payment = st.selectbox("Shipping to Edit", list_of_payment)
    selected_result = get_payment(selected_payment)
    # st.write(selected_result)
    if selected_result:
        Transaction_ID = selected_result[0][0]
        Mode = selected_result[0][1]
        Item_No = selected_result[0][2]
        Cunstomer_ID=selected_result[0][3]
        col1, col2 = st.columns(2)
        with col1:
            new_Transaction_ID = st.text_input("Transaction_ID:", Transaction_ID)
            if Mode == "UPI":
                new_Mode = st.selectbox("Train Type", ["UPI", "NEFT", "Cash_on_delivery"], index=0)
            if Mode == "NEFT":
                new_Mode = st.selectbox("Train Type", ["UPI", "NEFT", "Cash_on_delivery"], index=1)
            if Mode == "Cash_on_delivery":
                new_Mode = st.selectbox("Train Type", ["UPI", "NEFT", "Cash_on_delivery"], index=2)

        with col2:
            new_Item_No = st.text_input("Item_No :", Item_No)
            new_Customer_ID=st.text_input("Customer_ID",Cunstomer_ID)
        if st.button("Update Payment Details"):
            edit_payment_data(new_Transaction_ID, new_Mode, new_Item_No,new_Customer_ID, Transaction_ID)
            st.success("Successfully updated")

    result2 = view_all_payment_data()
    df2 = pd.DataFrame(result2, columns=['Transaction_ID', 'Mode', 'Item_No','price'])
    with st.expander("Updated data"):
        st.dataframe(df2)
