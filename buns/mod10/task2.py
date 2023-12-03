import requests
import re


def get_headings(url):
    response = requests.get(url)
    response.raise_for_status()

    headings = re.findall(r'<h3.*?>(.*?)<\/h3>', response.text, re.DOTALL)
    headings = [re.sub(r'<.*?>', '', heading).strip() for heading in headings]

    return headings


print(get_headings("http://www.columbia.edu/~fdc/sample.html"))