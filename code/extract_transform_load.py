import os
import json
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from apify_client import ApifyClient




def extract_tweets(api_token,actor_id,searchhashtag):
    '''
    api_token(string): personal api token, we get it from apify
    actor_id(string): scraper id which we 
    '''
    client = ApifyClient(api_token)


    run_input = {
        "searchTerms": [searchhashtag],
        "searchMode": "live",
        "addUserInfo": True,
        "scrapeTweetReplies": True,
        "urls": ["https://twitter.com/search?q=gpt&src=typed_query&f=live"],
    }

    run = client.actor(actor_id).call(run_input=run_input)
    dataset_id = run["defaultDatasetId"]
    
    dataset_items = []

    for item in client.dataset(dataset_id).iterate_items():
        dataset_items.append(item)

    result_file_path = 'tweets.json'

    with open(result_file_path, 'w') as file:
        json.dump(dataset_items, file, ensure_ascii=False, indent=4)

    print(f"Dataset items stored in '{result_file_path}'.")
    
    

def filter_dataset_items(input_path, output_path, desired_fields, hashtag_filter):
    """
    input_path (string): Path to the input JSON file containing the original dataset items.
    output_path (string): Path to save the filtered dataset items as a JSON file.
    desired_fields (list): A list of fields to be included in the filtered dataset items.
    hashtag_filter (string): The specific hashtag to filter by (lowercase).
    """

    with open(input_path, 'r') as file:
        data = json.load(file)

    
    filtered_data = []


    for item in data:

        filtered_item = {field: item[field] for field in desired_fields if field in item}


        hashtags = item.get('entities', {}).get('hashtags', [])
        filtered_item['hashtags'] = [{'text': hashtag['text']} for hashtag in hashtags]

        filtered_data.append(filtered_item)

    # Write the filtered data to a new JSON file
    with open(output_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)

    print(f'Filtered data has been saved to {output_path}')
    
def data_cleaning(output_file_path):
    df = pd.read_json(output_file_path)
    # Check if the DataFrame has the required columns
    if 'user_id_str' in df.columns and 'views_count' in df.columns and 'full_text' in df.columns  and 'hashtags' in df.columns:
        # Initialize an empty list to store the extracted data
        extracted_data = []

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            username = row['user_id_str']
            views_count = row['views_count']
            text = row['full_text']
            # Make sure the hashtags are in a list format
            if isinstance(row['hashtags'], list):
                hashtag_texts = [hashtag['text'] for hashtag in row['hashtags'] if 'text' in hashtag]
            else:
                hashtag_texts = []  # No hashtags or not in expected format

            # Append data to the list
            for hashtag_text in hashtag_texts:
                extracted_data.append({
                    'username': username,
                    'views_count': views_count,
                    'text': text,
                    'hashtag': hashtag_text
                })

        # Create a DataFrame from the extracted data
        extracted_df = pd.DataFrame(extracted_data)

        # Display the DataFrame
        extracted_df
    else:
        print("DataFrame does not have the required columns.")
        
        
    average_likes_per_hashtag = extracted_df.groupby('hashtag')['views_count'].mean().reset_index()
    
    top_10 = average_likes_per_hashtag.sort_values(by='views_count',ascending=False)
    top_10 = top_10.head(20)
    
    csv_file_path = 'top_10.csv'
    top_10.to_csv(csv_file_path, index=False)
    
    csv_file_path_extract = 'extracted_df.csv'
    extracted_df.to_csv(csv_file_path_extract, index=False)
    
    return top_10, extracted_df
    



def main():
    
    api_token = 'personalised-api-token'
    actor_id = "heLL6fUofdPgRXZie"
    searchterm = "#TeamIndia"


    input_file_path = 'tweets.json'
    output_file_path = 'required_tweet_content.json'


    desired_fields = [
        "full_text", "lang", "reply_count", "retweet_count", "retweeted",
        "user_id_str", "id_str", "url", "views_count", "created_at"
    ]


    extract_tweets(api_token,actor_id,searchterm)
    filter_dataset_items(input_file_path, output_file_path, desired_fields, 'businessanalysts')
    
    top_10, extracted_data = data_cleaning(output_file_path)
    
    return top_10,extracted_data
    
    
if __name__ == "__main__":
    main()
    print('successfully Extracted data ')




