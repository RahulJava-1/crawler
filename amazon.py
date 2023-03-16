from bs4 import BeautifulSoup
import requests

#Function to extract Title
def title(soup):
     
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
 
        title_value = title.string
 
        title_string = title_value.strip()
 
    except AttributeError:
        title_string = ""   
 
    return title_string
 
#Function to extract Product Price
def price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
 
        try:
            
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
 
        except:     
            price = ""  
 
    return price
 
# Function to extract Product Rating
def rating(soup):
 
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
         
    except AttributeError:
         
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 
 
    return rating
 
# Function to extract Reviews
def review(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
         
    except AttributeError:
        review_count = ""   
 
    return review_count
 
# Function to extract Product Availability
def product_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'}).string.strip()
        
 
    except AttributeError:
        available = "Not Available"
 
    return available

# Function to extract Products brand
def brand(soup):
    try:
        brand=soup.find("a",class_='a-link-normal').string.strip()
    except AttributeError:
        brand="Not Available"
    return brand

'''def url(soup):
    try:
        url=soup.find("link",attrs={'rel':'canonical'})['href']
    except AttributeError:
        url="Not Found"
    return url'''
'''def get_image(soup):
        try:
            image = soup.find("img", attrs={'id':"landingImage"})['data-old-hires']
        except AttributeError:
            image =" "
        return image'''
 
 
if __name__ == '__main__':
 
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                'Accept-Language': 'en-US'})
 
    # The webpage URL
    a=input("Enter product name: ")
    URL = "https://www.amazon.in/s?k="+a+"&ref=nb_sb_noss_2"
     
    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
 
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
 
    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
 
    # Store the links
    links_list = []
 
    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))
 
 
    # Loop for extracting product details 
    for link in links_list:
 
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
 
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

product_detail = [title(soup),price(soup),rating(soup),review(soup),product_availability(soup)]
with open('amazon.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(product_detail)
print("Data Saved...")
