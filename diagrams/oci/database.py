# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OCI


class _Database(_OCI):
    _type = "database"
    _icon_dir = "resources/oci/database"


class AutonomousDatabaseWhite(_Database):
    _icon = "autonomous-white.png"


class AutonomousDatabase(_Database):
    _icon = "autonomous.png"


class DatabaseserviceWhite(_Database):
    _icon = "databaseservice-white.png"


class Databaseservice(_Database):
    _icon = "databaseservice.png"


# Aliases

ADB = AutonomousDatabase
ADBWhite = AutonomousDatabaseWhite
DBService = Databaseservice
DBServiceWhite = DatabaseserviceWhite
