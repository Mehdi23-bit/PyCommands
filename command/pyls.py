# version 
from  config.PylsArgument import PylsArguments
from  parser.parser import Parser

def main():
  parser=Parser()
  arguments=PylsArguments().arguments
  parser.load(arguments)
  args=parser.parse_args()
  print(args)

if __name__== "__main__":
 	main()

print(__name__)
