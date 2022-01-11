import scrapy

class jobScrapy(scrapy.Spider):
    name = "jobs"

    start_urls = [
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    ]

    def parse(self, response):
        comp_name = response.css("h3.joblist-comp-name::text").extract_first()
        key_skills = response.css("span.srp-skills").extract_first()

        yield {
            'Company Name': comp_name,
            'Key_Skills': key_skills
        }

        # //*[contains(concat( " ", @class, " " ), concat( " ", "list-job-dtl", " " ))]//li[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]