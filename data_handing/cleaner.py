import csv

black_ids = set()


# def date_filter(date):
#     years.add(date[0:4])
#     return date[0:4] in ["2016", "2017"]


with open("russian-troll-tweets/tweets.csv", mode="r") as input_file:
    input_reader = csv.DictReader(input_file)
    for row in input_reader:
        black_ids.add(row["tweet_id"])

with open("us-election.csv", mode="r") as input_file:
    input_reader = csv.DictReader(input_file)
    for row in input_reader:
        header = row.keys()
        break
    with open("us-election-cleaned.csv", mode="w") as cleaned_file:
        clean_writer = csv.DictWriter(f=cleaned_file, fieldnames=header)
        clean_writer.writeheader()
        processed = 0
        for row in input_reader:
            if not (row["tweet-id"] in black_ids):
                clean_writer.writerow(row)
            processed += 1
            if processed % 1000 == 0:
                print(processed)
