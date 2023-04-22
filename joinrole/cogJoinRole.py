# ADDON IMPORTS
import addons.JoinRole.init as init

import addons.JoinRole.functions.commands.commandRequirements as commandRequirements
import addons.JoinRole.functions.commands.commandAdd as commandAdd
import addons.JoinRole.functions.commands.commandDelete as commandDelete
import addons.JoinRole.functions.commands.commandList as commandList
import addons.JoinRole.functions.events.eventOnMemberJoin as eventOnMemberJoin

import addons.JoinRole.handlers.handlerDatabaseInit as handlerDatabaseInit

# BOTASSISTANT IMPORTS
from services.serviceLogger import consoleLogger as Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
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
        await eventOnMemberJoin.onMemberJoin(member)
    

    groupJoinRole = discordCommands.SlashCommandGroup("joinrole", "Various commands to manage join role")

    # Verify if the bot has the prerequisites permissions
    @groupJoinRole.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)

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
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the add command.", str(ctx.command))
        await commandAdd.add(ctx, role)


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
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the delete command.", str(ctx.command))
        await commandDelete.delete(ctx, role)


    #t LIST
    @groupJoinRole.command(name="list", description="Command to remove a role from the newcomers list.")
    async def cmdList(
        self,
        ctx: discord.ApplicationContext
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the list command.", str(ctx.command))
        await commandList.list(ctx)
        


def setup(bot):
    if debug: Logger.debug("Loading cog: " + init.cogName)
    handlerDatabaseInit.databaseInit()
    bot.add_cog(JoinRole(bot))
    
    