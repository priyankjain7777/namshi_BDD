#refrence urllib;  https://stackoverflow.com/questions/3595363/properties-file-in-python-similar-to-java-properties

#!/usr/bin/python
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

print.config.get('DatabaseSection', 'database.dbname');