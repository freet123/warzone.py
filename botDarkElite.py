#-----------------------------------------------------------------------------
#                                MODULE (ne pas toucher)
import discord
import json
import os
from discord import Game
from discord.ext.commands import *
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import random
from discord.utils import get
import traceback
from discord.ext.commands import has_permissions, MissingPermissions

#-----------------------------------------------------------------------------
#---------------------ne pas toucher à ce qui est haut------------------------

#              à rajouter pour personnaliser le bot:

prefix = "z!" #rajoute le prefix dedans  
TOKEN = "Njk0MjIzMzgwNDkyMzIwODMw.XoIgkA.NPyR_YnA98AAkDTcKPVme9N9reA" #rajoute le token du bot que tu as créer
status_du_bot = discord.Status.online #mettre après le '.' par: online / idle / dnd / invisible
type_activity = discord.ActivityType.watching #mettre après le '.' par unknow / playing / streaming / listening / watching
activity = f"les inscriptions" #rajouter le status(ex: (regarde) le clan)

#------------------ne plus toucher a ce qui est plus bas----------------------
#-----------------------------------------------------------------------------
#                             CODE (ne pas toucher)

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print(f'\n\nBot qui se connecte : {client.user.name} - {client.user.id}\nVersion de discord : {discord.__version__}\n')
    print(f'Connecté !')
    await client.change_presence(status=status_du_bot, activity=discord.Activity(type=type_activity, name = activity))


@client.command()
async def inscription(ctx, th):
    user = ctx.message.author

    #try:
    with open(f'{th}.json', 'r') as f:
        users = json.load(f)

    await update_role(ctx, user, th)

    if not 'name' in users:
        users = {}
        users['name'] = []
        users['name'].append(f'{user.name}')

    else:
        users['name'].append(f'{user.name}')

    #await update_bdd(ctx, users, user, th)

    with open(f'{th}.json', 'w') as f:
        json.dump(users, f, indent = 4)

    await ctx.send(f"<a:spinner:688661108793671691> Vous avez été inscrit a la liste des {th}")
    #except:
        #await ctx.send("Veuiller spécifier quelle th vous êtes: (th9 / th10 / th11 / th12/ th13 )")


@client.command()
async def desinscription(ctx, th):
    user = ctx.message.author

    with open(f'{th}.json', 'r') as f:
        users = json.load(f)

    try:
        users['name'].remove(f'{user.name}')
        await ctx.send("<a:spinner:688661108793671691> Opération réussie, vous avez été désinscrit avec succès")

        th9 = discord.utils.get(ctx.guild.roles, id = 690263753190670350)
        th10 = discord.utils.get(ctx.guild.roles, id = 678148096366215188)
        th11 = discord.utils.get(ctx.guild.roles, id = 678148133150130188)
        th12 = discord.utils.get(ctx.guild.roles, id = 678148051142967298)
        th13 = discord.utils.get(ctx.guild.roles, id = 678147849715843093)

        if th == "th9":
            await user.remove_roles(th9)
        elif th == "th10":
            await user.remove_roles(th10)
        elif th == "th11":
            await user.remove_roles(th11)
        elif th == "th12":
            await user.remove_roles(th12)
        elif th == "th13":
            await user.remove_roles(th13)
        



    except:
        await ctx.send(f"<a:spinner:688661108793671691> Vous n'êtes pas inscrit à la liste des {th}")

    with open(f'{th}.json', 'w') as f:
        json.dump(users, f, indent = 4)



async def update_role(ctx, user, th):

    th9 = discord.utils.get(ctx.guild.roles, id = 690263753190670350)
    th10 = discord.utils.get(ctx.guild.roles, id = 678148096366215188)
    th11 = discord.utils.get(ctx.guild.roles, id = 678148133150130188)
    th12 = discord.utils.get(ctx.guild.roles, id = 678148051142967298)
    th13 = discord.utils.get(ctx.guild.roles, id = 678147849715843093)


    if th == "th9":
        if th9 in user.roles:
            await ctx.send("<a:spinner:688661108793671691> Vous avez déja ce rôle")
        else:
            await user.add_roles(th9)
            await ctx.send("<a:spinner:688661108793671691> Vous posséder maintenant ce rôle")
    elif th == "th10":
        if th10 in user.roles:
            await ctx.send("<a:spinner:688661108793671691> Vous avez déja ce rôle")
        else:
            await user.add_roles(th10)
            await ctx.send("<a:spinner:688661108793671691> Vous posséder maintenant ce rôle")
    elif th == "th11":
        if th11 in user.roles:
            await ctx.send("<a:spinner:688661108793671691> Vous avez déja ce rôle")
        else:
            await user.add_roles(th11)
            await ctx.send("<a:spinner:688661108793671691> Vous posséder maintenant ce rôle")
    elif th == "th12":
        if th12 in user.roles:
            await ctx.send("<a:spinner:688661108793671691> Vous avez déja ce rôle")
        else:
            await user.add_roles(th12)
            await ctx.send("<a:spinner:688661108793671691> Vous posséder maintenant ce rôle")
    elif th == "th13":
        if th13 in user.roles:
            await ctx.send("<a:spinner:688661108793671691> Vous avez déja ce rôle")
        else:
            await user.add_roles(th13)
            await ctx.send("<a:spinner:688661108793671691> Vous posséder maintenant ce rôle")
    else:
        await ctx.send("<a:spinner:688661108793671691> Veuiller spécifier quelle th vous êtes: (th9 / th10 / th11 / th12/ th13 )")

async def update_bdd(ctx, users, user, th):
    user = user.name

    if not 'name' in users:
        users = {}
        users['name'] = []
        users['name'].append(f'{user}')

    else:
        users['name'].append(f'{user}')

    



@client.command()
async def see_list(ctx, th):


    with open(f'{th}.json', 'r') as f:
            users = json.load(f)

    await ctx.send(f"{users['name']}")




        


client.run(os.environ['DISCORD_TOKEN'])