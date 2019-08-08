
import spacy
import code

nlp = spacy.load('en_core_web_lg')

class AddressParse:
    
    def __init__(self, address):
        self.address = address
        self. result = {
            'name': '',
            'street': '',
            'country': '',
            'ORG': '',
           'house number': '',
        }

    def parse_lines(self):
        lines = [line for line in self.address.split('\n') if line]
        lines_cl = []
        for line in lines:
            words = [word.title() for word in line.split(' ')]
            line = ' '.join(words)
            lines_cl.append(line)
        return lines_cl

    def get_name(self, lines):
        for line in lines:
            doc = nlp(line)
            for ent in doc.ents:
                #print(ent.label_)
                if ent.label_ == 'PERSON':
                    self.result['name'] = ent.text
                if ent.label_ == 'GPE':
                    self.result['country'] = ent.text
                if ent.label_ == 'ORG':
                    self.result['organisation'] = ent.text             
    
    def get_street(self, lines):
        for line in lines:
            words = [word.lower() for word in line.split(' ')]
            if 'street' in words or 'st' in words or 'strt' in words or 'ave' in words or 'avenue' in words or 'rd' in words or 'dr' in words or 'hwy' in words or 'blvd' in words or 'way' in words or 'lane' in words or 'route' in words or 'loop' in words:
                self.result['street'] = line
            elif 'suite' in words or "house no." in words or "house number" in words or "apt" in words or "hno." in words or "floor" in words:
                self.result['house number'] = line

    def street_using_ent(self, lines):
        for line in lines:
            doc = nlp(line)
            for ent in doc.ents:
                print(ent.label_)
                if ent.label_ in ['FAC', 'LOC']:
                    self.result['street'] = line

    def parse_street(self):
        lines = self.parse_lines()
        self.get_name(lines)
        self.get_street(lines)
        if self.result['street'] == '':
            self.street_using_ent(lines)
        print(self.result)

