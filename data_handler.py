import json
import pdb
import codecs
import pdb

def get_data():
    tweets = []
    files = ['ambos2.json']
    for file in files:
        with codecs.open('./tweet_data/' + file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        for line in data:
            tweet_full = json.loads(line)
            tweets.append({
                'id': tweet_full['id'],
                'text': tweet_full['text'].lower(),
                'label': tweet_full['label'],
                'name': "TESTE"
                })

    #pdb.set_trace()
    return tweets


if __name__=="__main__":
    tweets = get_data()
    print(tweets)