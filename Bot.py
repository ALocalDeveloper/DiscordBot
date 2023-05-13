import datetime
import disnake
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from asyncio import Server
activity = "Watching"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.all() 
intents.message_content = True
client = commands.Bot(command_prefix='?', intents=intents)

bot = commands.Bot(command_prefix="!",intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name="Port 8080"), status=discord.Status.idle)



async def on_ready():
    
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    
@bot.command()
async def embed(embed, userinput):
    Embedded = discord.Embed(title="Embed", description=userinput)
    await embed.send(embed = Embedded)
    await embed.send("Embed sent", delete_after=5)

@bot.command()
async def status(send):
    await send.send("Bot is running")
    await send.send('Latency is: {0}'.format(round(bot.latency, 1)))



@bot.command()
async def test(test):
    await test.send("!THIS IS A COMMAND FOR TESTING PURPOSES!")



@commands.has_permissions(kick_members=True)
@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await ctx.guild.kick(userName)
    


@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(self, ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx
  await ctx.send(f"{member} has been **banned**", delete_after=15)
  

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mod(ctx, member: discord.Member):
 
    guild = ctx.guild  
    
 
    
    role = get(guild.roles, name="Foretellers")
    await member.add_roles(role)

    
@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmod(ctx, member: discord.Member):
 
    guild = ctx.guild  
    
 
    
    role = get(guild.roles, name="Foretellers")
    await member.remove_roles(role)

@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, member:discord.User, *, reason=None):
    if reason == None:
        reason = f"No Reason Provided"
    await ctx.guild.unban(member, reason=reason)
    await ctx.send(f"{member.mention} has been **unbanned**", delete_after=15)
    embed = discord.Embed(title="Unban Log", description=f"{member.mention} has been **unbanned** by {ctx.author.mention}\n\nReason: `{reason}`\n\nUnbanned from: `{ctx.guild.name}`", color=0x1355ed)
    embed.add_field(name="User", value=f"{member}", inline=True)
    embed.add_field(name="UserID", value=f"{member.id}", inline=True)
    embed.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed.set_footer(text=f"Unban log - Banned user: {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    logchannel = bot.get_channel(1105539310884769832)
    await logchannel.send(embed=embed)
    await ctx.message.delete()
    print(f"Sucsessfully unbanned {member.name}")



class MyHelp(commands.HelpCommand):

    async def send_bot_help(self, mapping):
        """
        This is triggered when !help is invoked.

        This example demonstrates how to list the commands that the member invoking the help command can run.
        """
        filtered = await self.filter_commands(self.context.bot.commands, sort=True) # returns a list of command objects
        names = [command.name for command in filtered] # iterating through the commands objects getting names
        available_commands = "\n".join(names) # joining the list of names by a new line
        embed  = disnake.Embed(title="Help",description=available_commands)
        await self.context.send(embed=embed)

    async def send_command_help(self, command):
        """This is triggered when !help <command> is invoked."""
        await self.context.send("This is the help page for a command")

    async def send_group_help(self, group):
        """This is triggered when !help <group> is invoked."""
        await self.context.send("This is the help page for a group command")

    async def send_cog_help(self, cog):
        """This is triggered when !help <cog> is invoked."""
        await self.context.send("This is the help page for a cog")

    async def send_error_message(self, error):
        """If there is an error, send a embed containing the error."""
        channel = self.get_destination() # this defaults to the command context channel
        await channel.send(error)

bot.help_command = MyHelp()


@bot.command()
async def rickroll(roll):
    await roll.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
    

@bot.command()
async def wip(wip):
    
    await wip.send("Work in progress!")

@bot.command()
async def version(ver):
    vers = "Version 1.1.4-fix1"
    embed = discord.Embed(title="Version Branch: Test", description=vers, color=0x1355ed)
    await ver.send(embed = embed)
    





bot.run('token here')
