# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-JoinRole"
version = "1.1.4"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "joinrole"

# Name of the file containing the cog
cogFile = "cogJoinRole"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "manage_roles",
    "send_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",

    # Permission to add a role to the list of roles given when a user joins the server
    "cmdJoinRoleAdd" : "joinrole.add",

    # Permission to remove a role from the list of roles given when a user joins the server
    "cmdJoinRoleDelete" : "joinrole.delete",

    # Permission to list the roles given when a user joins the server
    "cmdJoinRoleList" : "joinrole.list"
}