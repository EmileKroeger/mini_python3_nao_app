<?xml version="1.0" encoding="UTF-8" ?>
<Package name="mini_python3_nao_app" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="main" src="scripts/main.py" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
</Package>
