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
emoji_list = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟️']
    if message.content.startswith("投票開始 "):
        vote_list = message.content[len("投票開始 "):].split()
        vote_title = vote_list.pop(0)
        result_str = "投票がはじまりました！\n「" + vote_title + "」\n\n選択肢：\n"
        vote_list_count = []
        for i in range(len(vote_list)):
            result_str = result_str + str(i) + "：" + vote_list[i] + "\n"
            vote_list_count.append(0)
        m = await message.channel.send(result_str)
        for i in range(len(vote_list)):
            await m.add_reaction(emoji_list[i])
            
@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = await client.fetch_user(payload.user_id)

    # 投票以外なら処理しない
    if not ("投票がはじまりました" in message.content):
        return

    # 投票の選択肢の数だけループ
    for r in message.reactions:

        # 今押した絵文字以外なら
        if str(payload.emoji) != str(r.emoji):

            # ユーザーが重複していたら減らす
            async for u in r.users():
                if user.id == u.id:
                    await message.remove_reaction(r.emoji, user)

client.run(TOKEN)
