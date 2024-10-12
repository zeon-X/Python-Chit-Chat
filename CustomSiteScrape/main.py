import requests
from bs4 import BeautifulSoup


def scrape_hard_search_data(start_page=1, end_page=3):
    base_url = "https://www.hrdsearch.com/search.php?keywords=&&page={}"
    company_data = []

    for page in range(start_page, end_page + 1):
        print(f"Scraping page {page}...")
        url = base_url.format(page)
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all company data entries
            companies = soup.find_all("div", class_="company-datail")

            for company in companies:
                # Extract company name
                name = company.find('h4').find('a').text.strip()

                # Extract phone number
                phone_tag = company.find(text=lambda x: x and "Phone:" in x)
                phone = phone_tag.split(":")[1].strip() if phone_tag else 'N/A'

                # Extract fax number
                fax_tag = company.find(text=lambda x: x and "Fax:" in x)
                # Assuming fax is the same as phone if not found
                fax = fax_tag.split(":")[1].strip() if fax_tag else "N/A"

                # Extract email
                email_tag = company.find(
                    'a', href=lambda x: x and x.startswith('mailto:'))
                email = email_tag.get('href').replace(
                    'mailto:', '').strip() if email_tag else 'N/A'

                # Extract website URL
                website_tag = company.find(
                    'a', href=lambda x: x and x.startswith('http'))
                website = website_tag.get('href') if website_tag else 'N/A'

                # Extract address
                # First <p> tag contains the address
                address_tag = company.find_all("p")[0]
                address = address_tag.text.strip() if address_tag else 'N/A'

                # Adding the collected data to the list
                company_data.append({
                    "Company Name": name,
                    "Phone Number": phone,
                    "Fax Number": fax,
                    "Email": email,
                    "Company URL": website,
                    "Address": address
                })
        else:
            print(f"Failed to retrieve page {
                  page}: Status code {response.status_code}")

    return company_data


# Specify the range of pages to scrape
start_page = 1  # Change this to your desired start page
end_page = 5    # Change this to your desired end page

# Fetching data for the specified range of pages
data = scrape_hard_search_data(start_page, end_page)

# Printing the scraped data
for idx, company in enumerate(data, start=1):
    print(f"Company {idx}:")
    for key, value in company.items():
        print(f"{key}: {value}")
    print("\n")
