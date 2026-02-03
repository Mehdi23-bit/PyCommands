from  argparse import ArgumentParser

class Parser(ArgumentParser):
	def __init(self,config,**kwargs):
		super().__init__(**kwargs)
	def load(self,arguments):
		for name,config in arguments.items():
			self.add_argument(name,**config)

