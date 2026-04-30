class Character:
    max_health = 100
    level = 1

    def __init__(self, naam, health, attack_power):
        self.naam = naam
        self.health = health
        self.attack_power = attack_power

    def ontvang_schade(self, schade):
        self.health = self.health - schade
        return self.health

    def genees(self, hoeveelheid):
        if hoeveelheid <= 0:
            return
        if self.health + hoeveelheid > self.max_health:
            self.health = self.max_health
        else:
            self.health += hoeveelheid

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def level_up(self):
        self.level += 1
        self.attack_power += 5
        self.max_health += 5

    def __str__(self):
        return f"{self.naam} Lv: {self.level} HP: {self.health} AP: {self.attack_power}"


class Warrior(Character):
    def __init__(self, naam, health, attack_power, armor):
        super().__init__(naam, health, attack_power)
        self.armor = armor

    def ontvang_schade(self, schade):
        return super().ontvang_schade(schade - self.armor)

    def shield_bash(self):
        return self.attack_power


class Mage(Character):
    def __init__(self, naam, health, attack_power, mana):
        super().__init__(naam, health, attack_power)
        self.mana = mana

    def cast_spell(self, spell_naam):
        match spell_naam:
            case "fireball":
                if self.mana >= 20:
                    self.mana -= 20
                    return self.attack_power + 5
            case "heal":
                if self.mana >= 15:
                    self.health += 25


class Rogue(Character):
    def __init__(self, naam, health, attack_power, stealth):
        super().__init__(naam, health, attack_power)
        self.stealth = stealth


class Battle:
    def fight(self, c1, c2):
        print(f"GEVECHT START: {c1.naam} vs {c2.naam}")

        count = 1
        while c1.is_alive() or c2.is_alive():
            print(f"Beurt {count}:")
            count += 1

            if isinstance(c1, Warrior):
                print(f"{c1.naam} valt aan! ({c1.attack_power} schade)")
                print(
                    f"{c2.naam} HP: {c2.health} -> {c2.ontvang_schade(c1.shield_bash())}"
                )

            if isinstance(c1, Mage):
                print(f"{c1.naam} cast fireball!")
                print(
                    f"{c2.naam} HP: {c2.health} -> {c2.ontvang_schade(c1.cast_spell("fireball"))}"
                )

            if isinstance(c1, Rogue):
                pass

            if not c2.is_alive():
                break

            print(f"Beurt {count}:")
            count += 1

            if isinstance(c2, Warrior):
                print(f"{c2.naam} valt aan! ({c2.attack_power} schade)")
                print(
                    f"{c1.naam} HP: {c1.health} -> {c1.ontvang_schade(c2.shield_bash())}"
                )

            if isinstance(c2, Mage):
                print(f"{c2.naam} cast fireball!")
                print(
                    f"{c1.naam} HP: {c1.health} -> {c1.ontvang_schade(c2.cast_spell("fireball"))}"
                )

            if isinstance(c2, Rogue):
                pass

            if not c1.is_alive():
                break


if __name__ == "__main__":
    warrior = Warrior("Aragorn", health=100, attack_power=15, armor=5)
    mage = Mage("Gandalf", health=80, attack_power=20, mana=100)
    rogue = Rogue("Legolas", health=90, attack_power=12, stealth=0.3)

    battle = Battle()
    battle.fight(warrior, mage)
