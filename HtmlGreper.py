#!/usr/bin/python3
import argparse
import os
import sys
import requests
import subprocess

class HtmlGreper:
    # Initializing Some Variables.
    def __init__(self):
        self.dirlist = []
        self.dirnames = []
        self.greplist = []
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    def createdir(self):
        # Creates a Directory To Save HTML Source Code Files.
        try:
            htmldir = os.path.join(os.getcwd(),"Htmlfiles")
            if not os.path.exists(htmldir):
                os.mkdir(htmldir)
            os.chdir(htmldir)
        except Exception as e:
            # Handling Errors While Creating Directory.
            print("Some Error Occured While Creating Htmlfiles Directory...")
            print(e)
            sys.exit(1)

    def getdirlist(self,dirfile):
        # Creating Web Dirs List using File Provided by User.
        try:
            with open(dirfile,"r+") as fp:
                templist = fp.readlines()
                templist2 = [i.strip() for i in templist if i]
                for i in templist2:
                    if i:
                        self.dirlist.append(i)
        except Exception as e:
            # Handling Exception While Creating Web Dirs List.
            print(f"Some Error Occured {e}")
            sys.exit(1)

    def getdirnames(self):
        # Simple function to change Web Dirs Names To Use As File Names.
        # Creating New List of The Changed Web Dirs Names To File Names.
        try:
            for k in self.dirlist:
                self.dirnames.append(k.replace("://", "_").replace(".", "_").replace("/", "_").replace("?", "_"))
        except:
            pass

    def gethtmlsource(self):
        # Main Function To Fetch HTML Source Code From Web using List We Created Above.
        print("Starting Collecting Html Source")
        print("~" * 50)
        # Loop For both Web dir Links and Their related File Names(To Save If We get HTML from Them).
        for i,j in zip(self.dirlist,self.dirnames):
            self.get = requests.get(i,headers=self.headers,timeout=5)
            if self.get.status_code == 200:
                text = self.get.text
                with open(j,"w") as f:
                    f.write(text)
                print(f"Got For : {i}")
            else:
                print(f"\nSome Error Occured:- {i}")
                print(f"Status Code For Error = {self.get.status_code}\n")
                continue
        print("~" *50)
        print("Finished Collecting Html Source")

    def Searchkeyword(self,keyword,ignorecase=False):
        # Main Keyword Searching Function To Search KeyWord in Collected HTML Source Files.
        # Searching In Current Directory if used together with HTML Fetching Function.
        if self.args.dirfile:
            # Running Loop Through List of HTML Source Files To Grep Keyword(Using Subprocess).
            for i,j in zip(self.dirnames,self.dirlist):
                try:
                    if ignorecase:
                        output = subprocess.run(["grep","-i",keyword,i],capture_output=True,text=True)
                        if output.returncode == 0:
                            self.greplist.append(j)
                    else:
                        output = subprocess.run(["grep", keyword, i], capture_output=True, text=True)
                        if output.returncode == 0:
                            self.greplist.append(j)
                except:
                    continue
            # Printing Output if Found Any Results.
            if self.greplist:
                print("-" * 50)
                print("These Directories Contains the Given Keyword\n")
                for i in self.greplist:
                    print(i)
                print("-" * 50)
            else:
                print("Nothing Found")
        # Searching By Going In Already Fetched HTML Source Files Directory.
        else:
            # Changing Directory and Creating New List of Files Inside There.
            os.chdir(os.path.join(os.getcwd(),"Htmlfiles"))
            lsout = subprocess.run(["ls","-1"],capture_output=True,text=True)
            newdirlist = [files for files in lsout.stdout.split("\n") if files]
            # Running Loop to Get List Of Files Containing Given Keyword.
            for i in newdirlist:
                try:
                    if ignorecase:
                        output = subprocess.run(["grep","-i",keyword,i],capture_output=True,text=True)
                        if output.returncode == 0:
                            self.greplist.append(i)
                    else:
                        output = subprocess.run(["grep", keyword, i], capture_output=True, text=True)
                        if output.returncode == 0:
                            self.greplist.append(i)
                except:
                    continue
            # Printing Output if Found any Results.
            if self.greplist:
                print("-" *50)
                print("These Files Contains the Given Keyword\n")
                for i in self.greplist:
                    print(i)
                print("-" * 50)
            else:
                print("Nothing Found")

    def arguments(self):
        # ArgsParse Function To Create Parser Object And Create Arguments.
        self.parser = argparse.ArgumentParser(description="Html searcher for Emails and Flags...",
                                         usage="%(prog)s -f [Filename]",
                                         epilog="""
                                         Example:
                                                %(prog)s -f dirlist.txt -a
                                         """,)
        self.parser.add_argument("-f","--file",
                            metavar='',
                            dest="dirfile",
                            help="input Directory List File")
        self.parser.add_argument("-g","--grep",
                            help="Search Given Keyword",
                            dest="grep",
                            metavar='')
        self.parser.add_argument("-i", "--ignorecase",
                                 help="ignore case sensitivity while searching",
                                 dest="ignore",
                                 action="store_true")
        self.args = self.parser.parse_args()

    def argscheck(self):
        # Checking Arguments Provided By User And Running Functions Accordingly.
        if len(sys.argv) == 1:
            self.parser.print_help()
            sys.exit(1)
        else:
            if self.args.dirfile:
                self.getdirlist(self.args.dirfile)
                self.getdirnames()
                self.createdir()
                self.gethtmlsource()
            if self.args.grep:
                if self.args.ignore:
                    self.Searchkeyword(self.args.grep,ignorecase=True)
                else:
                    self.Searchkeyword(self.args.grep)
            else:
                sys.exit(1)

if __name__=='__main__':
    obj = HtmlGreper()
    obj.arguments()
    obj.argscheck()