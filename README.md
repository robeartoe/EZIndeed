EZIndeed
======

#### A simple Indeed.com wrapper that works with both python2 and python3. It'll be easy to find your next dream job, EZIndeed.

Usage:
------
EZIndeed has only two classes. EZIndeed and JobListing. You can search for jobs with EZIndeed, and you can either return a list of JobListing objects or the full unaltered json. When you return a list of JobListing objects, you can access it's attributes or full json, or you can look up more detail to that job with the jobDetails method.


``` python
from EZIndeed import EZIndeed
pubID = "xxxxxxxxxxxxxxx"

test = EZIndeed(pubID)

##search(Query=None,Location="US",Country="US",searchLimit= 5,full=False) Defaults
TestSearch = test.search("Python Web Dev Internship","Chicago,IL","US",3)

for job in TestSearch:
    print(job) #Prints full json result
    print(job.jobtitle)
    print(job.result)
    print(job.jobkey)
    print(job.company)
    print(job.snippet)
    print(job.RelativeTime)
    print(job.date)
    print(job.city)
    print(job.url)


for job in TestSearch:
    JobDetails = test.jobDetails(job)
    print(JobDetails) #Prints full json result
    print(JobDetails.jobtitle)
    print(JobDetails.result)
    print(JobDetails.jobkey)
    print(JobDetails.company)
    print(JobDetails.snippet)
    print(JobDetails.RelativeTime)
    print(JobDetails.date)
    print(JobDetails.city)
    print(job.url)

TestSearch = test.search("Python Web Dev Internship","Seattle,WA","US",3,full=True)

```

Instructions:
------
* Download Zip, unpack into your project.
* Install from requirements.txt
``` bash
pip install -r requirements.txt
```

* import to your project
``` python
from EZIndeed import EZIndeed
```
* Get Indeed Publisher ID from visiting [here](https://www.indeed.com/publisher).

That's all!

To find more help visit Indeeds API page, for more detailed info about locations, country codes, etc.

Support
-------

If you are having issues, please let me know.
Email Me at: robertruiz61296@gmail.com

License
-------

The project is licensed under the MIT license.
