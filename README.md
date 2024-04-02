
# Twitter Sentiment Analysis Project

## Project Overview

This project leverages the power of Python to extract tweets from Twitter, transform the data for readability and analysis, and then perform sentiment analysis to understand public opinion on various topics. Designed for businesses, researchers, and policymakers, this tool offers valuable insights into public sentiment, aiding in informed decision-making processes.

## Business Problem Addressed

In today's digital world, social media platforms are a goldmine of public sentiment and opinion. For brands, understanding these sentiments can significantly influence reputation, marketing strategies, and product development. However, analyzing sentiment manually on a large scale is nearly impossible. This project addresses this challenge by automating the extraction, transformation, and analysis of Twitter data, providing a scalable solution to gauge public sentiment efficiently.

## Installation

Before running this project, ensure you have Python 3.x installed.  Additionally, the following Python libraries are required:
- Pandas
- NLTK
- TextBlob
- Matplotlib
- WordCloud
- ApifyClient


## Usage

### Setting Up

First, obtain an API token from Apify, which you'll need to access their Twitter scraper services. Insert this token into the `extract_tweets` function in the `extract_transform_load.py` script.

### Execution Workflow

1. Run `extract_transform_load.py` to extract tweets based on specific hashtags, transform the data into a readable format, and load it into CSV files for further analysis.
2. Execute `sentimental_analysis.py` to analyze the sentiment of the processed tweets, categorizing them into positive, negative, or neutral sentiments and generating visual representations of the analysis results.

### Data Handling Scripts Explained

- `extract_transform_load.py`: Extracts tweets, filters based on hashtags and desired fields, and saves the cleaned data into CSV files.
- `sentimental_analysis.py`: Cleans tweet texts, calculates their sentiment polarity, categorizes sentiments, and visualizes the results through various plots and word clouds.

## Code Overview

### Extracting, Transforming, and Loading (ETL)

- **Extraction**: Uses ApifyClient to scrape tweets.
- **Transformation**: Filters tweets to include only relevant information, applies data cleaning, and prepares the dataset for analysis.
- **Loading**: Saves the transformed data into CSV files for easy access and further analysis.

### Sentiment Analysis

- **Preprocessing**: Cleans and prepares tweet text for analysis.
- **Analysis**: Utilizes TextBlob to assess sentiment polarity and categorize tweets accordingly.
- **Visualization**: Generates plots and word clouds to visually represent sentiment analysis findings.







