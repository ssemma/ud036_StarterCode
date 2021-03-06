import media
import fresh_tomatoes
import httplib
import json
import requests
import config


# Apply API_KEY
API_KEY = config.init()

conn = httplib.HTTPSConnection("api.themoviedb.org")

payload = "{}"

# Get the upcoming movie's id, title, poster_path, through request url
conn.request("GET",
             "/3/movie/upcoming?page=1&language=en-US&api_key=" + API_KEY,
             payload)


res = conn.getresponse()
data = res.read()

# JSON the results of the data of all movies
informations = data.decode("utf-8")
json_informations = json.loads(informations)

# print(json_informations)
# print(json_informations["results"][1]["poster_path"])
# print(len(json_informations["results"]))
# iterate data of all movies to obtain their'id, title, poser_image_url
movies = []
for i in range(0, len(json_informations["results"])):
    dictionary_movie = {"title": json_informations["results"][i]["title"],
                        "id": json_informations["results"][i]["id"],
                        "poster_image": "https://image.tmdb.org/t/p/w500" +
                        json_informations["results"][i]["poster_path"]}
    movies. append(dictionary_movie)
    # print(movies[i])
    dictionary_movie = {}

# Get youtube url for each movie
for movie in movies:
    # Query the video information for each movie
    url = "https://api.themoviedb.org/3/movie/" + str(movie["id"]) + "/videos?language=en-US&api_key=" + API_KEY

    load = "{}"

    response = requests.request("GET", url, data=load)
    # print(response.text)
    # print(response.text["results"][0]["key"])

    # JSON the results of all video information for each movie
    json_video = json.loads(response.text)
    # print(json_video)
    # print(json_video["results"][0]["key"])

    # Extract the youtube key and put into each movie
    youtube_key = json_video["results"][0]["key"]
    youtube_url = {"trailer_youtube": "https://www.youtube.com/watch?v=" +
                   youtube_key}
    movie. update(youtube_url)
    # print movie["trailer_youtube"]

# Instantiate Each movie
readymovies = []

for movie in movies:
    movie["id"] = media.Movie(movie["title"], movie["poster_image"],
                  movie["trailer_youtube"])
    # print(movie["title"])
    # store them in a list
    readymovies.append(movie["id"])  
# print readymovies

# Input all the values that needed in the page
fresh_tomatoes.open_movies_page(readymovies)
