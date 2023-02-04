# pip install mysql-connector-python
import mysql.connector
import pandas as pd
import streamlit

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="courier"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Admin(Admin_ID int, First_Name varchar(30),'
              'Last_Name varchar(30),'
              'email varchar(30), Address TEXT)')


# c.execute('alter table admin add primary key(Admin_ID)')
# c.execute('alter table customer add primary key(Customer_ID)')

def create_customer_table():
    c.execute('CREATE TABLE IF NOT EXISTS Customer(Customer_id int, First_name varchar(30), Last_name varchar(30), '
              'Email varchar(30), Phone int , Dob DATE , Age int , AdminID int)')


def create_hub_table():
    c.execute('CREATE TABLE if not exists hub(HubID int NOT NULL, Name varchar(20), Location varchar(20),Phone_NO int '
              ',AdminID int)');


def create_courier_table():
    c.execute('create table if not exists courier(Courier_ID varchar(20),Courier_Type varchar(20), '
              'Courier_Destination varchar(20), '
              'customer_ID int, PRIMARY KEY(Courier_ID) , Foreign key(customer_ID) references customer(Customer_ID));')


def create_track_table():
    c.execute('create table if not exists track(Order_No int, Order_received varchar(20), Order_picked varchar(20), '
              'Out_for_delivery varchar(20), Reached_destination varchar(20), AdminID int , PRIMARY KEY(Order_No) , '
              'FOREIGN KEY (AdminID) references Admin(Admin_ID));')


def create_shipping_table():
    c.execute(
        'create table if not exists shipping(Item_No int , Weight int , Destination varchar(20), Final_delivery_date '
        'date, '
        'Courier_ID varchar(20),PRIMARY KEY(Item_No) , FOREIGN KEY(Courier_ID) references Courier(Courier_ID));')


def create_payment_table():
    c.execute('create table if not exists payment(Transaction_ID int, Mode varchar(20), Item_No int)')


def add_data(Admin_id, First_name, Last_name, Email, Address):
    c.execute('INSERT INTO Admin(Admin_id, First_name, Last_name, Email, Address) VALUES (%s,%s,%s,%s,'
              '%s)',
              (Admin_id, First_name, Last_name, Email, Address))
    mydb.commit()


def add_customer_data(Customer_id, First_name, Last_name, Email, Phone, Dob, Age, AdminID):
    c.execute('INSERT INTO Customer(Customer_id, First_name, Last_name, Email, Phone, Dob, Age, AdminID) VALUES (%s,'
              '%s,%s,%s,%s,%s,%s,%s)',
              (Customer_id, First_name, Last_name, Email, Phone, Dob, Age, AdminID))
    mydb.commit()


def add_hub_data(Hub_id, Name, Location, Phone, AdminID):
    c.execute('INSERT INTO hub(HubID, Name, Location, Phone_NO, AdminID) VALUES (%s,%s,%s,%s,%s)',
              (Hub_id, Name, Location, Phone, AdminID))
    mydb.commit()


def add_courier_data(Courier_ID, Courier_Type, Courier_Destination, customer_ID):
    c.execute('INSERT INTO courier(Courier_ID,Courier_Type,Courier_Destination,customer_ID) VALUES (%s,%s,%s,%s)',
              (Courier_ID, Courier_Type, Courier_Destination, customer_ID))
    mydb.commit()


def add_track_data(Order_no, Order_received, Order_picked, Out_for_delivery, Reached_destination, AdminID):
    c.execute('INSERT INTO track(Order_no, Order_received , Order_picked,Out_for_delivery,Reached_destination,'
              'AdminID) VALUES (%s,%s,%s,%s,%s,%s)',
              (Order_no, Order_received, Order_picked, Out_for_delivery, Reached_destination, AdminID))
    mydb.commit()


def add_shipping_data(Item_No, Weight, Final_delivery_date, customer_ID, Hub_id):
    c.execute('INSERT INTO shipping(Item_No, Weight, Final_delivery_date,customer_ID,Hub_id) VALUES (%s,%s,'
              '%s,%s,%s)', (Item_No, Weight, Final_delivery_date, customer_ID, Hub_id))


def add_payment_data(Item_No, Transaction_ID, Mode, Customer_ID):
    c.execute('INSERT INTO payment(Item_No,Transaction_ID, Mode,Customer_ID) VALUES (%s,%s,%s,%s)',
              (Item_No, Transaction_ID, Mode, Customer_ID))


def view_all_data():
    c.execute('SELECT * FROM Admin')
    data = c.fetchall()
    return data


def view_all_customer_data():
    c.execute('SELECT * FROM Customer')
    data = c.fetchall()
    return data


def view_all_hub_data():
    c.execute('SELECT * FROM Hub')
    data = c.fetchall()
    return data


def view_all_courier_data():
    c.execute('SELECT * FROM courier')
    data = c.fetchall()
    return data


def view_all_track_data():
    c.execute('SELECT * FROM track')
    data = c.fetchall()
    return data


def view_all_shipping_data():
    c.execute('SELECT * FROM shipping')
    data = c.fetchall()
    return data


def view_all_payment_data():
    c.execute('SELECT * FROM payment')
    data = c.fetchall()
    return data


def view_only_names():
    c.execute('SELECT Admin_ID FROM Admin')
    data = c.fetchall()
    return data


def view_only_customer_names():
    c.execute('SELECT Customer_ID FROM Customer')
    data = c.fetchall()
    return data


def view_only_hub_names():
    c.execute('SELECT HubID FROM Hub')
    data = c.fetchall()
    return data


def view_only_courier_names():
    c.execute('SELECT Courier_ID FROM Courier')
    data = c.fetchall()
    return data


def view_only_track_names():
    c.execute('SELECT Order_No FROM track')
    data = c.fetchall()
    return data


def view_only_shipping_names():
    c.execute('SELECT Item_No FROM shipping')
    data = c.fetchall()
    return data


def view_only_payment_names():
    c.execute('SELECT Transaction_ID FROM payment')
    data = c.fetchall()
    return data


def view_courier_destination():
    c.execute('SELECT DISTINCT Courier_Destination from courier')
    data = c.fetchall()
    return data


def show_destination_based_courier(Courier_Destination):
    c.execute('select courier.Courier_ID,customer.First_Name,customer.Last_Name,courier.Courier_Type,p.Mode,'
              'p.Transaction_ID FROM Courier INNER JOIN customer on '
              'courier.customer_ID=customer.customer_ID AND courier.Courier_Destination="{}" LEFT JOIN payment p '
              'on customer.customer_ID = p.customer_ID'.format(Courier_Destination))
    data = c.fetchall()
    return data


def show_destination_with_max_courier():
    c.execute('SELECT courier_destination,MAX(Y.mycount) courierCount FROM (SELECT courier_destination,'
              'COUNT(Courier_ID) mycount FROM courier GROUP BY courier_destination) Y')
    data = c.fetchall()
    return data


def person_max_courier(Courier_Destination):
    c.execute('select customer_ID,First_name,Last_name,email,Phone,DOB,Age,MAX(mycount) couriercount FROM( '
              'select customer.customer_ID,customer.First_name,customer.Last_name,customer.email,customer.Phone,'
              'customer.DOB,customer.Age,courier.Courier_ID,COUNT(customer.customer_ID) mycount FROM Courier INNER '
              'JOIN customer on courier.customer_ID=customer.customer_ID AND courier.Courier_Destination="{}" '
              'GROUP BY customer.customer_ID ORDER BY COUNT(customer.Customer_ID) DESC) Y'.format(Courier_Destination))
    data = c.fetchall()
    return data;


def view_courier_customer():
    c.execute('SELECT courier.Courier_ID,courier.Courier_Type,courier.Courier_Destination,courier.customer_ID,'
              'customer.First_name,customer.Last_Name FROM courier INNER JOIN customer Where '
              'courier.customer_ID=customer.customer_ID')
    data = c.fetchall()
    return data


def view_courier_by_customer():
    c.execute('select * from courier_by_customer;')
    data = c.fetchall()
    return data


def get_admin(Admin_ID):
    c.execute('SELECT * FROM Admin WHERE Admin_ID="{}"'.format(Admin_ID))
    data = c.fetchall()
    return data


def get_customer(Customer_ID):
    c.execute('SELECT * FROM Customer WHERE Customer_ID="{}"'.format(Customer_ID))
    data = c.fetchall()
    return data


def get_hub(HubID):
    c.execute('SELECT * FROM Hub WHERE HubID="{}"'.format(HubID))
    data = c.fetchall()
    return data


def get_courier(CourierID):
    c.execute('SELECT * FROM Courier WHERE Courier_ID="{}"'.format(CourierID))
    data = c.fetchall()
    return data


def get_track(Order_No):
    c.execute('SELECT * FROM track WHERE Order_No="{}"'.format(Order_No))
    data = c.fetchall()
    return data


def get_shipping(Item_No):
    c.execute('SELECT * FROM shipping WHERE Item_No="{}"'.format(Item_No))
    data = c.fetchall()
    return data


def get_payment(Transaction_ID):
    c.execute('SELECT * FROM payment WHERE Transaction_ID="{}"'.format(Transaction_ID))
    data = c.fetchall()
    return data


def edit_admin_data(new_admin_id, new_first_name, new_last_name, new_email, new_address, admin_id):
    c.execute("UPDATE Admin SET Admin_ID=%s, First_Name=%s, Last_Name=%s, email=%s, Address=%s WHERE Admin_ID=%s",
              (new_admin_id, new_first_name, new_last_name, new_email, new_address, admin_id))
    mydb.commit()

    # data = c.fetchall()
    # return data


def edit_customer_data(new_Customer_id, new_First_name, new_Last_name, new_Email, new_Phone, new_Dob, new_Age,
                       new_AdminID, Customer_id):
    c.execute("UPDATE Customer SET Customer_ID=%s, First_Name=%s, Last_Name=%s, Email=%s, Phone=%s, Dob=%s, Age=%s, "
              "AdminID=%s WHERE Customer_ID=%s",
              (new_Customer_id, new_First_name, new_Last_name, new_Email, new_Phone, new_Dob, new_Age, new_AdminID,
               Customer_id))
    mydb.commit()


def edit_hub_data(new_hub_id, new_name, new_Location, new_phone, new_admin, hub_id):
    c.execute("UPDATE Hub SET HubID=%s, Name=%s, Location=%s, Phone_NO=%s, AdminID=%s WHERE HubID=%s",
              (new_hub_id, new_name, new_Location, new_phone, new_admin, hub_id))
    mydb.commit()


def edit_courier_data(new_Courier_ID, new_Courier_Type, new_Courier_Destination, new_customer_ID, Courier_ID):
    c.execute(
        "UPDATE Courier SET Courier_ID=%s, Courier_Type=%s, Courier_Destination=%s, customer_ID=%s WHERE Courier_ID=%s",
        (new_Courier_ID, new_Courier_Type, new_Courier_Destination, new_customer_ID, Courier_ID))
    mydb.commit()


def edit_track_data(new_Order_no, new_Order_received, new_Order_picked, new_Out_for_delivery, new_Reached_destinationn,
                    new_AdminID, Order_no):
    c.execute("UPDATE track SET Order_No=%s, Order_received=%s, Order_picked=%s, Out_for_delivery=%s,"
              "Reached_destination=%s,AdminID=%s WHERE Order_No=%s",
              (new_Order_no, new_Order_received, new_Order_picked, new_Out_for_delivery, new_Reached_destinationn,
               new_AdminID, Order_no))
    mydb.commit()


def edit_shipping_data(new_Item_No, new_Weight, new_Final_delivery_date, customer_id, Hub_id, Item_No):
    c.execute("UPDATE shipping SET Item_No=%s, Weight=%s, Final_delivery_date=%s,"
              "customer_ID=%s ,Hub_id=%s WHERE Item_No=%s",
              (new_Item_No, new_Weight, new_Final_delivery_date, customer_id, Hub_id, Item_No))
    mydb.commit()


def edit_payment_data(new_Item_No, new_Transaction_ID, new_Mode, new_Customer_ID, Transaction_ID):
    c.execute("UPDATE payment SET , Item_No=%s,Transaction_ID=%s, Mode=%s ,new_Customer_ID=%s WHERE Transaction_ID=%s",
              (new_Item_No, new_Transaction_ID, new_Mode, new_Customer_ID, Transaction_ID))
    mydb.commit()


def delete_data(Admin_ID):
    c.execute('DELETE FROM Admin WHERE Admin_ID="{}"'.format(Admin_ID))
    mydb.commit()


def delete_customer_data(Customer_ID):
    c.execute('DELETE FROM Customer WHERE Customer_ID="{}"'.format(Customer_ID))
    mydb.commit()


def delete_hub_data(HubID):
    c.execute('DELETE FROM Hub WHERE HubID="{}"'.format(HubID))
    mydb.commit()


def delete_courier_data(CourierID):
    c.execute('DELETE FROM courier WHERE Courier_ID="{}"'.format(CourierID))
    mydb.commit()


def delete_track_data(Order_No):
    c.execute('DELETE FROM track WHERE Order_No="{}"'.format(Order_No))
    mydb.commit()


def delete_shipping_data(Item_No):
    c.execute('DELETE FROM shipping WHERE Item_No="{}"'.format(Item_No))
    mydb.commit()


def delete_payment_data(Transaction_ID):
    c.execute('DELETE FROM payment WHERE Transaction_ID="{}"'.format(Transaction_ID))
    mydb.commit()


# LEFT JOIN AND INNER JOIN NESTED
def show_courier_not_shipped():
    c.execute('select Customer.Customer_ID,Customer.First_Name,'
              'Customer.Last_Name,Shipping.Item_No,Courier.Courier_ID from ((customer left join shipping on '
              'customer.customer_ID=shipping.customer_ID)LEFT JOIN courier on courier.customer_ID '
              '=customer.customer_ID);')
    data = c.fetchall()
    return data


def truncate_courier_by_customer():
    c.execute('truncate table courier_by_customer;')
    mydb.commit()


def insert_courier_by_customer():
    c.execute('insert into courier_by_customer select Customer.Customer_ID,Customer.First_Name, Customer.Last_Name,'
              'Payment.Item_No,Courier.Courier_ID from ((customer left join payment on '
              'customer.customer_ID=payment.customer_ID)LEFT JOIN courier on courier.customer_ID '
              '=customer.customer_ID) where Item_No!=0;')


def function_query():
    c.execute('SELECT DISTINCT customer_id,First_Name,Last_Name,compute_amount4(customer_id) FROM courier_by_customer;')

    data = c.fetchall()
    return data


def total_revenue_on_dailybasis():
    c.execute(
        'select Final_delivery_date,sum(compute_amount3(customer_id)) from shipping group by Final_delivery_date;')
    data = c.fetchall()
    return data


def insert_revenue_dailybasis():
    c.execute('insert into delivery select Final_delivery_date,sum(compute_amount3(customer_id)) from shipping group '
              'by Final_delivery_date;')
    mydb.commit()


def truncate_revenue_dailybasis():
    c.execute('truncate table delivery;')
    mydb.commit()


def Q(query):
    if streamlit.button("Enter"):
        c.execute(query)
        data = c.fetchall()
        df3 = pd.DataFrame(data)
        with streamlit.expander("Result"):
            streamlit.dataframe(df3)


def item_delivery_today():
    c.execute('select shipping.Item_No,shipping.Final_delivery_date,shipping.Customer_ID,Hub.Name ,Hub.Location from '
              'shipping inner join hub on shipping.Hub_id= Hub.HubID where shipping.Final_delivery_date=curdate();')
    data = c.fetchall()
    return data


def item_delivery_tomorrow():
    c.execute(
        'select shipping.Item_No,shipping.Final_delivery_date,shipping.Customer_ID,Hub.Name ,Hub.Location from '
        'shipping inner join hub on shipping.Hub_id= Hub.HubID where shipping.Final_delivery_date=curdate()+1;')
    data = c.fetchall()
    return data


def show_progress(num):
    statement = "SET @order_number={}"
    c.execute(statement.format(num))
    statement = "CALL delivery_prog1(@order_number,@ans)"
    c.execute(statement)
    statement = "SELECT (@ans/4)*100"
    c.execute(statement)
    data = c.fetchall()
    return data


def show_tables():
    c.execute('show tables')
    res = c.fetchall()
    tables = [i[0] for i in res]
    return tables


def view_table(table):
    c.execute(f'select * from {table}')
    res = c.fetchall()
    return res


def get_attributes(table):
    c.execute(f'select * from {table}')
    res = c.fetchall()
    attributes = c.column_names
    return attributes


def execute_query(query):
    try:
        c.execute(query)
        if query.split()[0].lower() not in ['select', 'show']:
            mydb.commit()
        data = c.fetchall()
        return [data, c.column_names]
    except BaseException as e:
        if str(e) == 'No result set to fetch from.':
            streamlit.success('query successful')
            return 1
        streamlit.error(e)
        return 0
