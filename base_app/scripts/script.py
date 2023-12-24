import requests
from bs4 import BeautifulSoup
import os
def download_wikipedia_first_paragraph(page_title):
    """
    Downloads the first paragraph of a Wikipedia page and saves it to a text file.
    
    :param page_title: Title of the Wikipedia page.
    """
    print("I am called")
    # Replace spaces with underscores for proper URL formatting
    page_title = page_title.replace(' ', '_')

    # Wikipedia page URL
    url = f"https://en.wikipedia.org/wiki/{page_title}"

    # Send a request to the URL
    response = requests.get(url)
    print(os.getcwd())
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first paragraph in the page content
        first_paragraph = soup.find('p')
        
        if first_paragraph:
            # Write the text of the first paragraph to a file
            with open(f"{page_title}_first_paragraph.txt", "w", encoding='utf-8') as file:
                file.write(first_paragraph.get_text())
            return f"First paragraph of '{page_title}' saved to file."
        else:
            return "First paragraph not found."
    else:
        return "Failed to retrieve the Wikipedia page."

# Example usage
# result = download_wikipedia_first_paragraph("Python_(programming_language)")
# result
