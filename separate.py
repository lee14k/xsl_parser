import json
from collections import defaultdict

# Original data
data = [
    {"type": "Flowering Shrubs", "title": "Almond, Pink Flowering", "description": "Double pink flowers in early spring.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Althea, Lil' Kim Red", "description": "Carmine-red blooms.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Althea, Magenta Chiffon", "description": "Magenta-purple powderpuff blooms.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Azalea, Mandarin Lights", "description": "Orange flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Balloon Flower, Sentimental Blue", "description": "Balloon-shaped buds that open to saucer-like blue flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Barberry, Rose Glow", "description": "New foliage is pink with splash of cream 4' height.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Barberry, Sunjoy Orange Pillar", "description": "Vivid orange foliage, narrow growth habit.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Barberry, Sunjoy Sequins", "description": "Colorful new growth variegation of white, pink and mint green.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Burning Bush, Dwarf", "description": "Rounded plant with purple-red fall color and corky bark.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Butterfly Bush, Lo & Behold Pink Micro Chip", "description": "Dwarf form with orchid pink blooms.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Butterfly Bush, Miss Violet", "description": "Violet flower.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Butterfly Bush, Royal Red", "description": "Purple red flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Buttonbush, Sugar Shack", "description": "Red fruit, glossy red tip foliage native.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Chokeberry, Low Scape Mound", "description": "Stays 2' tall and wide with black fruit.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Dogwood, Bailey's Red Twig", "description": "Bright red stems, white flowers, blue berries.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Dogwood, Variegated", "description": "Variegated foliage with bright red winter branches.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Elderberry, Black Lace", "description": "Lacy purple black foliage.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Elderberry, Lemony Lace", "description": "Bright yellow foliage.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Forsythia, Show Off", "description": "Abundant large golden flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Honeysuckle, Goldflame", "description": "Pink buds to yellow flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Annabelle", "description": "Large white blooms.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Climbing", "description": "Produces white flowers in late June to early July with a slight fragrance.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Eclipse", "description": "Deep purple foliage with red flowers. Mophead", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Endless Summer", "description": "Blue mophead flower.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Endless Summer Bloomstruck", "description": "Pink/blue mophead flower.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Endless Summer Summer Crush", "description": "Big raspberry red or neon purple blooms. Mophead", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Fire Light", "description": "White flowers that finish rich red.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Limelight Prime", "description": "Lime green flowers. Improved Limelight.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Pinky Winky", "description": "Two toned flower heads white/pink.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Hydrangea, Quick Fire Fab", "description": "Early blooming paniculata, large blooms.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Lilac, Bloomerang Dark Purple", "description": "Reblooming dark purple flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Lilac, Bloomerang Purpink", "description": "Rebloomer with pink to purple flowers. 3-5' tall.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Ninebark, Ginger Wine", "description": "Orange/red to burgundy foliage.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Ninebark, Summer Wine Black", "description": "Very dark foliage, white flowers in spring; 5-6' tall and wide.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Ninebark, Tiny Wine", "description": "Compact form with dark maroon foliage.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Potentilla, Happy Face Pink Paradise", "description": "Clear pink semi-double flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Potentilla, Happy Face Yellow", "description": "Extra-large, bright yellow flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Rhododendron, PJM Elite", "description": "Lavender pink flower and slightly more compact than PJM.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "St. John's Wort, Gemo", "description": "Yellow flowers in summer.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Summersweet, Ruby Spice", "description": "Reddish pink flower in summer.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Viburnum, Common Snowball", "description": "3in diameter clusters of white flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Weigela, Midnight Sun", "description": "Dwarf with orange-red foliage.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Weigela, My Monet", "description": "Pink/white/green variegated foliage.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Weigela, Sonic Bloom Wine", "description": "Rebloomer with dark foliage and pink flowers.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Weigela, Wine & Roses", "description": "Dark burgundy foliage with pink bloom.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Willow, Dappled", "description": "Foliage mottled in white, green and pink.", "className": "griditem"},
    {"type": "Flowering Shrubs", "title": "Witchhazel, Vernal", "description": "Yellow to orange flowers in late winter to early spring.", "className": "griditem"}
]

# Separate data by type
separated_data = defaultdict(list)
for item in data:
    separated_data[item["type"]].append(item)

# Function to format JSON without quotes around keys
def json_without_quotes(data):
    json_str = json.dumps(data, indent=2)
    # Replace only the key quotes, not the value quotes
    json_str = json_str.replace('{\n  "', '{\n  ').replace('",', ',').replace('": ', ': ').replace('\n  "', '\n  ').replace('\n]', ']')
    return json_str

# Write each type to a separate JSON file
for type_name, items in separated_data.items():
    filename = type_name.replace("/", "_").replace(" ", "_") + ".json"
    with open(filename, 'w') as f:
        formatted_json = json_without_quotes(items)
        f.write(formatted_json)
    print(f"Saved {len(items)} items to {filename}")
    