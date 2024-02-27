import requests
from typing import Dict, Any, List


def get_deezer_album_info(deezer_id: str) -> Dict[str, Any]:
    """
    Retrieve album information from the Deezer API.

    Args:
        deezer_id (str): The ID of the album on Deezer.

    Returns:
        dict: A dictionary containing the extracted album information.
    """
    url = f"https://deezerdevs-deezer.p.rapidapi.com/album/{deezer_id}"
    headers = {
        "X-RapidAPI-Key": "[key]",  # Replace with your key
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        extracted_data = {
            "cover": data.get("cover_medium", ""),
            "contributors": [contributor.get("name", "") for contributor in data.get("contributors", [])],
            "label": data.get("label", ""),
            "tracklist": [track.get("title", "") for track in data.get("tracks", {}).get("data", [])]
        }
        return extracted_data
    else:
        print("Failed to retrieve data from the API:", response.status_code)
