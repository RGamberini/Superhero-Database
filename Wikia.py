import requests
class Wikia:
    def __init__(self, scheme, url, path):
        self.scheme = scheme
        self.url = url
        self.path = path

    def _generate_request_url(self, scheme, url, **query):
        return scheme + "://" + url + "/" + self.path + "?" +\
        "&".join(["%s=%s" % (key, value) for (key, value) in query.items()])

    def request(self, **query):
        return self._generate_request_url(self.scheme, self.url, **query)

    def request_json(self, **query):
        query = self._generate_request_url(self.scheme, self.url, **query)
        _request = requests.get(query)
        error = False
        print("Sent request {}\nReceived {} {}".format(query, _request.status_code, _request.headers['content-type']))
        if (_request.status_code != 200):
            print(r.text)
            error = True
        return _request.json(), error


class WikiaScraper:
    def __init__(self, wikia):
        self.wikia = wikia

    def get_category_members(self, cmtitle, cmlimit, cmcontinue=None):
        category_query = {"action":"query","list":"categorymembers","format":"json","cmtitle":cmtitle, "cmlimit":cmlimit}

        if (cmcontinue != None):
            category_query["cmcontinue"] = cmcontinue

        working_json, error = self.wikia.request_json(**category_query)
        #working_json = requests.get(self.wikia.request(**category_query)).json()

        # Grab the useful part out of the response
        raw_hero_data = working_json["query"]["categorymembers"]

        # Grab the continue string
        cmcontinue = working_json["query-continue"]["categorymembers"]["cmcontinue"]

        # Go through the json and pull the Title and pageid for each article
        articles = [(dictionary['title'],str(dictionary['pageid'])) for dictionary in raw_hero_data]

        return articles, cmcontinue

    def get_article_content(self, ids):
        article_query = {"action":"query", "prop":"revisions","rvprop":"content","format":"json","pageids":ids,"rvsection":"0"}
        working_json, error = self.wikia.request_json(**article_query)
        #working_json = requests.get(self.wikia.request(**article_query)).json()
        return working_json['query']['pages']
