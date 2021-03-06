import yaml
import os
base_loc = os.path.dirname(os.path.realpath(__file__))
last_index = base_loc.rfind("/")
base_loc = base_loc[0:last_index] + "/"
print(base_loc)

config_filepath = base_loc + "config/config.yml"
print(config_filepath);
stream = open(config_filepath, "r")
dictionary = yaml.load(stream)

class Config(object):
	def __init__(self, conf):
		self.CONFIG = conf;

	def __getattr__(self, query):
		if query in self.CONFIG:
			ans = self.CONFIG[query];
			if "path" in query:
				ans = base_loc + ans
			return ans
		else:
			return None

CONFIG = Config(dictionary)
