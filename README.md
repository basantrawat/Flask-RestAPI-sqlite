# Flask - REST API 

REST API pulling data from a sqlite Database. Performing HTTP GET, POST, PUT, & DELETE requests.


# Using cURL for HTTP Requests

## GET REQUEST
For getting data from USERS table
`curl -i http://localhost:5000/users`
OR
`curl -i http://localhost:5000/users/<user_id>`

For getting data from PROFESSION table
`curl -i http://localhost:5000/profession`

## POST REQUEST
`curl -i -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "name=value&address=value&dob=value" http://localhost:5000/users`

## PUT REQUEST
`curl -i -H "Content-Type: application/x-www-form-urlencoded" -X PUT -d "name=value&address=value" http://localhost:5000/users/<user_id>`

## DELETE REQUEST
`curl -X DELETE http://localhost:5000/users/<user_id>`


# To read more about cURL
`https://gist.github.com/subfuzion/08c5d85437d5d4f00e58`