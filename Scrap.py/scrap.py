import requests
from bs4 import BeautifulSoup

all_jobs = []

url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings'


def scrape_page(url):
  print(f"Scraping {url}")

  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  jobs = soup.find('section', class_='jobs').find_all('li')[1:-1]

  for job in jobs:
    title = job.find('span', class_='title').text
    company_info = job.find_all('span', class_='company')

    if len(company_info) == 3:
      company, position, region = company_info
      url = job.find('div',class_="tooltip--flag-logo").next_sibling.get('href')
      job_data = {
        'title': title,
        'company': company.text,
        'position': position.text,
        'region': region.text,
        'url': f"https://weworkremotely.com{url}",
      }
      all_jobs.append(job_data)
    else:
      print(f"Skipping job due to unexpected company info structure: {company_info}")


def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  return len( soup.find('div', class_='pagination').find_all('span', class_='page'))


total_pages = get_pages(
    'https://weworkremotely.com/remote-full-time-jobs?page=1')

for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(len(all_jobs))
'''
keywords =[
  'flutter',
  'python',
  'golang'
] 
r = requests.get('https://remoteok.com/remote-flutter-jobs')
print(r.status_code)
print(r.content)
'''
