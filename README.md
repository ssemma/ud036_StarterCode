#  Movie Trailer Website
It contains all my favoriate movies. You can click on each picture of the HTML page, it will pop out the movie trailer
from youtube.

## Install
1. This program is only compatible for **python 2.7.9**
2. You can visit the website [here](https://www.python.org/downloads/release/python-279/) to download 
3. Please register an account from [TMDb](https://www.themoviedb.org/)
4. In your **TMDb account**, go to setting, then go to API, then create an API KEY
5. Please create a new python file--**config.py** in the same directory and folder with media.py, fresh_tomatoes.py,entertainment_center.py 
6. Please named the python file you create as **config.py**. 
7.  **content of config.py** 
```
    def init():
		API_KEY = "1234556"  # Please input your own TMDb API_KEY
		return API_KEY
```
## Instruction for running the program
1. Make sure media.py, fresh_tomatoes.py,entertainment_center.py and config.py are in the same folder 
2. Open entertainment_center.py and run the program 
3. It will display the movie trailer website


## Attribution
1. This product uses the TMDb API but is not endorsed or certified by TMDb 
2. The source code of the fresh_tomatoes.py is from [udacity](https://github.com/udacity/ud036_StarterCode)


