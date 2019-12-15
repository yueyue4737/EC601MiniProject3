Compare Mongo DB versus my SQL Yue Liu
===

1 Review major used database systems in cloud 
---

<p> To store tweets in the mini project1, it is necessary to use the database. SQL(structured query language) is efficient to reach the target record. <p> 

<p> The usage of database system in cloud(except MySQL and MongoDB) <p>
 
![All Text](https://github.com/yueyue4737/EC601MiniProject3/blob/master/Img/Product.png)

2 What is the difference between them?
---

![All Text](https://github.com/yueyue4737/EC601MiniProject3/blob/master/Img/Mysql_mongo.png)
<p> Basically, it is about SQL and NoSQL, the MySQL and MongoDB. <p>
  
![All Text](https://github.com/yueyue4737/EC601MiniProject3/blob/master/Img/Concept.png)

3 Implementation
---
<p> Requirements:
(1) Define user stories for store the data;
(2) Define user stories for displaying the data;
(3) Run unit test for the data module.
<p>
  
### 3.1 Twitter API+MySQL: track and store published tweets(.csv)
<p> (1) We are collecting the tweets about Vogue and Elle in a 10 columns table seperately; 
    (2) Be familiar with the basic usage of MySQL community server. <p>
      
### 3.2 Twitter API+MongoDB: track and store the live stream tweets(.txt/.json)
<p> (1) We are collecting the live tweets about Vogue and Elle;
    (2) To store the live tweets in mongoDB, we are converting them into a proper format. <p>
      
### 3.3 Double check the sentiments data in Google NLP: from MySQL to Mongo(.csv)
<p> (1) Google NLP: track the sentiment of two files;
    (2) set the user_id as the primary key;
    (3) import the .csv file into a NoSQL DB. <p>
      
### 3.4 Statistics Result and Visualization for Tweets

#### 3.4.1 Histogram: for a small size dataset

#### 3.4.2 Time Seires Analysis: for the large-scale research

*References: READ THE .pdf REPROT & THE ISSUE

Links
===

MiniProject3(GoogleDocs):
https://docs.google.com/document/d/16QcWpQQAjGRBR2D5RS91LO-QobxsKP3WgXyfDvgBHZc/edit?usp=sharing
