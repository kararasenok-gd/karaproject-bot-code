import keep_alive
import discord
from discord.ext import commands
#import requests
#from PIL import Image, ImageFont, ImageDraw
#import io
#from Cybernator import Paginator as pag

PREFIX = ("kp?", "kp!")
client = commands.Bot(command_prefix=PREFIX, description='Бот... Я бот... Просто обычный бот...')
client.remove_command('help')

# Words
hello_words = ['привет', 'здарова']
word_list1 = ['норм', 'нормально', 'хорошо', 'отлично']






# !hello


@client.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Даю краба {author}')

# !test


@client.command()
async def test(ctx):
    await ctx.send('бот работает!')

# !echo


@client.command(pass_context = True)
async def echo(ctx, *, message, amount = 1):
    await ctx.channel.purge( limit = amount )
    await ctx.send(message)

# !clear Чистка чата


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=99999):
    await ctx.channel.purge(limit=amount+1)

# !kick кик игрока


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason='Гнев Бога'):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'Бог в гневе и выкинул с олимпа { member.mention }')

# !ban Бан игрока


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason='Наверное ты и сам догадываешься'):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f'О мой бог этот парень реально пререшел черту { member.mention }')

# !unban разбанить игрока


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'Бог сегодня добрый , он простил {user.mention}')
        return

# !user_mute Замутить пользователя


@client.command()
@commands.has_permissions(administrator=True)
async def user_mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='холоп(mute)')
    await member.add_roles(mute_role)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Царь')
    await member.remove_roles(mute_role)
    await ctx.send(f'Бог забрал право голоса у {member.mention}')

# !user_unmute Замутить пользователя


@client.command()
@commands.has_permissions(administrator=True)
async def user_unmute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Царь')
    await member.add_roles(mute_role)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='холоп(mute)')
    await member.remove_roles(mute_role)
    await ctx.send(f'Бог вернул право голоса {member.mention}')

# !help Список команд


@client.command()
async def help(ctx):
    await ctx.send('Команды бота:\n'
                   '```kp!hello - Поздороваться с ботом```\n'
                   '```kp!test - команда для проверки бота на работу```\n'
                   '```kp!echo - эхо```\n'
                   '```kp!clear [количество сообщений+1] - Стереть сообщения```\n'
                   '```kp!kick - Кикнуть кого-либо (Использование только Администраторами)```\n'
                   '```kp!ban - Забанить кого-либо (Использование только Администраторами)```\n'
                   '```kp!unban - Разбанить кого-либо (Использование только Администраторами)```\n'
                   '```kp!user_mute - Замутить кого-либо (Использование только Администраторами)```\n'
                   '```kp!user_unmute - Размутить кого-либо (Использование только Администраторами)```\n'
                   '```kp!invite - даёт ссылку на приглашение бота```\n'
                   '```kp!donate - даёт ссылку на донат и показывает преймущества доната```\n'
                   '```kp!add / sub / multiply / divide - Сложить / Вычесть / Умножить / Разделить 2 числа (Пример: kp!add 2 2)```\n'
                   '***__А также 5 команд пасхалок!__***\n'
                   '***И да, для того что бы завершить установку создай 2 роли и назови их так:***\n'
                   '1. **Царь**\n'
                   '2. **холоп(mute)**\n'
                   'царя выдай себе ведь эта роль для работы команд mute и ban\n')

 

# !doradura_song


@client.command()
async def doradura_song(ctx):
    await ctx.send('Ты позвал меня на встречу (а)')
    await ctx.send('Ты позвал меня на встречу')
    await ctx.send('Я готовилась весь вечер')
    await ctx.send('Выбирала, что надеть мне')
    await ctx.send('Истрепала свои нервы')
    await ctx.send('Пришла, ждала почти два часа')
    await ctx.send('И ты написал: "Сорри, я проспал"')
    await ctx.send('Потому что Дора — дура')
    await ctx.send('Супердура, Дора — дура')
    await ctx.send('Потому что Дора — дура')
    await ctx.send('Супердура, Дора — дура')
    await ctx.send('Потому что, Дора — дура')
    await ctx.send('Супердура, Дора — дура')
    await ctx.send('Потому что, Дора — дура')
    await ctx.send('Супердура, Дора — дура')
    await ctx.send('↓')
    await ctx.send('↓')
    await ctx.send('↓')
    await ctx.send('↓')
    await ctx.send('Трек который напел бот: дора - Дорадура')


# kp!flex пасхалка

@client.command()
async def flex(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/931111225092362270/931872623846113360/2474-partytime11.gif')
  await ctx.send('Ты нашёл одну из пасхалок!')


#kp!krinzh

@client.command()
async def krinzh(ctx):
  await ctx.send('https://tenor.com/view/cringe-gif-23461072')
  await ctx.send('Ты нашёл одну из пасхалок!')

#kp!invite

@client.command()
async def invite(ctx):
  await ctx.send('Пригласить меня можно 2 способами:\n'
  '1. Через профиль (работает только на компьютере)\n'
  '2. Через ссылку: https://discord.com/api/oauth2/authorize?client_id=931553681772535859&permissions=8&scope=bot')

  #kp!kak_kakat_v_tualete

@client.command()
async def kak_kakat_v_tualete(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/898289371348877362/932309655466700880/unknown.png')
  await ctx.send('Ты нашёл одну из пасхалок!')


#kp!donate

@client.command()
async def donate(ctx):
  await ctx.send('Поддержать автора монетой можно по этой ссылке: https://www.donationalerts.com/r/kararasenochek\n'
  'Что даёт монета которую ты отправил создателю:\n'
  '1. Лист всех пасхалок\n'
  '2. Специальную роль на сервере разроботчика (есть в его био(о себе))')


#kp!invisible

@client.command()
async def invisible(ctx):
  await ctx.send('_ _')
  await ctx.send('Ты нашёл одну из пасхалок!')


#kp!user_info

#@client.command(aliases = ['я'])
#async def user_info(ctx):
 # img = Image.new('RGBA', (400, 200), '#252920')
 # url = str(ctx.author.avatar_url)[:-10]
  #response = requests.get(url, stream = True)
 # response = Image.open(io.BytesIO(response.content))
 # response = response.convert('RGBA')
 # response = response.resize((100, 100), Image.ANTIALIAS)

  #img.paste(response, (15, 15, 115, 115))

 # idraw = ImageDraw.Draw(img)
 # name = ctx.author.name
 # tag = ctx.author.discriminator

  #headline = ImageFont.truetype('arial.ttf', size = 20)
  #undertext = ImageFont.truetype('arial.ttf', size = 12)

  #idraw.text((145, 15), f'{name}#{tag}', font = headline)
  #idraw.text((145, 50), f'ID: {ctx.author.id}', font = undertext)

  #img.save('karaproject_bot_user_card.png')

  #await ctx.send(file = discord.File(fp = 'karaproject_bot_user_card.png'))


#Команды для калькулятора

#Сложить

@client.command() 
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}")

#Вычесть

@client.command() 
async def sub(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}")

#Умножить

@client.command() 
async def multiply(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}")

#Разделить

@client.command() 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}")


#@client.event
#async def on_message( message ):
 # msg = message.content.lower()
  #if msg in hello_words:
   # await message.channel.send( 'Приветик! Как дела?' )
  #if msg in word_list1:
   # await message.channel.send('Ну это хорошо что хорошо')


@client.event
async def on_ready():
  print("Bot is ready!")

  await client.change_presence(activity=discord.Game(name=f"Живу на {len(client.guilds)} серверах! | kp!help")) 

keep_alive.keep_alive()

 





# Connect

client.run('token_here')




