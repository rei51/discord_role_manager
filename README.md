# discord_role_manager

Discordでロールを管理するBotのコードです．
TOKENには自身で作成したDiscordBotのトークンを入力してください．
Botを操作する前にBotに付与されているロールの権限を操作したいロールよりも上位にしてください．

実装したコマンドは3種類です．
例：Botの名前がmanager ，ロールの名前がrole1とすると
  @manager add role1 #メンションの送信者のロールに'role1'を追加します．
  @manager remove role1 #メンションの送信者のロールから'role1'を削除します．
  @manager show #送信者のロールを削除します．

24時間365日稼働させたい場合はHerokuなどを利用してください．
