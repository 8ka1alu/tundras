import re
import sys
import discord
import random
import asyncio
import time
import json
import os
import traceback
import math
from discord.ext import tasks
from datetime import datetime, timedelta, timezone
from func import diceroll

client = discord.Client()

TOKEN = os.environ['DISCORD_BOT_TOKEN']

JST = timezone(timedelta(hours=+9), 'JST')

onch_id = 673229098180411395 #Bot起動ログチャンネルのID
logch_id = 673412099350855702 #参加退出ログチャンネルのID
great_owner_id = 459936557432963103
saver_owner_id = 682541929220800512
msg_count = 0

@client.event
async def on_ready():
    embed = discord.Embed(
        title = "起動ログ",
        description = f"**{client.user.name}**\n起動しました",
        color = random.choice((0,0x1abc9c,0x11806a,0x2ecc71,0x1f8b4c,0x3498db,0x206694,0x9b59b6,0x71368a,0xe91e63,0xad1457,0xf1c40f,0xc27c0e,0xe67e22,0x95a5a6,0x607d8b,0x979c9f,0x546e7a,0x7289da,0x99aab5))
    )
    embed.timestamp = datetime.now(JST)
    await client.get_channel(onch_id).send(embed=embed)
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('ノア起動')    
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='発言数：0'))

@client.event
async def on_member_join(member):
    guild = member.guild 
    member_count = sum(1 for member in guild.members if not member.bot)
    bot_count = sum(1 for member in guild.members if member.bot)
    logch = client.get_channel(logch_id)
    msg = [
        f"鳥だ！飛行機だ！いや{member.mention}",
        f"綺麗な月と{member.mention}ですね……",
        f"まぶしい朝には{member.mention}を一杯！うまい！",
        f"{member.mention}がご降臨なさった！崇め敬え奉れ！",
        f"にげろ！{member.mention}だ！",
        f"{member.mention}生きとったんかワレ！",
        f"うるせえ{member.mention}なげるぞ！",
        f"あ！{member.mention}だ！",
        f"予期されていたかのように{member.mention}が現れた……",
        f"野生の{member.mention}が現れた！",
        f"綺麗な夕日と{member.mention}に乾杯"
    ]
    embed = discord.Embed(
        title = "ようこそ！",
        description = random.choice(msg) + f"\n現在のメンバーは**{str(member_count)}**人です。\nBotは**{str(bot_count)}**個です。",
        color = random.choice((0,0x1abc9c,0x11806a,0x2ecc71,0x1f8b4c,0x3498db,0x206694,0x9b59b6,0x71368a,0xe91e63,0xad1457,0xf1c40f,0xc27c0e,0xe67e22,0x95a5a6,0x607d8b,0x979c9f,0x546e7a,0x7289da,0x99aab5))
    )
    embed.timestamp = datetime.now(JST) 
    await logch.send(embed=embed) 
    
@client.event
async def on_member_remove(member):
    guild = member.guild 
    member_count = sum(1 for member in guild.members if not member.bot)
    bot_count = sum(1 for member in guild.members if member.bot)
    logch = client.get_channel(logch_id)
    msg = [
        f"森へおかえり、{member.mention}",
        f"僕は全てを失った。金も、名誉も、{member.mention}も",
        f"だれだゴミ箱に{member.mention}を入れたのは",
        f"ねえマミー、僕の{member.mention}はどこー？",
        f"さようならっ{member.mention}！",
        f"{member.mention}\nあいつは良い奴だったよ",
        f"{member.mention}は星になったのさ"
    ]
    embed = discord.Embed(
        title = "さようなら(´;ω;｀)！",
        description = random.choice(msg) + f"\n現在のメンバーは**{str(member_count)}**人です。\nBotは**{str(bot_count)}**個です。",
        color = random.choice((0,0x1abc9c,0x11806a,0x2ecc71,0x1f8b4c,0x3498db,0x206694,0x9b59b6,0x71368a,0xe91e63,0xad1457,0xf1c40f,0xc27c0e,0xe67e22,0x95a5a6,0x607d8b,0x979c9f,0x546e7a,0x7289da,0x99aab5))
    )
    embed.timestamp = datetime.now(JST)  
    await logch.send(embed=embed) 
    
@client.event
async def on_message(message):
    if message.content == ("nsinfo"):
        guild = message.guild
        role = next(c for c in guild.roles if c.name == '@everyone')
        t_locked = 0
        v_locked = 0
        online = 0
        offline = 0
        idle = 0
        dnd = 0
        pin = 0
        if guild.mfa_level == 0:
            mfamsg = "メンバーに2要素認証を必要としていません"
        else:
            mfamsg = "メンバーに2要素認証を必要としています"
        if guild.premium_subscription_count == None:
            pmmc = "0"
        else:
            pmmc = guild.premium_subscription_count
        for member in guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.status == discord.Status.dnd:
                dnd += 1
        for channel in guild.text_channels:
            if channel.overwrites_for(role).read_messages is False:
                t_locked += 1
        for channel in guild.voice_channels:
            if channel.overwrites_for(role).connect is False:
                v_locked += 1
        total = online + offline + idle + dnd
        if total > 499:
            large = "大"
        elif total > 249:
            large = "中"
        else:
            large = "小"
        embed = discord.Embed(title=f"サーバー情報", color=0x2ECC69)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="‣サーバー名", value=f"**{guild.name}**", inline=False)
        embed.add_field(name="‣サーバーの説明", value=f"**{guild.description}**", inline=False)
        embed.add_field(name="‣サーバーID", value=f"**{guild.id}**")

        embed.add_field(name="‣サーバーの大きさ", value=f"**{large}**")
        embed.add_field(name="‣サーバー地域", value=f"**{guild.region}**")
        embed.add_field(name="‣サーバーの旗", value=f"**{guild.banner}**")
        embed.add_field(name="‣オーナー", value=f"||**{guild.owner.mention}**||", inline=False)
        embed.add_field(name="‣チャンネル数",
                        value=f"総合チャンネル数　:**{len(guild.text_channels) + len(guild.voice_channels)}個**(🔒×**{t_locked + v_locked}**)\nテキストチャンネル:**{len(guild.text_channels)}個**(🔒×**{t_locked}**)\nボイスチャンネル　:**{len(guild.voice_channels)}個**(🔒×**{v_locked}**)")
        embed.add_field(name="‣カテゴリー数", value=f"**全て:{len(guild.categories)}**")
        embed.add_field(name="‣役職数", value=f"**{len(guild.roles)}職**", inline=False)
        embed.add_field(name="‣メンバー数",
                        value=f"総メンバー:**{total}人**\nオンライン:**{online}人**\nオフライン:**{offline}人**\n退席中　　:**{idle}人**\n取り込み中:**{dnd}人**",
                        inline=False)
        embed.add_field(name="‣サーバーのブースト状態",
                        value=f"サーバーブーストレベル　:**Lv.{guild.premium_tier}**\nサーバーブーストユーザー:**{pmmc}人**", inline=False)
        embed.add_field(name="‣二段階認証", value=f"**{mfamsg}**", inline=False)
        embed.set_footer(text = datetime.now(JST))
        await message.channel.send(embed=embed)
     
    url_re = r"https://discordapp.com/channels/(\d{18})/(\d{18})/(\d{18})"
    url_list  = re.findall(url_re,message.content)
    
    for url in url_list:
        guild_id,channel_id,message_id = url
        channel = client.get_channel(int(channel_id))

        if channel is not None:
            got_message = await channel.fetch_message(message_id)

            if got_message is not None:
                await message.channel.send(embed=open_message(got_message))

    if message.author.bot:  # ボットを弾く。
        return

    if message.content.startswith("ndc"):
        # 入力された内容を受け取る
        say = message.content 

        # [idc ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('idc ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)

    if message.content == 'nrestart': 
        if message.author.id == great_owner_id:
            await message.channel.send('5秒後に再起動します')
            await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(name='再起動待機'))
            await asyncio.sleep(5)
            await client.logout()  
            os.execv(sys.executable,[sys.executable, os.path.join(sys.path[0], __file__)] + sys.argv[1:])  
        if not message.author.id == great_owner_id:
            await message.channel.send('貴方にこのコマンドの使用権限はありません')   

    if message.content == 'nclear': 
        if message.author.id == great_owner_id or message.author.id == saver_owner_id:
            await message.channel.purge()  
            await message.channel.send("ログを削除しました")
        if not message.author.id == great_owner_id:
            if not message.author.id == saver_owner_id:
                await message.channel.send('貴方にこのコマンドの使用権限はありません')   

    if 'おは' in message.content: #から始まるメッセージ
        #指定したチャンネルとメッセージを送ったチャンネルが同じIDなら実行
        if message.author.id == great_owner_id:
            await message.channel.send('おはようございます！開発者様！今日も一日頑張って下さい！')
        elif message.author.id == saver_owner_id:
            await message.channel.send('おはようございます！オーナーさん！今日も一日頑張って下さい！') 
        else:
            await message.channel.send(f"{message.author.mention} さん。おはようございます。") 

    if 'おやす' in message.content: #から始まるメッセージ
        #指定したチャンネルとメッセージを送ったチャンネルが同じIDなら実行
        if message.author.id == great_owner_id:
            await message.channel.send('おやすみなさい！開発者様！今日も一日お疲れさまでした！') 
        elif message.author.id == saver_owner_id:
            await message.channel.send('おやすみなさい！オーナーさん！今日も一日お疲れさまでした！') 
        else:
            await message.channel.send(f"{message.author.mention} さん。おやすみなさい。") 
 
    GLOBAL_CH_NAME = "破壊工房" # グローバルチャットのチャンネル名
    GLOBAL_WEBHOOK_NAME = "hakai-webhook" # グローバルチャットのWebhook名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する
        await message.delete()

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        for channel in global_channels:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)

            if webhook is None:
                await message.channel.webhook_create(name=GLOBAL_WEBHOOK_NAME)
                
            await webhook.send(content=message.content,
                username=message.author.name,
                avatar_url=message.author.avatar_url_as(format="png"))


    global msg_count
    if message.guild.id == 628566224460185630:
        return
    if not message.author.bot:
        msg_count += 1
        await client.change_presence(status=discord.Status.idle,activity=discord.Game(name=f'発言数：{msg_count}'))
    
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


