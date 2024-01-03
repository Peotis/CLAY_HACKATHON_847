import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode pengembangan
            if hasil[0] == "KRESEK\n" and hasil[1] >= 0.6:
                await ctx.send('Ini adalah sampah kresek')
                await ctx.send('Berikut adalah link refensi untuk  mendaur ulang sampah kresek :')
                await ctx.send('https://www.youtube.com/watch?v=e9yOgIAOyKY')
            elif hasil[0] == 'KARDUS\n' and hasil[1] >= 0.6:
                await ctx.send('Ini merupakan sampah kardus')
                await ctx.send('Berikut ini adalah link refensi untuk mendaur ulang sampah kardus : ')
                await ctx.send('https://www.youtube.com/watch?v=-fvlyHqSbZQ')
            elif hasil[0] == 'BOTOL\n' and hasil[1] >= 0.6:
                await ctx.send('Ini merupakan sampah botol')
                await ctx.send('Berikut ini adalah link refensi untuk mendaur ulang sampah botol : ')
                await ctx.send('https://www.youtube.com/watch?v=Pw5SHeNVCPI')
            elif hasil[0] == 'GELAS-PLASTIK\n' and hasil[1] >= 0.6:
                await ctx.send('Ini merupakan sampah gelas plastik')
                await ctx.send('Berikut ini adalah link refensi untuk mendaur ulang sampah gelas plastik : ')
                await ctx.send('https://www.youtube.com/watch?v=4oyizKR0zNg')
            else:
                await ctx.send('Sampah tidak terdeksi')

    else:
        await ctx.send('GAMBAR TIDAK VALID/GAADA >:/')

bot.run("TOKEN")
