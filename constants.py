from pathlib import Path # to import csv using relative paths with ease, without this it depends on IDE or environment configuration

# Create custom palette for colouring
type_palette = {
    "Bug": "#A8B820",  # Greenish
    "Dark": "#705848",  # Dark Brown
    "Dragon": "#7038F8",  # Purple
    "Electric": "#F8D030",  # Yellow
    "Fairy": "#EE99AC",  # Pink
    "Fighting": "#C03028",  # Reddish Brown
    "Fire": "#F08030",  # Orange
    "Flying": "#A890F0",  # Light Purple
    "Ghost": "#705898",  # Dark Purple
    "Grass": "#78C850",  # Green
    "Ground": "#E0C068",  # Sandy Brown
    "Ice": "#98D8D8",  # Light Blue
    "Normal": "#A8A878",  # Grayish
    "Poison": "#A040A0",  # Purple
    "Psychic": "#F85888",  # Pinkish Red
    "Rock": "#B8A038",  # Brownish
    "Steel": "#B8B8D0",  # Light Gray
    "Water": "#6890F0",  # Blue
}

# Initialize the global variable for data_frame
data_frame = None

data_path = Path(__file__).parent / "data" / "Pokemon.csv"
output_directory = Path(__file__).parent / "output"