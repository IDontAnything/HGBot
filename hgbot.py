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
                'tunnelman': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\tunnelman.mp3', 
                'bloody': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\bloodyfuckyou.mp3',
                'ramadan': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\ramadan.mp3', 
                'doorstuck': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\doorstuck.mp3', 
                'meat': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\meat.mp3',
                'human': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\imonlyhuman.mp3',
                'rats': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\rats.mp3',
                'tokyoghoul': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\tokyoghoul.mp3',
                'bingchilling': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\bingchilling.mp3',
                'ohmygod': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\ohmygod.mp3',
                'mayo': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\mayonnaisewow.mp3', 
                'refrigerators': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\loverefrigerators.mp3',
                'gnomewoo': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\gnomewoo.mp3',
                'lemonpepperchicken': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\fourbigguys.mp3',
                'pillarmen': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\pillarmen.mp3',
                'letsgo': 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\letsgo.mp3'
                # Add more member ID and audio/message mappings as needed
            }

audio_files = {
                #Terry
                '253323936912244737': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\tunnelman.mp3', 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\pillarmen.mp3', ],
                #Sajid
                '102477837407113216': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\ramadan.mp3', 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\doorstuck.mp3', 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\meat.mp3'],
                #Lane
                '102822692897423360': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\imonlyhuman.mp3'],
                #Tommy
                '109029965239971840': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\rats.mp3', 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\fourbigguys.mp3'],
                #Irene
                '1086124701224538163': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\tokyoghoul.mp3'],
                #Jing
                '927707014845587476': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\bingchilling.mp3'],
                #Bitna
                '318223619236954115': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\ohmygod.mp3'],
                #Brandon
                '102559904346157056': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\mayonnaisewow.mp3', 'C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\loverefrigerators.mp3'],
                #Noah
                '89571033807343616': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\gnomewoo.mp3'],
                #Sara
                '126933549654736896': ['C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\letsgo.mp3']
                # Add more member ID and audio/message mappings as needed
            }

message_files = {
                #Sajid
                '102477837407113216': ["Not enough HG.", "https://tenor.com/view/islam-allah-quran-muslim-alhumdulillah-gif-17648936"],
                #Tommy
                '109029965239971840': ["Not enough HG."],
                #Lane
                '102822692897423360': ["https://tenor.com/view/tyler1-loltyler1-screaming-dead-wtf-gif-17500255"]
            }

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
    await bot.load_extension('cogs.rps')

@bot.command(name= 'commands')
async def help(ctx):
    await ctx.send('The commands for HGBot are:\n     !commands: lists all commands,\n     !leave: to make the bot leave the voice channel,\n     !play: to play certain audio clips in voice chat,\n     !pokemon: to summon a random pokemon,\n     !challenge @user: to challenge someone to Rock Paper Scissors,\n     !gimme role: to give yourself a role,\n     !remove role: to get rid of a role you have,\n     !hopon role: to tell user of a role to play a game.')

#burger king response
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return
    if ("burger king" or "Burger King") in message.content.lower():
        await message.channel.send("I'm in the drive-thru of Burger King\nCan I please get a Whopper Jr. with onion rings?\nMake it a meal so I can get a drink\nNo, I'm not finished, that's not everything\nCan I please get a Double Whopper with no cheese?\nCan I please get a number two with a large drink?\nI got money so I don't care how much it costs me\nSo just throw in some extra friеs, don't make them salty\n\nAll this cheese gonna makе my booty drip drip\nI'm lactose intolerant, I don't sip milk\nIf I see a sight of cheese, I'ma trip trip\nI'ma sit on your toilet seat and doodoo then dip\nSo you got my lil' Whopper Jr.? (I didn't forget that)\nAnd you got my Double Whopper? (I didn't forget that)\nWhat about my onion rings? (Hold on, you can sit back)\nBurger King, they know me now\nCheese, I don't want that\n(Grrr) And I'm getting hungry now\nI know you heard that\nWaiting for my onion rings so I don't have to turn back\nBurger King, don't play with me, y'all nuggets is so trash\nNuggets taste like rabbit nipples, why y'all even serve that?\nBetter stop playing and just give me all of my food\nEither I pay you right now or leave the drive-thru\nGave me the bag and then I took a bite of my food\nThere's cheese in my mouth (I'm gonna doodoo)\n\nI'm in the drive-thru of Burger King\nMan, they just gave me a Whopper Jr. with hella cheese\nMade it a meal, so yes, I got my drink\nBut why they gon' put cheese on everything?\nThey put cheese on my Double Whopper with no cheese\nI'll be takin' a number two in the morning\nHold on, can I please be excused for a moment?\nThe cheese already in my body, booty farting (I farted)\n\nWait, di- did you just fart in my drive-thru?\nYo, com- yo, you can't be serious\nIt's just cheese\nIt's just cheese\nQueso, cheese")
    await bot.process_commands(message)
    
#chickfila response
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return
    if ("chickfila" or "chick-fil-a" or "ChickFilA" or "Chick-Fil-A") in message.content.lower():
        await message.channel.send("Closed on Sundays.")
    await bot.process_commands(message)

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
                audio_source = FFmpegPCMAudio('C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\audiofiles\\vineboom.mp3')

            channel = bot.get_channel(1087906252622930012)
            if str(member.id) in message_files:
                message = random.choice(message_files.get(str(member.id)))
                print(f"Sending message for {member.display_name}: {message}")
                await channel.send(message)

            # Play audio file
            audio_sources = discord.PCMVolumeTransformer(audio_source, volume=0.05)
            vc.play(audio_sources)

            # Wait for audio to finish playing
            while vc.is_playing():
                if after.channel != voice_channel:
                    await vc.disconnect()
                else:
                    await asyncio.sleep(1)
                
            # Disconnect from voice channel
            await vc.disconnect()

@bot.command(name= 'leave')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")      

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

@bot.event
async def on_command_error(ctx, error):
        if str(error) == 'arg is a required argument that is missing.':
            await ctx.channel.send(f'Use "!play list" to see the list of play commands.')
        if str(error) == 'member is a required argument that is missing.':
            await ctx.channel.send(f'Use "!challenge @member" to challenge a user to a game of "Rock Paper Scissors".')
        else:
            await ctx.channel.send(f'poopy')

#summons pokemon
@bot.command(name= 'pokemon')
async def pokemon(ctx):
    channel = bot.get_channel(1087906252622930012)
    number = random.randrange(1,500)
    print(number)
    if str(number) == '69':
        print('Shiny!')
        await ctx.send(f"{ctx.author.mention}")
        await channel.send(file=discord.File('C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\pokepngs\\shinynumel.png'))
    else:
        print('Numel!')
        await channel.send(file=discord.File('C:\\Users\\Administrator\\Documents\\HGBOT\\HGBOT\\discbotstuff\\pokepngs\\numel.png'))

#gives user roles
@bot.command()
async def gimme(ctx, *, rolename):
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    if role is None:
        await ctx.send(f"Sorry, the {rolename} role does not exist.")
        return
    try:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you now have the {role.name} role!")
    except discord.Forbidden:
        await ctx.send("Sorry, I don't have permission to assign that role.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")

#removes role from user
@bot.command()
async def remove(ctx, *, rolename):
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    if role is None:
        await ctx.send(f"Sorry, the {rolename} role does not exist.")
        return
    try:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you now do not have the {role.name} role.")
    except discord.Forbidden:
        await ctx.send("Sorry, I don't have permission to assign that role.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")

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