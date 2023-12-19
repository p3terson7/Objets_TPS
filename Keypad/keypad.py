from gpiozero import Button
from signal import pause

# Définir les broches GPIO pour les lignes et les colonnes
rows = [Button(17), Button(27), Button(22), Button(5)]  # Remplacez par vos numéros de broche GPIO
cols = [Button(6), Button(13), Button(19), Button(26)]  # Remplacez par vos numéros de broche GPIO

# Définir le layout des touches du pavé numérique
keypad = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Cette fonction sera appelée lorsqu'un bouton est pressé
def on_key_pressed(row, col):
    key = keypad[row][col]
    print(f"Touche pressée: {key}")

# Configuration des événements pour chaque bouton
for i, row in enumerate(rows):
    for j, col in enumerate(cols):
        def create_callback(row, col):
            return lambda: on_key_pressed(row, col)
        
        # Attacher un événement à chaque bouton
        row.when_pressed = create_callback(i, j)

pause()  # Attendez indéfiniment et répondez aux événements
