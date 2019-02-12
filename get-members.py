#!/usr/bin/env python3

import requests
import os

# Basic setup
ORG_URL = 'https://api.github.com/orgs/:org/teams/:teamid/members/:user'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_USER = os.environ.get('GITHUB_USER')


# Generator for looping through the paged github results
def get_members():
    has_next_page = True
    page = 1
    while has_next_page:
        r = requests.get('{}?page={}'.format(ORG_URL, page), auth=(GITHUB_USER, GITHUB_TOKEN))
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
    for member_list in get_members():
        for member in member_list:
            """
            A basic exapmle of what can be done with the user object.
            A user looks like this:
            {
                'avatar_url': 'https://avatars0.githubusercontent.com/u/XXX',
                'events_url': 'https://api.github.com/users/XXX/events{/privacy}',
                'followers_url': 'https://api.github.com/users/XXX/followers',
                'following_url': 'https://api.github.com/users/XXX/following{/other_user}',
                 gists_url': 'https://api.github.com/users/XXX/gists{/gist_id}',
                'gravatar_id': '',
                'html_url': 'https://github.com/XXX',
                'id': 1234567,
                'login': 'XXX',
                'node_id': 'RANDOMSTUFF',
                'organizations_url': 'https://api.github.com/users/XXX/orgs',
                'received_events_url': 'https://api.github.com/users/XXX/received_events',
                'repos_url': 'https://api.github.com/users/XXX/repos',
                'site_admin': False,
                'starred_url': 'https://api.github.com/users/XXX/starred{/owner}{/repo}',
                'subscriptions_url': 'https://api.github.com/users/XXX/subscriptions',
                'type': 'User',
                'url': 'https://api.github.com/users/XXX'
            }
            We will get print the 'login' key, which is the users username.
           """
            print(member.get('login'))


main()
