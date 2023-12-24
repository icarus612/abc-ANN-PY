from os import path

def get_path(new_path=""):
		return path.realpath(path.join(path.dirname(__file__), new_path))

def get_file_name():
		return path.splitext(path.basename(__file__))[0]

class ANN_Shell:	
	def __init__(self, name=get_file_name(), model_type='keras'):
		self.name = name
		self.model_type = model_type
		self.model = self.load_model()
	
	@property
	def file_name(self):
		return f'{self.name}.{self.model_type}'
	
	@property
	def file_location(self):
		return get_path(f'../models/{self.file_name}')
	
	def load_model(self):
		pass
	
	def save_model(self):
		pass
	

if __name__ == '__main__':
	ann_shell = ANN_Shell()
	to_print = ['name', 'model_type', 'file_name', 'file_location']
	
	for item in to_print:
		key = item.replace('_', ' ').title()
		val = getattr(ann_shell, item)
		print(f'{key}: {val}')