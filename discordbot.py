import discord 
import os

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
    print('Hello World,投票botプログラム、起動しました')
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='投票受付'))#状態をidle　投票受付をプレイ中

@client.event
async def on_message(message):
    if message.author.bot:  # ボットを弾く。
        return 

#投票開始
    if message.content == '投票開始':
        await



client.run(TOKEN)
