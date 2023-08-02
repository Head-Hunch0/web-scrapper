from bs4 import BeautifulSoup
import requests
import random
import pandas as pd

def times_scrapper():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Reactjs&txtLocation='
    payload = {
            'from': 'submit',
            'actualTxtKeywords': 'Vuejs',
            'searchBy': 0,
            'rdoOperator': 'OR',
            'searchType': 'personalizedSearch',
            'luceneResultSize': 5,  # Update to retrieve 100 items
            'postWeek': 7,
            'txtKeywords': 'Vuejs',
            'pDate': 'I',
            'sequence': 2,
            'startPage': 1
        }
    htmml_text = requests.get(url,params=payload).text
    soup = BeautifulSoup(htmml_text,'lxml')

    project_data_list =[]

    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    print("Total Jobs Found:",len(jobs))
    for job in jobs:
        company_name= job.find('h3', class_='joblist-comp-name').text.replace(' ','').replace('(MoreJobs)', '')
        title= job.find('h2').text.replace(' ','')
        skills = job.find('span',class_='srp-skills').text.replace(' ','')
        pubdate = job.find('span', class_='sim-posted').span.text
        location = job.find('ul', class_='top-jd-dtl clearfix').span.text
        # hardcoded email address
        email = 'info@kaya.co.ke'

        # print(more_link) easier way to do whats below 
        # more_link = job.header.h2.a['href']

        #getting the link to the more details page
        u = str(job.find('h2'))
        test = BeautifulSoup(u, 'html.parser')
        a_tag = test.find('a')
        href_value = a_tag['href']

        # using the link to the details page to gather further info on the job listing
        # get website and job description 
        resp = requests.get(href_value).text
        test1 = BeautifulSoup(resp, 'html.parser')
        we = test1.find_all('span','basic-info-dtl')
        website=we[5].text
        desc = test1.find('div', 'jd-desc job-description-main')
        job_description = desc.get_text(strip=True).replace('Job Description', '')

        # generate random number as a salary as this site does not have salaries in some cases

        salary = random.randint(50000,999999)

        print(f' Company Name: {company_name}')
        print(f' Job Skills: {skills}')
        print(f' Job Title: {title}')


        project = {
            # "Project ID": project_id,
            "user_id": 1,
            "title": title,
            "tags": skills,
            "logo": 'Null',
            "company": company_name,
            "location": location,
            "email": email,
            "website": website,
            "description": job_description,
            "salary": salary,
            "from": 'TimesJobs'
        }

    #     project_data_list.append(project)
    # # # # # # # Create a DataFrame from the project data dictionary
    #     df = pd.DataFrame(project_data_list)
    #     df.to_csv('makazitest.csv', index=False)

# times_scrapper()

# def indeed_scrapper():
#     url = "https://www.indeed.com/jobs"


#     params = {
#         "q": "react js",
#         "l": "Remote",
#         "fromage": "7"
#     }

#     response = requests.get(url, params=params).text
#     print(response.content)


# indeed_scrapper()