import requests
from pathlib import Path


def download_files_to_local(url: str, file_destination: Path) -> bool:
    try:
        response = requests.get(url)
        response.raise_for_status()  

        file_destination.parent.mkdir(parents=True, exist_ok=True)
        file_destination.write_bytes(response.content)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False