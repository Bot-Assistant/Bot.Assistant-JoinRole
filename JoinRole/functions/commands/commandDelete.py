import addons.JoinRole.handlers.handlerJoinRole as handlerJoinRole

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail    


async def delete(ctx, role):

    # PERMISSIONS CHECK
    import addons.JoinRole.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdJoinRoleDelete") == False:
        return

    #Remove BDD
    handlerJoinRole.deleteRole(ctx.guild.id, role.id)
    
    #Message Commande
    embed = discord.Embed(title="Join Role", description="Join role removed from configuration: " + role.name, color=settingColors.red)
    embed.set_thumbnail(url=settingThumbnail.membersIcons)
    await ctx.respond(embed=embed)
