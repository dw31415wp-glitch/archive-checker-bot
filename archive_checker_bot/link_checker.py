import csv
from datetime import datetime
import re
from pathlib import Path
from typing import TypedDict


class LinkCheckResult(TypedDict):
    wayback_api_url: str
    wayback_url: str
    el_to_path: str
    page_title: str
    page_namespace: str
    el_to_domain_index: str

def load_csv():
    response = []
    csv_path = Path(__file__).resolve().parent.parent / "data" / "quarry-102912-untitled-run1079559.csv"
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            response.append(row)
    return response

def check_link(link) -> LinkCheckResult:
    path = link["el_to_path"]
    domain_index = link["el_to_domain_index"]
    domain_parts = domain_index.split("//")
    # reverse the domain part to get the domain
    # today.archive. to archive.today
    words = domain_parts[1].split(".")
    domain = ".".join(reversed(words[:2]))
    url = domain_parts[0] + "//" + domain + path
    # print(url)

    # extract url from path
    # match(/\/((?:\d{8,14}\/)?)(https?:\/\/.+)/);
    target_url = re.match(r"/((?:\d{8,14}\/)?)(https?:\/\/.+)", path)
    if target_url:
        #print(target_url.group(2))
        pass
    else:
        print("No match")

    # make wayback api url
    # http://archive.org/wayback/available?url=example.com
    wayback_url = f"http://archive.org/wayback/available?url={target_url.group(2)}"
    return {"wayback_api_url": wayback_url}

def check_wayback_api(link: LinkCheckResult):
    # make a request to the wayback api
    import requests

    response = requests.get(link["wayback_api_url"])
    if response.status_code == 200:
        data = response.json()
        if "archived_snapshots" in data and "closest" in data["archived_snapshots"]:
            closest = data["archived_snapshots"]["closest"]
            print(f"Archived URL: {closest['url']}")
            link["wayback_url"] = closest["url"]
        else:
            print("No archived snapshots found.")
    else:
        print(f"Error fetching Wayback API: {response.status_code}")

if __name__ == "__main__":
    links = load_csv()
    # write results to a new csv file
    # create time stamp for filename
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    results_path = Path(__file__).resolve().parent.parent / "data" / f"results_{timestamp}.csv"
    with results_path.open("w", newline="", encoding="utf-8") as file:
        fieldnames = ["page_title", "page_namespace", "wayback_api_url", "wayback_url", "el_to_domain_index",  "el_to_path"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for link in links:
            parsed = check_link(link)
            check_wayback_api(parsed)
            parsed.update({
                "el_to_path": link["el_to_path"],
                "page_title": link["page_title"],
                "page_namespace": link["page_namespace"],
                "el_to_domain_index": link["el_to_domain_index"],
            })
            if "wayback_url" in parsed:
                writer.writerow({
                    "wayback_api_url": parsed["wayback_api_url"],
                    "wayback_url": parsed["wayback_url"],
                    "el_to_path": link["el_to_path"],
                    "page_title": link["page_title"],
                    "page_namespace": link["page_namespace"],
                    "el_to_domain_index": link["el_to_domain_index"],
                })
                file.flush()
    #check_link()

