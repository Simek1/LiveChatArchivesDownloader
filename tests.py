import os
from dotenv import load_dotenv
from request import list_archives

load_dotenv()

token = os.getenv("TOKEN64")

list_archives(token)