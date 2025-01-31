import csv

def save_to_file(keyword, jobs):
    file = open(f"{keyword}.csv", "w")
    writter = csv.writer(file)
    writter.writerow(["company","position", "region","link"])

    for job in jobs:
        writter.writerow(job.values())

    file.close()