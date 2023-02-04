import pandas as pd
import streamlit as st
import plotly.express as px
from database import *
from procedure import *


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Admin ID', 'First_Name', 'Last_Name', 'Email', 'Address'])
    with st.expander("View Admin"):
        st.dataframe(df)

    result4 = total_revenue_on_dailybasis()
    df4 = pd.DataFrame(result4, columns=['Delivery Date', 'revenue'])
    with st.expander("Total revenue on daily basis"):
        st.dataframe(df4)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Add data to table"):
            insert_revenue_dailybasis()
            st.success("successfully added the above data to a table  ")
    with col2:
        if st.button("Remove data from table"):
            truncate_revenue_dailybasis()
            st.success("successfully removed all the data from the table ")

    c.execute('select Final_delivery_date,min(revenue) from delivery;')
    data = c.fetchall()
    df5 = pd.DataFrame(data, columns=['date', 'Min revenue'])
    with st.expander("The minimum revenue is "):
        st.dataframe(df5)

    c.execute('select Final_delivery_date,max(revenue) from delivery;')
    data1 = c.fetchall()
    df6 = pd.DataFrame(data1, columns=['Date', 'Max revenue'])
    with st.expander("The maximum revenue is "):
        st.dataframe(df6)

    list_of_destination = [i[0] for i in view_courier_destination()]
    selected_destination = st.selectbox("Courier in the particular destination", list_of_destination)
    st.warning("Do you want to show the courier details of all the courier's in ::{}".format(selected_destination))

    data=person_max_courier(selected_destination)
    df7=pd.DataFrame(data,columns=['customer_ID','First_name','Last_name','email','Phone','DOB','Age','Number of courier'])
    st.dataframe(df7)
    var1=df7._get_value(0,'customer_ID')

    c.execute('select courier.Courier_ID FROM Courier INNER JOIN customer on courier.customer_ID=customer.customer_ID '
              'And customer.customer_ID={} AND courier.courier_destination="{}"'.format(var1,selected_destination))
    data2=c.fetchall()
    df8=pd.DataFrame(data2,columns=['Courier_ID'])
    st.dataframe(df8)

    res = show_destination_with_max_courier()
    df = pd.DataFrame(res, columns=['Delivery Destination','Number of courier'])
    with st.expander("Destination with maximum number of courier to be delivered is "):
        st.dataframe(df)



def read_customer():
    result = view_all_customer_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Customer_id', 'First_name', 'Last_name', 'Email', 'Phone', ' Dob', 'Age', 'AdminID'])
    with st.expander("View Customer"):
        st.dataframe(df)


def read_hub():
    result = view_all_hub_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Hub_id', 'Name', 'Location', 'Phone', 'AdminID'])
    with st.expander("View Hub"):
        st.dataframe(df)

    result1=item_delivery_today()
    df1=pd.DataFrame(result1,columns=['Item_No','Final_delivery_date','Customer_ID','Name','Location'])
    with st.expander("Items to be delivered today"):
        st.dataframe(df1)

    result2 = item_delivery_tomorrow()
    df2 = pd.DataFrame(result2, columns=['Item_No', 'Final_delivery_date', 'Customer_ID', 'Name', 'Location'])
    with st.expander("Items to be delivered tomorrow"):
        st.dataframe(df2)


def read_courier():
    result = view_courier_customer()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Courier_ID', 'Courier_Type', 'Courier_Destination', 'customer_ID', "First_Name",
                               "Last_Name"])
    with st.expander("View Courier"):
        st.dataframe(df)

    with st.expander("Customer with total number of courier display"):
        task_df = df['customer_ID'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names="index", values='customer_ID')
        st.plotly_chart(p1)


def read_track():
    result = view_all_track_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Order_No', 'Order_received', 'Order_picked', 'Out_for_delivery', 'Reached_destination',
                               'AdminID'])
    with st.expander("View Track"):
        st.dataframe(df)

    with st.expander("Your delivery progress"):
        my_procedure()



def read_shipping():
    result = view_all_shipping_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Item_No', 'Weight', 'Final_delivery_date', 'customer_ID','Hub_id'])
    with st.expander("View shipping"):
        st.dataframe(df)

    result2 = show_courier_not_shipped()
    df1 = pd.DataFrame(result2, columns=['Customer_ID', 'First_Name', 'Last_Name', 'Item_No', 'Courier_ID'])
    nan_values = df1[df1['Item_No'].isna()]
    with st.expander("View customers whose couriers were not shipped"):
        st.dataframe(nan_values[['Customer_ID', 'First_Name', 'Last_Name']])




def read_payment():
    result = view_all_payment_data()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Item_No','Transaction_ID', 'Mode', 'Customer ID'])
    with st.expander("View Payment"):
        st.dataframe(df)


    col1, col2 = st.columns(2)
    with col1:
        if st.button("Add data"):
            insert_courier_by_customer()
            st.success("successfully added all the customers whose courier has reached shipping into the table ")
    with col2:
        if st.button("Remove data"):
            truncate_courier_by_customer()
            st.success("successfully removed all the data")

    result2 = view_courier_by_customer()
    df2 = pd.DataFrame(result2, columns=['Customer_ID', 'First_Name', 'Last_Name', 'Item_No', 'Courier_ID'])
    with st.expander("display customer whose courier will go for shipping (reach the hub)"):
        st.dataframe(df2)

    result3 = function_query()
    df3 = pd.DataFrame(result3, columns=['Customer_ID', 'First_Name', 'Last_Name', 'Amount'])
    with st.expander("Amount to be paid by each customer whose courier will be shipped"):
        st.dataframe(df3)







