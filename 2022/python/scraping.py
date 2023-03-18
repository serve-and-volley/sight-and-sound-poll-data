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
    for i in range(0, len(array)):
        array[i] = regex_strip_string(array[i]).strip()
    return array

def title_norm(title_string):
    prefixes = ["The", "A", "La", "Le", "L'", "Les", "An", "Il", "El", "Une", "Los", "Un", "Das", "O", "J'"]
    for prefix in prefixes:
        prefix_string = ', ' + prefix
        if title_string.find(prefix_string) > 1:
            if len(title_string) - (title_string.find(prefix_string) + len(prefix_string)) == 0:
                title_string = prefix + ' ' + title_string.replace(prefix_string, '')
    title_string = title_string.replace("L' ", "L'").replace("J' ", "J'")
    return title_string

def add2csv(array, filename):
    with open(filename, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(array)

def char_list(string):
    string_split = list(string)
    for char in string_split:
        if char not in characters:
            characters.append(char)

def string_clean(string):
    string = string.replace('½', ' 1/2')
    string = string.replace('…', '...')
    string = string.strip()
    try: string = string.encode('latin-1').decode('utf-8')
    except:
        try: string = string.encode('latin-1').decode('latin-1')
        except: string = string.encode('utf-8').decode('utf-8')
    if string.isupper() is True: string = string.title()
    return string

def strip_diacritics(string):
    convert = {
        '½':' 1/2',
        'Ã':'A',
        'Á':'A',
        'À':'A',
        'Ä':'A',
        'Â':'A',
        'É':'E',
        'È':'E',
        'Ô':'O',
        'Õ':'O',
        'Ö':'O',
        'Š':'S',
        'Ü':'U',
        'Ż':'Z',
        'ž':'z',
        'à':'a',
        'á':'a',
        'â':'a',
        'ã':'a',
        'ä':'a',
        'å':'a',
        'ā':'a',
        'æ':'ae',
        'ç':'c',
        'č':'c',
        'è':'e',
        'é':'e',
        'ê':'e',
        'ë':'e',
        'ē':'e',
        'ě':'e',
        'í':'i',
        'ï':'i',
        'ī':'i',
        'ł':'l',
        'ñ':'n',
        'ó':'o',
        'ô':'o',
        'õ':'o',
        'ö':'o',
        'ø':'o',
        'ō':'o',
        'ő':'o',
        'ò':'o',
        'ố':'o',
        'ř':'r',
        'š':'s',
        'ú':'u',
        'ü':'u',
        'û':'u',
        '°':''
    }
    string_split = list(string)
    for key in convert.keys():
        string = string.replace(key, convert[key])
    return string
