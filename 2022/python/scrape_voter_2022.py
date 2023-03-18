# Import functions from scraping.py file in same directory
from scraping import *

# URL for all the voters
voters_url = 'https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time/all-voters'
voters_tree = html_parse_tree(voters_url)

voter_url_suffix_xpath = '//*[@id="root"]/main/div/div[3]/dl/dl/div[1]/a/@href'
voter_url_suffix_array = xpath_parse(voters_tree, voter_url_suffix_xpath)
voter_count = len(voter_url_suffix_array)

# Voter URL prefix
voter_url_prefix = 'https://www.bfi.org.uk'

voter_names_xpath = '//*[@id="root"]/main/div/div[3]/dl/dl/div[1]/a/text()'
voter_names_array = xpath_parse(voters_tree, voter_names_xpath)

voter_poll_xpath = '//*[@id="root"]/main/div/div[3]/dl/dl/div[2]/text()'
voter_poll_array = xpath_parse(voters_tree, voter_poll_xpath)

voter_country_xpath = '//*[@id="root"]/main/div/div[3]/dl/dl/div[3]'
voter_country_array = xpath_parse(voters_tree, voter_country_xpath)

voters = []

for i in range(0, voter_count):

	voter_url_suffix = voter_url_suffix_array[i]
	voter_url = voter_url_prefix + voter_url_suffix
	voter_slug = voter_url_suffix.split('/')[4]
	voter_name = voter_names_array[i]
	voter_name_searchable = strip_diacritics(voter_name).lower()
	voter_poll = voter_poll_array[i]
	voter_country = voter_country_array[i].text
	
	voter = [voter_slug, voter_name, voter_name_searchable, voter_poll, voter_country, voter_url]
	add2csv(voter, 'voters_2022.csv')


