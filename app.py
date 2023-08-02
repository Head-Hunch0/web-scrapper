# import os
# import pandas as pd

# # Get the current working directory
# current_dir = os.getcwd()

# # Specify the input and output file names
# input_file = os.path.join(current_dir, 'project_data.csv')
# output_file = os.path.join(current_dir, 'output.csv')

# # Define the items to search for in the 'siren' column
# search_items = ['340876721', '123456789',
#                 '987654321']  # Add the desired items here
# # Read the CSV file into a pandas DataFrame with custom column names
# data = pd.read_csv(input_file, header=None, names=['column1', 'column2', 'column3', 'column4', 'column5',
#                                                    'siren', 'date', 'column8', 'column9', 'column10'])

# # Create a new column 'funded' and set the default value as ''
# data['funded'] = ''

# # Iterate over each row in the DataFrame
# for index, row in data.iterrows():
#     siren_value = str(row['siren'])

#     # Check if the 'siren' value is in the search_items list
#     if siren_value in search_items:
#         
#         print(search_items)

# # Save the modified DataFrame to a new CSV file
# data.to_csv(output_file, index=False)
# print(f"New column 'funded' added to the CSV file: {output_file}")


# import os
# import pandas as pd

# # Define the list of values to search for in the 'siren' column
# search_items = ['834783359', '820511962', '951553940', '898793435', '822740577', '822740577', '822740577', '811472513', '878534585', '828983031', '814307625', '881291959', '812982478', '911452571',
#                 '891649436', '831797055', '881638555', '910679778', '830494662', '910631449', '497736256', '823648100', '901480145', '901480145', '901480145', '901480145', '528682198', '829156983', '820538007', '823741479']

# # Get the current working directory
# current_dir = os.getcwd()

# # Specify the input and output file names
# input_file = os.path.join(current_dir, 'final_data.csv')
# output_file = os.path.join(current_dir, 'test.csv')

# # Read the CSV file into a pandas DataFrame
# data = pd.read_csv(input_file)

# # Check if the 'siren' column exists in the DataFrame
# if 'Project Siren' in data.columns:
#     # Create a new column 'funded' and set the default value as ''
#     data['comment'] = ''

#     selected_rows = []
#     # Iterate over each row in the DataFrame
#     for index, row in data.iterrows():
#         siren_value = str(row['Project Siren'])

#         # Check if the 'siren' value is in the search_items list
#         if siren_value in search_items:
#             data.at[index, 'comment'] = ''
#             selected_rows.append(row)

#     # Save the modified DataFrame to a new CSV file
#     data.to_csv(output_file, index=False)
#     print(f"New column 'funded' added to the CSV file: {output_file}")

#     # Print the selected rows
#     print("Selected Rows:")
#     for row in selected_rows:
#         print(row)
# else:
#     print("Column 'Project Siren' does not exist in the CSV file.")

# import os
# import pandas as pd

# # Get the current working directory
# current_dir = os.getcwd()

# # Specify the input and output file names
# input_file = os.path.join(current_dir, 'final_data.csv')
# output_file = os.path.join(current_dir, 'test.csv')
# search_items_file = os.path.join(current_dir, 'collecting_sirens.csv')

# # Read the CSV file into a pandas DataFrame
# data = pd.read_csv(input_file)

# # Check if the 'Project Siren' column exists in the DataFrame
# if 'Project Siren' in data.columns:
#     # Create a new column 'comment' and set the default value as ''
#     data['comment'] = ''

#     # Read the search items from the file
#     search_items_df = pd.read_csv(search_items_file, header=None)

#     # Loop through each SIREN number
#     for row in search_items_df.itertuples(index=False):
#         for siren_value in row:
#             siren_value = str(siren_value).strip()
#             if siren_value:
#                 # Find the matching row in the DataFrame and update the 'comment' column
#                 mask = data['Project Siren'] == siren_value
#                 data.loc[mask, 'comment'] = 'collecting'

#     # Save the modified DataFrame to a new CSV file
#     data.to_csv(output_file, index=False)
#     print(f"New column 'comment' added to the CSV file: {output_file}")
# else:
#     print("Column 'Project Siren' does not exist in the CSV file.")


import os
import pandas as pd

# Get the current working directory
current_dir = os.getcwd()

# Specify the input and output file names
input_file = os.path.join(current_dir, 'finaltest.csv')
output_file = os.path.join(current_dir, 'finaltest.csv')
search_items_folder = os.path.join(current_dir, 'search_item')

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(input_file)

# Check if the 'Project Siren' column exists in the DataFrame
if 'Project Siren' in data.columns:
    # Create a new column 'comment' and set the default value as ''
    # data['comment'] = ''

    # Loop through each file in the search_items folder
    for filename in os.listdir(search_items_folder):
        search_items_file = os.path.join(search_items_folder, filename)

        # Read the search items from the file
        search_items_df = pd.read_csv(search_items_file, header=None)

        # Get the filename without extension as the comment text
        comment_text = os.path.splitext(filename)[0]

        # Loop through each SIREN number
        for row in search_items_df.itertuples(index=False):
            for siren_value in row:
                siren_value = str(siren_value).strip()
                if siren_value:
                    # Find the matching row in the DataFrame and update the 'comment' column
                    mask = data['Project Siren'] == siren_value
                    data.loc[mask, 'comment'] = comment_text

    # Save the modified DataFrame to a new CSV file
    data.to_csv(output_file, index=False)
    print(f"New column 'comment' added to the CSV file: {output_file}")
else:
    print("Column 'Project Siren' does not exist in the CSV file.")
