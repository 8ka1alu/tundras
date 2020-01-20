import discord 
import os
import asyncio
from discord.ext import tasks
from datetime import datetime
import re
import random
from func import diceroll

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID = 648435960077615127
great_owner_id = 459936557432963103
CHANNEL_ID3 = 664098210264121374
CHANNEL_ID_ALL = 668861946434682890

# 接続に必要なオブジェクトを生成
client = discord.Client()

#起動メッセージ
@client.event
async def on_ready():
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('Hello World,リマインドbotプログラム「project-RRN」、起動しました')
    channel = client.get_channel(CHANNEL_ID)
    await channel.purge()
    await channel.send(f'名前:{client.user.name}')  # ボットの名前
    await channel.send(f'ID:{client.user.id}')  # ボットのID
    await channel.send(f'Discord ver:{discord.__version__}')  # discord.pyのバージョン
    await channel.send('----------------')
    await channel.send('状態：BOT再起動しました。')   
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='創成の女神'))
    

@client.event
async def on_message(message):
    
    if 'Bumpを確認しました' in message.content:
        await message.channel.send('bumpを確認しました！2時間後お願いします！') 
        await asyncio.sleep(2*60*60)
        await message.channel.send('<@&650506130325372950> bumpチャンス！') 

    if message.author.bot:  # ボットを弾く。
        return 

    if message.content == 'ステータス':
        if message.author.guild_permissions.administrator:
            await message.channel.send(f'サーバー名：{message.guild.name}')
            await asyncio.sleep(0.1)
            await message.channel.send(f'現オーナー名：{message.guild.owner}')
            await asyncio.sleep(0.1)
            guild = message.guild
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            await message.channel.send(f'総人数：{all_count}人')
            await asyncio.sleep(0.1)
            await message.channel.send(f'ユーザ数：{member_count}')
            await asyncio.sleep(0.1)
            await message.channel.send(f'BOT数：{bot_count}')
            await asyncio.sleep(0.1) 
            await message.channel.send(f'総チャンネル数：{len(message.guild.channels)}個')
            await asyncio.sleep(0.1)
            await message.channel.send(f'テキストチャンネル数：{len(message.guild.text_channels)}個')
            await asyncio.sleep(0.1)
            await message.channel.send(f'ボイスチャンネル数：{len(message.guild.voice_channels)}個')
            await asyncio.sleep(0.1)
            embed = discord.Embed(title="サーバーアイコン")
            embed.set_image(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
        if not message.author.guild_permissions.administrator:
            await message.channel.send('貴方は管理者権限がありません。 \n You do not have admin roles !!')

    if message.content == 'ステータスE':
        if message.author.guild_permissions.administrator:
            embed = discord.Embed(title="この鯖のステータス",description="Embed式")
            embed.add_field(name="サーバー名",value=f'{message.guild.name}',inline=False)
            embed.add_field(name="現オーナー名",value=f'{message.guild.owner}',inline=False)
            guild = message.guild
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            embed.add_field(name="総人数",value=f'{all_count}',inline=False)
            embed.add_field(name="ユーザ数",value=f'{member_count}',inline=False)
            embed.add_field(name="BOT数",value=f'{bot_count}',inline=False)
            all_channel = len(message.guild.text_channels) + len(message.guild.voice_channels)
            embed.add_field(name="総チャンネル数",value= all_channel + '個',inline=False)
            embed.add_field(name="テキストチャンネル数",value=f'{len(message.guild.text_channels)}個',inline=False)
            embed.add_field(name="ボイスチャンネル数",value=f'{len(message.guild.voice_channels)}個',inline=False)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)

        if not message.author.guild_permissions.administrator:
            await message.channel.send('貴方は管理者権限がありません。 \n You do not have admin roles !!')

        #年月日
    if message.content.startswith('何日？') or message.content == '何日?':
        date = datetime.now()
        await message.channel.send(f'今日は{date.year}年{date.month}月{date.day}日です！')    
    if message.content.startswith('何時？') or message.content == '何時?':
        date = datetime.now()
        await message.channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')

    if message.content == 'nrestart': 
        if message.author.id == great_owner_id:
            await message.channel.send('再起動します')
            await asyncio.sleep(0.5)
            await client.logout()  
            os.execv(sys.executable,[sys.executable, os.path.join(sys.path[0], __file__)] + sys.argv[1:])  
        if not message.author.id == great_owner_id:
            await message.channel.send('貴方にこのコマンドの使用権限はありません')   

    if message.content == 'nclear': 
        if message.author.id == great_owner_id:
            await message.channel.purge()  
        if not message.author.id == great_owner_id:
            await message.channel.send('貴方にこのコマンドの使用権限はありません')   

    if not message.author.id == 664880378481213473:
        prob = random.random()
    
        if prob < 0.05:
            if not message.content.startswith("スロット"): 
                await message.add_reaction('💝')

    if message.content.startswith("スロット"): 
        suroto=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
        suroto1=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
        suroto2=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
        await asyncio.sleep(0.1)
        my_message = await message.channel.send('スロット結果がここに表示されます！')
        await asyncio.sleep(3)
        await my_message.edit(content='？|？|？')
        await asyncio.sleep(1)
        await my_message.edit(content=suroto + '|？|？')
        await asyncio.sleep(1)
        await my_message.edit(content=suroto + '|' + suroto1 + '|？')
        await asyncio.sleep(1)
        await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2)
        if suroto == suroto1 == suroto2:
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：大当たり！！')
        elif suroto == suroto1 or suroto == suroto2 or suroto1 == suroto2:
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：リーチ！')
        else:
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：ハズレ')
        
    if message.content.startswith("!dc"):
        # 入力された内容を受け取る
        say = message.content 

        # [!dc ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('!dc ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)
     
    if message.content == 'coin sn1' or message.content == 'coin sn2':
        if message.author.id == great_owner_id:
            coin=random.choice(('●', '○'))
            if message.content == 'coin sn1':
                my_message = await message.channel.send('コイントスをします！')
                await asyncio.sleep(3)
                await my_message.edit(content='定義：○は表、●は裏')
                await asyncio.sleep(3)
                await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：　```定義：○は表、●は裏```')
                await asyncio.sleep(2)
                await my_message.edit(content='　結果：' + coin + '```定義：○は表、●は裏 \n adid:sn1```')
                return
            elif message.content == 'coin sn2':
                my_message = await message.channel.send('コイントスをします！')
                await asyncio.sleep(3)
                await my_message.edit(content='定義：●は表、○は裏')
                await asyncio.sleep(3)
                await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
                await asyncio.sleep(0.5)
                await my_message.edit(content='抽選中：　```定義：●は表、○は裏```')
                await asyncio.sleep(2)
                await my_message.edit(content='　結果：'+ coin + '```定義：●は表、○は裏 \n adid:sn2```')
                return
        await message.channel.send('Error:You cannot use this command')  
        return

    if message.content == 'coin':
        coin=random.choice(('●', '○'))
        coin1=random.choice(('1', '2'))
        await asyncio.sleep(0.1)
        if coin1 == '1':
            my_message = await message.channel.send('コイントスをします！')
            await asyncio.sleep(3)
            await my_message.edit(content='定義：○は表、●は裏')
            await asyncio.sleep(3)
            await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：○は表、●は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：　```定義：○は表、●は裏```')
            await asyncio.sleep(2)
            await my_message.edit(content='　結果：' + coin + '```定義：○は表、●は裏 \n adid:sn' + coin1 + '```')
            
            return
        elif coin1 == '2':
            my_message = await message.channel.send('コイントスをします！')
            await asyncio.sleep(3)
            await my_message.edit(content='定義：●は表、○は裏')
            await asyncio.sleep(3)
            await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：○```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：●```定義：●は表、○は裏```')
            await asyncio.sleep(0.5)
            await my_message.edit(content='抽選中：　```定義：●は表、○は裏```')
            await asyncio.sleep(2)
            await my_message.edit(content='　結果：'+ coin + '```定義：●は表、○は裏 \n adid:sn' + coin1 + '```')
            
            return
        await message.channel.send('Error')

    if message.content == "!help":
        page_count = 0 #ヘルプの現在表示しているページ数
        page_content_list = ["ヘルプコマンドです。\n➡絵文字を押すと次のページへ",
            "ヘルプコマンド2ページ目です。\n➡絵文字で次のページ\n⬅絵文字で前のページ",
            "ヘルプコマンド最後のページです。\n⬅絵文字で前のページ"] #ヘルプの各ページ内容
        
        send_message = await message.channel.send(page_content_list[0]) #最初のページ投稿
        await send_message.add_reaction("➡")

        def help_react_check(reaction,user):
            '''
            ヘルプに対する、ヘルプリクエスト者本人からのリアクションかをチェックする
            '''
            emoji = str(reaction.emoji)
            if reaction.message.id != send_message.id:
                return 0
            if emoji == "➡" or emoji == "⬅":
                if user != message.author:
                    return 0
                else:
                    return 1

        while not client.is_closed():
            try:
                reaction,user = await client.wait_for('reaction_add',check=help_react_check,timeout=40.0)
            except asyncio.TimeoutError:
                return #時間制限が来たら、それ以降は処理しない
            else:
                emoji = str(reaction.emoji)
                if emoji == "➡" and page_count < 2:
                    page_count += 1
                if emoji == "⬅" and page_count > 0:
                    page_count -= 1

                await send_message.clear_reactions() #事前に消去する
                await send_message.edit(content=page_content_list[page_count])

                if page_count == 0:
                    await send_message.add_reaction("➡")
                elif page_count == 1:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 2:
                    await send_message.add_reaction("⬅")
                    #各ページごとに必要なリアクション

@client.event
async def on_member_join(member):
    await client.get_channel(CHANNEL_ID_ALL).purge()
    embed = discord.Embed(title="この鯖のステータス",description="Embed式")
    embed.add_field(name="サーバー名",value=f'{message.guild.name}',inline=False)
    embed.add_field(name="現オーナー名",value=f'{message.guild.owner}',inline=False)
    guild = message.guild
    member_count = sum(1 for member in guild.members if not member.bot) 
    bot_count = sum(1 for member in guild.members if member.bot) 
    all_count = (member_count) + (bot_count)
    embed.add_field(name="総人数",value=f'{all_count}',inline=False)
    embed.add_field(name="ユーザ数",value=f'{member_count}',inline=False)
    embed.add_field(name="BOT数",value=f'{bot_count}',inline=False)
    await client.get_channel(CHANNEL_ID_ALL).send(embed=embed)

#リムーブメッセージ
@client.event
async def on_member_remove(member):
    await client.get_channel(CHANNEL_ID_ALL).purge()
    embed = discord.Embed(title="この鯖のステータス",description="Embed式")
    embed.add_field(name="サーバー名",value=f'{message.guild.name}',inline=False)
    embed.add_field(name="現オーナー名",value=f'{message.guild.owner}',inline=False)
    guild = message.guild
    member_count = sum(1 for member in guild.members if not member.bot) 
    bot_count = sum(1 for member in guild.members if member.bot) 
    all_count = (member_count) + (bot_count)
    embed.add_field(name="総人数",value=f'{all_count}',inline=False)
    embed.add_field(name="ユーザ数",value=f'{member_count}',inline=False)
    embed.add_field(name="BOT数",value=f'{bot_count}',inline=False)
    await client.get_channel(CHANNEL_ID_ALL).send(embed=embed)


client.run(TOKEN)

#ノア
#グローバルチャット
