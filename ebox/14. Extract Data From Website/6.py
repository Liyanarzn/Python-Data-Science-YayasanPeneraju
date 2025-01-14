
import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.content
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Website not found")
        return None

def extract_tag_content(html_content, tag_name):
    if html_content is None:
        return "Website not found"

    soup = BeautifulSoup(html_content, 'html.parser')
    tag = soup.find(tag_name)

    if tag:
        return tag.text.strip()
    else:
        return f"No {tag_name} tag is present in website"

def main():
    try:
        # Input website URL
        url = input("Enter website URL:\n").strip()

        # Check if URL starts with http:// or https://, if not add it
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url

        # Fetch website content
        html_content = fetch_website_content(url)

        if html_content is None:
            return  # Exit the function if website content is not fetched successfully

        # Input tag name
        tag_name = input("Enter tag:\n").strip()

        # Extract and display tag content
        result = extract_tag_content(html_content, tag_name)
        print(result)

    except EOFError:
        print("Unexpected end of input. Please provide valid inputs.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
