import json


class Resources:
    url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html" #source URL


class data:
    #reading the JSON file
    f = open("C:\\Users\\Sevu Arjun\\PycharmProjects\\cawStudios\\utilities\\data.json")
    json_file = json.load(f)
    dump = json.dumps(json_file, separators=(',', ':'))

    #storing the data for assertion

    table101 = json_file[0]['name']
    table102 = str(json_file[0]['age'])
    table103 = json_file[0]['gender']
    table201 = json_file[1]['name']
    table202 = str(json_file[1]['age'])
    table203 = json_file[1]['gender']
    table301 = json_file[2]['name']
    table302 = str(json_file[2]['age'])
    table303 = json_file[2]['gender']
    table401 = json_file[3]['name']
    table402 = str(json_file[3]['age'])
    table403 = json_file[3]['gender']
    table501 = json_file[4]['name']
    table502 = str(json_file[4]['age'])
    table503 = json_file[4]['gender']

