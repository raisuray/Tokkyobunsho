import tools
import pprint

class Patent:
   
    def __init__(self, path):
        self.path = path
        self.doc = self.load_file()
        self.name = self.path.split('/')[-1]
        
    def print_name(self):
        print(self.name)
        
    def print_expmntl(self):
        pprint.pprint(self.doc)

    def load_file(self):
        with open(self.path, 'r') as f:
            self.doc = f.readlines()
        return self.extract()

    def extract(self):
        return tools.exct_experimental_section(self.doc)


if __name__ == '__main__':
    x = Patent('effect_words/1991185116.txt')
    x.print_name()