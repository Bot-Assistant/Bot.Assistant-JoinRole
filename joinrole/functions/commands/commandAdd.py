import addons.JoinRole.handlers.handlerJoinRole as handlerJoinRole

import services.serviceBot as serviceBot

import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail      


async def add(ctx, role):
    
    # PERMISSIONS CHECK
    import addons.JoinRole.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdJoinRoleAdd") == False:
        return

    #Ajout BDD
    handlerJoinRole.addRole(ctx.guild.id, role.id)
    
    #Message Commande
    embed = serviceBot.classBot.getDiscord().Embed(title="Join Role", description="New join role added: " + role.name, color=settingColors.green)
    embed.set_thumbnail(url=settingThumbnail.membersIcons)
    await ctx.respond(embed=embed)
