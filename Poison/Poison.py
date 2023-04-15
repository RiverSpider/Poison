actions = []
with open('Input9.txt', 'r') as f:
    for line in f:
        actions.append(line.strip())

ingredients = []
for i, action in enumerate(actions):
    parts = action.split()
    ingredients.append(parts[1:])

spell = ''
cast = []
answer = []
for i, action in enumerate(actions):
    parts = action.split()
    for j, ing in enumerate(ingredients[i]):
        if ing.isdigit():
            answer.pop(int(ingredients[i][j])-1)
            ingredients[i][j] = cast[int(ingredients[i][j])-1]
    if parts[0] == 'MIX':
        spell += 'MX' + ''.join(ingredients[i]) + 'XM'
    elif parts[0] == 'WATER':
        spell += 'WT' + ''.join(ingredients[i]) + 'TW'
    elif parts[0] == 'DUST':
        spell += 'DT' + ''.join(ingredients[i]) + 'TD'
    elif parts[0] == 'FIRE':
        spell += 'FR' + ''.join(ingredients[i]) + 'RF'
    cast.append(spell)
    answer.append(spell)
    spell = ''


with open('Output.txt', 'w') as f:
    f.write(''.join(answer))