import requests, json

longitude = input("Enter the longtitude")
latitude = input("Enter the latitude")

api = "QrlqoBRyFRdJI4r3Oj-cBLjBJ5foF4HmsA0kqPBbAT9V3H7Vc5qLb9eJS7xsfic1eXossM7u2KzY4gFqaar7XWlqk00L1izroRHJi2C4JvQSNCoZ8DNkq_LUL0wPZHYx"
url = f"https://api.yelp.com/v3/businesses/search?latitude={latitude}&longitude={longitude}&sort_by=best_match"


headers = {
    "accept": "appp/json",
    "Authorization": "Bearer "+api
}


response = requests.get(url,headers=headers)
restaurants = response.json()
if restaurants['businesses'][0]['is_closed']==True:
    status = "Closed"
else:
    status = "Opened"
print(
    "Name: ",restaurants['businesses'][0]['name'],"\n",
    "Image url: ",restaurants['businesses'][0]['image_url'],"\n",
    "Coordinates: ",restaurants['businesses'][0]['coordinates'],"\n",
    "Locations: ",restaurants['businesses'][0]['location'],"\n",
    "Status: ",status,
)
