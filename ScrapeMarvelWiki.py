from Wikia import Wikia, WikiaScraper
from Database import Database
import mwparserfromhell
import sqlite3
import os.path
import time

def get_from_template(template, toget):
    try:
        return template.get(toget)
    except ValueError:
        return ""

def format_template_string(template_string):
    if template_string != "":
        return template_string[template_string.find("=") + 1:].strip()
    else:
        return template_string

def pull_hero_info(template, toget):
    return [format_template_string(get_from_template(template, thing_to_get)) for thing_to_get in toget]

# Create a new scraper for marvel wikia
marvel = WikiaScraper(Wikia("http", "marvel.wikia.com", "api.php"))

# These are the tags to pull from the character template
_format = ("Alignment", "Gender", "Height", "Weight", "Identity", "MaritalStatus", "Eyes", "Hair", "PlaceOfBirth", "PlaceOfDeath","Citizenship","Occupation")

# Database creation
filename = "heros.db"
# Database is a wrapper over a sqlite3 connection
database = Database(filename)

# Check if the file already exists
if os.path.isfile("cmcontinue"):
    # If it does pick up where we left off
    with open("cmcontinue") as continuefile:
        _continue = continuefile.readline()

    articles, _continue = marvel.get_category_members("Category:Earth-616_Characters", 50, _continue)
else:
    # Else create a database and start scraping
    database.create_table("Heros", zip(("Title", "ID") + _format, ("text", "text UNIQUE") + tuple(["text" for i in range(len(_format))])))

    articles, _continue = marvel.get_category_members("Category:Earth-616_Characters", 51)

while True:
#for i in range(1):
    ids = "|".join([str(article[1]) for article in articles])

    articles = marvel.get_article_content(ids)
    duplicates = False

    for i, article in enumerate(articles.values()):
        wikitext = article['revisions'][0]['*']
        templates = mwparserfromhell.parse(wikitext).filter_templates()

        # Some characters pages are completely blank but if they aren't the first template
        # is the Character Template
        if len(templates) > 0:
            character_template = templates[0]
        else: break;
        character_template = pull_hero_info(character_template, _format)
        article['title'] = article['title'].replace(" (Earth-616)", "")

        try:
            database.insert("Heros", (article['title'], article['pageid']) + tuple(character_template))
        except sqlite3.IntegrityError:
            if not duplicates:
                print("{} with ID {} is a duplicate".format(article['title'], article['pageid']), end="")
            else:
                print(" {} {}".format(article['title'], article['pageid']),end="")

    database.commit()
    time.sleep(1)
    articles, _continue = marvel.get_category_members("Category:Earth-616_Characters", 51, _continue)

continuefile = open("cmcontinue", 'w')
continuefile.write(_continue)
continuefile.close()
