import json
from request import list_archives


def export_archive(token, token_type = "Basic", file_name = "exported_archives.json"): #function to export your whole archive
    with open(file_name, "w") as file: #file to which archive will be exported
        exporting = True
        page_id = ""
        while exporting:
            response = list_archives(token, token_type, page_id) #single API call
            if response[0] == 200:
                if "next_page_id" in response[1]: #if there is next page of response
                    page_id = response[1]["next_page_id"]
                else: #if there are no other pages of response
                    exporting = False
                json.dump(response[1], file, indent = 4)
                file.write("\n")
            else:
                print(f"API call has returned {response[0]} status")
                exporting = False
            return response[0] #status is returned to display status of request in gui

#if you're using the PAT authorization, then you need only to provide your token to the function, e.g. export_archive(your_token)