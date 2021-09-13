import requests, os, discord,json
from discord.ext import commands
from bs4 import BeautifulSoup
from utils import fetch_urls
import urllib3
http = urllib3.PoolManager()
client = discord.Client()


GUILDID = '867327192470781957'
IDTOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJkMzU5Y2I0Yi1iNGRmLTRhYTgtOGQ0NS0xNmFmNzg3YWU5YTYiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTY0NjI1NTk4NywiaWF0IjoxNjMwNDg1OTg3LCJlbWFpbCI6InBvbGJhb3V3ZXQzQGdtYWlsLmNvbSJ9.4KCuOyP21zawRxY7e59zU6-cpKHYO93kye-_96Q4Ht_NTTanV-bsXHLo-QBGyhdgYN9MdmWHDi9Or_uYS_z1g-lehawGmbVUc0O6f7z2YDAOJPqOlUlk2yTV7CSoIuu4vg3kfgBDcSIBI8u9WghAGoPH4BexMnUnSauQD-ayNqCjJpQe8q_LuaWCaTLaFn9wUPOncy74tK6ZBXrl-SV8tcGsB8sXBOeXXTO66H28wFJEXas7vsHQFLx6RVbszBYs0FII0U_pyMOsREqGRrrfxAQXZ_2UpCFbhJO9PIIPLkFzBXjgsu42JYRZsVuJ3eQ7DQoQ3JSStut2_EK3SvTNYg"
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"




@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILDID:
            break
    
    print(
        f'{client.user} is connected to the following guild :\n'
        f'{guild.name}(id: {guild.id})'
    )



@client.event
async  def on_message(message):
	urls = fetch_urls(message.content)
	for url in urls:
		if "https://www.chegg.com/homework-help/"  in url:
			await message.reply( f'{message.author.mention} \n  Extracting your answer pls wait')
			page =http.request('GET', url,

			headers={'User-Agent':USERAGENT ,
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Referer': url,
    'Connection': 'keep-alive',
    'Cookie': IDTOKEN,
    'Upgrade-Insecure-Requests': '1',
    'If-None-Match': '"26fd3-EKpH9vUiB7dNGZfVLRVy9BM+Gog"',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'})
			pageContent = str(page.data.decode("utf-8"))
			soup = BeautifulSoup(pageContent.replace('"//', '"https://'),"html.parser")
			file = open('ans.html', 'w')
			file.write(pageContent)
			file.close()
			url = "https://siasky.net/skynet/skyfile"
			payload={}

			files = [
				('file', ("Ans.html", open('./ans.html', 'rb'), 'text/html'))
			]
			headers7 = {
				'referrer': 'https://siasky.net/'
			}
			response = requests.request("POST", url, headers=headers7, data=payload, files=files)
			print(response.text)
			linkup = "https://siasky.net/" + response.json()["skylink"]
			my_files = [discord.File('ans.html')]
			await message.reply( f'{message.author.mention} \n your requested answer : '+ linkup)

client.run("ODg2OTU2MDY2ODcxNTg2ODg2.YT9INQ.DHCJB4DK4WFS1aUlb4ErS_Jw6Zk")
