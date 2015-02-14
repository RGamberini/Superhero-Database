import requests
import mwparserfromhell

def requestUrl(scheme, url, path, **query):
    return scheme + "://" + url + "/" + path + "?" +\
    "&".join(["%s=%s" % (key, value) for (key, value) in query.items()])

scheme = "http"
url = "marvel.wikia.com"
path = "api/v1"
pathAdd = "Articles/List"
query = {"category":"Earth-616_Characters", "limit":"100"}
r = requests.get(requestUrl(scheme, url, path + "/" + pathAdd, category="Earth-616_Characters", limit="100"))
heros = r.json()['items']
ids = ""
for i in range(len(heros)):
    ids += str(heros[i]['id']) + "|"
ids = ids[:len(ids)-1]
path = "api.php"
query = {"action":"query", "prop":"revisions","rvprop":"content","format":"json","pageids":ids,"rvsection":"0"}
r = requests.get(requestUrl(scheme, url, path, **query))
print(requestUrl(scheme, url, path, **query))
print(len(r.json()['query']['pages'].items()))
for key, value in r.json()['query']['pages'].items():
    wikitext = value['revisions'][0]['*']
    wikicode = mwparserfromhell.parse(wikitext)
    templates = wikicode.filter_templates()
    try:
        alignment = templates[0].get("Alignment")
    except ValueError:
        alignment = "None"

    try:
        gender = templates[0].get("Gender")
    except ValueError:
        gender = "None"
    print(alignment.strip(),": ", gender.strip())
