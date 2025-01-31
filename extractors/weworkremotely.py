import requests
from bs4 import BeautifulSoup
from extractors.job import Job


def extract_weworkremotely_jobs(keyword):
    all_jobs = []

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    response = requests.get(
        f"https://weworkremotely.com/remote-jobs/search?term={keyword}",
        headers={"User-Agent": user_agent})

    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all("section", class_="jobs")

    for section in sections:
        jobs = section.find_all("li")[:-1]
        for job in jobs:
            if "feature--ad" in job["class"]:
                continue
            company = job.find("span", class_="company").text.strip()
            position = job.find("span", class_="title").text.strip()
            region = job.find("span", class_="region").text.strip()
            link = job.select(":scope > a")[0]["href"].strip()
            link = f"https://weworkremotely.com{link}"
            all_jobs.append(
                Job(company=company,
                    position=position,
                    region=region,
                    link=link,
                    reference="weworkremotely.com"))

    return all_jobs
