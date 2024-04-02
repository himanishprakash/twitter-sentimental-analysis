## Detailed Code Overview

### Extracting, Transforming, and Loading Data (`extract_transform_load.py`)

#### Extraction Process

- Utilizes the `ApifyClient` with a provided API token to connect to Apify's Twitter Scraper actor. This allows for the extraction of tweets in real time based on specified hashtags or search terms.
- The extracted tweets are initially saved as a JSON file, which includes comprehensive data returned by the scraper, such as tweet content, user info, and engagement metrics.

#### Transformation Steps

- Filters the raw extracted tweet data to retain only the desired fields, such as the full text, language, and various counts (replies, retweets), through a specified list of fields.
- Additionally, filters tweets based on a specific hashtag to ensure relevance to the topic of interest. This step involves parsing the hashtag entities within each tweet and selecting those that match the target hashtag.
- The script also performs cleaning operations on the data, such as extracting relevant hashtags from tweets and preparing the data for sentiment analysis. This includes normalizing text data and structuring it into a format suitable for analysis.

#### Loading Mechanism

- Transforms the filtered and cleaned tweet data into a Pandas DataFrame, which is then used to calculate and analyze metrics such as average views per hashtag.
- Saves the transformed data into CSV files: one containing the cleaned tweet data and another listing the top hashtags based on engagement metrics. This facilitates easy access and analysis in subsequent steps.

### Sentiment Analysis (`sentimental_analysis.py`)

#### Preprocessing Functionality

- Cleans the tweet text by lowering case, removing URLs, mentions, non-alphanumeric characters, and stop words to focus on the meaningful text that contributes to sentiment.
- Utilizes NLTK for tokenization, stopwords removal, and stemming, preparing the text for accurate sentiment analysis.

#### Analysis Core

- Employs the `TextBlob` library to compute the polarity of tweets, a numerical score indicating the sentiment from negative to positive. Each tweet is then classified as 'Positive', 'Neutral', or 'Negative' based on its polarity score.
- This script not only analyzes overall tweet sentiment but also delves into the sentiment of individual words within tweets, providing a granular view of the sentiment expressed.

#### Visualization Techniques

- Generates bar charts to visualize metrics such as average views per hashtag, offering insights into engagement patterns.
- Produces pie charts to depict the distribution of sentiments across the dataset, providing a visual summary of public opinion.
- Creates word clouds to highlight frequently occurring words in the tweets, with color coding to indicate sentiment (positive or negative), offering an immediate visual representation of the prevalent sentiments and topics.
