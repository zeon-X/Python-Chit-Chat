from googlesearch import search
import requests
from bs4 import BeautifulSoup


def scrape_google(query):
    search_results = []

    # Perform Google search and collect URLs
    for url in search(query, num_results=10):
        search_results.append(url)

    return search_results


def scrape_company_details(url):
    try:
        # Request the page content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract company name, or anything available
        title = soup.find('title').text.strip() if soup.find(
            'title') else 'No title found'
        return {'url': url, 'title': title}

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


# Example queries
queries = [
    '"Sales Director" "30 to 200 employees" site:linkedin.com',
    '"Sales Manager" "30 to 200 employees" site:linkedin.com',
]


for query in queries:
    print(f"Searching for: {query}")
    search_results = scrape_google(query)

    for url in search_results:
        company_details = scrape_company_details(url)
        if company_details:
            print(company_details)
