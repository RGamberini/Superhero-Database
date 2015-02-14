import requests
def requestUrl(scheme, url, path, **query):
    return scheme + "://" + url + "/" + path + "?" +\
    "&".join(["%s=%s" % (key, value) for (key, value) in query.items()])

scheme = "http"
url = "marvel.wikia.com"
path = "api/v1"
pathAdd = "Articles/List"
query = {"category":"Earth-616_Characters", "limit":"100"}
url = requestUrl(scheme, url, path + "/" + pathAdd, category="Earth-616_Characters", limit="100")
r = requests.get(url)
heros = r.json()['items']
print(heros)
for i in range(len(heros)):
    print(heros[i]['title'] + " " + str(heros[i]['id']))
