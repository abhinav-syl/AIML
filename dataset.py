import spacy
import pandas as pd
import asyncio
import json

class data():
    def __init__(self):
        self.df = pd.read_csv('IMDB Dataset.csv')
        self.df.head()
        self.nlp = spacy.load("en_core_web_sm")
        try:
            with open('nouns.json', 'r') as outfile:
                self.word_dict = json.load(outfile)
        except Exception as E:
            print(E)
            self.word_dict = {}
            self.word_dict['City'] = ['']
            self.word_dict['Person'] = ['']
            self.word_dict['count'] = 0

    def get_nouns(self, lists):
        for i in lists:
            doc = self.nlp(i)
            for ent in doc.ents:
                # print(ent.text, ent.label_)
                if ent.label_ == 'PERSON':
                    self.word_dict['Person'].append(ent.text)
                elif ent.label_ == 'GPE':
                    self.word_dict['City'].append(ent.text)

    def run(self):
        for i in range(self.word_dict['count'], len(self.df), 100):
            print(i)
            self.get_nouns(self.df['review'][i:i + 100])
            self.word_dict['count'] = i
            self.store_json()

        df_nouns = pd.DataFrame(data=nouns, columns=['Word', 'Type'])
        print(df_nouns)

    def store_json(self):
        json_object = json.dumps(self.word_dict)
        with open('nouns.json', 'w') as json_file:
            json_file.write(json_object)


data().run()