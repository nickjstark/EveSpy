import tkinter as tk
import json, requests

baseURL = "https://esi.tech.ccp.is/latest/"
character_ids = {}
zkillURL = "https://zkillboard.com/api/losses/characterID/"


# class GUI(tk.Frame):
#     def __init__(self, master=None):
#         super(GUI, self).__init__()
#         self.master = master
#         self.input = tk.StringVar()
#         self.output = ""
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.text = tk.Text(self, width=50, height=25)
#         self.entry = tk.Entry(self, textvariable=self.input)
#
#         self.text.grid(row=1, column=0)
#         self.entry.grid(row=0, column=0)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Loss Info")
#     root.geometry("650x500")
#     gui = GUI(root)
#     gui.pack()
#     gui.mainloop()


# Need to get character ID from CCP API
def get_character_id(charName):
    '''
    Get the character ID from the character name
    :param charName: Characters name
    :return: character ID
    '''
    parameters = {
        'categories': 'character',
        'datasource': 'tranquility',
        'language': 'en-us',
        'search': charName,
        'strict': 'true'
    }
    r = requests.get(baseURL + 'search/', params=parameters)
    if r.status_code == requests.codes.ok and 'character' in r.json():
        character_ids[charName] = r.json()['character']
        cID = r.json()['character'][0]
        print(cID)
        return cID

def get_losses(cID):
    '''
    Take Character ID from get_character_id, and get recent losses from zKill
    :param cID: Character ID, retrieved from get_character_id function
    :return: recent loss information
    '''
    headers = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Tykho - Loss Info (Under Development)"
    }
    rz = requests.get(zkillURL + str(cID) + "/", headers=headers)
    print(json.dumps(rz.json(), indent=4, sort_keys=True))


cID = get_character_id(str(input("Enter a Pilot's name: ")))
print(get_losses(cID))