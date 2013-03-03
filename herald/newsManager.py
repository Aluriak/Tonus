# -*- coding: utf-8 -*-
#########################
#       NEWS MANAGER
#########################
# Note: use python 2 for feedparser

#########################
# IMPORTS               #
#########################
import feedManager
import feedparser



#########################
# DECLARATIONS          #
#########################
def getNews(urls = [], lastFeed = []):
        """Return list of (channelURL, feedNotRead). Wait list of URLs and ancient feeds"""
        # list à retourner
        returnList = []
        # feeds récupérés
        feeds = [] 

        # Récupération des flux
        # feed est une list de duets (url, feed de l'url)
        for url in urls:
                try:    feeds.append((url, feedparser.parse(url)))
                except: print("ERROR: \""+url+"\" don't give any feed.")

        #########################
        # FONCTIONS             #
        #########################
        # comparaison anciens/nouveaux 
        for feed in feeds:
                iterator = 0
                try: 
                        lastItem = feed[1]["items"][iterator]
                        # tant que le lien du feed ne correspond pas à celui lu la dernière fois
                        while lastItem["link"] != lastFeed.get(feed[0]):
                                # on ajoute l'item au prochain
                                returnList.append((feed[0], lastItem))
                                iterator += 1
                                lastItem = feed[1]["items"][iterator]
                except:
                        print("ERROR: reading of feed "+feed[0]+" have meet an error")
                        



        # sauvegarde des nouveaux items
        result = {}
        for feed in feeds:
                try:
                        lastItem = feed[1]["items"][0]
                        result[feed[0]] = lastItem["link"]
                except:         pass
        feedManager.saveFeeds(result)

        
        # return List
        return returnList



