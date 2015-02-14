import requests
import mwparserfromhell
from Wikia import Wikia

def get_from_template(template, toget):
    try:
        return template.get(toget)
    except ValueError:
        return "Missing"

def format_template_string(template_string):
    if template_string != "Missing":
        return template_string[template_string.find("=") + 1:].strip()
    else:
        return template_string

def pull_hero_info(template, toget):
    return [format_template_string(get_from_template(template, thing_to_get)) for thing_to_get in toget]


# Wikia holds some of our information for us to make things easier
marvel = Wikia("http", "marvel.wikia.com", "api.php")

# Generate the query here we're asking for a list of category members from the category "Earth-616_Characters"
category_query = {"action":"query","list":"categorymembers","format":"json","cmtitle":"Category:Earth-616_Characters"}#, "cmlimit":"100"}

# Generate the request in the Wikia object specifying we want to use our "api" api
# and passing the query we just made. Then in turn pass that request to our getter
# and convert it to json
working_json = requests.get(marvel.request(**category_query)).json()

# Grab the useful part out of the response
raw_hero_data = working_json["query"]["categorymembers"]

# Grab the continue string
cmcontinue = working_json["query-continue"]["categorymembers"]["cmcontinue"]

# Go through the json and pull the Title and pageid for each article
articles = [(dictionary['title'],str(dictionary['pageid'])) for dictionary in raw_hero_data]

# Now iterate through the ids in articles and generate a string to append onto our next request
ids = "|".join([str(article[1]) for article in articles])

# Specify our next query, this time we want the content from all the articles from the response
article_query = {"action":"query", "prop":"revisions","rvprop":"content","format":"json","pageids":ids,"rvsection":"0"}
working_json = requests.get(marvel.request(**article_query)).json()
raw_hero_data = working_json['query']['pages']

for i, hero in enumerate(raw_hero_data.values()):
    wikitext = hero['revisions'][0]['*']
    templates = mwparserfromhell.parse(wikitext).filter_templates()

    hero_info = templates[0]
    hero_info = pull_hero_info(hero_info, ("Alignment", "Gender", "Height", "Weight", "MaritalStatus", "Eyes", "Hair", "PlaceOfBirth"))
    print(hero['title'].replace("(Earth-616)", "").strip(), hero_info)
