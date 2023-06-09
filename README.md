Software Requirements Specification
for
Machine Learning in Diabetes
Version 1.0
 
 
 
Prepared by
saransh kumar  
 
 
 
 
1.Introduction
Document Purpose: To detect if the person is suffering from diabetes using glucose and blood pressure as features and Diabetes as label.

https://github.com/github/AS_AI_ML/blob/assets/unnamed.png


Product Scope: helps to check if a person has diabetics
Intended Audience: Developer, Tester
2.Overall Description
Product Overview:
Product Functionality:
 	R1: Download data in CSV format
 	R2: Using pandas extract features and label from CSV file
 	R3: Build ML Model using ML Algorithm
 	R4: Predict using the test cases 

1.2 Scope
The Diabetes Detection System is designed to predict the presence of diabetes based on input features. It utilizes Naive Bayes and Decision Tree classifiers for prediction.

1.3 Document Conventions
Requirement IDs: Each requirement is identified with a unique ID.
Use Case Diagrams: UML notation is used to represent the use cases.
Sequence Diagrams: UML notation is used to represent the interactions between system components.
1.4 Intended Audience and Reading Suggestions
The intended audience for this document includes the development team, stakeholders, and anyone involved in the development or evaluation of the Diabetes Detection System. It is recommended to read the document in its entirety to gain a comprehensive understanding of the system requirements.

1.5 References
2. Overall Description
2.1 Product Perspective
The Diabetes Detection System is a standalone software application that operates on input data and utilizes machine learning algorithms for diabetes prediction.

2.2 Product Features
Data input and preprocessing.
Training and testing data split.
Naive Bayes classifier for diabetes prediction.
Decision Tree classifier for diabetes prediction.
Prediction output and result interpretation.
2.3 User Classes and Characteristics
The Diabetes Detection System is designed for healthcare professionals, researchers, or individuals interested in predicting diabetes. Users should have basic knowledge of data input and interpretation.

2.4 Operating Environment
The system should be compatible with the following:

Operating System: [Specify the supported operating systems]
Hardware Requirements: [Specify the minimum hardware requirements]
2.5 Design and Implementation Constraints
The system should be implemented using Python programming language.
Required Python packages: numpy, pandas, scikit-learn.
2.6 User Documentation
User documentation, including user guides and manuals, will be provided to guide users on system installation, data input, and result interpretation.

3. Functional Requirements
3.1 Requirement 1: Data Input
The system shall allow users to input diabetes-related data.
The data should include relevant features such as glucose levels, blood pressure, BMI, etc.
3.2 Requirement 2: Training and Testing Data Split
The system shall split the input data into training and testing datasets.
The split ratio should be configurable by the user.
3.3 Requirement 3: Naive Bayes Classifier
The system shall train a Naive Bayes classifier using the training data.
The classifier should be capable of predicting the presence or absence of diabetes based on the input features.
3.4 Requirement 4: Decision Tree Classifier
The system shall train a Decision Tree classifier using the training data.
The classifier should be capable of predicting the presence or absence of diabetes based on the input features.
3.5 Requirement 5: Prediction Output
The system shall provide prediction output for the testing data.
The output should include predicted labels and accuracy measures.
4. Non-Functional Requirements
4.1 Performance
The system shall provide predictions within an acceptable response time.
The system should handle large datasets efficiently.
4.2 Reliability
The system should produce accurate and reliable predictions.
The classifiers should be evaluated using appropriate performance metrics.
4.3 Usability
The system should have a user-friendly interface for data input and result interpretation.
Error messages and notifications should be clear and informative.
4.4 Security
The system should handle user data securely and protect it from unauthorized access.
5. System Models



System Test Plan: Diabetes Detection System
1. Introduction
The purpose of this System Test Plan is to outline the testing approach for the Diabetes Detection System. The system utilizes Naive Bayes and Decision Tree classifiers to predict the presence of diabetes based on input features. The goal of the system testing is to ensure that the system performs accurately and reliably in predicting diabetes.

2. Test Objectives
The main objectives of the system testing are:

Verify the accuracy of the Naive Bayes classifier in predicting diabetes.
Verify the accuracy of the Decision Tree classifier in predicting diabetes.
Validate the system's ability to handle different input features and data distributions.
Ensure that the system handles exceptions and errors gracefully.
3. Test Environment
The system testing will be conducted in the following environment:

Operating System: [Specify the operating system(s) used for testing]
Python Version: [Specify the Python version used]
Required Packages: numpy, pandas, sklearn, matplotlib, seaborn
4. Test Scenarios
The system test scenarios are as follows:

Scenario 1: Naive Bayes Classifier Accuracy
Objective: Verify the accuracy of the Naive Bayes classifier in predicting diabetes.

Test Steps:

Load the diabetes dataset.
Split the data into training and testing sets.
Train the Naive Bayes classifier on the training data.
Make predictions on the testing data.
Calculate the accuracy of the predictions using the true labels.
Compare the accuracy against an expected threshold.
Record the results and observations.
Scenario 2: Decision Tree Classifier Accuracy
Objective: Verify the accuracy of the Decision Tree classifier in predicting diabetes.

Test Steps:

Load the diabetes dataset.
Split the data into training and testing sets.
Train the Decision Tree classifier on the training data.
Make predictions on the testing data.
Calculate the accuracy of the predictions using the true labels.
Compare the accuracy against an expected threshold.
Record the results and observations.
5. Test Data
The system testing will utilize the diabetes dataset provided in the code. The dataset will be split into training and testing sets using a test size of 25%.

6. Test Deliverables
The following deliverables will be produced as part of the system testing:

Test results and observations for each test scenario.
Any issues or defects encountered during testing.
7. Test Execution
The system testing will be performed by executing the Python code provided. The test steps outlined in each scenario will be followed, and the test results will be recorded.

8. Test Criteria
The system testing will be considered successful if the following criteria are met:

The Naive Bayes classifier achieves an accuracy above a predefined threshold.
The Decision Tree classifier achieves an accuracy above a predefined threshold.
The system executes without any critical errors or exceptions.
9. Test Schedule
The system testing will be conducted according to the following schedule:

Start Date: 03/06/2023
End Date: 07/06/2023
Test Execution Time: [Specify the estimated time for test execution]
10. Test Risks and Mitigation
The potential risks associated with system testing are:

Data quality issues in the diabetes dataset.
Overfitting or underfitting of the classifiers.
Performance issues due to large datasets.
Mitigation measures include:

Ensuring the diabetes dataset is accurate and reliable.
Monitoring and fine-tuning the classifiers to address overfitting or underfitting.
Optimizing the system's performance by handling large datasets efficiently.
11. Test Dependencies
The system testing is dependent on the following:

Availability of the diabetes dataset.
Proper installation and configuration of the required Python packages.
