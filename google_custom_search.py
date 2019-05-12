import json, requests, sys, logging

# api key
API_KEY = "API KEY HERE"
# custom search ID
CX_RPGTIPS = "CUSTOM SEARCH ID HERE"
# custom search api URL
URL = 'https://www.googleapis.com/customsearch/v1'

def main(argv):
    logging.basicConfig(filename='google_custom_search.log', level=logging.DEBUG)
    logging.info('Started')
    logging.debug("argv=%s" % argv)
    query = "QUERY STRING HERE"

    headers = {
        "Content-Type": "application/json",
        "Referer" : "http://source.domain/"
    }
    params = {
        "key": API_KEY,
        "cx": CX_RPGTIPS,
        "q": query,
        "prettyPrint": "true"
    }
    response = requests.get(URL, headers = headers, params = params)
    response.raise_for_status()
    #logging.debug("response.text=%s" % response.text)
    results = json.loads(response.text)
    if (results.get('queries').get('nextpage') != 'None'):
        print("queries.nextpage=%s" % results.get('queries').get('nextpage'))
    for item in results.get('items'):
        print(item.get('title'), item.get('link'))
    logging.info('Finished')

main(sys.argv)