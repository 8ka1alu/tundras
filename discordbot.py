import discord 
import os
import asyncio
import re
import random

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

#サーバー・チャンネルID
sayas = 654239524016357377
saya_wc = 654239524016357380
tests = 683613604645175308
test_wc = 683613604645175311

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
    member_count = len(set(bot.get_all_members()))
    if member.guild.id == sayas:
        await client.get_channel(saya_wc).send(f"<@{member.id}>さんいらっしゃい！")
    elif member.guild.id == tests:
        await client.get_channel(test_wc).send(f"<@{member.id}>さんいらっしゃい！\n" + member_count)

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

def open_message(message):
    """
    メッセージを展開し、作成した埋め込みに各情報を添付し返す関数
    Args:
        message (discord.Message) : 展開したいメッセージ
    Returns:
        embed (discord.Embed) : メッセージの展開結果の埋め込み
    """
    color_code = random.choice((0,0x1abc9c,0x11806a,0x2ecc71,0x1f8b4c,0x3498db,0x206694,0x9b59b6,0x71368a,0xe91e63,0xad1457,0xf1c40f,0xc27c0e,0xe67e22,0x95a5a6,0x607d8b,0x979c9f,0x546e7a,0x7289da,0x99aab5))
    embed = discord.Embed(title=message.content,description=f"[メッセージリンク]({message.jump_url})",color=color_code)

    embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url) #メッセージ送信者
    embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url) #メッセージのあるサーバー
    embed.timestamp = message.created_at #メッセージの投稿時間

    if message.attachments:
        embed.set_image(url=message.attachments[0].url) #もし画像があれば、最初の画像を添付する
    return embed

client.run(TOKEN)
