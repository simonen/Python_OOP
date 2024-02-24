from project.hero import Hero
from project.elf import Elf
from project.muse_elf import MuseElf
from project.wizard import Wizard
from project.soul_master import SoulMaster
from project.dark_wizard import DarkWizard
from project.knight import Knight
from project.dark_knight import DarkKnight
from project.blade_knight import BladeKnight


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
print('-')
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
print('-')
muse = MuseElf("MMM", 14)
print(str(muse))
print('-')
wizard = Wizard("Wizzu", 511)
print(wizard)
print('-')
dizzy = DarkWizard("Dark Wizzy", 5)
print(dizzy)
print('-')
sol = SoulMaster("Sol", 5)
print(sol)
print('-')
knight = Knight('Knight', 10)
print(knight)
print('-')
dark = DarkKnight('Da11ight', 121)
print(dark)
print(dark.level)
print('-')
blade = BladeKnight('Palaqk', 322)
print(str(blade), ', class:', blade.__class__.__bases__[0].__name__)
