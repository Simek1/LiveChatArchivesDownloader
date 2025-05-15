import axios from "https://cdn.skypack.dev/axios";

async function list_archives(token, authorizationType = "Basic", pageId = ""){
    const url = "https://api.livechatinc.com/v3.5/agent/action/list_archives";

    const headers = {
        headers: {
            "Authorization": `${authorizationType} ${token}`,
            "Content-Type": "application/json"
        }
    };
    let data;
    if (pageId == ""){
        data = {
            "limit": 10,
            "filters": {
                "event_types": {
                    "values": ["message", "filled_form"]
                }
            }
        };
    } else {
        data = {
            "page_id": pageId
        };
    }
    console.log(url)
    console.log(data)
    console.log(headers)
    const response = await axios.post(url, data, headers);

    return response;
};

async function requests(token, authorizationType = "Basic"){
    let exporting = true;
    let pageId = "";
    const blobParts = [];
    while (exporting){
        const response = await list_archives(token, authorizationType, pageId);
        if (response.status === 200){
            if ("next_page_id" in response.data){
                pageId = response.data.next_page_id;
            } else {
                exporting = false;
            }
            blobParts.push(JSON.stringify(response.data));
        }
    }
    console.log(blobParts)
};

/*
let r = await list_archives("");
console.log(r.data);
*/
/*
let r = await requests("")
console.log(r)
*/