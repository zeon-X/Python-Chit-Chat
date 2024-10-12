import requests
from bs4 import BeautifulSoup


def scrape_gifts_association_data(start_mid=1, end_mid=133):
    base_url = "http://www.giftsassociation.org.sg/sga/accounts&func=prop&mid={}"
    company_data = []

    for mid in range(start_mid, end_mid + 1):
        print(f"Scraping mid {mid}...")
        url = base_url.format(mid)
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract company name
            company_name = soup.find('h1').text.strip()

            # Initialize a dictionary to hold the company's data
            company_info = {
                "Company Name": company_name,
                "Address": "N/A",
                "Contact Person": "N/A",
                "Designation": "N/A",
                "Phone": "N/A",
                "Email": "N/A",
                "Website": "N/A"
            }

            # Extract other details from the table
            profile_table = soup.find("div", class_="profile").find("table")
            rows = profile_table.find_all("tr")

            for row in rows:
                # Get the key (first cell)
                key_cell = row.find('td', valign="top", width="100")
                if key_cell:
                    key = key_cell.text.strip()

                    # Get the value (second cell)
                    value_cell = row.find_all('td')[1]  # Get the second <td>
                    if value_cell:
                        value = value_cell.text.strip()

                        # Update company_info based on the key
                        if key in company_info:
                            company_info[key] = value

            # Extract the email link if it exists
            email_link = soup.find(
                'a', href=lambda x: x and x.startswith('mailto:'))
            if email_link:
                company_info["Email"] = email_link.get(
                    'href').replace('mailto:', '').strip()

            # Extract the website link if it exists
            website_link = soup.find(
                'a', href=lambda x: x and x.startswith('http'))
            if website_link:
                company_info["Website"] = website_link.get('href').strip()

            # Adding the collected data to the list
            company_data.append(company_info)

        else:
            print(f"Failed to retrieve mid {
                  mid}: Status code {response.status_code}")

    return company_data


start_mid = 1
end_mid = 10
# Fetching data for the specified range of mids
data = scrape_gifts_association_data(start_mid, end_mid)

# Printing the scraped data
for idx, company in enumerate(data, start=1):
    print(f"Company {idx}:")
    for key, value in company.items():
        print(f"{key}: {value}")
    print("\n")
