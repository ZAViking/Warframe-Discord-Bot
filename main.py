import discord
from discord.ext import commands
import os
import random
#from replit import db
#import warframe
from keep_alive import keep_alive
from melee import melee_ready
from primary import primary_ready
from secondary import secondary_ready
from warframe import warframe_ready

client = commands.Bot(command_prefix = ".")

#  embed=discord.Embed(title="Text", description="Text Here", color=0x00d9ff)
#  embed.add_field(name="Text", value="Text", inline=False)
#  embed.set_footer(text="Text Here")
#  await ctx.send(embed=embed)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game(".botCommands"))
  print("Bot is ready")

def WarframeTypes():
  print("Warframes added")


@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server.')

@client.command()
async def botCommands(ctx):
  embed = discord.Embed(
    title="Here are the commands:\n1] .ping \n2] .8ball \n3] .warframeCommands \n4] ."
  )
  await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx,*, question):
  responses = ['It is certain.',
              'It is decidedly so.',
              'Without a doubt.',
              'Yes – definitely.',
              'You may rely on it.',
              'As I see it, yes.',
              'Most likely.',
              'Outlook good.',
              'Yes.',
              'Signs point to yes.',
              'Reply hazy, try again.',
              'Ask again later.',
              'Better not tell you now.',
              'Cannot predict now.',
              'Concentrate and ask again.',
              'Dont count on it.',
              'My reply is no.',
              'My sources say no.',
              'Outlook not so good.',
              'Very doubtful.']
  await ctx.send(f'Question: {question}\nAnswers: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=50):
  await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}')

########################################################################################################################
#Game commands
@client.command()
async def warframeCommands(ctx):
  embed=discord.Embed(title="Here are the commands:", description="These are used for warframe!", color=0x00d9ff)
  embed.add_field(name="Ability Tiers", value="1] .abilityCommands", inline=False)
  embed.add_field(name="MoA Builds", value="2] .moaBuilds", inline=False)
  embed.add_field(name="AMP Builds", value="3] .ampBuild", inline=False)
  embed.add_field(name="Kuva Lich", value="4] .kuvaLich", inline=False)
  embed.add_field(name="Warframe Tiers", value="4] .warframeTiers", inline=False)
  embed.set_footer(text="If you are unsure of what they do then you just dumb")
  await ctx.send(embed=embed)

#Warframe
@client.command()
async def abilityCommands(ctx):
  embed=discord.Embed(title="Ability Tiers", description="Here are your best abilities in tiers", color=0x00d9ff)
  embed.add_field(name="S Tier", value="Rhino - Roar\nNidus - Larva", inline=False)
  embed.add_field(name="A Tier", value="Protea: Dispensary\nMirage: Eclipse\nValkyr: Warcry\nHildryn: Pillage\nWisp: Breach Surge\nKhora: Ensnare\nChroma:Elemental Ward\nEquinox: Rest and Rage\nWukong: Defy\nNova: Null Star", inline=False)
  embed.add_field(name="B Tier", value="Ivara: Quiver\nOberon: Smite\nHarrow: Condemn\nMesa: Shooting Gallery\nGauss: Thermal Sunder\nOctavia: Resonator\nXaku: Whisper\nNezha: Fire Walker\nAsh: Shuriken\nBaruuk: Lull\nSaryn: Molt\nAtlas: Petrify\nVolt: Shock\nRevenant: Reave", inline=False)
  embed.add_field(name="C Tier", value="Mag: Pull\nInaros: Desiccation\nGara: Spectrorage\nNekros: Terrify\nLimbo: Banish\nFrost: Ice Wave\nHydroid: Tempest Barrage\n Nyx: Mind Control", inline=False)
  embed.add_field(name="D Tier", value="Loki: Decoy\nZephyr: Airburst", inline=False)
  embed.set_footer(text="If you are unsure of what they do then you just dumb")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def moaBuilds(ctx):
  embed=discord.Embed(title="MOA Build", description="This is the best MOA combinations", color=0x00d9ff)
  embed.add_field(name="Build 1:", value="Lambeo MOA, Krisys Core, Aegron Gyro, Drimper Bracket", inline=False)
  embed.add_field(name="Build 2:", value="Oloro MOA, Alcrom Core, Hextra Gyro, Drimper Bracket", inline=False)
  embed.add_field(name="Build 3:", value="Para MOA, Krisys Core, Munit Gyro, Drimper Bracket", inline=False)
  embed.set_footer(text="For more info, go to the Wiki")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def ampBuilds(ctx):
  embed=discord.Embed(title="???", description="???", color=0x00d9ff)
  embed.add_field(name="???", value="???", inline=False)
  embed.add_field(name="???", value="???", inline=False)
  embed.add_field(name="???", value="???", inline=False)
  embed.set_footer(text="???")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def kuvaLich(ctx):
  #https://cog-creators.github.io/discord-embed-sandbox/
  embed=discord.Embed(title="Kuva Lich", description="This is the elements for Lich Weapons", color=0x00d9ff)
  embed.add_field(name="Best Mission for Lich is:", value="Saturn, Cassini", inline=False)
  embed.add_field(name="Impact:", value="Baruuk, Gauss, Grendel, Rhino, Wukong, Zephyr", inline=False)
  embed.add_field(name="Heat:", value="Chroma, Ember, Inaros, Nezha, Vauban, Wisp", inline=False)
  embed.add_field(name="Cold:", value="Gara, Hildryn, Revenant, Titania, Trinity", inline=False)
  embed.add_field(name="Electricity", value="Banshee, Excalibur, Limbo, Nova, Valkyr, Volt", inline=False)
  embed.add_field(name="Toxin:", value="Atlas, Ivara, Khora, Nekros, Nidus, Oberon, Saryn", inline=False)
  embed.add_field(name="Magnetic:", value="Magnetic: Harrow, Hydroid, Mag, Mesa", inline=False)
  embed.add_field(name="Radiation:", value="Ash, Equinox, Garuda, Loki, Mirage, Nyx, Octavia", inline=False)
  embed.set_footer(text="For more info, go to the Wiki")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def warframeTiers(ctx):
  embed=discord.Embed(title="Warframe Tiers", description="Here are your best warframes in tiers", color=0x00d9ff)
  embed.add_field(name="S Tier", value="Saryn\nWisp\nMesa\nOctavia", inline=False)
  embed.add_field(name="A Tier", value="Nova\nKhora\nVolt\nNidus\nTrinity\nGara\nRhino\nEquinox\nBaruuk\nProtea\nMirage\nLavos\nGauss\nNezha\nIvara\nRevenant\nHarrow\nNekros\nTitania\nChroma\nEmber\nOberon\nInaros\nLimbo\nVauban", inline=False)
  embed.add_field(name="B Tier", value="Excalibur\nHildryn\nMag\nXaku\nAsh\nFrost\nValkyr\nLoki\nGaruda\nBanshee\nAtlas", inline=False)
  embed.add_field(name="C Tier", value="Hydroid\nGrendel\nNyx\nZephr", inline=False)
  embed.add_field(name="D Tier", value="Guess theres none?", inline=False)
  embed.set_footer(text="If you are unsure of what they do then you just dumb")
  await ctx.send(embed=embed)

#overextended = name="Overextended", value="This is a mod", inline=False


@client.command(pass_context=True)
async def equinoxgoodnight(ctx):
  embed=discord.Embed(title="Equinox Sleep build", description="Mostly used for focus farming or power leveling", color=0x00d9ff)
  embed.add_field(name="Aura Mod", value="Text", inline=False)
  embed.add_field(name="2nd Aura Mod", value="Text", inline=False)
  embed.add_field(name="[F] Overextended", value="Text", inline=False)
  embed.add_field(name="[F] Adaptation", value="Text", inline=False)
  embed.add_field(name="Primed Flow", value="Text", inline=False)
  embed.add_field(name="Augur Reach", value="Text", inline=False)
  embed.add_field(name="[F] Primed Continuity", value="Text", inline=False)
  embed.add_field(name="Stretch", value="Text", inline=False)
  embed.add_field(name="Streamline", value="Text", inline=False)
  embed.add_field(name="Anything extra", value="Text", inline=False)
  embed.set_footer(text="Run this with a .orthos Prime")
  await ctx.send(embed=embed)

########################################################################################################################
@client.command(pass_context=True)
async def valheim(ctx):
  embed=discord.Embed(title="Valheim", description="Just general tips", color=0x00d9ff)
  embed.add_field(name="Buildings", value="Destroy old buildings to harvest wood quickly", inline=False)
  embed.add_field(name="???", value="Upgrade your workbench by crafting a chopping block and tanning rack", inline=False)
  embed.add_field(name="???", value="Their's no repair cost, so it's easy to keep your gear pristine", inline=False)
  embed.add_field(name="???", value="Sail your raft with WASD", inline=False)
  embed.add_field(name="???", value="Tame boars with mushrooms", inline=False)
  embed.add_field(name="???", value="Carry a weapon on your back with the R key", inline=False)
  embed.add_field(name="???", value="You'll need to defeat the first boss to craft a pickaxe", inline=False)
  embed.add_field(name="???", value="There's (currently) no way to increase your inventory", inline=False)
  embed.add_field(name="???", value="For a fishing rod, you'll have to find the trader", inline=False)
  embed.add_field(name="???", value="Hide the HUD with Ctrl+F3", inline=False)
  await ctx.send(embed=embed)

melee_ready()
primary_ready()
secondary_ready()
warframe_ready()

keep_alive()
client.run(os.getenv('TOKEN'))