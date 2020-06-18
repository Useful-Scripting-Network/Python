import requests

def resolver(loc, verbose=False, hops=1):
    if(verbose): 
        print(f"{hops}: {loc}") 
        hops=hops+1
    url = requests.head(loc)
    url = url.headers["Location"]
    try:
        nexturl = resolver(url, verbose, hops)
        if nexturl == url:
            pass
        else:
            return nexturl
    except:
        return url


# If we are running the file directly, lets add some arguments for our script. 
if __name__ == "__main__":
    import argparse
    import re
    parser = argparse.ArgumentParser(description="Get the final location of a URL")
    parser.add_argument("-u", "--url", help="Enter the URL to expand", default="http://google.com")
    parser.add_argument("-v", "--verbose", action='store_true', help="Trace location verbosely to find the final URL", default=False)

    # gather arguments
    args = parser.parse_args()
    url = args.url
    verbose = args.verbose

    if re.match(r'http', url):
        print(resolver(url, verbose))
    else:
        print("Reformatting URL needs to begin with http/https")
        url = f"http://{url}"
        print(resolver(url, verbose))
