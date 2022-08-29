import json

class speech:
    def __init__(self):
        self.sent = {}
        # open the data from the json file
        with open('speechToText.json', 'r') as infile:
            self.sent = json.load(infile)
        # for i in self.sent:
        #     print(i)
    
    def run(self):
        # declare an empty dict to store words with their timeframe as a key
        self.timestamps = {}
        
        for i in self.sent['results'][0]['alternatives'][0]['timestamps']:
            print(i)
            self.timestamps[str(i[1]) + ' - ' +str(i[2])] = i[0]
        
        # print(self.timestamps)

        # declare an empty dict to store speakers with their timeframe as a key
        self.speakers = {}
        for i in self.sent['speaker_labels']:
            self.speakers[str(i['from']) + ' - ' + str(i['to'])] = i['speaker']

        # print(self.speakers)
        speaker = -1
        for i in self.speakers:
            # if the previous speaker is different than current one, change the line and speaker
            if speaker != self.speakers[i]:
                print('\nspeaker ',self.speakers[i], ' - ', end=' ')
            
            # set speaker to store the previous speaker in order to compare with the next one
            speaker = self.speakers[i]
            print(self.timestamps[i], end=' ')


if __name__ == "__main__":
    speech().run()