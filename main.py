import discord
import time
import os
import sys
import asyncio
import json
import typing
import pyowm
import youtube_dl

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from discord import utils
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
from random import *


bot = commands.Bot(command_prefix='ц.', intents=discord.Intents.all())
TOKEN = "ODgyNTI5NTc4NDc0NjkyNjI4.GT0MVZ.FOQtVu1up-gCoZeDWP1EaKxjAT8bOwGQWMfTg4"
YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


HELLO_WORDS = ['привет', 'здравствуйте', 'приветик', 'всем привет', 'ку', 'Всем ку', 'Всем здарова', 'Всем дарова', 'Всем дароу', 'Дароу', 'здарова']
HELLO_ANSWERS = ['Приветики:wave:', 'Привет)', 'Здравствуй', ]



#Когда он запустился
@bot.event
async def on_ready():
    print("Цаворит в онлайне;)")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('v1.0 ц.чтотыумеешь') )

@bot.event
async def on_message(message):
    msg = message.content.lower()

    if msg in HELLO_WORDS:
        await message.channel.send(choice(HELLO_ANSWERS))
    
    await bot.process_commands(message)

@bot.command()
async def рандомное_число(ctx):
    await ctx.send(f"Ваше число: {random()}")

@bot.command()
async def random_number(ctx):
    await ctx.send(f"Your number: {random()}")

#Команда повтори
@bot.command()
async def повтори(ctx, *, args):
    await ctx.send(args)

@bot.command()
async def repeat(ctx, *, args):
    await ctx.send(args)


#Команда Пинг
@bot.command()
async def пинг(ctx):
    await ctx.reply(f'Понг {round(bot.latency * 1000)} мс')
    print("У кого-то сегодня походу слабый интернет)...")

@bot.command()
async def ping(ctx):
    await ctx.reply(f'pong {round(bot.latency * 1000)} ms')


#Команда о помощи
@bot.command()
async def чтотыумеешь(ctx):
    embed=discord.Embed(title="Вы использовали команду помощи", description="Тут вы можете ознакомиться о том как пользоваться мной:", color=0x00fa9a)
    embed.set_author(name="- Arcadeog (Главный создатель бота)", url="https://www.tiktok.com/@arcadeog", icon_url="https://cdn.discordapp.com/attachments/926046222869991475/1020204989097979944/aa9e0af70b5f13c9104e30d560387903.png")
    embed.add_field(name="ц.повтори", value="Повторю то что мне скажут", inline=False)
    embed.add_field(name="ц.привет", value="Привет.", inline=False)
    embed.add_field(name="ц.какдела", value="(Думаю и так ясно)", inline=False)
    embed.add_field(name="ц.пинг", value="Показываю свой пинг (Не твой)", inline=False)
    embed.add_field(name="ц.чтотыумеешь", value="Показываю это окно (Которое ты читаешь)", inline=False)
    embed.add_field(name="ц.когдаобновление", value="Говорю когда обновление (Проверяйте раз в неделю может что-то будет менятся)", inline=False)
    embed.add_field(name="ц.погода", value="Показываю погоду в месте котором ты мне указал (Используется OpenWeatherMap)", inline=False)
    embed.add_field(name="ц.эмбед", value="Тест на эмбед", inline=False)
    embed.add_field(name="ц.очистить(очисти)", value="Очищаю чат", inline=False)
    embed.add_field(name="ц.зайти", value="Зайти в Голосовой канал", inline=False)
    embed.add_field(name="ц.выйти", value="Выйти из голосового канала", inline=False)
    embed.add_field(name="ц.пауза", value="Поставить музыку на паузу", inline=False)
    embed.add_field(name="ц.рандомное_число  ", value="Выдаёт абсолютно рандомное число", inline=False)
    embed.add_field(name="А ещё кик и бан", value="Думаю тоже понятно что они делают", inline=False)
    embed.set_footer(text="Это пока что всё..")
    await ctx.send(embed=embed)
    
    print("Меня попросили о помощи;)")

#Команда Когда обновление
@bot.command()
async def когдаобновление(ctx):
    embed = discord.Embed(title="Нарушение❗",
            description="Вам был выдан варн.. Тип нарушение: Ты слижком милый:3",
            timestamp="ц.варн (Уже в процессе)",
            colour = discord.Colour.from_rgb(0, 250, 154))
    await ctx.reply(embed)

#Команда Погода
@bot.command()
async def погода(ctx, city):
    #config_dict = get_default_config()
    #config_dict['language'] = 'ru'
    #owm = pyowm.OWM('095cf29b891a2f66e2989b3b8f162ac8', config_dict)
    #mgr = owm.weather_manager()
    #observation = mgr.weather_at_place(city)
    #w = observation.weather
    #temperature = w.temperature('celsius')
    #embed = discord.Embed(title=f"Погода - {city}", description=f"Сейчас там {w.status}", color=0x00fa9a)
    #embed.add_field(name="Температура", value=temperature+"°C", inline=False),
    #embed.add_field(name="Влажность", value=w.humidity + "%", inline=True),
    #embed.add_field(name="Детальный статус", value=w.detailed_status, inline=False),
    #embed.add_field(name="Облачность", value=w.clouds + "%", inline=False)

    await ctx.send("> Coming in 20.09.2022")

@bot.command()
async def weather(ctx, city):
    #owm = pyowm.OWM('095cf29b891a2f66e2989b3b8f162ac8')
    #mgr = owm.weather_manager()
    #observation = mgr.weather_at_place(city)
    #w = observation.weather
    #temperature = w.temperature('celsius')
    #embed = discord.Embed(title=f"Weather - {city}", description=f"For now there {w.status}", color=0x00fa9a)
    #embed.add_field(name="Temperature (Celsius)", value=temperature+"°C", inline=False),
    #embed.add_field(name="Humidity", value=w.humidity + "%", inline=True),
    #embed.add_field(name="Detailed status", value=w.detailed_status, inline=False),
    #embed.add_field(name="Clouds", value=w.clouds + "%", inline=False)

    await ctx.send("> Coming in 20.09.2022")

#Тест на эмбэд
@bot.command()
async def эмбед(ctx):
    await ctx.reply(embed=discord.Embed(
            title="Это тест на эмбед",
            description="Да, я хочу это зделать",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
        ))

@bot.command()
async def embed(ctx):
    await ctx.reply(embed=discord.Embed(
            title="This is test for embed",
            description="Yes, i want to do it",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
        ))

#Команда Очистки
@bot.command()
@commands.has_permissions(manage_messages=True)
async def очистить(ctx, amount):
    await ctx.reply(f"Сейчас через 3 секунды очищю {amount} сообщений")
    time.sleep(3)
    await ctx.channel.purge(limit = amount + 2)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def очисти(ctx, amount):
    await ctx.reply(f"Сейчас через 3 секунды очищю {amount} сообщений")
    time.sleep(3)
    await ctx.message.author.channel.purge(limit = amount + 2)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    await ctx.reply(f"Now i clear {amount} messages in 3 seconds")
    time.sleep(3)
    await ctx.message.author.channel.purge(limit = amount + 2)

@очистить.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Ошибка❗",
            description="Использование: ц.очистка (Количество)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Ошибка❗",
        description="Недостаточно прав",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@очисти.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Ошибка❗",
            description="Использование: ц.очистка (Количество)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Ошибка❗",
        description="Недостаточно прав",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@clear.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Error❗",
            description="Example: ц.clear (Amount)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Error❗",
        description="Not enough permissions",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

#Кик
@bot.command()
@commands.has_permissions(kick_members=True)
async def кик(ctx, member: commands.MemberConverter, reason=None):
    await ctx.guild.kick(member)
    await ctx.send(embed=discord.Embed(
            title="Успешно✅",
            description="Пользователь был успешно кикнут из сервера",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: commands.MemberConverter, reason=None):
    await ctx.guild.kick(member)
    await ctx.send(embed=discord.Embed(
            title="Succesful✅",
            description="Member has been kicked from server",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@кик.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Ошибка❗",
            description="Использование: ц.кик (Участник)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Ошибка❗",
        description="Недостаточно прав",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@kick.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Error❗",
            description="Example: ц.kick (Member)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Error❗",
        description="Not enough permissions",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

#Бан
@bot.command()
@commands.has_permissions(ban_members=True)
async def бан(ctx, member: commands.MemberConverter, reason=str):
    await ctx.guild.kick(member)
    await ctx.send(embed=discord.Embed(
            title="Успешно✅",
            description="Пользователь был успешно забанен",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: commands.MemberConverter, reason=str):
    await ctx.guild.kick(member)
    await ctx.send(embed=discord.Embed(
            title="Succesful✅",
            description="Member has been banned from server",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@бан.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Ошибка❗",
            description="Использование: ц.бан (Участник) (Причина)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Ошибка❗",
        description="Недостаточно прав",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@ban.error
async def error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(
            title="Error❗",
            description="Example: ц.ban (Member)",
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(embed=discord.Embed(
        title="Error❗",
        description="Not enough permissions",
        timestamp=ctx.message.created_at,
        colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@bot.command()
@commands.has_permissions(ban_members=True)
async def разбан(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discrimination) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(
            title="Успешно✅",
            description="Пользователь был успешно разбанен" ,
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discrimination) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(
            title="Succesful✅",
            description="Member has been unbaned" ,
            timestamp=ctx.message.created_at,
            colour = discord.Colour.from_rgb(0, 250, 154)
            ))

@bot.command()
async def зайти(ctx):
    vc = await ctx.message.author.voice.channel.connect()
    await ctx.send(f"Подключился")

@bot.command()
async def join(ctx):
    vc = await ctx.message.author.voice.channel.connect()
    await ctx.send(f"Connect")

@bot.command()
async def выйти(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Я не подключен... Зачем меня останавлвать.")

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Im not connected.. Why trying to stop me?")

@bot.command()
async def пауза(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Сейчас музыка не играет")

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("For now, music dont play")

@bot.command()
async def продолжить(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Эта песня не остановлена")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("This song isnt stopped")

@bot.command()
async def стоп(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Я не подключен... Зачем меня останавлвать.")

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Im not connected.. Why trying to stop me?")



bot.run(TOKEN)
