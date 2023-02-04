import streamlit as st
import mysql.connector


from procedure import *

from create import *
from database import *
from delete import *
from read import *
from update import *
from query_box import QueryBox


def main():
    st.title("COURIER MANAGEMENT SYSTEM")
    menu = ["Admin", "Customer", "Hub", "Courier", "Payment", "Shipping", "Track", "Query"]
    options = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Admin":
        choice1 = st.sidebar.selectbox("Options", options)
        if choice1 == "Add":
            st.subheader("Enter Admin Details:")
            create()
        elif choice1 == "View":
            st.subheader("View Admin Details")
            read()

        elif choice1 == "Edit":
            st.subheader("Update Admin Details")
            update()

        elif choice1 == "Remove":
            st.subheader("Delete Admin details")
            delete()

        else:
            st.subheader("About Admin")

    elif choice == "Customer":
        choice1 = st.sidebar.selectbox("Options", options)
        create_customer_table()
        if choice1 == "Add":
            st.subheader("Enter Customer Details:")
            create_customer()
        elif choice1 == "View":
            st.subheader("View Customer Details")
            read_customer()

        elif choice1 == "Edit":
            st.subheader("Update Customer Details")
            update_customer()

        elif choice1 == "Remove":
            st.subheader("Delete Customer details")
            delete_customer()

        else:
            st.subheader("About Customer")

    elif choice == "Hub":
        choice1 = st.sidebar.selectbox("Options", options)
        create_hub_table()
        if choice1 == "Add":
            st.subheader("Enter Hub Details:")
            create_hub()
        elif choice1 == "View":
            st.subheader("View Hub Details")
            read_hub()

        elif choice1 == "Edit":
            st.subheader("Update Hub Details")
            update_hub()

        elif choice1 == "Remove":
            st.subheader("Delete Hub details")
            delete_hub()

        else:
            st.subheader("About Hub")

    elif choice == "Courier":
        choice1 = st.sidebar.selectbox("Options", options)
        create_courier_table()
        if choice1 == "Add":
            st.subheader("Enter Courier Details:")
            create_courier()
        elif choice1 == "View":
            st.subheader("View Courier Details")
            read_courier()

        elif choice1 == "Edit":
            st.subheader("Update Courier Details")
            update_courier()

        elif choice1 == "Remove":
            st.subheader("Delete Courier details")
            delete_courier()

        else:
            st.subheader("About Courier")

    elif choice == "Track":
        choice1 = st.sidebar.selectbox("Options", options)
        create_track_table()
        if choice1 == "Add":
            st.subheader("Enter Track Details:")
            create_track()
        elif choice1 == "View":
            st.subheader("View Track Details")
            read_track()

        elif choice1 == "Edit":
            st.subheader("Update Track Details")
            update_track()

        elif choice1 == "Remove":
            st.subheader("Delete Track details")
            delete_track()

        else:
            st.subheader("About Track")

    elif choice == "Shipping":
        choice1 = st.sidebar.selectbox("Options", options)
        create_shipping_table()
        if choice1 == "Add":
            st.subheader("Enter Shipping Details:")
            create_shipping()
        elif choice1 == "View":
            st.subheader("View Shipping Details")
            read_shipping()

        elif choice1 == "Edit":
            st.subheader("Update Shipping Details")
            update_shipping()

        elif choice1 == "Remove":
            st.subheader("Delete Shipping details")
            delete_shipping()

        else:
            st.subheader("About Shipping")

    elif choice == "Payment":
        choice1 = st.sidebar.selectbox("Options", options)
        create_payment_table()
        if choice1 == "Add":
            st.subheader("Enter Payment Details:")
            create_payment()
        elif choice1 == "View":
            st.subheader("View Payment Details")
            read_payment()

        elif choice1 == "Edit":
            st.subheader("Update Payment Details")
            update_payment()

        elif choice1 == "Remove":
            st.subheader("Delete Payment details")
            delete_payment()

        else:
            st.subheader("About Payment")

    elif choice == "Query":
        st.subheader("Query Window")
        QueryBox()



if __name__ == '__main__':
    main()
