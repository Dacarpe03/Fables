import requests
from bs4 import BeautifulSoup

# The webpage containing the fables
WEBPAGE_URL = "https://www.aesopfables.com"

# Different sections of the webpage where the fables are located
SECTIONS = [f"{WEBPAGE_URL}/aesop1.html",
			f"{WEBPAGE_URL}/aesop1.html",
			f"{WEBPAGE_URL}/aesop3.html",
			f"{WEBPAGE_URL}/aesop4.html",
			f"{WEBPAGE_URL}/aesop5.html",
			f"{WEBPAGE_URL}/aesop6.html"]


def get_fable_section(section_url):
	"""
	Function that extracts the hrefs from a section of the webpage
	
	Input:
		section_url (string): The url of the section

	Returns:
		fable_hrefs (list): A list with all the hrefs found in the section html
	"""
	
	response = requests.get(section_url)
	soup = BeautifulSoup(response.text, "html.parser")
	fable_hrefs = [fable_link.get('href') for fable_link in soup.find_all('a')]
	return fable_hrefs


def get_fable_links_list():
	"""
	Function that iterates over the sections of the webpage scrapping all their hrefs
	Input:
		None

	Returns:
		fable_links_list (string): A list with all the hrefs found in the sections' htmls
	"""
	fable_links_list = []

	for i, section in enumerate(SECTIONS):
		print(f"Getting fable links from section {i+1} ({section})")
		section_fable_links = get_fable_section(section)
		fable_links_list += section_fable_links

	return fable_links_list


def remove_non_fable_links(fable_links_list):
	"""
	Removes the hrefs that don't link to a fable, in this case the ones that don't start with '/cgi'
	Input:
		fable_links_list (list): The list with all the hrefs to filter

	Returns:
		only_fable_links_list (list): The list with the hrefs that link to a fable in the webpage
	"""
	print("Removing non fable links")
	only_fable_links_list = [fable_link for fable_link in fable_links_list if fable_link.startswith('/cgi')]
	return only_fable_links_list


def complete_fable_links_urls(fable_links_list):
	"""
	Function that add the webpage url in front of the relative path of the fable link

	Input:
		fable_links_list (list): The list with the relative hrefs that link to a fable in the webpage

	Returns:
		complete_fable_links_list (list): The list with the complete fables' urls
	"""
	print("Completing fable urls")
	complete_fable_links_list = [f"{WEBPAGE_URL}{fable_link}" for fable_link in fable_links_list]
	return complete_fable_links_list


def save_fable_links(fable_urls_list,
					 filepath):
	"""
	Function that writes the fable urls in a file

	Input:
		fable_urls_list (string): The list with the fables' urls
		filepath (string): The path of the file where the urls will be written

	Returns:
		None
	"""
	print("Writing urls in a file")
	with open(filepath, "w") as file:
		for fable_url in fable_urls_list:
			file.write(fable_url+"\n")
		print("Success")

if __name__ == "__main__":

	fable_links_list = get_fable_links_list()
	fable_links_list = remove_non_fable_links(fable_links_list)
	fable_urls_list = complete_fable_links_urls(fable_links_list)
	save_fable_links(fable_urls_list, "../Data/fable_urls.txt")

