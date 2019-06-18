import discord
from discord.ext import commands
import time
import asyncio
import datetime as DT

heros = ("orbotp/.gitignore/heros")
client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild( 414142903649173534 )
    v_u = ["zoordax#7914"]
    channels = ["monstres"]
     
   

    if str (message.channel) in channels and str(message.author) in v_u:
        if message.content.find ("$hello") != -1:
            await message.channel.send ("hi")
        elif message.content == "$users":
            await message.channel.send (f"""# of Members: {id.member_count}, at {DT.datetime.now()}""")

    if str( message.channel ) in channels and str(message.author) in v_u:
        if message.content == "!monstres":
            embed = discord.Embed( title="**Monstre**" , description="Pour utiliser le bot taper : \n **!le_monstre**", color = 0xff1c21 )
            embed.add_field( name="***>>>***Tous les monstres***<<<***" , value="\n ailedegivre \nailesnoires\nbetedesneiges\nchaman\ndrider\nepinator\ngargantua\ngriffon\nfaucheuse\nmorphalange\ntroyen\nlarve\nnoceros\nreineabeille\nsabrecroc\ntitan\nwyrm" )
            await message.channel.send( content=None , embed=embed )


    if str( message.channel ) in channels and str(message.author) in v_u :
        if message.content.find ("!loutre") != -1:
            await message.channel.send("<@415175231565463552> koya est out !!!")

    if str( message.channel ) in channels :
        if message.content.find ("!golem") != -1:
            await message.channel.send(file=discord.File('heros/golem.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!wyrm") != -1:
            await message.channel.send(file=discord.File('heros/wyrm.jpg'))

    if str( message.channel ) in channels:
        if message.content.find( "!titan" ) != -1:
            await message.channel.send( file=discord.File( 'heros/titan.jpg' ) )


    if str( message.channel ) in channels :
        if message.content.find ("!sabrecroc") != -1:
            await message.channel.send(file=discord.File('heros/sabrecroc.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!reineabeille") != -1:
            await message.channel.send(file=discord.File('heros/abeille.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!noceros") != -1:
            await message.channel.send(file=discord.File('heros/noceros.jpg'))


    if str( message.channel ) in channels :
        if message.content.find ("!larve") != -1:
            await message.channel.send(file=discord.File('heros/larve.jpg'))


    if str( message.channel ) in channels :
        if message.content.find ("!troyen") != -1:
            await message.channel.send(file=discord.File('heros/troyen.jpg'))



    if str( message.channel ) in channels :
        if message.content.find ("!morphalange") != -1:
            await message.channel.send(file=discord.File('heros/morphalange.jpg'))


    if str( message.channel ) in channels :
        if message.content.find ("!morphalange") != -1:
            await message.channel.send(file=discord.File('heros/morphalange.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!betedesneiges") != -1:
            await message.channel.send(file=discord.File('heros/bneige.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!faucheuse") != -1:
            await message.channel.send(file=discord.File('heros/faucheuse.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!griffon") != -1:
            await message.channel.send(file=discord.File('heros/griffon.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!gargantua") != -1:
            await message.channel.send(file=discord.File('heros/gargantua.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!epinator") != -1:
            await message.channel.send(file=discord.File('heros/epinator.jpg'))


    if str( message.channel ) in channels :
        if message.content.find ("!drider") != -1:
            await message.channel.send(file=discord.File('heros/drider.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!ailedegivre") != -1:
            await message.channel.send(file=discord.File('heros/givre.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!ailenoires") != -1:
            await message.channel.send(file=discord.File('heros/Anoir.jpg'))

    if str( message.channel ) in channels :
        if message.content.find ("!chaman") != -1:
            await message.channel.send(file=discord.File('heros/chaman.jpg'))





client.run("NTYzNDMxNzc2MjI4MjEyNzU3.XQkGmw.K1hOqWcCx0M_PXrixFvx0PX6UOY")
