# █▀█ █▄░█   █▀▄▀█ █▀▀ █▀▄▀█ █▄▄ █▀▀ █▀█   ░░█ █▀█ █ █▄░█
# █▄█ █░▀█   █░▀░█ ██▄ █░▀░█ █▄█ ██▄ █▀▄   █▄█ █▄█ █ █░▀█
import addons.JoinRole.functions.commands.commandAdd as funcAdd
import addons.JoinRole.functions.commands.commandDelete as funcDelete
import addons.JoinRole.functions.commands.commandList as funcList
import addons.JoinRole.functions.events.eventOnMemberJoin as funcEventOnMemberJoin

import addons.JoinRole.handlers.handlerDatabaseInit as handlerDatabaseInit

import addons.JoinRole.init as init

from services.serviceLogger import consoleLogger as Logger
import services.servicePermissionCheck as servicePermissionCheck
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()

class JoinRole(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    # EVENTS LISTENERS
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await funcEventOnMemberJoin.onMemberJoin(member)
    

    groupJoinRole = discordCommands.SlashCommandGroup("joinrole", "Various commands to manage join role")

    # Verify if the bot has the permissions
    @groupJoinRole.command(name="permissions", description="Check the permissions of the bot")
    async def cmdSFXPermissions(self, ctx: commands.Context):
        await servicePermissionCheck.permissionCheck(ctx, init.addonPermissions)

    #t ADD
    @groupJoinRole.command(name="add", description="Command to define the roles when users arrive.")
    async def cmdAdd(
        self,
        ctx: discord.ApplicationContext, 
        role: discord.Option(
            discord.SlashCommandOptionType.role,  
            required=True
        )
    ):
        await funcAdd.add(ctx, role)


    #t DELETE
    @groupJoinRole.command(name="delete", description="Command to remove a role from the newcomers list.")
    async def cmdDelete(
        self,
        ctx: discord.ApplicationContext,
        role: discord.Option(
            discord.SlashCommandOptionType.role,  
            required=True
        )
    ):
        await funcDelete.delete(ctx, role)


    #t LIST
    @groupJoinRole.command(name="list", description="Command to remove a role from the newcomers list.")
    async def cmdList(
        self,
        ctx: discord.ApplicationContext
    ):
        await funcList.list(ctx)
        


def setup(bot):
    if debug: Logger.debug("Loading Join Role")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(JoinRole(bot))
    
    