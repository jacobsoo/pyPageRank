import httplib, sys

prhost='toolbarqueries.google.com'
prpath='/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s'

# Banner
def Banner():
    print("=================================================")
    print("pyPageRank v0.1                                  ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <DomainName>") % (cmd)
    print("     : If no DomainName is supplied, it will query for Google.com\n")
    
# Function definitions
def GetHash (query):
    SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE. Yes, I'm talking to you, scammer."
    Result = 0x01020345
    for i in range(len(query)) :
        Result ^= ord(SEED[i%len(SEED)]) ^ ord(query[i])
        Result = Result >> 23 | Result << 9
        Result &= 0xffffffff 
    return("8%x" % Result)

def GetPageRank (query):
    conn = httplib.HTTPConnection(prhost)
    hash = GetHash(query)
    path = prpath % (hash,query)
    conn.request("GET", path)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

if __name__ == '__main__':
    Banner()
    if len(sys.argv)>1:
        site=sys.argv[1]
    else:
        help_menu(sys.argv[0])
        site='http://www.google.com'
    pr = GetPageRank(site)
    print("The page rank of %s is %s" % (site, pr))
