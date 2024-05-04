#!/usr/bin/env python
# coding: utf-8


get_ipython().run_line_magic('env', 'GOOGLE_API_KEY=AIzaSyB3WX56Uk7po6i83hcdaG6xjs9trsjdubQ')


import pathlib
import textwrap
import time

import google.generativeai as genai


from IPython import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


try:
    # Used to securely store your API key
    from google.colab import userdata

    # Or use `os.getenv('API_KEY')` to fetch an environment variable.
    GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
except ImportError:
    import os
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)


import pandas as pd
import sys

csv_path = sys.argv[1]
df = pd.read_csv(csv_path)


print(df.head())  # Display the first few rows of the data frame



# Function to process each CVE and call Gemini for descriptions
def process_cve(cve_id):
  # The prompt for Gemini
  prompt = f"""## Vulnerability Details for CVE-{cve_id}

What is the description of the vulnerability CVE-{cve_id}?

## Attack Vectors
How can CVE-{cve_id} be exploited?

## Possible Attacks
What are some specific attacks that could leverage CVE-{cve_id}?

## Impact
What are the potential consequences of CVE-{cve_id} being exploited?

## Root Cause
What is the underlying cause of CVE-{cve_id}?

## Patch/Remediation
How can CVE-{cve_id} be fixed or mitigated?

## Severity Score
What is the overall base security score of CVE-{cve_id}?

## Threat Score Impact
How does the severity of CVE-{cve_id} affect the overall threat score (Very High, High, Medium, Low)?

## Possibility of Threat
How likely is it that CVE-{cve_id} will be exploited (Very High, High, Medium, Low)?

## Vulnerability of Asset
How critical is the asset that is vulnerable to CVE-{cve_id} (Very High, High, Medium, Low)?


"""

  # Use Gemini to generate text for each section of the prompt
  response = genai.generate_text(prompt=prompt)
  response_data = response.candidates[0]

  # Process the response and extract relevant information
  # (This part requires parsing the response text based on prompt structure)
  description = response_data['output'].split("\n\n**Description:**\n\n")[1].split("\n\n")[0]   # Extract description from response
  attack_vector = response_data['output'].split("\n\n**Attack Vectors:**\n\n")[1].split("\n\n")[0]
  possible_attack = response_data['output'].split("\n\n**Possible Attacks:**\n\n")[1].split("\n\n")[0]
  impact = response_data['output'].split("\n\n**Impact:**\n\n")[1].split("\n\n")[0]
  root_cause = response_data['output'].split("\n\n**Root Cause:**\n\n")[1].split("\n\n")[0]    
  patch = response_data['output'].split("\n\n**Patch/Remediation:**\n\n")[1].split("\n\n")[0]
  tsi = response_data['output'].split("\n\n**Threat Score Impact:**\n\n")[1].split("\n\n")[0]
  pt = response_data['output'].split("\n\n**Possibility of Threat:**\n\n")[1].split("\n\n")[0]
  va = response_data['output'].split("\n\n**Vulnerability of Asset:**\n\n")[1].split("\n\n")[0]
  sev_score = response_data['output'].split("\n\n**Severity Score:**\n\n")[1].split("\n\n")[0]
  

# Create a dictionary to store the information for this CVE
  cve_data = {
      "CVE ID": cve_id,
      "Description": description,
      "Attack Vector": attack_vector,
      "Possible Attacks": possible_attack,
      "Impact": impact,
      "Root Cause": root_cause,
      "Patch/Remediation": patch,
      "Threat Score Impact": tsi,
      "Possibility of Threat": pt,
      "Vulnerability of Asset": va,
      "Severity Score": sev_score
      
  }
  return cve_data


# Process each CVE in the DataFrame
cve_details = []

for index,row in df.head(5).iterrows():
  cve_id = row["vulnerability"]
  cve_data = process_cve(cve_id)
  cve_details.append(cve_data)



# Write data to a text file
with open("cve_report.txt", "w") as outfile:
  for cve_data in cve_details:
    # Add CVE ID in a simulated large font (using headers)
    outfile.write(f"#  CVE ID: {cve_data['CVE ID']}\n\n")
    # Add attributes and data with placeholders for different font sizes
    outfile.write(f"Description: {cve_data['Description']}\n\n")
    outfile.write(f"Severity Score: {cve_data['Severity Score']}\n\n\n")
    outfile.write(f"Attack Vectors: {cve_data['Attack Vector']}\n\n")
    outfile.write(f"Possible Attacks: {cve_data['Possible Attacks']}\n\n")
    outfile.write(f"Impact: {cve_data['Impact']}\n\n")
    outfile.write(f"Root Cause: {cve_data['Root Cause']}\n\n")
    outfile.write(f"Patch/Remediation: {cve_data['Patch/Remediation']}\n\n")
    outfile.write(f"Threat Score Impact: {cve_data['Threat Score Impact']}\n\n")
    outfile.write(f"Possibility of Threat: {cve_data['Possibility of Threat']}\n\n")
    outfile.write(f"Vulnerability of Asset: {cve_data['Vulnerability of Asset']}\n\n")


