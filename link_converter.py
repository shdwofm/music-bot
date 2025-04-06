import requests
from typing import Optional

def get_alt_link(original_url: str, target_platform: str) -> Optional[str]:
    try:
        response = requests.get(
            "https://api.song.link/v1-alpha.1/links",
            params={"url": original_url}
        )

        print(f"[DEBUG] Odesli Status Code: {response.status_code}")
        data = response.json()
        print(f"[DEBUG] Full Response:\n{data}")

        links_by_platform = data.get("linksByPlatform", {})

        if target_platform in links_by_platform:
            return links_by_platform[target_platform].get("url")

    except Exception as e:
        print(f"Ошибка при обращении к Odesli: {e}")

    return None
