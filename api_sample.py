import requests
import pandas as pd

# 🔑 Replace with your own API key
api_key = "AIzaSyD0tgyb28aXM6x5RpGmGvj1rG41kygzvYc"

# Example: Search for books about Data Science
query = "Data Science"

url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"

response = requests.get(url)
data = response.json()

# Let's see what we got
print(data.keys())
books = []

for item in data["items"]:
    volume = item["volumeInfo"]
    books.append({
        "Title": volume.get("title"),
        "Authors": ", ".join(volume.get("authors", [])),
        "Publisher": volume.get("publisher"),
        "PublishedDate": volume.get("publishedDate"),
        "Category": ", ".join(volume.get("categories", [])) if "categories" in volume else None,
        "AverageRating": volume.get("averageRating"),
        "PageCount": volume.get("pageCount")
    })

df = pd.DataFrame(books)
print(df.head())
df.to_csv("google_books_data.csv", index=False)
print("Data saved successfully ✅")