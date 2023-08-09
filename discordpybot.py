import discord
from discord.ext import commands


class Questionnaire(discord.ui.Modal, title='Questionnaire Response'):
    name = discord.ui.TextInput(label='Name')
    answer = discord.ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Howdy, {self.answer}!', ephemeral=True)

        #user = interaction.user
        #channel = interaction.channel
        channel = bot.get_channel(channel id)
        message = await channel.fetch_message(message id)
        #message = interaction.message
        #messageid =  1138606997172912238
        await message.edit(content=f'NEW RULE: {self.answer}')
        #new_message = f'{user.mention} answered: {self.answer}'
        #await channel.edit_message(message.id, content=new_message) no attribute called edit message


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id} )")

bot = Bot()

@bot.tree.command()
async def textbox(interaction: discord.Interaction):
    modal = Questionnaire()
    await interaction.response.send_modal(modal)

bot.run("token")