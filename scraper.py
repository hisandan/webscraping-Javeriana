import requests


def merge_cookies(cookie_text, cookie_dict):
    text = cookie_text
    for key, value in cookie_dict.items():
    # print(key, value)
     cookie_text += "; "+key+"="+value   
     print(key, "   --", value)
    return cookie_text


def dict_to_cookie(dic):
    text = ""
    for key, value in dic.items():
    # print(key, value)
     text += "; "+key+"="+value   

    return text[2:]


url = "https://csg.javeriana.edu.co/psc/CS92GST/EMPLOYEE/SA/c/ESTABLISH_COURSES.CLASS_SEARCH.GBL"

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'es-419,es;q=0.9',
  'Connection': 'keep-alive',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'Cookie': 'ExpirePage=https://csg.javeriana.edu.co/psc/CS92GST/; PS_DEVICEFEATURES=new:1; PS_LASTSITE=https://csg.javeriana.edu.co/psc/CS92GST/; PS_LOGINLIST=https://csg.javeriana.edu.co/CS92GST; SignOnDefault=GUEST'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.cookies.get_dict(), "\n\n")
new_cookies_dict = response.cookies.get_dict()
fist_dict = new_cookies_dict

## GOING TO SECOND AUTH

import requests

url = "https://csg.javeriana.edu.co/psc/CS92GST/EMPLOYEE/SA/c/ESTABLISH_COURSES.CLASS_SEARCH.GBL?&"
cookie = "PS_DEVICEFEATURES=new:1"
cookie = merge_cookies(cookie, new_cookies_dict)

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'es-419,es;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': cookie,
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.cookies.get_dict(), "\n\n")
new_cookies_dict = response.cookies.get_dict()

print("\n\n", new_cookies_dict)
# new_cookies_dict = {**response.cookies.get_dict(), **new_cookies_dict}

#print(response.text)

## GOING TO RETRIEVING DATA


import requests

url = "https://csg.javeriana.edu.co/psc/CS92GST/EMPLOYEE/SA/c/ESTABLISH_COURSES.CLASS_SEARCH.GBL"

payload=r'ICAJAX=1&ICNAVTYPEDROPDOWN=0&ICType=Panel&ICElementNum=0&ICStateNum=4&ICAction=CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH&ICModelCancel=0&ICXPos=0&ICYPos=142&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=2U4%2F8m7CiNKLM4yNKG3bqR4%2F25umtY75uqL%2B3FPvO9w%3D&ICActionPrompt=false&ICTypeAheadID=&ICBcDomData=UnknownValue&ICPanelName=&ICFind=&ICAddCount=&ICAppClsData=&CLASS_SRCH_WRK2_STRM$35$=2230&SSR_CLSRCH_WRK_SSR_OPEN_ONLY$chk$4=N&SSR_CLSRCH_WRK_SUBJECT_SRCH$2=&SSR_CLSRCH_WRK_DESCR$10=algebra'


cookies_dict = {"BIGipServerpool_cs_guest" : "33626634.48411.0000",
"TS01351dd6":"011137a605695f40c8705b9409413c9f58436d8a9ecdf15a1a610460c17cc4fe4746d09c4c3cd6cb0135b16eb1c1d59ba8f262fb9d",
"ExpirePage": "https://csg.javeriana.edu.co/psc/CS92GST/",
"PS_LOGINLIST":"https://csg.javeriana.edu.co/CS92GST",
"PS_TOKEN": "!ozsFXce04/8s+/nhEAUGuz+AhI8oiWHG/fhHsxPdH5OwU+XmpzznrYnr//fL89SK7FsTq7eEDu12nyqEV+6riVdy1TZ4CVcUYnkY/jexQcWIlIsWFTZ/u+P9RWsLsbQy2CeZHSwDjMNv4yn6AxoDm2nwr6FkAwjoDnIg8Zq8O0WzIdIh9ztxT3CmXMc/ESc5BiTslEwei/TR6d87p7jf0rXR/305U5Ob8ajC9yL5cM6hpYZrOtZjQUDU1yaE0+NV2Qsx9iUCiru/PjPQHeYpBc8qycLpyUEEQ0y/KUP2c0IvORyNyphfttpV2AhPAMBFxzWODz1ZhabmFMbtgV8=",
"PS_TokenSite": "https://csg.javeriana.edu.co/psc/CS92GST/?javeriana-edu-co-CS-PORTAL-PSJSESSIONID",
"SignOnDefault": "GUEST",
"PS_LASTSITE": "https://csg.javeriana.edu.co/psc/CS92GST/",
"PS_DEVICEFEATURES":"width:1366 height:768 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0",
"psback": "%22%22url%22%3A%22https%3A%2F%2Fcsg.javeriana.edu.co%2Fpsc%2FCS92GST%2FEMPLOYEE%2FSA%2Fc%2FESTABLISH_COURSES.CLASS_SEARCH.GBL%3F%26%22%20%22label%22%3A%22B%C3%BAsqueda%20de%20Clases%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fcsg.javeriana.edu.co%2Fpsc%2FCS92GST%2FEMPLOYEE%2FSA%22%22",
"javeriana-edu-co-CS-PORTAL-PSJSESSIONID": "NtemcIMQP7t3gVPhAnUNDWr1JyJsXEf_!100792201",
"TS0160f120": "011137a6050ecdbd37cad2af84fa40c860d493a23916a0a535e69b2318793cf74496f107a3f0ab4e232790e50270f98e54ca081f15",
"PS_TOKENEXPIRE": "5_Oct_2022_04:39:27_GMT",

}
new_cookies_dict.pop('PS_LASTSITE', None)
new_cookies_dict.pop('SignOnDefault', None)
new_cookies_dict.pop('BIGipServerpool_cs_guest', None)
#new_cookies_dict.pop('TS01351dd6', None)
new_cookies_dict.pop('PS_LOGINLIST', None)
new_cookies_dict.pop('PS_DEVICEFEATURES', None)
#new_cookies_dict.pop('PS_TokenSite', None)
#new_cookies_dict.pop('ExpirePage', None)
#new_cookies_dict.pop('PS_TOKEN', None)
#new_cookies_dict.pop('PS_TOKENEXPIRE', None)
#new_cookies_dict.pop('javeriana-edu-co-CS-PORTAL-PSJSESSIONID', None)
#new_cookies_dict.pop('TS0160f120', None)
# new_cookies_dict.pop('PS_TOKEN', None)
print("going to set...")
for key, value in new_cookies_dict.items():
     print(key, "-----",value)
     cookies_dict[key] = value

#cookies_dict["PS_TOKEN"] = fist_dict["PS_TOKEN"]
cookies_dict["PS_TOKENEXPIRE"] = "adsf"
#cookie_default = merge_cookies (cookie_default,new_cookies_dict)
#print(cookie_default)
#cookie_default = 'BIGipServerpool_cs_guest=33626634.48411.0000; TS01351dd6=011137a605695f40c8705b9409413c9f58436d8a9ecdf15a1a610460c17cc4fe4746d09c4c3cd6cb0135b16eb1c1d59ba8f262fb9d; ExpirePage=https://csg.javeriana.edu.co/psc/CS92GST/; PS_LOGINLIST=https://csg.javeriana.edu.co/CS92GST; PS_TOKEN=!ozsFXce04/8s+/nhEAUGuz+AhI8oiWHG/fhHsxPdH5OwU+XmpzznrYnr//fL89SK7FsTq7eEDu12nyqEV+6riVdy1TZ4CVcUYnkY/jexQcWIlIsWFTZ/u+P9RWsLsbQy2CeZHSwDjMNv4yn6AxoDm2nwr6FkAwjoDnIg8Zq8O0WzIdIh9ztxT3CmXMc/ESc5BiTslEwei/TR6d87p7jf0rXR/305U5Ob8ajC9yL5cM6hpYZrOtZjQUDU1yaE0+NV2Qsx9iUCiru/PjPQHeYpBc8qycLpyUEEQ0y/KUP2c0IvORyNyphfttpV2AhPAMBFxzWODz1ZhabmFMbtgV8=; PS_TokenSite=https://csg.javeriana.edu.co/psc/CS92GST/?javeriana-edu-co-CS-PORTAL-PSJSESSIONID; SignOnDefault=GUEST; PS_LASTSITE=https://csg.javeriana.edu.co/psc/CS92GST/; PS_DEVICEFEATURES=width:1366 height:768 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; psback=%22%22url%22%3A%22https%3A%2F%2Fcsg.javeriana.edu.co%2Fpsc%2FCS92GST%2FEMPLOYEE%2FSA%2Fc%2FESTABLISH_COURSES.CLASS_SEARCH.GBL%3F%26%22%20%22label%22%3A%22B%C3%BAsqueda%20de%20Clases%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fcsg.javeriana.edu.co%2Fpsc%2FCS92GST%2FEMPLOYEE%2FSA%22%22; javeriana-edu-co-CS-PORTAL-PSJSESSIONID=NtemcIMQP7t3gVPhAnUNDWr1JyJsXEf_!100792201; TS0160f120=011137a6050ecdbd37cad2af84fa40c860d493a23916a0a535e69b2318793cf74496f107a3f0ab4e232790e50270f98e54ca081f15; PS_TOKENEXPIRE=5_Oct_2022_04:39:27_GMT; ExpirePage=https://csg.javeriana.edu.co/psc/CS92GST/; PS_DEVICEFEATURES=new:1; PS_LASTSITE=https://csg.javeriana.edu.co/psc/CS92GST/; PS_LOGINLIST=https://csg.javeriana.edu.co/CS92GST; PS_TOKEN=!2NmMGOm3SsWs1mHhEAUGuz+AhI8oiYsAcUuv4pOHXLyYGbkEekBbMHkhy2Nady6p8mEFWD969bZlvknUHfXE3jauKiGzRMB6QfEq93ulZtsrFf0Mjza2z0WMacpAP8zMqTTH5qFNAW+PSeUcCuRLqmiJZipwaGruv1Gbf7+rMALAzQZIpM5/V6fUp7JPhfzBqhlykKeBBbuJtk06EMST8+Heb6dAFPm3nEoPKGoAPx+DB13qtIq5cns8aLPFdUs2H1NGRku2pJ97f3WHBSAvy8v+zIhtxbhv88wML9cAoe+hXBDXQvywf/IW4LDzUruTp5tXBsc1YL7Cgw==; PS_TOKENEXPIRE=5_Oct_2022_03:17:49_GMT; PS_TokenSite=https://csg.javeriana.edu.co/psc/CS92GST/?javeriana-edu-co-CS-PORTAL-PSJSESSIONID; SignOnDefault=GUEST; TS01351dd6=011137a6053d72f289d63624b6e4d4179f83fe77350db2dda821a8be2c8b1d92c9b08b3d49bb36f19970396b79e007e4d42f843a10; javeriana-edu-co-CS-PORTAL-PSJSESSIONID=KfKmJkXbN76wkonuR6bSpOUg-glW9g_H!808463455; BIGipServerpool_cs_guest=50403850.48411.0000; TS0160f120=011137a6053d72f289d63624b6e4d4179f83fe77350db2dda821a8be2c8b1d92c9b08b3d49bb36f19970396b79e007e4d42f843a10'
cookie_default = dict_to_cookie(cookies_dict)
headers = {
  'Accept': '*/*',
  'Accept-Language': 'es-419,es;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': cookie_default,
  'Origin': 'https://csg.javeriana.edu.co',
  'Referer': 'https://csg.javeriana.edu.co/psc/CS92GST/EMPLOYEE/SA/c/ESTABLISH_COURSES.CLASS_SEARCH.GBL?&',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(cookie_default)

print(response.text)




