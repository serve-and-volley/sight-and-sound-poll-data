# Import functions from scraping.py file in same directory
from scraping import *

# URL for all the voters
voters_url = 'https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time/all-voters'
voters_tree = html_parse_tree(voters_url)

# Set up 'voters' array of voter URL suffixes

voter_url_suffix_xpath = '//*[@id="root"]/main/div/div[3]/dl/dl/div[1]/a/@href'
voter_url_suffix_array = xpath_parse(voters_tree, voter_url_suffix_xpath)
voter_count = len(voter_url_suffix_array)

# Voter URL prefix
voter_url_prefix = 'https://www.bfi.org.uk'

for i in range(0, voter_count):
	voter_url_suffix = voter_url_suffix_array[i]
	voter_url = voter_url_prefix + voter_url_suffix
	voter_url_tree = html_parse_tree(voter_url)

	voter_slug = voter_url_suffix.split('/')[4]

	voter_role_xpath = '//*[@id="root"]/main/div[1]/p/text()[1]'
	try:
		voter_role_parsed = xpath_parse(voter_url_tree, voter_role_xpath)
		voter_role = voter_role_parsed[0].encode('latin-1').decode('utf-8')
	except: voter_role = ''

	film_count_xpath = '//*[@id="root"]/main/div[2]/table/tbody/tr'
	film_count = len(xpath_parse(voter_url_tree, film_count_xpath))

	film_titles_xpath = '//*[@id="root"]/main/div[2]/table/tbody/tr/td[1]'
	film_titles_array = xpath_parse(voter_url_tree, film_titles_xpath)

	film_year_xpath = '//*[@id="root"]/main/div[2]/table/tbody/tr/td[2]'
	film_year_array = xpath_parse(voter_url_tree, film_year_xpath)

	film_directors_xpath = '//*[@id="root"]/main/div[2]/table/tbody/tr/td[3]'
	film_directors_array = xpath_parse(voter_url_tree, film_directors_xpath)
	
	for j in range(0, film_count):

		film_title_parsed = film_titles_array[j].text
		film_title = string_clean(film_title_parsed)
		film_title_searchable = strip_diacritics(film_title).lower()
		film_year = film_year_array[j].text
		film_director_parsed = film_directors_array[j].text
		if film_director_parsed is None:
			film_director = ''
			film_director_searchable = ''
		else:
			film_director = string_clean(film_director_parsed)
			film_director_searchable = strip_diacritics(film_director).lower()

		vote_row = [voter_slug, voter_role, film_count, film_title, film_title_searchable, film_year, film_director, film_director_searchable]
		add2csv(vote_row, 'votes_2022.csv')

	print([i, voter_slug, voter_role, film_count])
