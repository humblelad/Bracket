#!/usr/bin/python3
import requests
import re

comments = "<\W*--.*?--\W*>"
#<!-- -->



def finder(f):

    for url in f:
        finds = []


        a = re.sub("\n|%0a", "", url)

        response = requests.get(a, allow_redirects=True)

        for comment in re.findall(comments, response.text):
            finds.append(comment)

        if len(finds) > 0:
            print("\n[+] " + str(response.status_code) + " " + url)
            for find in finds:

                if len(find) > 240:
                    print(find[:240])
                    print("[...]\n")
                else:
                    print(find)




def main():
    with open(arguments.file) as f:
        finder(f)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Bracket is a tool to find all html comments in a site  for a given url.')
    parser.add_argument('--file', '-f', action='store', dest='file', required=True)

    arguments = parser.parse_args()

    main()