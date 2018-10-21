import csv

tweet_ids = set()

with open("los-angeles-election-merged.csv", mode="w") as output_file:
    with open("la-election-polls.csv", mode="r") as input_file:
        input_reader = csv.DictReader(input_file)
        for row in input_reader:
            header = row.keys()
            break
        output_writer = csv.DictWriter(f=output_file, fieldnames=header)
        output_writer.writeheader()
        for row in input_reader:
            if not(row["tweet-id"] in tweet_ids):
                output_writer.writerow(row)
                tweet_ids.add(row["tweet-id"])

    with open("la-elections.csv", mode="r") as input_file:
        input_reader = csv.DictReader(input_file)
        for row in input_reader:
            if not(row["tweet-id"] in tweet_ids):
                output_writer.writerow(row)
                tweet_ids.add(row["tweet-id"])

    with open("los-angeles-election-polls.csv", mode="r") as input_file:
        input_reader = csv.DictReader(input_file)
        for row in input_reader:
            if not(row["tweet-id"] in tweet_ids):
                output_writer.writerow(row)
                tweet_ids.add(row["tweet-id"])

    with open("los-angeles-election.csv", mode="r") as input_file:
        input_reader = csv.DictReader(input_file)
        for row in input_reader:
            if not(row["tweet-id"] in tweet_ids):
                output_writer.writerow(row)
                tweet_ids.add(row["tweet-id"])
