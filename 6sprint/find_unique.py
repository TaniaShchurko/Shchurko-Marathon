import json
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
def parse_user(file_wr, *file_read):
    result=[]
    checking=[]
    for file in file_read:
        try:
            with open(file) as json_file:
                    data = json.load(json_file)
                    for i in range(len(data)):
                        if 'name' in data[i].keys():
                            if data[i]['name'] not in checking:
                                checking.append(data[i]['name'])
                                result.append(data[i])
        except FileNotFoundError:
            logging.error(f"File {file} doesn't exist")
    with open(file_wr, "w") as write_file:
        json.dump(result, write_file, indent=4)