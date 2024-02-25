import requests
from bs4 import BeautifulSoup


WEBPAGE_URL = "https://www.aesopfables.com"
SECTIONS = ["{WEBPAGE_URL}/aesop1.html",
			"{WEBPAGE_URL}/aesop1.html",
			"{WEBPAGE_URL}/aesop3.html",
			"{WEBPAGE_URL}/aesop4.html",
			"{WEBPAGE_URL}/aesop5.html",
			"{WEBPAGE_URL}/aesop6.html"]


def get_fable_section(section_url):

	response = requests.get(section_url)
	soup = BeautifulSoup(response.text, "html.parser")
	fable_hrefs = [fable_link.get('href') for fable_link in soup.find_all('a')]
	return fable_hrefs


def get_fable_links_list():

	fable_links_list = []

	for i, section in enumerate(SECTIONS):
		print("Getting fable links from section {i} ({section})")
		section_fable_links = get_fable_section(section)
		fable_links_list += section_fable_links

	return fable_links_list


def remove_non_fable_links(fable_links_list):

	only_fable_links_list = [fable_link for fable_link in fable_links_list if fable_link.startswith('/cgi')]
	return only_fable_links_list


if __name__ == "__main__":

	fable_links_list = get_fable_links()
	fable_links_list = remove_non_fable_links(fable_links_list)

