import json
import urllib.request
from datetime import datetime

def fetch_reliefweb_headline():
    # UN ReliefWeb API endpoint for Middle East humanitarian reports
    url = "https://api.reliefweb.int/v1/reports?appname=theglobaltabloid&filter[field]=country.iso3&filter[value]=PSE&limit=1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data and 'data' in data and len(data['data']) > 0:
                return data['data'][0]['fields']['title']
    except Exception as e:
        print("API Fetch Error:", e)
    return "Palestine/Gaza Humanitarian Update"

def generate_json():
    latest_title = fetch_reliefweb_headline()
    
    output_data = {
        "last_updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "stats": {
            "gaza_killed": "61,700+",
            "syria_deaths": "500,000+",
            "sudan_killed": "150,000+",
            "total_displaced": "40M+",
            "active_conflicts": "11",
            "improving": "2"
        },
        "latest_headline": latest_title
    }

    with open("data.json", "w") as f:
        json.dump(output_data, f, indent=2)

if __name__ == "__main__":
    generate_json()
