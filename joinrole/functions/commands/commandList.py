import addons.JoinRole.handlers.handlerJoinRole as handlerJoinRole

import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger   

import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail    


async def list(ctx):

    # PERMISSIONS CHECK
    import addons.JoinRole.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdJoinRoleList") == False:
        return

    # Get join role list
    joinRoleList = handlerJoinRole.listRole(ctx.guild.id)
    
    #Message Commande
    embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="List of configured join roles", color=settingColors.green)
    embed.set_thumbnail(url=settingThumbnail.membersIcons)
    
    if joinRoleList != []:
        for role in joinRoleList:
            roleName = serviceBot.classBot.getDiscord().utils.get(ctx.guild.roles, id=role[0])
            embed.add_field(name=roleName, value="Role ID is " + str(role[0]), inline=False)
    else:
        embed.add_field(name="No roles configured", value="Type the command /joinrole add to add roles to users who join the Discord.", inline=False)
    message = await ctx.respond(embed=embed)
    
    #Logs
    await serviceDiscordLogger.discordLogger.info("The list of join roles has been requested by  " + ctx.author.name, ctx.guild.id)