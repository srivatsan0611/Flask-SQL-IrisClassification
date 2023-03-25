CREATE DATABASE flask_login;
USE flask_login;



CREATE TABLE Accounts ( 
username varchar(50) NOT NULL,
password varchar(255) NOT NULL
);

INSERT INTO Accounts VALUES ("Srivatsan123","Srivatsan03"),("Surya123","Surya03"),("Test","Test123");
SELECT *FROM Accounts;


