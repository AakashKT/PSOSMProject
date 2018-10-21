import csv
years = set()
hashtags = {}

with open("russian-troll-tweets/tweets.csv", mode="r") as troll_file:
    troll_reader = csv.DictReader(troll_file)
    processed = 0
    for row in troll_reader:
        # print row["hashtags"]
        # years.add(row["created_str"][0:4])
        # for tag in row["hashtags"][1:-1].split(","):
        #     tag = tag[1:-1]
        #     if tag in hashtags.keys():
        #         hashtags[tag] += 1
        #     else:
        #         hashtags[tag] = 1
        print(row.keys())
        processed += 1
        if processed >= 1:
            # if processed >= 1000000:
            break
        # break
print(processed)
sortedTags = hashtags.items()
sortedTags = sorted(sortedTags, key=lambda tag: tag[1], reverse=True)
print(sortedTags[1:20])
query = ""
for (tag, count) in sortedTags[1:21]:
    query += " OR "+tag
query = query[4:]
print(query)
print(years)
