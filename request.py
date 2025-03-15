import requests



def list_archives(token, authorization_type = "Basic"):
    url = "https://api.livechatinc.com/v3.5/agent/action/list_archives"

    headers = {
        "Authorization": f"{authorization_type} {token}",
        "Content-Type": "application/json"
    }
    data = {
        "limit": 100,
        "filters": {
            "event_types": {
                "values": ["message", "filled_form"]
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())



