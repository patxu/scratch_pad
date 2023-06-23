# send a POST request to apply for a job at Plaid

import requests

url = 'https://contact.plaid.com/jobs'
app = {
  "name": "Patrick Xu",
  "email": "patrickxu13@gmail.com",
  "resume": "http://patrickxu.com/resume.pdf",
  "phone": "978-412-5505",
  "job_id": "14e4d70d-efd9-4483-8d9e-935b30895a10", # leave as is
  "github": "https://github.com/patxu", # optional
  "website": "http://patrickxu.com/", # optional
  "location": "Cambridge", # optional
  "favorite_candy": "Milka Bar", # optional
  "superpower": "I leave things better than I find them" # optional
}

x = requests.post(url, json = app)
print(x.text)
