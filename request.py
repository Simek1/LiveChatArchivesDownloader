import requests



def list_archives(token, authorization_type = "Basic", page_id = ""):
    url = "https://api.livechatinc.com/v3.5/agent/action/list_archives"

    headers = {
        "Authorization": f"{authorization_type} {token}",
        "Content-Type": "application/json"
    }
    if page_id == "":
        data = {
            "limit": 100,
            "filters": {
                "event_types": {
                    "values": ["message", "filled_form"]
                }
            }
        }
    else: 
        data = {
            "page_id": page_id
        }
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)


