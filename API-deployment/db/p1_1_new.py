from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3


def p0(param):
    print("----------p0 is started-------------")
    idl = []
    conn = sqlite3.connect("db/mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("""select * from scrapped""")
    df = pd.DataFrame(cursor.fetchall())
    texts = ["https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/new-real-estate-project-houses/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/new-real-estate-project-apartments/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/garage/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/office/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/business/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/industry/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/land/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/tenement/for-sale?countries=BE&page={}&orderBy=relevance",
             "https://www.immoweb.be/en/search/other/for-sale?countries=BE&page={}&orderBy=relevance"]
    pages = [333, 333, 33, 84, 80, 63, 164, 57, 281, 167, 6]
    if param == "full":
        try:
            for itxt in range(len(texts)):
                print(texts[itxt], " has ", pages[itxt], " pages")
                for a in range(pages[itxt]-1):
                    try:
                        link = texts[itxt].format(a+1)
                        print(a+1, ". page is processing")
                        response = requests.get(link)
                        text = str(BeautifulSoup(
                            response.content, 'lxml').find('iw-search'))
                        first = text.index("results-storage")
                        text = text[first:len(text)]
                        end = text.index("}]'")
                        try:
                            data = eval(text[18:end+1])
                            ids = [x["id"] for x in data]
                            for i in range(len(ids)):
                                if int(ids[i]) not in [int(x) for x in df[0]]:
                                    idl.append(ids[i])
                            pass
                        except:
                            pass
                        pass
                    except:
                        pass
            pass
        except:
            pass
    else:
        try:
            itxt = param
            print(texts[itxt], " has ", pages[itxt], " pages")
            for a in range(pages[itxt]-1):
                try:
                    link = texts[itxt].format(a+1)
                    print(a+1, ". page is processing")
                    response = requests.get(link)
                    text = str(BeautifulSoup(
                        response.content, 'lxml').find('iw-search'))
                    first = text.index("results-storage")
                    text = text[first:len(text)]
                    end = text.index("}]'")
                    try:
                        data = eval(text[18:end+1])
                        ids = [x["id"] for x in data]
                        for i in range(len(ids)):
                            if int(ids[i]) not in [int(x) for x in df[0]]:
                                idl.append(ids[i])
                        pass
                    except:
                        pass
                    pass
                except:
                    pass
            pass
        except:
            pass
    conn = sqlite3.connect("db/mydatabase.db")
    pd.DataFrame(index=idl).to_sql(name='news', con=conn, if_exists='replace')
    print("p1_1 ######", len(idl),
          "new records found and added to 'news' table ######")
    conn.close()
