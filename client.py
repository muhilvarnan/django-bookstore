import requests
import json 

def get_top_selling_books():
	"""
	get top selling books
	"""
	response = requests.get("http://localhost:8000/top/selling_books")
	for book in json.loads(response.content):
		print book

def get_top_authors():
	"""
	get top authors
	"""
	response = requests.get("http://localhost:8000/top/authors")
	for author in json.loads(response.content):
		print author

if __name__=="__main__":
	print "Book Store API client"
	print "Press 1 to see top Selling Books"
	print "Press 2 tp see top author"
	choice = int(raw_input())
	if choice == 1:
		get_top_selling_books()
	else:
		get_top_authors()