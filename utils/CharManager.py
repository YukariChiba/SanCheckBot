import json
import os
from utils.Models.Investigator import Investigator
import utils.Judgements.Creation as Creation
from utils.Models.Effects import Effects


def SaveChar(c, uid):
    with open(os.getenv("DATA_DIR") + uid + ".json", "w") as f:
        json.dump(c.toJson(), f)


def InitSaveChar(uid, age=None):
    c = Investigator()
    c = Creation.CharInit(c, age=age)
    SaveChar(c, uid)
    return c


def RemoveChar(uid):
    if CharExists(uid):
        os.remove(os.getenv("DATA_DIR") + uid + ".json")
        return True
    else:
        return False


def ApplyChange(c, cg: Effects):
    for i in cg.attrs:
        setattr(c, i, max(0, getattr(c, i) + cg.attrs[i]))
    return c


def CharExists(uid):
    return os.path.isfile(os.getenv("DATA_DIR") + uid + ".json")


def ReadChar(uid):
    if CharExists(uid):
        with open(os.getenv("DATA_DIR") + uid + ".json") as f:
            return Investigator.fromJson(json.load(f))
    else:
        return None
