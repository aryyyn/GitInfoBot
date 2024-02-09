import requests
from discord.ext import commands
import discord



@commands.command(name='getgit', aliases=["gg"])
async def avatar(ctx, link):
    removefirst = link.split('.com/')[1]
    username = removefirst.split('/')[0]
    Repo = removefirst.split('/')[1]

    commit_history = get_commit_history(username, Repo)

    if commit_history:
        for commit in commit_history:
            print(commit['commit']['author']['name'], commit['commit']['message'])


def get_commit_history(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        return "Failed"





