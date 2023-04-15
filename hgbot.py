# hgbot.py
import discord
import os
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
import io

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Set up the intents for your bot
intents = discord.Intents.all()
intents.members = True
intents.voice_states = True
intents.typing

bot = commands.Bot(command_prefix='!', intents=intents)


play_list = {
                'tunnelman': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\tunnelman.mp3', 
                'bloody': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\bloodyfuckyou.mp3',
                'ramadan': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\ramadan.mp3', 
                'doorstuck': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\doorstuck.mp3', 
                'meat': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\meat.mp3',
                'human': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\imonlyhuman.mp3',
                'rats': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\rats.mp3',
                'tokyoghoul': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\tokyoghoul.mp3',
                'bingchilling': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\bingchilling.mp3',
                'ohmygod': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\ohmygod.mp3',
                'mayo': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\mayonnaisewow.mp3', 
                'refrigerators': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\loverefrigerators.mp3',
                'gnomewoo': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\gnomewoo.mp3',
                'lemonpepperchicken': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\fourbigguys.mp3',
                'pillarmen': 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\pillarmen.mp3'
                # Add more member ID and audio/message mappings as needed
            }

audio_files = {
                #Terry
                '253323936912244737': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\tunnelman.mp3', 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\bloodyfuckyou.mp3', 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\pillarmen.mp3'],
                #Sajid
                '102477837407113216': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\ramadan.mp3', 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\doorstuck.mp3', 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\meat.mp3'],
                #Lane
                '102822692897423360': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\imonlyhuman.mp3'],
                #Tommy
                '109029965239971840': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\rats.mp3', 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\fourbigguys.mp3'],
                #Irene
                '1086124701224538163': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\tokyoghoul.mp3'],
                #Jing
                '927707014845587476': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\bingchilling.mp3'],
                #Bitna
                '318223619236954115': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\ohmygod.mp3'],
                #Brandon
                '102559904346157056': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\mayonnaisewow.mp3', 'C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\loverefrigerators.mp3'],
                #Noah
                '89571033807343616': ['C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\gnomewoo.mp3']
                # Add more member ID and audio/message mappings as needed
            }

message_files = {
                #Sajid
                '102477837407113216': ["Ramadan Mubarak, Sajid!", "SAJID, YOU CAN'T EAT", "Not enough HG."],
                #Tommy
                '109029965239971840': ["JOBLESS", "Not enough HG."]
            }

pokemons = ['C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\shinynumel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png', 'C:\\Users\\Terry\\Documents\\discbotstuff\\pokepngs\\numel.png']

role_ids = {
    'gunfire': 1096160139897229343,
    'borderlands': 1096172436971601931,
    'osu': 1096173196685877364,
    'league': 1096174821903183872
}

game_gifs = {
    'gunfire': 'https://tenor.com/view/anime-gunfire-reborn-gif-26444870',
    'borderlands': 'https://tenor.com/view/hop-on-borderlands-jakob-jakobs-gif-25907601',
    'osu': 'https://tenor.com/view/osu-gif-19944119',
    'league': 'https://tenor.com/view/kissing-league-league-of-legends-deku-gif-25637810'
}


@bot.event
async def on_ready():
    print("Bot is connected to Discord")

#help command
class CustomHelpCommand(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", color=discord.Color.blurple())

        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [self.get_command_signature(c) for c in filtered]

           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "Commands")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

bot.help_command = CustomHelpCommand()

#bot joins vc when user joins to play sound
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        # Member joined a voice channel
        voice_channel = after.channel
        if not voice_channel.guild.voice_client:
            vc = await voice_channel.connect()
            audio_file_list = (audio_files.get(str(member.id)))
            if audio_file_list:
                # Play specific audio file for member
                audio_file = random.choice(audio_file_list)
                print(f"Playing audio file for {member.display_name}: {audio_file}")
                audio_source = FFmpegPCMAudio(audio_file)
            else:
                # Play default audio file for all other members
                print(f"No audio file found for {member.display_name}, playing default audio file")
                audio_source = FFmpegPCMAudio('C:\\Users\\Terry\\Documents\\discbotstuff\\audiofiles\\vineboom.mp3')

            channel = bot.get_channel(1087906252622930012)
            if str(member.id) in message_files:
                message = random.choice(message_files.get(str(member.id)))
                print(f"Sending message for {member.display_name}: {message}")
                await channel.send(message)

            # Play audio file
            audio_sources = discord.PCMVolumeTransformer(audio_source, volume=0.05)
            vc.play(audio_sources)

            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()

#bot leaves vc
@bot.command(name= 'leave')
async def leave(ctx):
    """Makes the bot leave voice channel."""
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")      


#bot joins vc to play sound
@bot.command(name= 'play')
async def play(ctx, arg):
    if play_list.get(str(arg)) is not None:
        if not ctx.author.voice:
            await ctx.send("You are not connected to a voice channel.")
            return
        voice_client = ctx.voice_client
        if not voice_client:
            voice_client = await ctx.author.voice.channel.connect()
        else:
            await voice_client.move_to(ctx.author.voice.channel)
        if voice_client.is_playing():
            voice_client.stop()
        sounds = play_list.get(str(arg))
        print(sounds)
        sound = FFmpegPCMAudio(sounds)
        soundes = discord.PCMVolumeTransformer(sound, volume=0.05)
        voice_client.play(soundes)
        if (arg) == 'gnomewoo':
            await ctx.send('WOO')
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
    if arg == "list":
        keys = list(play_list.keys())
        keys1 = str(keys).replace("'", "")
        keys2 = keys1.replace("[", "")
        keys3 = keys2.replace("]", "")
        await ctx.send(keys3)

#sends message for errors
@bot.event
async def on_command_error(ctx, error):
        if str(error) == 'arg is a required argument that is missing.':
            await ctx.channel.send(f'Use "!play list" to see the list of play commands.')
        #else:
            #await ctx.channel.send(f'poopy')

#summons pokemon
@bot.command(name= 'pokemon')
async def pokemon(ctx):
    channel = bot.get_channel(1087906252622930012)
    pokemon = random.choice(pokemons)
    print(pokemon)
    await channel.send(file=discord.File(pokemon))

#bot mentions role and send gif
@bot.command(name= 'hopon')
async def hopon(ctx, arg):
    if str(arg) is not None:
        roles = role_ids.get(str(arg))
        role = discord.utils.get(ctx.guild.roles, id = roles)
        await ctx.send(f'{role.mention} Hop on {arg}')
        gif = game_gifs.get(str(arg))
        await ctx.send(gif)

bot.run(TOKEN)