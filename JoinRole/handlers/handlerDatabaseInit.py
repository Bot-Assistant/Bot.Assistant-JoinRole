import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

# Create the database if it does not exist
def databaseInit():
    if settingBot.databaseType == "MariaDB":
        # Table structure
        tableName = "addon_joinrole_roles"
        columns = [
            ["serverID", "BIGINT NOT NULL"], 
            ["roleID", "BIGINT NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        # Table structure
        tableName = "addon_joinrole_roles"
        columns = [
            ["serverID", "integer NOT NULL"], 
            ["roleID", "integer NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

