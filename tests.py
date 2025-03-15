import os
from dotenv import load_dotenv
from request import list_archives
from export_archive import export_archive

load_dotenv()

token = os.getenv("TOKEN64")

list_archives(token)

test1 = list_archives(token)
print(test1[0])

export_archive(token)