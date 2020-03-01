import discord 
import os
import asyncio

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#起動メッセージ
@client.event
async def on_ready():
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('Hello World,インスニウム、起動しました')
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='インスニウム'))#状態をidle　投票受付をプレイ中

@client.event
async def on_member_join(member):
    await message.channel.send(f"{member}さんいらっしゃい！")

@client.event
async def on_message(message):

    url_re = r"https://discordapp.com/channels/(\d{18})/(\d{18})/(\d{18})"
    url_list  = re.findall(url_re,message.content)
    
    for url in url_list:
        guild_id,channel_id,message_id = url
        channel = client.get_channel(int(channel_id))

        if channel is not None:
            got_message = await channel.fetch_message(message_id)

            if got_message is not None:
                await message.channel.send(embed=open_message(got_message))
 
client.run(token)
