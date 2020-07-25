from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        elif "good morning" in message.content.lower():
            await message.channel.send("Good Morning! :sunrise:")
        elif "good night" in message.content.lower():
            await message.channel.send("Night and sweet dreams! :first_quarter_moon_with_face:")
        elif "and then he waddled away" in message.content.lower():
            await message.channel.send("*waddle waddle waddle*")
        elif "do you think waddle dee should be in smash?" in message.content.lower():
            await message.channel.send("YES")
        elif "can we get an f in the chat" in message.content.lower():
            await message.channel.send(":regional_indicator_f:")
        elif "colors weave into a spire of flame" in message.content.lower():
            await message.channel.send("Distant sparks call to a past still unamed...")
        elif "who's the best kirby in Waddling Gaming?" in message.content.lower():
            await message.channel.send("probably prix")
        elif "can we get a petfroge in the chat" in message.content.lower():
            await message.channel.send("https://images-ext-2.discordapp.net/external/H3akJEvJbTEc1ZPGqEU4wapDdZDQhOyul_9Bh3KkStU/https/cdn.discordapp.com/emojis/731940867547594793.gif")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
