#Standard imports
from ast import alias
import os, discord, random, sys, asyncio
from discord.ext import commands
from datetime import datetime, timedelta

import data.config as config

bot = commands.Bot(command_prefix=config.prefix)

#Command modules
import utils.utils as utils


#########################################
######### CHECKS ########################
#########################################

#Check if author is an admin
def _is_admin(ctx):
    return ctx.author.id == int(os.environ.get('ADMIN_ID'))

#########################################
######### EVENTS ########################
#########################################

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

    await utils.set_status(bot)

# @bot.event
# async def on_message(message):
#     pass

@bot.event
@bot.listen()
async def on_reaction_add(reaction,user):

    #Ignore bot's reaction add
    if user == bot.user:
        return

    msg = reaction.message
    embeds_reacted = msg.embeds
    emote = reaction.emoji

    #Quote message 
    if False and emote == '💬' and msg.guild.id == config.hobo_server:
        _quote_channel = msg.guild.get_channel(config.hobo_quote_chan)
        _embed = await utils.embed_quote(msg)
        await utils.send_embed(_embed, msg.channel)



#########################################
######### COMMANDS ######################
#########################################

@bot.command(name='bing')
async def _ping(ctx):
    await utils.send_message("bong", ctx.channel)



#########################################
######### IMPLICIT ######################
#########################################

@bot.event
async def on_message(msg):
    
    if msg.content == "erm...":
        await utils.send_message("he's right behind me, isn't he?", msg.channel)

#### ADMIN ONLY ####

@bot.command(name='exit')
@commands.check(_is_admin)
async def _exit(ctx):
    print("Exiting bot...")
    await bot.logout()


def main():
    bot.run(os.environ.get('TOKEN'))

if __name__ == "__main__":
    main()