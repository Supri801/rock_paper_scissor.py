import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch data from a website
def fetch_data(url):
    # Send an HTTP request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully fetched data from {url}")
    else:
        print(f"Failed to retrieve data from {url}")
        return []

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract relevant data (e.g., titles of articles)
    data = []
    for item in soup.find_all('h2'):  # Change this based on what you're extracting
        title = item.get_text(strip=True)
        data.append({'Title': title})

    return data

# Function to save data into a CSV file
def save_to_csv(data, filename):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Save the data to CSV
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main function to run the scraping process
def main():
    # URL of the target website
    url = 'https://example.com'  # Replace with the website you want to scrape

    # Fetch data from the website
    data = fetch_data(url)

    # If data is fetched successfully, save it to CSV
    if data:
        save_to_csv(data, 'scraped_data.csv')

# Run the script
if __name__ == '__main__':
    main()
