import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# def get_fomc_statements(url):
#     # Send a GET request to the website
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code != 200:
#         print("Couldn't retrieve webpage.")
#         return []

#     # Parse HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find press release links
#     press_release_divs = soup.find_all("div", class_="col-xs-12")
#     print(soup)
#     return[]

def get_text_from_one_site(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the main content area containing the press release text
    content_div = soup.find("div", class_="col-xs-12 col-sm-8 col-md-8")
    
    if not content_div:
        print("Failed to find the main content area.")
        return None
    
    # Extract text from the relevant paragraphs
    paragraphs = content_div.find_all("p")
    press_release_text = "\n\n".join(paragraph.get_text(strip=True) for paragraph in paragraphs)
    
    return relevant_text(press_release_text)

def relevant_text(text):
    voting_index = text.find("Voting for")
    
    if voting_index != -1:
        return text[:voting_index].strip()
    
    return text