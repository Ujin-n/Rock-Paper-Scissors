# create the planets.txt
file = open('planets.txt', mode='w', encoding='utf-8')
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    file.write(planet + '\n')
file.close()
