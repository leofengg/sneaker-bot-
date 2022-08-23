import discord
from stockx import search


TOKEN = ''

intents = discord.Intents().all()
bot = discord.Client(command_prefix='!', intents=intents)

#channelID = ''

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    #if message.channel.id != channelID:
        #return
    if message.content.split(' ')[0] == '!anya':
        query = message.content.replace('!anya ', '')

        item = search(query)

        embed = discord.Embed( title = item['title'], url = 'https://stockx.com/' + item['urlKey'])

        embed.set_thumbnail( url=item['media']['imageUrl'])

        embed.add_field( name = 'Color Way', value = item['colorway'])
        embed.add_field( name = 'Style ID', value = item['styleId'])
        embed.add_field( name = "Lowest Ask", value = item['market']['lowestAsk'])


        await message.channel.send(embed=embed)

bot.run(TOKEN)
