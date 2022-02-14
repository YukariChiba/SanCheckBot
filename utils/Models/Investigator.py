import utils.Judgements.Creation as Creation


class Investigator:

    attributes = [
        "AGE", "STR", "CON", "DEX", "APP", "POW", "SIZ", "INT", "EDU", "LUK", "SAN", "HP", "MP", "MOV", "DB", "BUILD"
    ]

    skills_attributes = [
        "accounting",
        "anthropology",
        "archaeology",
        "art",
        "astronomy",
        "bargain",
        "biology",
        "chemistry",
        "climb",
        "conceal",
        "craft",
        "credit_rating",
        "cthulhu_mythos",
        "disguise",
        "dodge",
        "drive_auto",
        "electric_repair",
        "fast_talk",
        "first_aid",
        "geology",
        "hide",
        "history",
        "jump",
        "law",
        "library Use",
        "listen",
        "locksmith",
        "martial_arts",
        "mechanical_repair",
        "medicine",
        "natural_history",
        "navigate",
        "occult",
        "operate_heavy_machinery",
        "other_language",
        "own_language",
        "persuade",
        "pharmacy",
        "photography",
        "physics",
        "pilot",
        "psychoanalysis",
        "psychology",
        "ride",
        "sneak",
        "spot_hidden",
        "swim",
        "throw",
        "track"
    ]

    combat_skills_attributes = [
        "fist",
        "grapple",
        "headbutt",
        "kick",
        "axe",
        "club",
        "dagger",
        "knife",
        "rapier",
        "wabre",
        "wword",
        "handgun",
        "machine_gun",
        "rifle",
        "shotgun",
        "smg",
    ]

    def __init__(self):
        self.skills = {}
        self.combat_skills = {}
        for attribute in self.attributes:
            setattr(self, attribute, 0)
        for attribute in self.attributes:
            setattr(self, "init" + attribute, 0)
        for skill_attribute in self.skills_attributes:
            self.skills[skill_attribute] = 0
        for combat_skill_attribute in self.combat_skills_attributes:
            self.combat_skills[combat_skill_attribute] = 0

    def toJson(self):
        ret = {}
        for attribute in self.attributes:
            ret[attribute] = getattr(self, attribute)
        for attribute in self.attributes:
            ret["init" + attribute] = getattr(self, "init" + attribute)
        ret['skills'] = self.skills
        ret['combat_skills'] = self.combat_skills
        return ret

    def fromJson(j):
        i = Investigator()
        for attribute in i.attributes:
            setattr(i, attribute, j[attribute])
        for attribute in i.attributes:
            setattr(i, "init" + attribute, j["init" + attribute])
        i.skills = j["skills"]
        i.combat_skills = j["combat_skills"]
        return i
