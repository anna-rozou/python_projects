import json


# .............FUNCTIONS.................
def json_function(data_1):
    with open("json_trans.txt", "w") as f:  # create a new file-> json_trans
        f.write(json.dumps(data_1))         # convert dictionary into a string and write in json_trans
    f.close()


# ..............MAIN.....................
with open("input.json", "r") as read_file:  # open the json file as read_file
    data = json.load(read_file)             # load json data into data
read_file.close()                           # close the json file
print(data)
json_function(data)
