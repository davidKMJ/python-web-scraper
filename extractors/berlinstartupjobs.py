import requests
from bs4 import BeautifulSoup
from extractors.job import Job


def extract_berlinstartupjobs_jobs(keyword):
	all_jobs = []

	user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
	response = requests.get(
	    f"https://berlinstartupjobs.com/skill-areas/{keyword}",
	    headers={"User-Agent": user_agent})

	soup = BeautifulSoup(response.text, "html.parser")
	jobs = soup.find_all("li", class_="bjs-jlid")

	for job in jobs:
		company = job.find("a", class_="bjs-jlid__b").text.strip()
		position = job.find("h4", class_="bjs-jlid__h").find("a").text.strip()
		link = job.find("h4", class_="bjs-jlid__h").find("a")["href"].strip()
		all_jobs.append(
		    Job(
		        company=company,
		        position=position,
		        region="berlin",
		        link=link,
				reference="berlinstartupjobs.com"
		    ))

	return all_jobs
