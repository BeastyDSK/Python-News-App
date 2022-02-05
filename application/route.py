from sqlite3 import Date
from flask import render_template
from application.newsApi import getNewsData
from application import app


def modifyData(articles):
    """
    Modifies the incoming article data.
        1) Changes the date to DD-MMM-YYYY format
        2) Reduces the description to 180 letters
        3) Removes the record that dont have image element. 
    """
    art = []
    for i in range(0,len(articles)):
        if 'image' in articles[i].keys():
            date = articles[i]["datePublished"][0:10]
            date = date.split("-")
            date = Date(int(date[0]),int(date[1]),int(date[2]))
            articles[i]["datePublished"] = date.strftime("%d-%b-%Y")
            articles[i]["description"] = str(articles[i]["description"])[0:180] + "...."
            art.append(articles[i])
    return art

@app.route("/")
def home():
    """
    This is just a basic route to root html file.
    """
    return render_template("index.html",title="Coffee Time | Real Time News App",articles= modifyData(getNewsData()))


@app.route("/search=<topic>")
def search(topic=None):
    """
    This is like an API. For the given search result it will provide html based object. So no need to create the html elements in JS.
    """
    text = ""
    if topic != None:
        articles = modifyData(getNewsData(topic))
        for article in articles:
            text += f"""<article class="news-card">
                    <div class="heading">
                        <img
                            class="heading-img"
                            src="{ article['image']['thumbnail']['contentUrl'] }&w=1280&960&p=0"
                            alt="{ article['name'] }"
                        />
                        <h1 class="heading-text">{ article['name'] }</h1>
                    </div>
                    <div class="content flex-cont-vh">
                        <p class="content-date">
                            Date : { article['datePublished'] }
                        </p>
                        <p class="content-description">
                            { article['description'] }
                        </p>
                        <a
                            href="{ article['url'] }"
                            target="_blank"
                            class="readmore"
                            rel="noreferrer"
                            >Read More</a
                        >
                    </div>
                </article>\n"""
    return text