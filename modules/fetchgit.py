import requests
from discord.ext import commands
import discord



@commands.command(name='getgit', aliases=["gg"])
async def getgit(ctx, link):
    try:
        removefirst = link.split('.com/')[1]
        username = removefirst.split('/')[0]
        Repo = removefirst.split('/')[1]


        commit_history = get_commit_history(username, Repo)
        if commit_history:
            loading = await ctx.send("Loading....")
            commit_messages = ""
            for commit in commit_history:
                commit_messages += f"Author: {commit['commit']['author']['name']}:Commit Message: {commit['commit']['message']}\n"
                print(commit['commit']['author']['date'])
            await loading.delete()
            count = len(commit_messages)
            await ctx.send(f"```{commit_messages}\nCount:{count}```")

    except Exception as err:
        print(err)
        await ctx.send("something went wrong")


def get_commit_history(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        print(commits)
        return commits
    else:
        return "Failed"





