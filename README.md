# Amazon Product Reviews Scraper

This Python script scrapes Amazon product reviews for a specific product and writes the data to a CSV file.

## Requirements

- Python 3.x
- BeautifulSoup4
- urllib

## Installation

1. Clone the repository or download the script file.

2. Install the required Python libraries using pip:

    ```sh
    pip install beautifulsoup4
    ```

## Usage

1. Save the script as `scraper.py`.

2. Run the script:

    ```sh
    python scraper.py
    ```

3. The script will create a `file.csv` in the same directory, containing the scraped reviews.

## Script Overview

### `get_review_data(page_num)`

Fetches the HTML content of the review page for a given page number and returns a list of review posts.

### `parse_review(post)`

Parses a single review post and extracts relevant information such as user name, stars, date, title, content, comments, and the number of people who found the review helpful.

### `write_reviews_to_csv(filename, reviews)`

Writes the extracted review data to a CSV file.

## CSV Output

The CSV file will have the following columns:

- `user_name`: The name of the user who wrote the review.
- `stars`: The star rating given by the user.
- `date`: The date the review was written.
- `title`: The title of the review.
- `content`: The content of the review.
- `comments`: The number of comments on the review.
- `span`: The number of people who found the review helpful.

## Example

Here is an example of the output:

```csv
user_name,stars,date,title,content,comments,span
John Doe,5,January 1, 2021,Great product!,This product is amazing!,10,5
Jane Smith,4,February 15, 2021,Good but...,I liked it but it has some issues.,8,3
