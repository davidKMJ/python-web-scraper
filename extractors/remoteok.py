import requests
from bs4 import BeautifulSoup

all_jobs = []

def set_job(jobs):
  for job in jobs:
    title = job.find("h2").text.strip()
    company = job.find("h3").text.strip()
    region = "Not specified" if job.find("div", class_="location") == None else job.find("div", class_="location").text.strip()
    url = job.find("a")["href"].strip()

    job_data = {
      "title": title,
      "company": company,
      "region": region,
      "link": f"https://remoteok.com{url}"
    }
    all_jobs.append(job_data) 

def get_jobs(keyword):
  print(f"Scrapping {keyword}...")
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
  soup = BeautifulSoup(response.text, "html.parser")
  temp = soup.find("table", id="jobsboard").find_all("tr", class_="job")
  jobs = []
  for item in temp:
    jobs.append(item.find("td", class_="company position company_and_position"))

  set_job(jobs)
  return all_jobs
