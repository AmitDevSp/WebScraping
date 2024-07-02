from bs4 import BeautifulSoup
import urllib.request
import csv


def get_review_data(page_num):
    url = f'https://www.amazon.com/product-reviews/B07GNPDMRP/ref=cm_cr_getr_d_paging_btm_next_{page_num}/144-9847830-9079603?ie=UTF8&pd_rd_i=B07GNPDMRP&pd_rd_r=3deed5cf-45cf-11e9-87a3-d1c5d12b63d5&pd_rd_w=BDDXx&pd_rd_wg=bIHmf&pf_rd_p=90485860-83e9-4fd9-b838-b28a9b7fda30&pf_rd_r=NE7QZZPR7NK9VH6NQ1ZN&refRID=NE7QZZPR7NK9VH6NQ1ZN&pageNumber={page_num}'
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup.findAll('div', attrs={'data-hook': 'review'})
    except Exception as e:
        print(f"Error fetching data for page {page_num}: {e}")
        return []


def parse_review(post):
    review = {}
    review['user_name'] = post.find('span', attrs={'class': 'a-profile-name'}).text.strip().replace(',', '')
    review['stars'] = post.find('span', attrs={'class': "a-icon-alt"}).text.strip()[0].replace(',', '')
    review['date'] = post.find('span', attrs={'class': "a-size-base a-color-secondary review-date"}).text.strip().replace(',', '/')
    review['title'] = post.find('a', attrs={'class': "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"}).text.strip().replace(',', '')
    review['content'] = post.find('span', attrs={'class': "a-size-base review-text review-text-content"}).text.strip().replace(',', '')
    review['comments'] = post.find('span', attrs={'class': "review-comment-total aok-hidden"}).text.strip().replace(',', '')
    helpful_text = post.find('span', attrs={'class': "a-size-base a-color-tertiary cr-vote-text"})
    review['span'] = helpful_text.text.strip().split()[0] if helpful_text else '0'
    return review


def write_reviews_to_csv(filename, reviews):
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['user_name', 'stars', 'date', 'title', 'content', 'comments', 'span']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for review in reviews:
            writer.writerow(review)


all_reviews = []
for index in range(1, 5):
    posts = get_review_data(page_num)
    for post in posts:
        all_reviews.append(parse_review(post))

write_reviews_to_csv('file.csv', all_reviews)
