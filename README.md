# pip install gerstlix_python

## What is this? ##
Library for simplified access to the Gerstlix API

## Quick Guide ##
To access the methods of the module, you need to:
```py
import gerstlix_python
gx = gerstlixAPI(token="your_token")
```

## Example ##
```py
import gerstlix_python
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
.get_leader             : params = server, fractionId
.get_deputy             : params = server, fractionId
.get_members            : params = server, fractionId
.get_minister           : params = server, fractionId
.get_record_fraction    : params = server, fractionId
.get_status             : params = gameProject
.get_ghetto_territories : params = server
.get_old_players        : params = server
.get_rich_players       : params = server
.get_deputies           : params = server
.get_leaders            : params = server
.get_minister_list      : params = server
.get_records            : params = server
.get_ip                 : params = ip
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

Developer: travkacode
