# scraping-wines-from-web

This a scrapy example used as a part of a project for my university. the data extracted is from: 

- [house of wine](https://www.houseofwine.gr/how/) 
- [majestic](https://www.majestic.co.uk)

The project structured is the following 

`├── house_of_wines2.csv
├── majestic_wines2.csv
├── majestic_wines.csv
├── process_data.py
├── README.md
├── scrapy.cfg
├── scrapyWines
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── items.cpython-37.pyc
│   │   └── settings.cpython-37.pyc
│   ├── settings.py
│   ├── spiders
│   │   ├── get_wines_urls_houseofwine.py
│   │   ├── get_wines_urls_majestic.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── get_wines_urls_houseofwine.cpython-37.pyc
│   │   │   ├── get_wines_urls_majestic.cpython-37.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── scrapy_house_of_wine.cpython-37.pyc
│   │   │   └── scrapy_majestic_wine.cpython-37.pyc
│   │   ├── scrapy_house_of_wine.py
│   │   └── scrapy_majestic_wine.py
│   └── temp
│       ├── houseofwineFinale.txt
│       ├── houseofwineUrls.txt
│       ├── majesticUrls.txt
│       └── temp
│           └── product_house_wines.csv
├── temp
│   ├── housewines.csv
│   ├── housewinesFinal2.csv
│   ├── housewinesFinal.csv
│   └── housewines.txt
├── tmp
│   └── product_house_wines.csv
├── Untitled1.ipynb
├── Wines_data_visualization_and_analysis.ipynb
└── wines_final.csv  ` 

### Spiders 

There are the spiders used to extract the data from the two web pages mentioned before 

### Wines_final.csv

Is the cleaned dataset with almost 500 rows related to wines with the following columns: 

- **Alcohol_percent**: the percent of alcohol present in a wine. 
- **Country** : the country of where is the wine from. 
- **Discount_price**: discount price in euros 
- **Grape_variety**: The grape variety of the wine. 
- **Price **: Original price in euros. 
- **Producer**: wine's producer 
- **Wine_color**: wine's color: 
- **Year**: harvest year

### process_data.py 

In this python script the raw data is cleaned. 

###  Wines_data_visualization_and_analysis.ipynb 

Have visualizations and a simple analysis of the dataset in spanish. 



















