import requests
import threading
import argparse
from art import tprint
from sys import argv

tprint(";-FUZZER-;")
print("                  Coded by: AhmedT1337 (twitter)\n\n")

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help = "Provide the url you want to fuzz on.")
parser.add_argument("-w", "--wordlist", help = "Provide the wordlist file you want to fuzz with.")
parser.add_argument("-m", "--method", help = "Provide the method you want (GET, POST, PUT, HEAD, OPTIONS).", default = "GET")

args = parser.parse_args()

wordlist = str(args.wordlist)
method = str(args.method).lower()

if ("https://" in args.url) or ("http://" in args.url) :
    pass
else :
    print("Please provide a url that starts with https:// or http://")
    exit()

if "FUZZ" in args.url : pass
else :
    print("Please put the word FUZZ in the place you want to fuzz on in the url")
    exit()


try : wordlist = open(wordlist, "r").read().splitlines()
except :
    print("Please provide a valid wordlist")
    exit()



def fuzz(url, word):
    url = str(url).replace("FUZZ", word)
    try :
        exec(f"response = requests.{method}('{url}', timeout = 1)")
        exec('print(f"{response.status_code}      {len(response.content)/1024:.2f}KB      {url}")')
    except :
        pass
        
def main() :
    threads_list = [threading.Thread(target=fuzz, args=(args.url, word)) for word in wordlist]
    
    # start the threads
    for thread in threads_list:
        thread.start()

    # wait for the threads to complete
    for thread in threads_list:
        thread.join()
    

if __name__ == '__main__' :
    main()
