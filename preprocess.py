import preprocessor as p
import numpy as np
import json, sys

file_path = sys.argv[1]

'''
    Set options: which options should be removed from the text
'''
p.set_options(p.OPT.EMOJI)

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
    try:
        return True, embeddings[word]
    except:
        return False, 0

    # if word in embeddings.keys():
    #     return True, embeddings[word]

    # return False, 0
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

with open(file_path) as f:
    data = json.load(f)

print("CLEANING...")

final = []

done = 0
for tweet in data:
    cleanData = p.clean(tweet["text"].encode("utf-8"))
    features = make_feature(cleanData)
    tweet['tweet_features'] = features.tolist()
    done += 1
    print("%s" % done)

print("done")



with open('processed_data.json', 'w') as output_file:
    json.dump(data, output_file)


'''
'''
