import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

job_cards = soup.find_all("div", class_="card-content")

for job in job_cards:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")

    jobs.append([
        title.text.strip() if title else "N/A",
        company.text.strip() if company else "N/A",
        location.text.strip() if location else "N/A"
    ])

df = pd.DataFrame(jobs, columns=["Title", "Company", "Location"])
df.to_csv("jobs.csv", index=False)

print("Jobs scraped successfully 🚀")
print(df.head())