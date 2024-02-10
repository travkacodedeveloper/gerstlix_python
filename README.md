# pip install gerstlix_python

## What is this? ##
Library for simplified access to the Gerstlix API

## Quick Guide ##
To access the methods of the module, you need to:
```py
from gerstlix_python import *
gx = gerstlixAPI(token="your_token")
```

## Example ##
```py
from gerstlix_python import *
gx = gerstlixAPI(token="your_token")

result = gx.get_members(server=3, fractionId=1)
print(result)
```
### Output ###
```json
{
    "serverId": 1, 
    "serverName": "serverName", 
    "fractionId": 1, 
    "fractionName": "fractionName", 
    "playersLastUpdate": "2023-10-13 13:03:40", 
    "playersCount": 1, 
    "playersInfo": [
        {
            "nickname": "nickname", 
            "accountId": 1, 
            "rang": 1, 
            "rankLabel": "rankLabel", 
            "isLeader": true, 
            "isOnline": false, 
            "gameId": -1, 
            "level": -1
        }
    ]
}
```

## Currently available methods ##
```
.get_leader             : params = server, fractionId | return => json
.get_deputy             : params = server, fractionId | return => json
.get_members            : params = server, fractionId | return => json
.get_minister           : params = server, fractionId | return => json
.get_record_fraction    : params = server, fractionId | return => json
.get_status             : params = gameProject        | return => json
.get_info               : params = server             | return => json 
.get_ghetto_territories : params = server             | return => json
.get_old_players        : params = server             | return => json
.get_rich_players       : params = server             | return => json
.get_deputies           : params = server             | return => json
.get_leaders            : params = server             | return => json
.get_minister_list      : params = server             | return => json
.get_records            : params = server             | return => json
.get_ip                 : params = ip                 | return => json
.check_work_methods     : params = None               | return => json
.count_methods          : params = None               | return => int
```
## Types of parameters ##
```
server       : INTEGER
fractionId   : INTEGER
gameProject  : STRING [ arz, marz, rrp ]
ip           : IPv4
----------------------------------------
arz          : Arizona Role Play
marz         : Mobile Arizona Role Play
rrp          : Rodina Role Play
```

## Other information ##
[Gerstlix site](https://gerstlix.com/)
The module is specially designed for Gerstlix
