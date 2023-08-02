import datetime
import requests
from tabulate import tabulate
from datetime import datetime
import pandas as pd
import csv
import datetime


url = 'https://appli.crowdlending.fr/projects/projectsList'

# use gpt chat to get headers
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-store, no-cache, must-revalidate',
    'Content-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'googtrans=/fr/en; googtrans=/fr/en; _ga=GA1.2.276913420.1685641545; _gid=GA1.2.316756310.1686240983; sess_ci=85nmike34631nguvfp58tf23j05ohstl',
    'Origin': 'https://appli.crowdlending.fr',
    'Referer': 'https://appli.crowdlending.fr/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

payload = {
    'draw': '2',
    'columns[0][data]': '',
    'columns[0][name]': 'p.id',
    'columns[0][searchable]': 'false',
    'columns[0][orderable]': 'false',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'nom',
    'columns[1][name]': 'p.nom',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'true',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'montant',
    'columns[2][name]': 'p.montant',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'true',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'plateforme',
    'columns[3][name]': 'p.plateforme',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'true',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': 'taux',
    'columns[4][name]': 'p.taux',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'true',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': 'duree',
    'columns[5][name]': 'p.duree',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'true',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': 'statutl2',
    'columns[6][name]': 'p.statutl2',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'true',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': 'lastpost',
    'columns[7][name]': 'lastpost',
    'columns[7][searchable]': 'false',
    'columns[7][orderable]': 'true',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'start': '0',
    'length': '7000',
    'search[value]': '',
    'search[regex]': 'false',
    # 'id_project': 'rewrite the script above with this data'
}


response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # print(data)
    # search_data = []
    project_count = 0  # Initialize the project count variable
    table_data = []  # List to store table rows
    project_data_list = []

    # Process each project
    for project in data['data']:
        # project_id = project['id']['plain']
        if project['nom']['plain'][-1] =="↵":
            project_name = project['nom']['plain'].replace("↵", "\\n")
        project_name = project['nom']['plain']
        project_amount = project['montant']['plain']
        project_platform = project['plateforme']['plain']
        project_interest_rate = project['taux']['plain']
        project_status = project['statut']['plain']
        project_siren = project['siren']['plain']
        project_duration = project['duree']['plain']
        project_comment = project['statutl2']['plain']
        # project_comment = 'funded'

        project_due_date_raw = project['datecloture']['plain']
            

        if project_due_date_raw is not None:

            input_formats = [
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S",
                "NULL",
                "",
                "%Y-%m-%d",
                "None",
                "%Y-%m-%dT%H:%M:%S.%f%z",
                "%Y-%m-%dT%H:%M:%S.%f",
                "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S.%f%z",
                "%Y-%m-%d %H:%M:%S.%f",
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%d %H:%M:%S%z",
                "0000-00-00 00:00:00",
            ]

            output_format = "%d/%m/%Y"

            # Iterate over the input formats until a valid date is parsed
            parsed_date = None
            for date_format in input_formats:
                if date_format == ["None" , "NULL",""]:
                    parsed_date = ''
                    # continue
                try:
                    parsed_date = datetime.datetime.strptime(
                        project_due_date_raw, date_format)
                    break
                except ValueError:
                    pass

            # Check if a valid date was parsed
            if parsed_date is not None:
                project_due_date = parsed_date.strftime(output_format)
                # print(project_due_date) // printing the project_due_date
            else:
                print("Invalid date format:", project_due_date_raw,project_name)
        else:
            # print("project_due_date_raw is None")
            # assigns empty string to values on none as seen in line 219
            parsed_date = ''

        project_type = project['loantype']['plain']
        project_periodicity = project['loanperiodicity']['plain']
        project_note_plateforme = project['note']['plain']

      

        # Display project information
        # print("Project ID: ", project_id)
        # print("Project Name: ", project_name)
        # print("Project Amount: ", project_amount)
        # print("Project Platform: ", project_platform)
        # print("Interest Rate: ", project_interest_rate)
        # print("Project Status: ", project_status)
        # print("Project Siren: ", project_siren)
        # print("Project Due Date: ", project_due_date)
        # print("Project Due Date: ", project_due_date_raw)
        # print("Project Type: ", project_type)
        # print("Project Comment: ", project_comment)
        # print("Project Periodicty: ", project_periodicity)
        # print("Note Plateforme: ", project_note_plateforme)
        # print(search_data)

# new line
        # print("\n") 


        project_count += 1  # Increment the project count


    # Create a dictionary to store the project data
        project = {
            # "Project ID": project_id,
            "Project Name": project_name,
            "Project Amount": project_amount,
            "Project Platform": project_platform,
            "Interest Rate": project_interest_rate,
            "Project Status": project_status,
            "Project Siren": project_siren,
            "Project Duration": project_duration,
            "Project Due Date": project_due_date,
            "Project Type": project_type,
            "Project Periodicity": project_periodicity,
            "Note Plateforme": project_note_plateforme,
            "Project Comment": project_comment
        }

        project_data_list.append(project)
# # # # # # Create a DataFrame from the project data dictionary
        df = pd.DataFrame(project_data_list)
        df.to_csv('Vittoria.csv', index=False)

# Display the DataFrame
    # print(df)
    print("Total number of projects:", project_count)
        # else:
    # print("Request failed with status code:", response.status_code)
