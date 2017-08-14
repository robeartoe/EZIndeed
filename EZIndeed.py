#!/EZIndeed/bin/python

import requests

class EZIndeed(object):
    """docstring for EZIndeed."""
    def __init__(self, publisherID, limit=None):
        self.publisherID = publisherID
        if limit is None:
            self.limit = "10"
        self.limit = limit
        self.baseURL = "http://api.indeed.com/ads/"
        self.searchResults = None

    def search(self,keyword=None,location = 'US',countryCode = 'us'): #By DEFAULT location and countryCode is us. BUT it can be changed. Take note!
        SearchURL = self.baseURL + "/apisearch"
        r = requests.post(SearchURL,data = {'q':keyword,'l':location,'co':countryCode,'format':'json','v':'2','publisher':self.publisherID ,'limit': limit,  })
        # For all results in r:
        #   Create list, create JobListing for each result.
        #   Append to list, return list.


    def jobDetails(self,JobListing):
        jobkey = JobListing.jobkey
        JobDetailURL = self.baseURL + "/apigetjobs"
        r = request.post(JobDetailURL,data={'publisher':self.publisherID,'jobkeys':jobkey,'v':'2','format':'json'})
        return r

    def __repr__(self):
        return '<EZIndeed Object>'
    def __str__(self):
        return self.searchResults

class JobListing(object):
    def __init__(self,result):
        self.jobkey = jobkey
    def __repr__(self):
        return '<JobListing Object>'
    def __str__(self):
        return
