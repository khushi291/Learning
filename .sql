create table Customers
(
	Cust_ID int,
	Phone_No varchar(10),
	Email_ID varchar(20),
 	Risk_Flag varchar(20),
 	PRIMARY KEY(Cust_ID)
);

insert into Customers(Cust_ID, Phone_No, Email_ID, Risk_Flag) values
(1, '8421558775', 'abc@gmail.com', 'Medium Risk'),
(2, '7514552157', 'def@hotmail.com', 'Low Risk'),
(3, '9540558775', 'ghi@yahoo.com', 'Very High Risk'),
(4, '7413584845', 'jkl@gmail.com', 'Medium Risk'),
(5, '8187856896', 'mnop@gmail.com', 'High Risk')
