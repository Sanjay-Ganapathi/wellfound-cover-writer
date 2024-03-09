import requests


# Step 2: Fetch the HTML content
# Replace with the URL of the webpage you want to scrape
url = 'https://wellfound.com/l/2zY1j5'
response = requests.get(url)
print(response.text)
