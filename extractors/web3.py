import requests
from bs4 import BeautifulSoup
from extractors.job import Job
import re


def extract_web3_jobs(keyword):
    all_jobs = []

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    response = requests.get(f"https://web3.career/{keyword}-jobs",
                            headers={"User-Agent": user_agent})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("table", class_="table").find_all("tr",
                                                       class_="table_row")

    for job in jobs:
        if job.has_attr('id') and "sponsor" in job["id"]:
            continue
        company = job.find("h3").text.strip()
        position = job.find(
            "h2", class_="fs-6 fs-md-5 fw-bold my-primary").text.strip()
        region = job.find("td", class_="job-location-mobile").text.strip()
        link = job["onclick"]
        match = re.search(r"'(.*?)'", link)
        link = f"https://web3.career{match.group(1)}"
        all_jobs.append(
            Job(company=company,
                position=position,
                region=region,
                link=link,
                reference="web3.career"))
    
    # Page searching version - takes to much time
    # page = 1
    # response = requests.get(f"https://web3.career/{keyword}-jobs",
    #                         headers={"User-Agent": user_agent})
    # soup = BeautifulSoup(response.text, "html.parser")
    # current_page = soup.find("li", class_="page-item active").text
    # while f"{page}" == current_page:
    #     jobs = soup.find("table", class_="table").find_all("tr",
    #                                                        class_="table_row")

    #     for job in jobs:
    #         if job.has_attr('id') and "sponsor" in job["id"]:
    #             continue
    #         company = job.find("h3").text.strip()
    #         position = job.find(
    #             "h2", class_="fs-6 fs-md-5 fw-bold my-primary").text.strip()
    #         region = job.find("td", class_="job-location-mobile").text.strip()
    #         link = job["onclick"]
    #         match = re.search(r"'(.*?)'", link)
    #         link = f"https://web3.career/{match.group(1)}"
    #         all_jobs.append(
    #             Job(company=company,
    #                 position=position,
    #                 region=region,
    #                 link=link,
    #                 reference="web3.career"))

    #     page += 1
    #     response = requests.get(
    #         f"https://web3.career/{keyword}-jobs?page={page}",
    #         headers={"User-Agent": user_agent})
    #     soup = BeautifulSoup(response.text, "html.parser")
    #     current_page = soup.find("li", class_="page-item active").text
    return all_jobs
