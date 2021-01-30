



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/adamflasse/take_advantage_of_regression">
    <img src="assets/BecodeLogo.png" alt="Logo" width="240" height="180">
  </a>

  <h1 align="center">Take advantage of regression</h1>
  <h3 align="center">Becode project to test our skills about regression</h3>

  <p align="center">
    by Orhan N., Didier U., Naomi T. and Adam F.
    <br />
    
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  
* [Getting Started](#getting-started)
  * [Choosing the dataset](#choosing-the-dataset)
  * [Set Work Objectives](#set-work-objectives)
* [Data cleaning](#data-cleaning)
* [Data formatting](#data-formatting)
* [Selected models](#selected-models)
* [Evaluation](#evaluation)
* [How went our project?](#how-went-our-project?)




<!-- ABOUT THE PROJECT -->
## About The Project



In our learning path at Becode we had multiple group projects focusing on real estate in Belgium. First we had to scrape some websites to find data and make a solid dataset. Then we had to "merge" all the other groups dataset and work on them. We have essentially done some major data cleaning and then used what we learned about data visualization to make a presentation. We had a week to get familiar with all types of regression, after  which we were asked to test our knowledge to predict house prices on the Belgian market to the best of our abilities using the dataset of our previous mission.



<!-- GETTING STARTED -->
## Getting Started

Because of group changes, we had different datasets available in order to complete the mission. Consequently, we chose the most appropriate one to efficiently start the machine learning project.

### Choosing the dataset

The most appropriate dataset should have:

* the least texts and Nans possible
* no blanks 
* structured data. 

We therefore agreed to choose the dataset of Orhan's previous group.


### Set Work Objectives

To Start with, we chose the important features in order to make a proper cleaning and not waste our time on unused columns.
Secondly we transformed every text in each feature's column into numbers in order to make the model work.
Then we formated the data to train the model.
And finally we tested the different models out and identified the most accurate one.




<!-- USAGE EXAMPLES -->
## Data cleaning

As our target was the price, we determined what the features that affected our target the most were.
It turns out that is more relevant to keep the most of it because the models all performed better with more features than with the chosen ones.



We replaced the text with numbers in all the columns. We made sure that there are no duplicates or NANs.


<!-- ROADMAP -->
## Data formatting

Now that the dataset is ready we can divide the `X` and the `y`.
The `X` corresponds to our features and the `y` is the price.
Then we have to divide our dataset for the training session.


<!-- CONTRIBUTING -->
## Selected models

There are multiple models that we've tested such as Gradient Boosting Regressor, Polynomial Features, LinearRegression, ...



<!-- LICENSE -->
## Evaluation

| Model       |        Score        | 
| :--------- | :---------------: |
| Polynomial Regression | 0,72 |
| Extra Trees Regressor | 0,77 |
| Random Forest | 0,8 |
| Gradient Boosting Regressor | 0,84 |





<!-- CONTACT -->
## How went our project?

This has been a great experience for us all. We've learned new tools such as VSCode Live Share to make our remote collaboration easier and we combined the AGILE methodology and the pommodoro technique so we could be at our top level of efficiency in our work.





