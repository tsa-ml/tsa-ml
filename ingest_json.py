
from franz.openrdf.connect import ag_connect
import json
import os

def main(): 
    
    # connect to graph database
    pwd_ingest = "./ingestion/"
    json_ingest_file = [filename for filename in os.listdir(pwd_ingest) if filename.endswith('.json')]

    i = 0
    with ag_connect('surveydatacommons', host='localhost', port='10035',user='test', password='xyzzy', create = True) as conn:
        conn.openSession()
        for json_ingest in json_ingest_file:
            if i < 5:
                print("Processing ingest file: " + json_ingest)
                conn.addData(json.load(open(os.path.join(pwd_ingest, json_ingest), "r")), allow_external_references = True)
                i = i + 1
                conn.commit()
        conn.closeSession()

main()