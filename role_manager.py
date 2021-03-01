#discord.py を読み込む
import discord

#自分のBotのアクセストークンを入力してください
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
		
	# Botにメンションが送られたかどうかの判定
    if client.user in message.mentions:
        member = message.author # 送信者の情報
        order = message.content.split() # コマンドを空白で分割
		
        if order[1] == 'add': # addコマンド
            role_ = discord.utils.get(message.guild.roles, name=order[2]) # order[2]のロールの情報を取得
            if role_ is not None:
                await member.add_roles(role_) # ロール追加
                await message.channel.send(member.display_name+"に"+role_.name+"を追加しました")
            else:
                await message.channel.send("入力が間違っています")

        elif order[1] == 'remove': # removeコマンド
            role_ = discord.utils.get(message.guild.roles, name=order[2]) # order[2]のロールの情報を取得
            if role_ is not None:
                await member.remove_roles(role_) # ロール削除
                await message.channel.send(member.display_name+"から"+role_.name+"を削除しました")
            else:
                await message.channel.send("入力が間違っています)

        elif order[1] == 'show': # showコマンド
            await message.channel.send(message.author.roles)
		
        else:
            await message.channel.send("そのコマンドはありません")


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
