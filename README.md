# githublister
These scripts are made to orginize members/teams/repos in github.

Using githubs rest api - https://developer.github.com/v3/



$brew install python

$pip install virtualenv

$virtualenv venv

$source venv/bin/activate



Personal Acceess toknen needed for these scripts :  repo, admin:org, user



GET TEAMID 
curl -v -H "Authorization: token <GITHUB_TOKEN>" https://api.github.com/orgs/:org/teams?page=1 -H "Accept: application/vnd.github.hellcat-preview+json"


get-member.py - Get all the members in ORG
get-repos.py - Get all repos in ORG
add-user-to-team.py - Add users to specific team (Specify teamID and list of users)
add-repos-to-team.py - Add repos to team (Specify teamID and list of repos)
