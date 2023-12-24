import os

def get_current_path():
		return os.path.dirname(os.path.realpath(__file__))

def get_file_name():
		return os.path.basename(__file__)

class FileNameDescriptor:
    def __get__(self, instance, owner):
        return f'{instance.name}.{instance.model_type}'

class ANN_Shell:
	file_name = FileNameDescriptor()
	file_location = f'{get_current_path()}/{file_name}'
	
	def __init__(self, name=get_file_name(), model_type='keras'):
		self.name = name
		self.model_type = model_type
		self.model = self.load_model()
	
	def load_model(self):
		pass
	
	def save_model(self):
		pass
	

if __name__ == '__main__':
	ann_shell = ANN_Shell()
	to_print = ['name', 'model_type', 'file_name', 'file_location']
	print(ann_shell.file_name)
	for item in to_print:
		key = item.replace('_', ' ').title()
		val = getattr(ann_shell, item)
		print(f'{key}: {val}')