import requests
from bs4 import BeautifulSoup
from extractors.job import Job


def extract_remoteok_jobs(keyword):
	all_jobs = []

	user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	response = requests.get(
	    f"https://remoteok.com/remote-{keyword}-jobs",
	    headers={"User-Agent": user_agent}
	)

	soup = BeautifulSoup(response.text, "html.parser")
	jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

	for job in jobs:
		job = job.find("td", class_="company position company_and_position")
		if job is not None:
			title = job.find("h2").text.strip()
			company = job.find("h3").text.strip()
			region = job.find("div", class_="location")
			region = "Not specified" if region is None else region.text.strip()
			link = job.find("a")["href"].strip()

			all_jobs.append(
			    Job(
			        company=company,
			        position=title,
			        region=region,
			        link=f"https://remoteok.com{link}",
					reference="remoteok.com"
			    )
			)

	return all_jobs
