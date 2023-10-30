
import configparser



config_file_name = './experiments/deepmedic_CWT_general.yaml'
config_test = configparser.ConfigParser()  # open a new cfg parser to avoid memories from the previous cfg
config_test.optionxform = str
# config_test.read(test_config_name)
fp = open(config_file_name)
newstring = '[default]\n' + fp.read()  # insert a section name
config_test.read_string(newstring)
for section in config_test.sections():
    print(f"[{section}]")
    for key in config_test[section]:
        value = config_test[section][key]
        print(f"{key} = {value}")
    print()