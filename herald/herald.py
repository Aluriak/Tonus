# -*- coding: utf-8 -*-
#########################
#       HERALD            
#########################


#########################
# IMPORTS               #
#########################
# LOCAL MODULES
import newsManager
import feedManager


def printNews():
        """Print the news, with use of news and feed Managers"""
        # obtentions des listes d'URL
        urls = feedManager.loadURLs()
        # feeds récupérés au dernier appel
        lastFeeds = feedManager.loadFeeds()


        # obtention des dernières news
        toPrint = newsManager.getNews(urls, lastFeeds)

        # affichages
        actualFeed = ""
        for item in toPrint:
                if actualFeed != item[0]:
                        actualFeed = item[0]
                        print(item[0])
                print("\t"+item[1]["link"])
        if toPrint == []:
                print ("Pas de nouvelles.")



def addNewURL():
        """ask a new url to user, and add it to url list"""
        urls = feedManager.loadURLs()
        newURL = raw_input("new URL is ")
        urls.append(newURL)
        printNews()
        feedManager.saveURLs(urls)





if __name__ == "__main__":
        printNews()
        termine = False
        while not termine:
                print("a = add new url, n = print news again, q = quit")
                answer = raw_input("?>")
                if answer.lower() == "a":
                        addNewURL()
                elif answer.lower() == "n":
                        printNews()
                elif answer.lower() == "q":
                        termine = True



