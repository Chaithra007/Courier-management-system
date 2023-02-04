import pandas as pd
import streamlit as st
from database import *


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Admin ID', 'First Name', 'Last Name', 'Email', 'Address'])
    with st.expander("Current admin details"):
        st.dataframe(df)

    list_of_admin = [i[0] for i in view_only_names()]
    selected_admin = st.selectbox("Admin to Delete", list_of_admin)
    st.warning("Do you want to delete ::{}".format(selected_admin))
    if st.button("Delete Admin"):
        delete_data(selected_admin)
        st.success("Admin has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Admin ID', 'First Name', 'Last Name', 'Email', 'Address'])
    with st.expander("Updated details"):
        st.dataframe(df2)


def delete_customer():
    result = view_all_customer_data()
    df = pd.DataFrame(result,
                      columns=['Customer_id', 'First_name', 'Last_name', 'Email', 'Phone', ' Dob', 'Age', 'AdminID'])
    with st.expander("Current customer details"):
        st.dataframe(df)

    list_of_customer = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Customer to Delete", list_of_customer)
    st.warning("Do you want to delete ::{}".format(selected_customer))
    if st.button("Delete Customer"):
        delete_customer_data(selected_customer)
        st.success("Customer has been deleted successfully")
    new_result = view_all_customer_data()
    df2 = pd.DataFrame(new_result,
                       columns=['Customer_id', 'First_name', 'Last_name', 'Email', 'Phone', ' Dob', 'Age', 'AdminID'])
    with st.expander("Updated details"):
        st.dataframe(df2)


def delete_hub():
    result = view_all_hub_data()
    df = pd.DataFrame(result,
                      columns=['Hub_id', 'Name', 'Location', 'Phone', 'AdminID'])
    with st.expander("Current Hub details"):
        st.dataframe(df)

    list_of_hub = [i[0] for i in view_only_hub_names()]
    selected_hub = st.selectbox("Hub to Delete", list_of_hub)
    st.warning("Do you want to delete ::{}".format(selected_hub))
    if st.button("Delete Hub"):
        delete_hub_data(selected_hub)
        st.success("Hub has been deleted successfully")
    new_result = view_all_hub_data()
    df2 = pd.DataFrame(new_result,
                       columns=['Hub_id', 'Name', 'Location', 'Phone', 'AdminID'])
    with st.expander("Updated details"):
        st.dataframe(df2)


def delete_courier():
    result = view_all_courier_data()
    df = pd.DataFrame(result,
                      columns=['Courier_ID', 'Courier_Type', 'Courier_Destination', 'customer_ID'])
    with st.expander("Current Courier details"):
        st.dataframe(df)

    list_of_courier = [i[0] for i in view_only_courier_names()]
    selected_courier = st.selectbox("Hub to Delete", list_of_courier)
    st.warning("Do you want to delete ::{}".format(selected_courier))
    if st.button("Delete Courier"):
        delete_courier_data(selected_courier)
        st.success("Courier has been deleted successfully")
    new_result = view_all_courier_data()
    df2 = pd.DataFrame(new_result,
                       columns=['Courier_ID', 'Courier_Type', 'Courier_Destination', 'customer_ID'])
    with st.expander("Updated details"):
        st.dataframe(df2)


def delete_track():
    result = view_all_track_data()
    df = pd.DataFrame(result,
                      columns=['Order_No', 'Order_received', 'Order_picked', 'Out_for_delivery', 'Reached_destination',
                               'AdminID'])
    with st.expander("Current track details"):
        st.dataframe(df)

    list_of_track = [i[0] for i in view_only_track_names()]
    selected_track = st.selectbox("Track to Delete", list_of_track)
    st.warning("Do you want to delete ::{}".format(selected_track))
    if st.button("Delete Track"):
        delete_track_data(selected_track)
        st.success("Track has been deleted successfully")
    new_result = view_all_track_data()
    df2 = pd.DataFrame(new_result,
                       columns=['Order_No', 'Order_received', 'Order_picked', 'Out_for_delivery', 'Reached_destination',
                                'AdminID'])
    with st.expander("Updated details"):
        st.dataframe(df2)


def delete_shipping():
    result = view_all_shipping_data()
    df = pd.DataFrame(result,
                      columns=['Item_No', ' Weight', 'Final_delivery_date', 'customer_ID','hubid'])
    with st.expander("Current shipping details"):
        st.dataframe(df)

    list_of_shipping = [i[0] for i in view_only_shipping_names()]
    selected_shipping = st.selectbox("shipping to Delete", list_of_shipping)
    st.warning("Do you want to delete ::{}".format(selected_shipping))
    if st.button("Delete shipping"):
        delete_shipping_data(selected_shipping)
        st.success("shipping has been deleted successfully")
    new_result = view_all_shipping_data()
    df2 = pd.DataFrame(new_result,
                       columns=['Item_No', ' Weight', 'Final_delivery_date', 'customer_ID','hubid'])
    with st.expander("Updated details"):
        st.dataframe(df2)


def delete_payment():
    result = view_all_payment_data()
    df = pd.DataFrame(result,
                      columns=['Transaction_ID', 'Mode', 'Item_No','price'])
    with st.expander("Current payment details"):
        st.dataframe(df)

    list_of_payment = [i[0] for i in view_only_payment_names()]
    selected_payment = st.selectbox("payment to Delete", list_of_payment)
    st.warning("Do you want to payment ::{}".format(selected_payment))
    if st.button("Delete payment"):
        delete_payment_data(selected_payment)
        st.success("payment has been deleted successfully")
    new_result = view_all_payment_data()
    df2 = pd.DataFrame(new_result,
                       columns=['Transaction_ID', 'Mode', 'Item_No','price'])
    with st.expander("Updated details"):
        st.dataframe(df2)
