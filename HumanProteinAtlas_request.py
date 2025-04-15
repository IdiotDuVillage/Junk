#!/bin/python
#Goal of this function is to retrieve datas from Human Protein Atlas
#More options are available on the doc through this link : 
# https://www.proteinatlas.org/about/help/dataaccess


import requests
import pandas as pd

def Search(string,name):
# Set up the Human Protein Atlas API endpoint for a search
    string.replace(" ","+")
    url = "https://www.proteinatlas.org/api/search_download.php"
    params = {
        "search": string,  # Replace with your gene or protein of interest
        "format": "json",
        "columns": "g,gs,eg,gd,up,chr,chrp,pc,upbp,secl",  
        "compress": "no",  # Switch to yes if you want gz-compressed results
    }

# Make the request to the Human Protein Atlas API
    response = requests.get(url, params=params)

# Check if the request was successful
    if response.status_code == 200:
        data = response.json()

    # Process the data as needed
        for entry in data:
            gene_symbol = entry.get("Gene")
            gene_symbol_synonym = entry.get("Gene synonym")
            Ensembl_ID = entry.get("Ensembl")
            Gene_description = entry.get("Gene description")
            Uniprot = entry.get("Uniprot")
            Chromosome = entry.get("Chromosome")
            Position = entry.get("Position")
            Protein_class = entry.get("Protein class")
            Biological_Process = entry.get("Biological process")
            Secretome_location =entry.get("Secretome location")
            Secretome_function = entry.get("Secretome function")
 # If needed, each details can be printed
 #           print(f"Gene Symbol: {gene_symbol}")
 #           print(f"Gene Symbol Synonym: {gene_symbol_synonym}")
 #           print(f"Gene description: {gene_description}")
 #           print(f"Uniprot : {Uniprot}")
 #           print(f"Chromosome : {Chromosome}")
 #           print(f"Position : {Position}")
 #           print(f"Protein class : {Protein_class}")
 #           print(f"Biological process : {Biological_Process}")
 #           print(f"Secretome location : {Secretome_location}")
 #           print(f"Secretome function : {Secretome_function}")
 #           print("\n")
    else:
        print(f"Error: {response.status_code}")

    return pd.DataFrame(data)
