import preprocessor as p
import numpy as np
import json

'''
    Set options: which options should be removed from the text
'''
p.set_options(p.OPT.URL, p.OPT.EMOJI)

'''
    Load all the embeddings
'''
embeddings = {}
with open('glove.twitter.27B.200d.txt') as f:
  for line in f:
    values = line.split()
    word = values[0]
    embed = np.array(values[1:], dtype=np.float32)
    embeddings[word] = embed
    # break

'''
    Helper function
'''
def embed(word):
    if word in embeddings.keys():
        return True, embeddings[word]
    return False, 0

'''
    Make feature for the given text
'''
def make_feature(text):
    count = 0
    features = np.zeros(200)
    words = text.split()
    for word in words:
        is_embeddable, embedding_value = embed(word)
        if is_embeddable:
            features += embedding_value
            count += 1
    if count == 0:
        return features
    return features / count

with open('data.json') as f:
    data = json.load(f)

for tweet in data:
    cleanData = p.clean(tweet["tweet_text"].encode("utf-8"))
    features = make_feature(cleanData)
    tweet['tweet_features'] = features.tolist()

with open('processed_data.json', 'w') as output_file:
    json.dump(data, output_file)


'''
'''
