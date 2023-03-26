# README
This repository contains a Flask application that uses a Random Forest Classifier to classify the Iris Dataset.

## Prerequisites
This system requires Python 3 and the following libraries:

- Flask
- PyMySQL
- Scikit-learn


## Files
The repository includes the following files:

- model.py: A Python script that contains the Random Forest Classifier to classify the Iris Dataset.
- index.html: A HTML file that serves as the login page.
- success.html: A HTML file that is displayed after authentication and takes four inputs (Sepal Width, Sepal Length, Petal Width, and Petal Length). After submitting the inputs, the page redirects to results.html.
- results.html: A HTML file that predicts the flower species based on the inputs provided in success.html.
- model.pkl: A pickle file that contains the trained Random Forest Classifier.
- app.py: The main Flask application that ties everything together.
- style.css: A CSS file that contains the styles for the HTML pages in the application. It is used to format and style the HTML elements present in index.html, success.html, and results.html.
## How to run the application

1. Clone the repository to your local machine
2. Ensure that Python, Flask, and all necessary dependencies are installed.
3. Open the terminal/command prompt and navigate to the cloned directory.
4. Run python app.py to start the application.
5. Open a web browser and go to http://localhost:5000 to access the login page.
6. Enter the username and password to access the success page.
7. In the success page, enter the values for Sepal Width, Sepal Length, Petal Width, and Petal Length and click on "Submit".
8. The predicted flower species will be displayed on the results page.

## Existing Authentications in the DataBase
**Username Password**
1. Test Test123
2. Srivatsan123 Srivatsan03
3. Surya123 Surya03

## Acknowledgments
- The Iris Dataset is obtained from the UCI Machine Learning Repository.
- The Flask framework is developed by Pallets.
- The Random Forest Classifier is developed using scikit-learn, a Python library for machine learning.
