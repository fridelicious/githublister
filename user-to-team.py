#!/usr/bin/env python3

import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--group', required=True, help="Group to add to")
parser.add_argument('--file', required=True, help="File to read users from")

ORG_URL = 'https://api.github.com'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_USER = os.environ.get('GITHUB_USER')

members = []


def main():
    args = parser.parse_args()

    member_file = args.file
    group = args.group
    if not os.path.exists(member_file):
        raise Exception("Could not find file {}".format(member_file))
    with open(member_file) as member_file_in:
        members = member_file_in.read().split()


    if not os.environ.get('GITHUB_TOKEN'):
        raise ValueError('You must set GITHUB_TOKEN')
    if not os.environ.get('GITHUB_USER'):
        raise ValueError('You must set GITHUB_TOKEN')

    print("Addings {} members to {}".format(len(members), group))
    group_exists = requests.get(ORG_URL+ '/teams/{}/members'.format(group), auth=(GITHUB_USER, GITHUB_TOKEN))
    group_exists.raise_for_status()
    for member in members:
        print("Adding {}".format(member))
        r = requests.put(ORG_URL+ '/teams/{}/members/{}'.format(group, member), auth=(GITHUB_USER, GITHUB_TOKEN))
        #For adding read/write access
        #r = requests.put(ORG_URL+ '/teams/{}/members/{}'.format(group, member),data='{"permission": "push"}', auth=(GITHUB_USER, GITHUB_TOKEN))
        if r.status_code == 422:
          pass
        else:
          r.raise_for_status()

main()
