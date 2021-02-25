# This flask api is deployed on Heroku.

**Heroku app link : https://shop-items-api-at-heroku.herokuapp.com/**

### Guide :
It works on following endpoints:

1) /getitems 
This will give you all available items in a shop along with their price.

2) /<provide any item name>
e.g: /bag , /cap, /mobile
This will give you price of that specific item, if item is not available then it will return "item is not available".
  
3) /additem
This will add any new item along with it price in mongoDB.

This is how it will give you results.
