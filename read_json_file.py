import json
from tqdm import tqdm
import sqlite3
import ast
import os

create_schema=False
if 'assignment3.db' not in os.listdir():
    create_schema=True
    
connection= sqlite3.connect('assignment3.db')

db= connection.cursor()  

# If database hasnt been created create the schema
if create_schema:
    db.execute('CREATE TABLE "Authors" ( "ID" VARCHAR(10), "FNAME" TEXT, "LNAME" TEXT )')
    db.execute('CREATE TABLE "Paper" ("ID"	VARCHAR(10) NOT NULL,"Title"	TEXT NOT NULL,"Submitter_firstname"	TEXT,"Submitter_lastname"	    TEXT,"LastUpdate"	TEXT,PRIMARY KEY("ID"))')
    db.execute('CREATE TABLE "Citations" ("ID"	VARCHAR(10),"CITE_ID"	VARCHAR(10))')
    db.execute('CREATE TABLE "Categorys" ("ID"	VARCHAR(10),"Category"	TEXT)')
    connection.commit()
    






# if you are writing csv file make sure to set encoding
with open('arXiv21.json', 'r', encoding="utf-8") as json_file:
    for line in tqdm(json_file):
        # data is a dictionary of attributes
        paper = json.loads(line)
        paper_id = paper['id']
        lst_author = paper['authors']
        #inserting categorys
        for category in paper['categories'].split():
            db.execute(f'INSERT INTO Categorys (ID,CATEGORY) VALUES(\'{paper_id}\',\'{category}\'  );')
            pass
            
    
        # Inserting authors
        for authors in lst_author:
            # Was getting exceptions when single quotes were present
            authors=authors.replace("'","")
            # For getting first and last names
            first_and_last=authors.split()
            #formatting a insert query for authors
            db.execute(f'INSERT INTO Authors (ID,FNAME,LNAME) VALUES(\'{paper_id}\',\'{first_and_last[-1]}\',\'{first_and_last[0]}\');')
            
        
        for citation in ast.literal_eval(paper['cited']):
            db.execute(f'INSERT INTO Citations (ID,Cite_ID) VALUES(\'{paper_id}\',\'{citation}\');')
        #Cleaned the strings
        title=paper['title'].replace("'","")
        submitter_first_and_last=paper["submitter"].replace("'","").split()
        submitter_fname=submitter_first_and_last[-1]
        submitter_lname=submitter_first_and_last[0]
        db.execute(f'INSERT INTO Paper (ID,Title,Submitter_firstname,Submitter_lastname,LastUpdate) VALUES(\'{paper_id}\',\'{title}\',\'{submitter_fname}\',\'{submitter_lname}\',\'{paper["last_update"]}\'  );')
        
#This commits all querys to the database file
connection.commit()