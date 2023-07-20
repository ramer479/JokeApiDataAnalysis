# JokeApiDataAnalysis
JokeApiDataAnalysis

Requirement
Step 1: Fetching Jokes from Joke API

Choose a publicly available Joke API that provides jokes with different categories and ratings.
Use Python to make API requests and fetch a substantial amount of jokes (e.g., 500-1000 jokes) along with their categories and ratings.
Step 2: Data Analysis

Clean and preprocess the fetched joke data.
Perform exploratory data analysis to gain insights into the joke categories, ratings, and other relevant statistics.
Step 3: Setting up PostgreSQL Database

Install PostgreSQL and the required Python libraries to interact with the database (e.g., psycopg2).
Create a database and a table to store the joke data. The table schema could include fields like joke_id, category, content, rating, etc.
Step 4: Incremental Data Loading to PostgreSQL

Implement a mechanism to incrementally load the cleaned joke data into the PostgreSQL database. This means you should be able to add new jokes to the database without losing any existing data.
Step 5: Chart Creation

Utilize popular Python data visualization libraries like Matplotlib, Seaborn, or Plotly to create insightful charts based on the data. Some potential chart ideas are:
Bar chart showing the distribution of jokes in different categories.
Box plot showing the distribution of joke ratings.
Time-series chart showing the incremental growth of jokes in the database.
Pie chart displaying the proportion of jokes in each category.
Step 6: Web Interface (Optional)

Create a simple web interface using Flask or Django, allowing users to view the charts and search for jokes by category or rating range.
Step 7: Documentation

Write clear and concise documentation explaining the project's purpose, how to run the code, and any external dependencies.
Remember to adhere to best practices, such as handling errors gracefully, ensuring data security, and implementing proper error logging. Have fun with the project, and it will provide you with valuable experience in working with APIs, databases, data analysis, and data visualization using Python!

















=============================================================================
# AS class 

import requests
import yaml

class JokeAPIRequest:
    def __init__(self, config_file):
        self.config_file = config_file
        self.api_config = self.read_config()

    def read_config(self):
        with open(self.config_file, "r") as file:
            return yaml.safe_load(file)

    def construct_api_url(self):
        base_url = "https://v2.jokeapi.dev/joke/"
        categories = ",".join(self.api_config["categories"])
        lang = self.api_config["lang"]
        contains = self.api_config["contains"]
        amount = self.api_config["amount"]

        api_url = f"{base_url}{categories}?lang={lang}&contains={contains}&amount={amount}"
        return api_url

    def make_api_request(self):
        api_url = self.construct_api_url()
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch jokes. Error code: {response.status_code}")
            return None

if __name__ == "__main__":
    api_request = JokeAPIRequest("api_config.yaml")
    jokes = api_request.make_api_request()

    if jokes:
        for index, joke in enumerate(jokes["jokes"], 1):
            print(f"{index}. {joke['setup']} {joke['delivery']}")
    else:
        print("No jokes found. Please check your configuration or try again later.")



# As Functions as Module :
# api_request.py

import requests
import yaml

def read_config(config_file):
    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def construct_api_url(api_config):
    base_url = "https://v2.jokeapi.dev/joke/"
    categories = ",".join(api_config["categories"])
    lang = api_config["lang"]
    contains = api_config["contains"]
    amount = api_config["amount"]

    api_url = f"{base_url}{categories}?lang={lang}&contains={contains}&amount={amount}"
    return api_url

def make_api_request(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch jokes. Error code: {response.status_code}")
        return None

if __name__ == "__main__":
    config_file = "api_config.yaml"
    api_config = read_config(config_file)
    api_url = construct_api_url(api_config)
    jokes = make_api_request(api_url)

    if jokes:
        for index, joke in enumerate(jokes["jokes"], 1):
            print(f"{index}. {joke['setup']} {joke['delivery']}")
    else:
        print("No jokes found. Please check your configuration or try again later.")


# api_request.py

import requests
import yaml

def read_config(config_file):
    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def construct_api_url(api_config):
    # ... (same as before)

def make_api_request(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch jokes. Error code: {response.status_code}")
        return None

def api_request_handler(config_file):
    api_config = read_config(config_file)
    api_url = construct_api_url(api_config)
    return make_api_request(api_url)

if __name__ == "__main__":
    config_file = "api_config.yaml"
    jokes = api_request_handler(config_file)

    if jokes:
        for index, joke in enumerate(jokes["jokes"], 1):
            print(f"{index}. {joke['setup']} {joke['delivery']}")
    else:
        print("No jokes found. Please check your configuration or try again later.")
