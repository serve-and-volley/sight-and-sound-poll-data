from lxml import html
import requests
import re
import json
import csv
import sys

def html_parse_tree(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree

def xpath_parse(tree, xpath):
    result = tree.xpath(xpath)
    return result

def regex_strip_string(string):
    string = re.sub('\n', '', string).strip()
    string = re.sub('\r', '', string).strip()
    string = re.sub('\t', '', string).strip()
    return string

def regex_strip_array(array):
    for i in xrange(0, len(array)):
        array[i] = regex_strip_string(array[i]).strip()
    return array

def array2csv(array, filename):
    csv_array = array
    csv_out = open(filename + ".csv", 'w')
    mywriter = csv.writer(csv_out)
    for row in csv_array:
        mywriter.writerow(row)
    csv_out.close()

voter_url = "http://www.bfi.org.uk/films-tv-people/sightandsoundpoll2012/voters"
voter_tree = html_parse_tree(voter_url)

votes_url_prefix = "http://www.bfi.org.uk/films-tv-people/sightandsoundpoll2012/voter/"

table_count_xpath = "//div[@class='sas-poll-az-list-group']"
table_count_parsed = xpath_parse(voter_tree, table_count_xpath)
table_count = len(table_count_parsed)

voters = []
votes = []

for table in range(1, table_count + 1):
    row_count_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr"
    row_count_parsed = xpath_parse(voter_tree, row_count_xpath)
    row_count =  len(row_count_parsed)

    for row in range(1, row_count + 1):
        voter_name_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[1]/p/a/text()"
        voter_name_parsed = xpath_parse(voter_tree, voter_name_xpath)
        voter_name = voter_name_parsed[0].encode('utf-8').decode('utf-8')

        voter_url_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[1]/p/a/@href"
        voter_url_parsed = xpath_parse(voter_tree, voter_url_xpath)
        voter_url = voter_url_parsed[0]

        voter_url_split = voter_url.split('/')
        voter_id = voter_url_split[6]

        voter_role_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[2]/p/text()"
        voter_role_parsed = xpath_parse(voter_tree, voter_role_xpath)
        if len(voter_role_parsed) == 0:
            voter_role = ''
        else:
            voter_role = voter_role_parsed[0]

        voter_nationality_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[3]/p/text()"
        voter_nationality_parsed = xpath_parse(voter_tree, voter_nationality_xpath)
        if len(voter_nationality_parsed) == 0:
            voter_nationality = ''
        else:
            voter_nationality = voter_nationality_parsed[0]     

        voter_gender_xpath = "//div[@class='sas-poll-az-list-group'][" + str(table) + "]/table/tr[" + str(row) + "]/td[4]/p/text()"
        voter_gender_parsed = xpath_parse(voter_tree, voter_gender_xpath)
        if len(voter_gender_parsed) == 0:
            voter_gender = ''
        else:
            voter_gender = voter_gender_parsed[0]       

        votes_url = votes_url_prefix + voter_id
        votes_tree = html_parse_tree(votes_url)

        voter_description_xpath = "//div[@class='secondary box sas-poll-voter-details']/p/text()"
        voter_description_parsed = xpath_parse(votes_tree, voter_description_xpath)

        if len(voter_description_parsed) == 3:
            voter_title = voter_description_parsed[0].encode('utf-8').decode('utf-8')
            voter_nationality = voter_description_parsed[1].encode('utf-8').decode('utf-8')

            critic_category = voter_description_parsed[2].find("critics")
            director_category = voter_description_parsed[2].find("directors")
            if critic_category > -1:
                poll_category = "critics poll"
            if director_category > -1:
                poll_category = "directors poll"

        else:
            voter_title = ''
            voter_nationality = ''
            critic_category = voter_description_parsed[0].find("critics")
            director_category = voter_description_parsed[0].find("directors")
            if critic_category > -1:
                poll_category = "critics poll"
            if director_category > -1:
                poll_category = "directors poll"       

        voter_comments_xpath = "//div[@class='wysiwyg']/p/text()"
        voter_comments_parsed = xpath_parse(votes_tree, voter_comments_xpath)
        if len(voter_comments_parsed) == 0:
            voter_comments = ''
        else:
            voter_comments = voter_comments_parsed[0].encode('utf-8').decode('utf-8')

        film_count_xpath = "//table[@class='sas-poll']/tr"
        film_count_parsed = xpath_parse(votes_tree, film_count_xpath)
        film_count = len(film_count_parsed)
        
        voters.append([voter_name, voter_id, voter_url, voter_role, voter_nationality, voter_gender, poll_category, voter_title, voter_nationality, film_count, voter_comments])
        #print([voter_name, voter_id, voter_url, voter_role, voter_nationality, voter_gender, poll_category, voter_title, voter_nationality, film_count, voter_comments])
        array2csv(voters, 'voters_2012')        

        for film in range(1, film_count + 1):
            film_title_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[1]/p/text() | //table[@class='sas-poll']/tr[" + str(film) + "]/td[1]/p/a/text()"
            film_title_parsed = xpath_parse(votes_tree, film_title_xpath)
            film_title = film_title_parsed[0].encode('utf-8').decode('utf-8')
            
            film_url_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[1]/p/a/@href"
            film_url_parsed = xpath_parse(votes_tree, film_url_xpath)
            if len(film_url_parsed) == 0:
                film_url = ''
                film_id = ''
            else:
                film_url = film_url_parsed[0]
                film_url_split = film_url.split('/')
                film_id = film_url_split[4]

            film_year_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[2]/p/text()"
            film_year_parsed = xpath_parse(votes_tree, film_year_xpath)
            if len(film_year_parsed) == 0:
                film_year = ''
            else:
                film_year = film_year_parsed[0]

            film_director_xpath = "//table[@class='sas-poll']/tr[" + str(film) + "]/td[3]/p/text()"
            film_director_parsed = xpath_parse(votes_tree, film_director_xpath)
            if len(film_director_parsed) == 0:
                film_director = ''
            else:
                film_director = film_director_parsed[0].encode('utf-8').decode('utf-8')

            votes.append([voter_id, film_title, film_url, film_id, film_year, film_director])
        #print([voter_id, film_title, film_url, film_id, film_year, film_director])
        array2csv(votes, 'votes_2012')



