import requests as rq
import time
import json
import pyperclip

def mc_auth_token_into_refresh_token():
    code = input("Please input your Auth Token:")
    url = "https://login.live.com/oauth20_token.srf"
    client_id = input("Whats your client_id?If you don't know please input 00000000402b5328:")
    params = {
        "client_id": client_id,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": "https://login.live.com/oauth20_desktop.srf",
        "scope": "service::user.auth.xboxlive.com::MBI_SSL"
    }
    data = rq.get(url=url, params=params).text
    try:
        jsondata = json.loads(data)
        pyperclip.copy(data)
        print("CallBack from server:")
        print(data)
        print(">>>Access Token:\n")
        print(jsondata["access_token"])
        print(">>>Refresh Token\n:")
        print(jsondata["refresh_token"])
        print(">>>Token Expires in\n")
        print(jsondata["expires_in"])
        print("seconds.")
        print("The program will quit in 30s. All contents copied to clipboard.")
        time.sleep(30)
    except KeyError:
        print("Sorry! Can't process this token, please try again!")
        print("If it shows code invalid that means your code expired or doesn't exist.")
        print("If it shows wrong cliend_id that means your token was linked to another client_id.")
        print("Ask the peroson who gives you the token for help.\n\n")

def mc_refresh_token_refreshing():
    code = input("Please input your Refresh Token:")
    url = "https://login.live.com/oauth20_token.srf"
    client_id_re = input("Whats your client_id?If you don't know please input 00000000402b5328:")
    params = {
        "client_id": client_id_re,
        "refresh_token": code,
        "grant_type": "refresh_token",
        "redirect_uri": "https://login.live.com/oauth20_desktop.srf",
        "scope": "service::user.auth.xboxlive.com::MBI_SSL"
    }
    data = rq.get(url=url, params=params).text
    try:
        jsondata = json.loads(data)
        pyperclip.copy(data)
        print(data)
        print(">>>Access Token:\n")
        print(jsondata["access_token"])
        print(">>>Refresh Token\n:")
        print(jsondata["refresh_token"])
        print(">>>Token Expires in\n")
        print(jsondata["expires_in"])
        print("seconds.")
        print("The program will quit in 30s. All contents copied to clipboard.")
        time.sleep(30)
    except KeyError:
        print("Sorry! Can't process this token, please try again!")
        print("If it shows code invalid that means your code expired or doesn't exist.")
        print("If it shows wrong cliend_id that means your token was linked to another client_id.")
        print("Ask the peroson who gives you the token for help.\n\n")

print("Minecraft Token Request Client v1.0.0 by PWBC-China")
print("Fuctions:\n")
print("1.Get brand new tokens using the auth token")
print("2.Refresh an existing Refresh Token")
print("3.Exit Programm")
while True:
    answer = input("Which function do you want?")
    if answer == "1":
        mc_auth_token_into_refresh_token()
        continue
    elif answer == "2":
        mc_refresh_token_refreshing()
        continue
    elif answer == "3":
        break
    else:
        print("Error while handling input, please retype your choice.")
        continue
