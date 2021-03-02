#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : Cr4y0n
# @Software: PyCharm
# @Time    : 2020/10/29 15:14

import os
import requests
from random import choice, randint
from argparse import ArgumentParser

class BlogAC():
    def __init__(self):
        self.banner()
        self.args = self.parseArgs()
        self.init()
        self.loadURL()
        self.agentList = []
        self.xxfList = []
        self.refererList = []
        self.run()

    def banner(self):
        logo = r"""
 _     _               _      ___ 
| |__ | | ___   __ _  /_\    / __\
| '_ \| |/ _ \ / _` |//_\\  / /   
| |_) | | (_) | (_| /  _  \/ /___ 
|_.__/|_|\___/ \__, \_/ \_/\____/ 
               |___/              

    Author: Cr4y0n
    Version: V1.0
        """
        msg = "This is a blog access count script.\n"
        print("\033[91m" + logo + "\033[0m")
        print(msg)

    def init(self):
        print("Start init……")
        print("\nmethod:", self.args.method)
        print("timeout:", self.args.timeout)
        msg = ""
        if os.path.isfile("./url.txt"):
            msg += "Load url.txt successfully\n"
        else:
            msg += "\033[31mLoad url.txt Failed\033[0m\n"
        if self.args.randomAgent:
            if os.path.isfile("./userAgent.txt"):
                msg += "Load userAgent.txt successfully\n"
            else:
                msg += "\033[31mLoad userAgent.txt failed\033[0m\n"
        if self.args.randomXXF:
            if os.path.isfile("./XXF.txt"):
                msg += "Load XXF.txt successfully\n"
            else:
                msg += "\033[31mLoad XXF.txt failed\033[0m\n"
        if self.args.randomReferer:
            if os.path.isfile("./Referer.txt"):
                msg += "Load Referer.txt successfully\n"
            else:
                msg += "\033[31mLoad Referer.txt failed\033[0m\n"
        print(msg)
        if "failed" in msg:
            print("Init failed, Please check the environment.")
            os._exit(0)
        print("Init successfully")

    def parseArgs(self):
        parser = ArgumentParser()
        parser.add_argument("-c", "--count", required=True, type=int, help="access count")
        parser.add_argument("-m", "--method", required=False, default="get", choices=["get", "post"],  help="http method(get or post)")
        parser.add_argument("-t", "--timeout", required=False, type=int, default=3,  help="request timeout(default 3)")
        parser.add_argument("-d", "--data", required=False,  help="http request data")
        parser.add_argument("-rC", "--randomCount", required=False, type=int, default=0, help="random request count(random in [count-rC, count+rC])")
        parser.add_argument("-rA", "--randomAgent", required=False, action="store_true",help="random request User-Agent")
        parser.add_argument("-rX", "--randomXXF", required=False, action="store_true", help="random request X-Forwarded-For")
        parser.add_argument("-rR", "--randomReferer", required=False, action="store_true",help="random request Referer")
        parser.add_argument("-v", "--view", required=False, action="store_true", help="view details")
        return parser.parse_args()

    def readFile(self, file):
        resultList = []
        with open(file) as f:
            for line in f.readlines():
                resultList.append(line.strip())
        return resultList
    def loadURL(self):
        self.urlList = self.readFile("./url.txt")
    def loadRandomAgent(self):
        self.agentList = self.readFile("./userAgent.txt")
    def loadRandomXXF(self):
        self.xxfList = self.readFile("./XXF.txt")
    def loadRandomReferer(self):
        self.refererList = self.readFile("./Referer.txt")

    def createHeader(self):
        header = {}
        if self.args.randomAgent:
            self.loadRandomAgent()
            header["user-agent"] = choice(self.agentList)
        if self.args.randomXXF:
            self.loadRandomXXF()
            header["X-Forwarded-For"] = choice(self.xxfList)
        if self.args.randomReferer:
            self.loadRandomReferer()
            header["Referer"] = choice(self.refererList)
        return header

    def run(self):
        if not self.urlList:
            print("[-] Please check 'url.txt' file.")
            os._exit(0)
        for url in self.urlList:
            successCount = 0
            attemptCount = self.args.count + randint(0, self.args.randomCount)
            print("-" * 20, "\nURL：\033[32m%s\033[0m"% (url))
            for i in range(attemptCount):
                try:
                    if self.args.method == "post":
                        rep = requests.post(url=url, headers=self.createHeader(), timeout=self.args.timeout)
                    else:
                        rep = requests.get(url=url, headers=self.createHeader(), timeout=self.args.timeout)
                    if rep.status_code == 200:
                        successCount += 1
                        print("attempt：%d Success" %(i + 1))
                    else:
                        print("attempt：%d Error" % (i + 1))
                except:
                    print("attempt：%d Error" % (i + 1))
            print("\nattemptCount：\033[31m%d\033[0m   successCount：\033[32m%d\033[0m" %(attemptCount, successCount))

if __name__ == "__main__":
    BlogAC()
