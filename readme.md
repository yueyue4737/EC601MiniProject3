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
<p> Requirements: <p>
<p> (1) Define user stories for store the data; <p>
<p> (2) Define user stories for displaying the data; <p>
<p> (3) Run unit test for the data module. <p>
  
### 3.1 Twitter API+MySQL: track and store published tweets(.csv)
<p> (1) We are collecting the tweets about Vogue and Elle in a 10 columns table seperately; <p>
<p> (2) Be familiar with the basic usage of MySQL community server. <p>
      
### 3.2 Twitter API+MongoDB: track and store the live stream tweets(.txt/.json)
<p> (1) We are collecting the live tweets about Vogue and Elle; <p>
<p> (2) To store the live tweets in mongoDB, we are converting them into a proper format. <p>
      
### 3.3 Double check the sentiments data in Google NLP: from MySQL to Mongo(.csv)
<p> (1) Google NLP: track the sentiment of two files; <p>
<p> (2) set the user_id as the primary key; <p>
<p> (3) import the .csv file into a NoSQL DB. <p>
      
### 3.4 Statistics Result and Visualization for Tweets

#### 3.4.1 Histogram: for a small size dataset

#### 3.4.2 Time Seires Analysis: for the large-scale research

![All Text](https://github.com/yueyue4737/EC601MiniProject3/blob/master/Img/ts0.png)

![All Text](https://github.com/yueyue4737/EC601MiniProject3/blob/master/Img/ts4.png)

*References: READ THE .pdf REPROT & THE ISSUE

Notes: 
===

### 1 no need to do complicated design
<p> I did database design in my specialization courses. In this miniproject, there is no need to use all the commands, because our goal is to store at the very beginning part. <p>

### 2 no need to store images
<p> It is not properly matched the goal of this project. <p>
<p> For more inforation, see: https://stackoverflow.com/questions/6472233/can-i-store-images-in-mysql<p>
 
### 3 time series analysis
<p> I can do it by using R or MS excel, for consistensy, pandas is applied in this project. <p>
 
### 4 error handling in twitter API
<p> I finished the first few drafts very early, but error code '89' appeared again and again. It is successfully only after putting all the code in one .py file. For now, I am thinking about server issue. <p>
 
<p> For more information, see: https://developer.twitter.com/en/docs/basics/response-codes <p>
 
<p> BE CAREFUL: there is a slightly difference between error code and response code! <p>

Links
===

MiniProject3(GoogleDocs):
https://docs.google.com/document/d/16QcWpQQAjGRBR2D5RS91LO-QobxsKP3WgXyfDvgBHZc/edit?usp=sharing
