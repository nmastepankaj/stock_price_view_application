
# Stock Price View Application

In this I have completed the basic implementation of getting stock price.

## Installation

First clone the github repository

```bash
  git clone https://github.com/nmastepankaj/stock_price_view_application.git
```

Open the repository folder in any code editor (VS code) or open any terminal.
Move to the backend folder and install all the requirements.

```bash
  cd stock_data
```

You need to create virtual environment for the project. If you don't have virtualenv the install it using the below command :-

```bash
  virtualenv venv
```

Now, activate the virtual environment using the below command.
If you're window user :-

```bash
  ./venv/Scripts/activate
```


If you're linux user :-

```bash
  source venv/bin/activate
```


install all the project requirements

```bash
  pip install -r requirement.txt
```

If you are using the same databse present in the repository then no need to do the below steps
Now, you need to create migrations and migrate all the migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

User: pankaj 
Passowrd: pankaj
Create super user for your project

```bash
  python manage.py createsuperuser
```

Run your project

```bash
  python manage.py runserver
```

Now your application is ready to use. First register a user and login with the provided credentials.

In this prject to get the bhavcopy of the stock data we need to run the function `refresh_data` present in the `main/shares.py` this function can be called from the APi but need to run in the backgroud because it takes a lot of time. So, if we want to have this functioality need to setup celery for running the background task.


## APIs of our project

- A GET route for the top 10 stocks.
  curl for this route
```curl
    curl --location 'http://127.0.0.1:8000/api/get_top10_stocks' \
    --header 'Cookie: csrftoken=zauPe4jvWB4K7phC7871fNUDlXRdCP06mwBd3jhmkFdSJAhCGGcfaP5WaIBWkqM4'
```

- A GET route to find stocks by name.
  curl for this api
```
  curl --location 'http://127.0.0.1:8000/api/get_stock_by_name/IRFC' \
  --header 'Cookie: csrftoken=zauPe4jvWB4K7phC7871fNUDlXRdCP06mwBd3jhmkFdSJAhCGGcfaP5WaIBWkqM4'
```

- A GET router to get stock price history list for UI graph.
Curl of this API
```
curl --location 'http://127.0.0.1:8000/api/get_stock_price_history_list/3456' \
--header 'Cookie: csrftoken=zauPe4jvWB4K7phC7871fNUDlXRdCP06mwBd3jhmkFdSJAhCGGcfaP5WaIBWkqM4'
```

- A POST route to add a stock to favourites and A DELETE route to remove a stock from favourites.
We need user which should be authenticated so I used TokenAuthentication for it can be easily accessiable
I have implemented both these functionality using the same API. If a stock is already is in favourite list then remove it from favourite list

Curl for this API
```
curl --location --request POST 'http://127.0.0.1:8000/api/add_stocks_to_favourite/56' \
--header 'Authorization: Token 53d7562952f6ec9f9913a8ae644fd4fe3b77dfc0' \
--header 'Cookie: csrftoken=zauPe4jvWB4K7phC7871fNUDlXRdCP06mwBd3jhmkFdSJAhCGGcfaP5WaIBWkqM4'
```

- A GET route to see favourite stocks.
Curl for this API
```
curl --location 'http://127.0.0.1:8000/api/get_favourite_stocks' \
--header 'Authorization: Token 53d7562952f6ec9f9913a8ae644fd4fe3b77dfc0' \
--header 'Cookie: csrftoken=zauPe4jvWB4K7phC7871fNUDlXRdCP06mwBd3jhmkFdSJAhCGGcfaP5WaIBWkqM4'
```


## Authors
- [@nmastepankaj](https://www.github.com/nmastepankaj)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://nmastepankaj.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nmastepankaj/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/nmastepankaj)


## 🚀 About Me
I'm Pankaj student of IIIT Una. Working on backend in Django and frontend in React.


## Feedback
If you have any feedback, please reach out to us at my profile link provided above.

