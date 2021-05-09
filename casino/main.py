import discord
from discord.ext import commands,tasks

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="", intents=intents)
#command_prefix:Botunuzu çağırırken kullanmak istediğiniz parametre.


@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="KOLPAÇİNO"))
    print("Ben Hazırım!")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hoşgeldin")
    await channel.send(f"{member.mention} aramıza katıldı. Hoş geldin!")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gidenler")
    await channel.send(f"{member} aramızdan ayrıldı :(")


@Bot.event
async def on_message(message):
    mesaj = message.content.lower()
    if mesaj == "günaydın":
        await message.channel.send("Sabah yürek yemiş buraya gelmiş!")
    elif mesaj == "nasılsın":
        await message.channel.send("Altın kapılarımız kan oldu Tayfun!")
    elif mesaj == "seni seviyorum":
        await message.channel.send("olur olur yeriz")
    elif mesaj == "beyler":
        await message.channel.send("Buyur koçum")
    elif mesaj == "valorant":
        await message.channel.send("Bizi bitirdin be!")
    elif mesaj == "sen kimsin?":
        await message.channel.send("Hayırdır İngiltere Prensi’yle mi konuşuyorum?");
    elif mesaj == "@everyone":
        await message.channel.send("Boş yere everyone atmayın lütfen")
    elif mesaj == "merhaba":
        await message.channel.send("Size de merhaba")
    elif mesaj == "mal bot":
        await message.channel.send("Benim adım bomba soyadım ölüm lan!")
    elif mesaj == "mal mısın":
        await message.channel.send("Sensin o kardeşim")
    elif mesaj == "say":
        for x in range(1, 11):
            await message.channel.send(x)
    elif mesaj == "manyak":
        await message.channel.send(file=discord.File('Gif/2.gif'))
    elif mesaj == "iyi geceler":
         await message.channel.send(file=discord.File('Foto/1.png'))



Bot.run(tokeniniz)
