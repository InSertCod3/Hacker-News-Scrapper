from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests


class Scraper ():
    def __init__(self, traing_data):
        self.cl = NaiveBayesClassifier(traing_data)

    def classifier(self, data):
        return self.cl.classify(data)

    def fetch_data(self):
        BASEURL = "https://news.ycombinator.com/news?p="
        for n in range(1):
            r = requests.get(BASEURL + str(n))
            soup = BeautifulSoup(r.content, "html.parser")
            for title in soup.findAll('tr', {'class': 'athing'}):  # Fetch Title
                for t in title.findAll('a', text=True):
                    art_title = t.text.encode("utf8")
                    art_link = t['href']
                    print (self.classifier(art_title), art_title)

# Trainging Data (More Data For Accuracy)
pos_t_data = [
    ('this is a very funny movie!', 'pos'),
    ('RoboVM is winding down', 'pos'),
    ('New effort to study astronomical signal after almost 40 years.', 'pos'),
    ('Cheap Docker images with Nix.', 'pos'),
    ("How and why to make your software faster", 'pos')
]

neg_t_data = [
    ("CDC map quietly confirms the Haitian cholera epidemic started by UN peacekeepers.", "neg"),
    ("Microsoft Sues Justice Department Over Secret Customer Data Searches.", "neg"),
    ("He Got Greedy: How the U.S. Government Hunted Encryption Programmer Paul Le Roux", "neg"),
    ("36,000 Verizon workers go on strike", "neg"),
    ("The other kind of JavaScript fatigue", "neg")]

if __name__ == "__main__":
    s = Scraper(traing_data=pos_t_data + neg_t_data)
    s.fetch_data()
