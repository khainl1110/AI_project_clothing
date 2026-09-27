from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

try:
    database = client.get_database("sample_airbnb")
    movies = database.get_collection("listingsAndReviews")

    # Queries for a movie that has the title 'Back to the Future'
    query = { "title": "Back to the Future" }
    movie = movies.find_one(query)

    print(json.dumps(movie, indent=4, default=str))

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)


