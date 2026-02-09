hp_damage = lambda h, dmg : h - dmg

damage = 20
hp = 100

print(f'Your character took {damage} points of damage')
#                       damage mispelt on prompt ^^
print(f'Your character has droped from {hp} hit points to \
{hp_damage(hp, damage)} hit points available')