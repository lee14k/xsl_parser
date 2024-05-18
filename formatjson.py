# Original data
data = [
  {
    "type": "Fruit Trees",
    "title": "Apple, Braeburn",
    "description": "Medium to large fruits are green-striped with dark red.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Cortland",
    "description": "Bears heavy crops of large red-striped fruit with white flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Empire",
    "description": "Medium sized dark red, striped fruit.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Fuji",
    "description": "Medium sized fruits are reddish-green in color.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Gala",
    "description": "Medium sized fruits have golden-yellow skin with reddish blush.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Granny Smith",
    "description": "Large, waxy, smooth green skin with small white lenticels.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Honeycrisp",
    "description": "Very large fruits are scarlet-red over a yellow background.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Honeygold",
    "description": "Golden with red blush, very sweet.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, McIntosh",
    "description": "Medium to large, nearly round fruit with bright red skin.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Pink Lady",
    "description": "Attractive pink blush over a yellow undertone.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Red Delicious",
    "description": "Medium to large with red to striped skin.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, State Fair",
    "description": "Medium-sized fruit striped with reddish-orange over a yellow background.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Wealthy",
    "description": "Large red-skinned fruit with white pink-veined flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Wolf River",
    "description": "Pale yellow skin with a dull red blush on enormous fruit.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Yellow Delicious",
    "description": "Large with clear yellow skin, similar in shape to 'Red Delicious'.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apple, Zestar",
    "description": "Mostly red, crisp, with sweet and tart taste.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apricot, Chinese Mormon",
    "description": "Medium sized fruit with yellow to medium orange color and a red blush.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Apricot, Moorpark",
    "description": "Juicy, sweet fruit. Good for fresh eating, drying or canning.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Cherry, Montmorency",
    "description": "Fruit is large with brilliant red skin and firm yellow flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Cherry, North Star",
    "description": "A genetic dwarf, excellent for the home garden.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Peach, Contender",
    "description": "Zone 4 hardiness.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Pear, Bartlett",
    "description": "Medium to large yellow fruit with sweet and tender flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Pear, Summercrisp",
    "description": "Medium-sized fruit with green skin and crisp sweet flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Plum, Methley",
    "description": "Small to medium fruit with reddish skin and red flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Plum, Stanley",
    "description": "Large dark blue fruits with sweet, greenish-yellow, juicy flesh.",
    "className": "griditem"
  },
  {
    "type": "Fruit Trees",
    "title": "Plum, Toka",
    "description": "Large red-skinned fruits with yellow flesh.",
    "className": "griditem"
  }
]


# Initialize an empty list to hold the new structure
products = []

# Get the keys (indices) from the "PRODUCT NAME" dictionary
indices = data["PRODUCT NAME"].keys()

# Loop through the indices and construct the new product structure
for idx in indices:
    product = {
        "title": data["PRODUCT NAME"][idx],
        "type": data["PRODUCT TYPE"][idx],
        "description": data["DESCRIPTION"][idx],
    }
    products.append(product)

# Print the transformed structure without quotes around keys
print("[")
for product in products:
    print("  {")
    print(f"    type: '{product['type']}',")
    print(f"    title: '{product['title']}',")
    print(f"    description: '{product['description']}',")
    print(f"     className:'griditem',")

    print("  },")
print("]")