# -*- coding: utf-8 -*-
#########################
#       FEEDMANAGER            
#########################


#########################
# IMPORTS               #
#########################
try:    import cPickle as pickle
except: import pickle



#########################
# DECLARATIONS          #
#########################
FILE_FEED = "save_feeds"
FILE_URL = "save_urls"

#########################
# FONCTIONS             #
#########################
def saveFeeds(feeds = []):
        """wait a dictionnarie of feed, and save them in FILE_FEED
        format key=>value is urlChannel=>urlLastFeed"""
        try: 
                file_feed = open(FILE_FEED, "w")
                pickle.dump(feeds, file_feed)
                file_feed.close()
        except: 
                print("The "+FILE_FEED+" not opened. No saving.")


def loadFeeds():
        """Loads feed since FILE_FEED, and return them"""
        feeds = {}
        try:    
                file_feed = open(FILE_FEED, "r")
                feeds = (pickle.load(file_feed))
                file_feed.close()
        except: 
                print("ERROR: the "+FILE_FEED+" not opened. No loading.")
        return feeds







def saveURLs(urls = []):
        """wait a list of url, and save them in FILE_URL"""
        try: 
                file_url = open(FILE_URL, "w")
                pickle.dump(urls, file_url)
                file_url.close()
        except: 
                print("The "+FILE_URL+" not opened. No saving.")


def loadURLs():
        """Loads url since FILE_URL, and return them in a list"""
        urls = []
        try:    
                file_url = open(FILE_URL, "r")
                urls = (pickle.load(file_url))
                file_url.close()
        except: 
                print("ERROR: the "+FILE_URL+" not opened. No loading.")

        return urls


