# -*- coding: utf-8 -*-
#########################
#       HERALD            
#########################


#########################
# IMPORTS               #
#########################
# STD MODULES
import threading
import thread
# LOCAL MODULES
import newsManager
import feedManager


class Herald(threading.Thread):
        """Thread where work Herald, of Tonus AI"""

        ########################### INIT ######################################
        def __init__(self):
                threading.Thread.__init__(self)


        ########################### RUN ######################################
        def run(self):
                """Manage Herald"""
                self.printNews()
                termine = False
                while not termine:
                        print("a = add new url, n = print news again, q = quit")
                        answer = raw_input("?>")
                        if answer.lower() == "a":
                                self.addNewURL()
                        elif answer.lower() == "n":
                                self.printNews()
                        elif answer.lower() == "q":
                                termine = True


        ########################### PRINT NEWS ######################################
        def printNews(self):
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



        ########################### ADD NEW URL ######################################
        def addNewURL(self):
                """ask a new url to user, and add it to url list"""
                urls = feedManager.loadURLs()
                newURL = raw_input("new URL is ")
                urls.append(newURL)
                printNews()
                feedManager.saveURLs(urls)





if __name__ == "__main__":
        Herald = Herald() # start herald

