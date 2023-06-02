import pywhatkit
import pyttsx3
import Main
import wikipedia
from pywikihow import WikiHow, search_wikihow
import os


def GoogleSearch(term):
    query = term.replace("adora", "")
    query = query.replace("what is", "")
    query = query.replace("how to", "")
    query = query.replace("  ", "")
    query = query.replace("what is mean by", "")
    writeab = str(query)

    ooo = open("Data.txt","w")
    ooo.write(writeab)
    ooo.close()

    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Main.Speak(how_to_func[0].summary)
    else:
        search = wikipedia.summary(Query, 2)
        Main.Speak(f": According to your search :{search}")

GoogleSearch("what is photosynthesis")