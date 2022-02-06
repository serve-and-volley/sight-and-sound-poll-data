# Import functions from scraping.py file in same directory
from scraping import *

# Add CSV headers for Voters CSV
voters_header = ['voter_id', 'voter_name', 'voter_name_searchable', 'poll_category', 'voter_role', 'voter_title', 'voter_nationality', 'voter_gener', 'film_count', 'voter_comments']
add2csv(voters_header, 'voters_2012.csv')

# Add CSV headers for Votes CSV
votes_header = ['voter_id','raw_film_title',  'normed_film_title', 'searchable_film_title', 'film_director', 'film_director_searchable', 'film_year', 'film_id']
add2csv(votes_header, 'votes_2012.csv')

# Main URL for 2012 poll data
# https://www2.bfi.org.uk/films-tv-people/sightandsoundpoll2012

# Voter data URL prefix
# http://www.bfi.org.uk/films-tv-people/sightandsoundpoll2012/voter/[voter_id]

# Film data URL prefix
# https://www2.bfi.org.uk/films-tv-people/[film_id]

# Voter URL prefix to scrape the votes data
votes_url_prefix = "http://www.bfi.org.uk/films-tv-people/sightandsoundpoll2012/voter/"

# Initialize tree to scrape voter data
voter_url = "http://www.bfi.org.uk/films-tv-people/sightandsoundpoll2012/voters"
voter_tree = html_parse_tree(voter_url)
table_count_xpath = "//div[@class='sas-poll-az-list-group']"
table_count_parsed = xpath_parse(voter_tree, table_count_xpath)
table_count = len(table_count_parsed)

# Initialize Missing Film IDs associative array
missing_films = {}
missing_film_counter = 10000

# Iterate through all the voters in: https://www2.bfi.org.uk/films-tv-people/sightandsoundpoll2012/voters
for table in range(1, table_count + 1):
    row_count_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr"
    row_count_parsed = xpath_parse(voter_tree, row_count_xpath)
    row_count =  len(row_count_parsed)

    for row in range(1, row_count + 1):
        # Voter name (raw and searchable)
        voter_name_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[1]/p/a/text()"
        voter_name_parsed = xpath_parse(voter_tree, voter_name_xpath)
        voter_name = voter_name_parsed[0].encode('utf-8').decode('utf-8')
        voter_name_searchable = strip_diacritics(voter_name).lower()

        # Voter ID
        voter_url_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[1]/p/a/@href"
        voter_url_parsed = xpath_parse(voter_tree, voter_url_xpath)
        voter_url = voter_url_parsed[0]
        voter_url_split = voter_url.split('/')
        voter_id = voter_url_split[6]

        # Voter role
        voter_role_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[2]/p/text()"
        voter_role_parsed = xpath_parse(voter_tree, voter_role_xpath)
        if len(voter_role_parsed) == 0:
            voter_role = ''
        else:
            voter_role = voter_role_parsed[0]

        # Voter nationality
        voter_nationality_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[3]/p/text()"
        voter_nationality_parsed = xpath_parse(voter_tree, voter_nationality_xpath)
        if len(voter_nationality_parsed) == 0:
            voter_nationality = ''
        else:
            voter_nationality = voter_nationality_parsed[0]     

        # Voter gender
        voter_gender_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[4]/p/text()"
        voter_gender_parsed = xpath_parse(voter_tree, voter_gender_xpath)
        if len(voter_gender_parsed) == 0:
            voter_gender = ''
        else:
            voter_gender = voter_gender_parsed[0].lower()

        # Set up for scraping the votes
        votes_url = votes_url_prefix + voter_id
        votes_tree = html_parse_tree(votes_url)

        voter_description_xpath = "//div[@class='secondary box sas-poll-voter-details']/p/text()"
        voter_description_parsed = xpath_parse(votes_tree, voter_description_xpath)

        # Voter title, poll category, 
        if len(voter_description_parsed) == 3:
            voter_title = voter_description_parsed[0].encode('utf-8').decode('utf-8')
            critic_category = voter_description_parsed[2].find("critics")
            director_category = voter_description_parsed[2].find("directors")
            if critic_category > -1:
                poll_category = "critics poll"
            if director_category > -1:
                poll_category = "directors poll"

        else:
            voter_title = ''
            critic_category = voter_description_parsed[0].find("critics")
            director_category = voter_description_parsed[0].find("directors")
            if critic_category > -1:
                poll_category = "critics poll"
            if director_category > -1:
                poll_category = "directors poll"       

        # Voter comments
        voter_comments_xpath = "//div[@class='wysiwyg']/p/text()"
        voter_comments_parsed = xpath_parse(votes_tree, voter_comments_xpath)
        if len(voter_comments_parsed) == 0:
            voter_comments = ''
        else:
            voter_comments = voter_comments_parsed[0].encode('utf-8').decode('utf-8')

        # Voter film count
        film_count_xpath = "//table[@class='sas-poll']/tr"
        film_count_parsed = xpath_parse(votes_tree, film_count_xpath)
        film_count = len(film_count_parsed)

        # Add data to voters_row
        voter_row = [voter_id, voter_name, voter_name_searchable, poll_category, voter_role, voter_title, voter_nationality, voter_gender, film_count, voter_comments]

        # Write to CSV
        add2csv(voter_row, 'voters_2012.csv')

        # Output to command line
        print([voter_id, voter_name, poll_category, voter_role, voter_name_searchable, voter_title, voter_nationality, voter_gender, film_count])
        
        # Scrape the film votes for each voter URL
        for film in range(1, film_count + 1):
            # Film title (raw, normed, searchable)
            film_title_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[1]/p/text() | //table[@class='sas-poll']/tr[" + str(film) + "]/td[1]/p/a/text()"
            film_title_parsed = xpath_parse(votes_tree, film_title_xpath)
            film_title_raw = film_title_parsed[0].encode('utf-8').decode('utf-8')
            film_title = title_norm(film_title_raw)
            film_title_searchable = strip_diacritics(film_title).lower()
            
            # Film ID
            film_url_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[1]/p/a/@href"
            film_url_parsed = xpath_parse(votes_tree, film_url_xpath)
            if len(film_url_parsed) == 0:
                film_url = ''
                # Create film IDs for missing film IDs
                if film_title in missing_films.keys():
                    film_id = missing_films[film_title]
                else:
                    missing_film_counter = missing_film_counter + 1
                    film_id = missing_film_counter
                    missing_films[film_title] = film_id
                    add2csv([film_id, film_title], 'missing_film_ids.csv')
            else:
                film_url = film_url_parsed[0]
                film_url_split = film_url.split('/')
                film_id = film_url_split[4]

            # Film year
            film_year_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[2]/p/text()"
            film_year_parsed = xpath_parse(votes_tree, film_year_xpath)
            if len(film_year_parsed) == 0:
                film_year = ''
            else:
                film_year = film_year_parsed[0]

            # Film director (raw and searchable)
            film_director_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[3]/p/text()"
            film_director_parsed = xpath_parse(votes_tree, film_director_xpath)
            if len(film_director_parsed) == 0:
                film_director = ''
            else:
                film_director = film_director_parsed[0].encode('utf-8').decode('utf-8')
            film_director_searchable = strip_diacritics(film_director).lower()
            
            # Write to CSV
            votes_row = [voter_id, film_title_raw, film_title, film_title_searchable, film_director, film_director_searchable, film_year, film_id]
            add2csv(votes_row, 'votes_2012.csv')