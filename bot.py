import discord
from discord.ext import commands

TOKEN = "MTQ2NTY3ODM1MzgyNTY2NTE1Nw.GBucl1.ZYAvCvpvDhmcfFQaaiyDpy8oYapeE9zNcBbH8I"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


class RoleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="(ஐ ﾉ壊れた風の朋友)", style=discord.ButtonStyle.primary)
    async def friend(self, interaction: discord.Interaction, button: discord.ui.Button):

        role = discord.utils.get(interaction.guild.roles, name="(ஐ ﾉ壊れた風の朋友)")

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("已移除身分組", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("已獲得身分組", ephemeral=True)


@bot.event
async def on_ready():
    bot.add_view(RoleView())
    print(f"機器人已上線：{bot.user}")


@bot.command()
async def roles(ctx):

    embed = discord.Embed(
        title="🎭 領取身分組",
        description="點擊下面按鈕領取",
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed, view=RoleView())


bot.run(TOKEN)