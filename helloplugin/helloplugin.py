from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        elif "hey <@736351307841142915>" in message.content.lower():
            await message.channel.send("Hello! <:BandanaDeeWave:735641686348398713>")
        elif "good morning guys" in message.content.lower():
            await message.channel.send("Good Morning! :sunrise:")
        elif "good afternoon guys" in message.content.lower():
            await message.channel.send("Good Afternoon! :white_sun_cloud:")
        elif "good night guys" in message.content.lower():
            await message.channel.send("Night and sweet dreams! :first_quarter_moon_with_face:")
        elif "and then he waddled away" in message.content.lower():
            await message.channel.send("*waddle waddle (waddle)*")
        elif "until the very next day" in message.content.lower():
            await message.channel.send("*Bum bum bum bum ba-da-dum*")
        elif "do you think waddle dee should be in smash?" in message.content.lower():
            await message.channel.send("YES")
        elif "can we get an f in the chat" in message.content.lower():
            await message.channel.send(":regional_indicator_f:")
        elif "colors weave into a spire of flame" in message.content.lower():
            await message.channel.send("Distant sparks call to a past still unamed...")
        elif "can we get a petfroge in the chat" in message.content.lower():
            await message.channel.send("https://images-ext-2.discordapp.net/external/H3akJEvJbTEc1ZPGqEU4wapDdZDQhOyul_9Bh3KkStU/https/cdn.discordapp.com/emojis/731940867547594793.gif")
        elif "can I get a high five? " in message.content.lower():
            await message.channel.send(f"{ctx.author.mention} :orange_heart: https://media.discordapp.net/attachments/698534935723507755/737420105721577622/KirbyHigh52.gif")
        elif "can I get a hug? " in message.content.lower():
            await message.channel.send(f"{ctx.author.mention} :orange_heart: https://media.discordapp.net/attachments/698534935723507755/737420867591471194/KirbyHug.gif")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
