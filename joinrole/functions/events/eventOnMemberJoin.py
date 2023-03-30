import addons.JoinRole.handlers.handlerJoinRole as handlerJoinRole
import services.serviceDiscordLogger as serviceDiscordLogger

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def onMemberJoin(member):
    # Get join role list
        joinRoleList = handlerJoinRole.listRole(member.guild.id)
        
        if joinRoleList != None:
            for role in joinRoleList:

                joinRole = discord.utils.get(member.guild.roles, id=role[0])

                await member.add_roles(joinRole)
