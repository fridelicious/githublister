#!/usr/bin/env python3

import requests
import os

# Basic setup
ORG_URL = 'https://api.github.com/orgs/:org/repos'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_USER = os.environ.get('GITHUB_USER')


# Generator for looping through the paged github results
def get_repos():
    has_next_page = True
    page = 1
    while has_next_page:
        r = requests.get('{}?page={}&visibility=public'.format(ORG_URL, page), auth=(GITHUB_USER, GITHUB_TOKEN))
        r.raise_for_status()
        links = r.headers['link'].split(',')
        has_next_page = any(
            [l.find('next') >= 0 for l in links]
        )
        yield r.json()
        page = page + 1

"""
The main function, here we check a few values then loop
over the results returned from the github api.
"""
def main():
    if not os.environ.get('GITHUB_TOKEN'):
        raise ValueError('You must set GITHUB_TOKEN')
    if not os.environ.get('GITHUB_USER'):
        raise ValueError('You must set GITHUB_TOKEN')
    for repo_list in get_repos():
        for repo in repo_list:
            print(repo['name'])


main()
