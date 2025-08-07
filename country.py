class India:
    def capital(self):
        print("New Dheli is the capital of India.")
    def language(self):
        print("Hindi is the language of India.")
    def type(self):
        print("India is a developing country.")
class Japan:
    def capital(self):
        print("Tokyo is the capital of Japan.")
    def language(self):
        print("Japanese is the language of Japan.")
    def type(self):
        print("Japan is a High tech country.")
obj_ind=India()
obj_jap=Japan()
for country in (obj_ind,obj_jap):
    country.capital()
    country.language()
    country.type()