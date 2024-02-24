from project.band_members.musician import Musician


class Singer(Musician):

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.VALID_SKILLS[self.__class__.__name__]:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)

        return f"{self.name} learned to {new_skill}."
