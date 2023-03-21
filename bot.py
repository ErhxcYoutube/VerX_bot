import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
      print("Bot jest online")
      await client.change_presence(activity=discord.Streaming(name="?help / ?invite", url="https://discord.gg/5WMZqqvDzX"))

@client.command()
async def invite(ctx):
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name="Link z zaproszeniem bota https://discord.com/api/oauth2/authorize?client_id=1087680615744286781&permissions=8&scope=bot", value="invite link", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def prefix(ctx):
    await ctx.send(" Bot prefix '?' ")

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Komendy", description="Komendy w bocie", color=0xff0000)
    embed.add_field(name="Ban", value="?ban (Banuje osobe z serwera)", inline=False)
    embed.add_field(name="Unban", value="?unban (Daje unabnuje osobe zbanowaną)", inline=False)
    embed.add_field(name="Kick", value="?kick (Wyrzuca osobe z serwera)", inline=False)
    embed.add_field(name="Warn", value="?warn (Daje warna członkowi)", inline=False)
    embed.add_field(name="Mute", value="?mute (Mutuje członka)", inline=False)
    embed.add_field(name="Clear", value="?clear (usuwa wiadomości)", inline=False)
    embed.add_field(name="Prefix", value="?prefix (pokazuje prefix bota)", inline=False)
    embed.add_field(name="Invite", value="?invite (link z zaproszeniem bota)", inline=False)
    embed.add_field(name="Support", value="?support (link z zaproszeniem bota na serwer)", inline=False)
    embed.add_field(name="Bot jest w trakcie tworzenia", value="Bot jest w trakcie tworzenia", inline=False)
    embed.set_footer(text="Komendy Od Bota")
    await ctx.author.send(embed=embed)
    await ctx.send(" **Wiadomość została wysłana w wiadomości prywatnej** ")

@client.command()
@has_permissions(ban_members=True)
async def graj(ctx, game):
    await client.change_presence(activity=discord.Game(name=game))

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="Brak powodu."):
    await member.ban(reason=reason)
    embed=discord.Embed(description=f"{member} Został/ła zbanowany/a za {reason}.", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await ctx.send(embed=embed)
    embed=discord.Embed(description=f"Zostałeś/aś zbanowany/a za {reason}. Jeśli uważasz, że ban był niesłuszny, zgłoś się po odwołanie na discord: K0lol#0262", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await ctx.send(" **Dostał bana** ")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="Brak powodu."):
    await member.kick(reason=reason)
    embed=discord.Embed(description=f"{member} Został/ła wyrzucony/a za {reason}.", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await ctx.send(embed=embed)
    embed=discord.Embed(description=f"Zostałeś/aś wyrzucony/a za {reason}. Jeśli uważasz, że wyrzucenie było niesłuszne, zgłoś się po odwołanie na discord: K0lol#0262", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await ctx.send(" **Dostał kicka** ")

@client.command()
@has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member,time ,reason="Brak powodu."):
    mute_log = discord.utils.get(ctx.guild.channels, id=944015781690216448)
    unmute_log = discord.utils.get(ctx.guild.channels, id=944015805417406494)
    muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
    Użytkownik=discord.utils.get(ctx.guild.roles, name="Użytkownik")
    time_convert = {"s":1, "m":60, "h":3600,"d":86400}
    tempmute= int(time[0]) * time_convert[time[-1]]
    await ctx.message.delete()
    await member.remove_roles(Użytkownik)
    await member.add_roles(muted_role, reason=reason)
    embed = discord.Embed(description= f"{member.mention} Został wyciszony/a za {reason}.", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await mute_log.send(embed=embed)
    await asyncio.sleep(tempmute)
    await member.remove_roles(muted_role)
    await member.add_roles(Użytkownik)
    user = client.get_user(f"{ctx.author.mention}")
    embed = discord.Embed(description= f"{member.mention} Został odciszony/a.", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await unmute_log.send(embed=embed)

@client.command()
@has_permissions(kick_members=True)
async def clear(ctx, ilosc = 2500):
    clear_log = discord.utils.get(ctx.guild.channels, id=944751147435061308)
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=ilosc)
    embed=discord.Embed(description=f"{ctx.author.mention} Usunął/ęła {ilosc} wiadomośći z kanału <#{ctx.channel.id}>", color=0x096a82)
    embed.set_author(name=f"Autor: {ctx.author}")
    await clear_log.send(embed=embed)



client.run("MTA4NzY4MDYxNTc0NDI4Njc4MQ.GoLakv.PccPkhvL3sAuYk8RI8LM0PUnyp5GMsrInSR8DY")
