from wos import WosClient
import wos.utils
import os
from pathlib import Path

#Load creds-----------------------
from dotenv import load_dotenv
env_path = Path.home() / '.env'
load_dotenv(env_path)

with WosClient('nipun.arora@rutgers.edu.', 'Ontofollies0!') as client:
    print(wos.utils.query(client, 'AU=chomsky'))

from scholarly import scholarly
scholarly.search_pubs("agency"))


from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
from urllib.parse import quote_plus as url_encode
import json, pathlib
myCl = ElsClient(os.getenv("rut_els_api"))

doc_srch = ElsSearch("star trek vs star wars",'sciencedirect')
doc_srch.execute(myCl, get_all = False)
print ("doc_srch has", len(doc_srch.results), "results.")