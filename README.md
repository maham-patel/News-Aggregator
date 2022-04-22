# News-Aggregator
This repository serves an assignment for the Backend Developer position at Stellic

<!-- ABOUT THE PROJECT -->
## About The Project

The application is built in accordance with the newaggregator guidelines given by Stellic. All features except favourite and testing using pytests are implemented. All the contraints are implemented, along with project documentation and unit-tests.

<br>


#### What's Not Implemented
favourite and testing using pytests are not implemented.


<br>

### Built With

* [Python](http://python.org/)
* [Django](https://docs.djangoproject.com/en/4.0/)
* [RestApi](https://www.django-rest-framework.org/)



<!-- GETTING STARTED -->
## Getting Started

#### General Technique to Aggregate

1. Get list of registered APIs
2. Loop over APIs
3. Make JSON object of configurations for each API
4. Write JSON parsers for each API
5. Combine result in uniform format to display
6. Return results



#### Detailed Approach

Every Request to API should be async; put the request in job tracker, get results and push back responses

##### News Listing Endpoint:
api.route('/news')

def get_top_news():
  1. Get all available APIs
  2. Call each API for getting top 10 news in JSON; Listing Function for Each API
  3. Aggregate news from all APIs, discard empty responses
       

##### News Search Endpoint
api.route('/news?query=bitcoin')

def get_search_results():
  1. Get all available APIs
  2. Call each API with search query to get top 10 results in JSON; Searching Function for Each API
  3. Aggregate results from all APIs, discard empty responses


##### Other Helper Functions
  1. News_API json parser for listing responses; 
    should return only required fields; ["title",  "link", "source"]
  2. Reddit_API json parser for listing results


### Prerequisites

To run this project, should install project dependencies:

1. Python3
2. pip
3. Django
4. Django Rest Framework
5. Intsall Python packages


<br>

### Instructions to Run


1. Clone the repo
```sh
git clone https://github.com/maham-patel/News-Aggregator.git
```
2. Open terminal in project folder
```sh 
cd News-Aggregator
```

3. Runserver
```sh
python manage.py runserver
```

4. Check results at endpoint

