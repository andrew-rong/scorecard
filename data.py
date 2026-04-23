from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv('api-key')

headers = {'Authorization': f'Bearer {api_key}'}

response = requests.get("https://api.stlouisfed.org/fred/v2/release/observations?release_id=52&format=json", 
                        headers=headers) 




response = requests.get(f"https://api.stlouisfed.org/fred/series?series_id=CPALTT01USM657N&api_key={api_key}&file_type=json")

print(response.content)