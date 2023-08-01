# JokeApiDataAnalysis
JokeApiDataAnalysis


joke_api_project/
    ├── dao/
    │   ├── __init__.py
    │   ├── api.py
    │   └── exceptions.py
    ├── etl/
    │   ├── __init__.py
    │   ├── jokeapi.py
    │   ├── data_processing.py
    │   └── database.py
    ├── data_analysis/
    │   ├── __init__.py
    │   ├── category_distribution.py
    │   └── rating_distribution.py
    ├── config/
    │   └── config.yaml
    ├── tests/
    │   ├── __init__.py
    │   ├── test_api.py
    │   ├── test_jokeapi.py
    │   ├── test_data_processing.py
    │   └── test_database.py
    ├── requirements.txt
    └── main.py


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
21-07-2023

The refactored `api.py` with the specified methods looks good and provides a solid foundation for your project. Here are some additional suggestions to ensure robustness and improve the overall code structure:

1. Error Handling: Implement comprehensive error handling in each method. Consider using specific exceptions to handle different types of errors, such as connection errors, API response errors, or configuration errors. Proper error handling will make your code more resilient and user-friendly.


Error handling can be done in both the base class (`GenericAPI`) and the extended class (`JokeAPI`). The choice depends on the level of abstraction and whether the error handling is generic or specific to the API implementation.

1. Error Handling in Base Class (`GenericAPI`):
In the base class, you can handle errors that are common to all API implementations, such as connection errors, HTTP request failures, or generic API response errors. You can raise custom exceptions to indicate specific error types and provide meaningful error messages.

Here's an example of handling connection errors in `api.py`:

```python
import requests
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class APIError(Exception):
    pass

class GenericAPI(ABC):
    # ...

    def make_api_request(self, url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIError(f"Error connecting to the API: {e}")
        except requests.exceptions.HTTPError as e:
            raise APIError(f"API returned an error: {e}")
        except ValueError as e:
            raise APIError(f"Invalid JSON response: {e}")
```

2. Error Handling in Extended Class (`JokeAPI`):
In the extended class, you can handle errors that are specific to the joke API implementation, such as API response format discrepancies, missing joke categories, or any other API-specific errors.

```python
from api import GenericAPI

class JokeAPI(GenericAPI):
    # ...

    def fetch_jokes(self, category: str = None, count: int = 10) -> List[Dict[str, Any]]:
        try:
            # ...
            jokes_data = self.make_api_request(url, params=params)
            # ...

            return jokes_data
        except APIError as e:
            # Handle the specific APIError here, or re-raise it if necessary
            raise e
```

By handling errors at different levels, you achieve a good separation of concerns. The base class focuses on generic error handling, while the extended class deals with more specific API implementation errors.

Keep in mind that these examples provide a simple illustration of error handling. In a real project, you may want to handle a wider range of errors, log the errors for debugging purposes, and customize the error messages to be more informative and user-friendly.

Overall, proper error handling is crucial for making your application robust, improving user experience, and identifying potential issues during development and deployment.

2. Logging: Incorporate a logging mechanism to log important events, errors, and debugging information. Logging is crucial for troubleshooting and understanding the behavior of your application during development and production.

3. Input Validation: Validate input parameters, such as endpoint names and configuration file paths, to ensure they meet the expected criteria. This prevents unexpected behavior or security vulnerabilities due to malformed inputs.

4. Configuration Validation: Check that the configuration loaded from the YAML file contains all the necessary fields and that they have the correct data types. This will help prevent issues arising from missing or incorrect configuration settings.

5. Exception Propagation: Instead of raising generic exceptions like `Exception` in the `read_config` method, consider raising more specific exceptions with meaningful messages to indicate the exact cause of the error.

6. Configurability: Allow more configuration options in the YAML file, such as custom headers, authentication tokens, or timeouts. This makes your API more flexible and easier to adapt to different use cases.

7. Unit Tests: Write unit tests to ensure the correctness of each method's behavior under different scenarios. Unit tests help you catch bugs early and provide confidence in your code's functionality.

8. Separate Data and Functionality: Consider separating the data (jokes) and the API functionality (fetching and processing jokes) into different classes or modules. This separation of concerns will improve code organization and maintainability.

9. Use Libraries for Database and Data Analysis: When working with databases and data analysis, consider using well-established libraries like SQLAlchemy for database interactions and pandas for data manipulation and analysis. These libraries offer robust functionality and optimizations.

10. Data Storage: Decide whether you want to store fetched jokes in a local JSON file or a database like SQLite or PostgreSQL. Choose a storage solution based on the size of the dataset and the performance requirements of your application.

Remember that achieving a robust pattern and code often involves iterative development and continuous improvement. Regularly review and refactor your code to incorporate best practices and address potential issues as your project progresses. Additionally, documenting your code and design decisions will be beneficial for future maintenance and collaboration with other developers.












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
