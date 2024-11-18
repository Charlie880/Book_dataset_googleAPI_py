# import requests
# import pandas as pd

# API_KEY = "Your google API"
# OUTPUT_CSV = "books_dataset.csv"

# # Function to fetch data from Google Books API
# def fetch_books(query, max_results=10):
#     url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&key={API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error: {response.status_code}")
#         return None

# # Parse the book data
# def parse_books(data):
#     books = []
#     for item in data.get("items", []):
#         volume_info = item.get("volumeInfo", {})
#         books.append({
#             "Book ID": item.get("id", ""),
#             "Title": volume_info.get("title", ""),
#             "Authors": ", ".join(volume_info.get("authors", [])),
#             "Published Date": volume_info.get("publishedDate", ""),
#             "Publisher": volume_info.get("publisher", ""),
#             "ISBN": next((identifier.get("identifier", "") for identifier in volume_info.get("industryIdentifiers", [])), ""),
#             "Category": ", ".join(volume_info.get("categories", [])),
#             "Book Cover Image": volume_info.get("imageLinks", {}).get("thumbnail", ""),
#         })
#     return books

# # Main function to create dataset
# def create_dataset(queries):
#     all_books = []
#     for query in queries:
#         data = fetch_books(query)
#         if data:
#             books = parse_books(data)
#             all_books.extend(books)
#     return all_books

# # Example queries (keywords to search books)
# queries = ["Data Science", "Python Programming", "Machine Learning", "Artificial Intelligence"]

# # Fetch and save the dataset
# books_data = create_dataset(queries)
# df = pd.DataFrame(books_data)
# df.to_csv(OUTPUT_CSV, index=False)
# print(f"Dataset saved to {OUTPUT_CSV}")

# import pandas as pd
# import mysql.connector

# # XAMPP MySQL connection details
# db_config = {
#     "host": "localhost",
#     "user": "root",
#     "password": "",
#     "database": "MIS"
# }

# # Path to your CSV file
# csv_file = "books_dataset.csv"

# # Read the dataset
# df = pd.read_csv(csv_file)

# # Function to insert data into MySQL
# def insert_books_to_mysql(dataframe):
#     try:
#         # Connect to the database
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()

#         # Insert each record
#         for _, row in dataframe.iterrows():
#             sql = """
#             INSERT INTO books (id, title, authors, published_date, publisher, isbn, category, book_cover_image)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#             """
#             values = (
#                 row["Book ID"],
#                 row["Title"],
#                 row["Authors"],
#                 row["Published Date"] if pd.notnull(row["Published Date"]) else None,
#                 row["Publisher"],
#                 row["ISBN"],
#                 row["Category"],
#                 row["Book Cover Image"]
#             )
#             cursor.execute(sql, values)

#         # Commit changes
#         connection.commit()
#         print(f"{cursor.rowcount} records inserted successfully.")

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# # Call the function to insert data
# insert_books_to_mysql(df)
