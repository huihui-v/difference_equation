import json
import sys

def parse(CONFIG_NAME):
    config = open(CONFIG_NAME)
    # print (config)
    json_config = json.load(config)
    config.close()
    return json_config