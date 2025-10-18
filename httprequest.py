import requests
import http.client
import re

url = 'https://www.w3schools.com/python/demopage.php'
myheaders = {
    "Content-Type":"application/json", 
    ":authority": "en14.forgeofempires.com", 
    ":method":"POST",
    ":path": "/game/json?h=s2N4-ZvwOmThou6ZrfYOeAqw",
    ":scheme": "https"
      }

myobj = [
    {
        "__class__": "ServerRequest",
        "requestData": [],
        "requestClass": "CityProductionService",
        "requestMethod": "pickupAll",
        "requestId": 85
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            567,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 86
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            929,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 87
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            952,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 88
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            953,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 89
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            955,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 90
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            960,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 91
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            963,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 92
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            964,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 93
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1000,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 94
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1001,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 95
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1002,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 96
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1005,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 97
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1006,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 98
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1021,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 99
    },
    {
        "__class__": "ServerRequest",
        "requestData": [
            1054,
            1
        ],
        "requestClass": "CityProductionService",
        "requestMethod": "startProduction",
        "requestId": 100
    }
]

#http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
http.client._is_legal_header_name = re.compile(r':|\A[^:\s][^:\r\n]*\Z').match
x = requests.post(url,headers= myheaders, json = myobj)

print(x)