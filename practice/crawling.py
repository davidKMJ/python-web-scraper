import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

jobs_db_1 = []


def scrape_weworkremotely():
    url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )

    jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]

    for job in jobs:
        if "feature--ad" in job["class"]:
            continue

        title = job.find("span", class_="title")
        region = job.find("span", class_="region")
        company, position, _ = job.select("span.company")
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        job_data = {
            "title": title.text,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{url}",
        }
        jobs_db_1.append(job_data)


scrape_weworkremotely()

jobs_db_2 = []

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.wanted.co.kr/")
time.sleep(1)
page.click("button.Aside_searchButton__rajGo")
time.sleep(1)
page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(1)
page.keyboard.down("Enter")
time.sleep(1)
page.click("a#search_tab_position")
for _ in range(5):
    time.sleep(1)
    page.keyboard.down("End")
time.sleep(1)
content = page.content()
page.screenshot(path="screenshot.png")
p.stop()

soup = BeautifulSoup(content, "html.parser")
jobs = soup.find_all("div", class_="JobCard_container__REty8")

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company = job.find("span", class_="JobCard_companyContent___EEde").text
    job_data = {
        "title": title,
        "company": company,
        "url": link,
    }
    jobs_db_2.append(job_data)
