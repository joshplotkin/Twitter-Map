Twitter Map
=========

This project was made with Priya Venkat during Fall 2014 and uses the following:
* AWS EC2, SQS, SNS)
* node.js (with socket.io for web socket)
* d3.js
* angular for front-end
* twitter API
* python for sentiment analysis 

[LINK TO TWITTER MAP](http://54.173.153.248:3000/) 

using the twitter-map: 
* allow a few moments for the data to populate (I would have used an in-memory solution such as redis or Apache Geode in hindsight)
* use the button on the nav bar to toggle between maps
* the number in the buttons are number of tweets (fewer for sentiment analysis since we have sentiment on fewer of those). if you leave the page open you should see the numbers in the buttons increasing in real time and the map adding points in real time (harder to see than the numbers going up) 
* to see the sentiment heatmap, click a positive and/or negative sentiment, plus any number of keywords
