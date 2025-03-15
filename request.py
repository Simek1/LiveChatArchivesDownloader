import requests



def list_archives(token, authorization_type = "Basic", page_id = ""): #single list_archives request, with limit of 100 chats
    url = "https://api.livechatinc.com/v3.5/agent/action/list_archives"

    headers = {                                                             #headers
        "Authorization": f"{authorization_type} {token}",
        "Content-Type": "application/json"
    }
    if page_id == "":
        data = {                                                            #request body, feel free to add there some filters
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

    return (response.status_code, response.json()) #function returns response status, and response



