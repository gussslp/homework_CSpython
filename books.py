import requests, json

book_name = input("введіть уривок книги: ")

book = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name+"+inauthor:keyes&key=AIzaSyCE1fuJ62Yr3qi_6xKcNt7cmgUh_WxXHA8")
book_info = book.json()
for i in range(1,6):
    print(i,": Title:",book_info['items'][i]['volumeInfo']['title'],'\n Author: ',book_info['items'][i]['volumeInfo']['authors'],'\n Published date: ',book_info['items'][i]['volumeInfo']['publishedDate'],'\n\n')
