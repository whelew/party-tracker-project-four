# **Party Tracker - A Dungeons and Dragons Role Playing Party Tracker**

# Table of Contents

## [Design](#design-1)

- [Entity Relationship Diagram](#entity-relationship-diagram)

## Design

### Entity Relationship Diagram:

Below are the inital designs for my projects models.

- As a developer creating ERD's before beginning the project helps flesh out the relationships needed between each database.
This minimises and reduces the risk of any changes needed later on in the project.

- I have come to the conclusion I will need seven seperate models:
1. [User](#user)
2. [Campaign](#campaign)
3. [Character](#character)
4. [Inventory](#inventory)
5. [InventoryItems](#inventoryitems)
6. [Item](#item)
7. [Monster](#monster)

#### User
![Entity Relationship Diagram of User](/static/images/user-erd.png)

- The User model will be done using django-allauth.
- When a user creates a new account they will be paired with an id as a primary key. 
This id will then be used as a foreign key for when the player wishes to create a campaign. 

- The current design includes four fields:
1. id (primary key)
2. username
3. email
4. password

#### Campaign
![Entity Relationship Diagram of Campaign](/static/images/campaign-erd.png)

- The Campaign model uses user_id as a foreign key to ensure when a user creates a campaign it will be kept paired to that users account permanently.

- The Campaign model will include four fields:
1. id (primary key)
2. name
3. description
4. user_id (foreign key to User)

#### Character
![Entity Relationship Diagram of Character](/static/images/character-erd.png)

- The Character model includes campaign_id as a foreign key to ensure that characters created in one campaign will always be paired to that campaign. 

- The Character model will include eleven fields:
1. id (primary key)
2. name
3. class
4. hit_points
5. strength
6. dexterity
7. constitution
8. intelligence
9. wisdom
10. charisma
11. campaign_id (foreign key to Campaign)

#### Inventory
![Entity Relationship Diagram of Inventory](/static/images/inventory-erd.png)

- The Inventory model is seperate from the character model so it may interact with InventoryItems seperately.
The design of the website will include a template that will show the user the character model and inventory model on the same page.
To ensure the character shows the correct inventory, Inventory uses character_id as a foreign key so that the inventory can be correctly paired with the character.

- The Inventory model will include 2 fields:
1. id (primary key)
2. character_id (foreign key to Character)

#### InventoryItems
![Entity Relationship Diagram of InvetoryItems](/static/images/inventory-items-erd.png)

- The InvetoryItems model will store items from the Item model using item_id as a foreign key. 
- It the uses inventory_id as a foreign key to make sure the items are placed in the correct inventory.

- The InventoryItems model will include 3 fields:
1. id (primary key)
2. inventory_id (foreign key to Inventory)
3. item_id (foreign key to Item)
4. quantity


#### Item
![Entity Relationship Diagram of Item](/static/images/item-erd.png)

- The Item models main purpose is to be a database stocked full of items for the user to add to their players inventory.
- The items will be added to the InventoryItems database using the id as primary key. 
- However item_name might be a better choice when implementation production begins.

- The Item model will include 3 fields:
1. id (primary key)
2. name
3. description

#### Monster
![Entity Relationship Diagram of Monster](/static/images/monster-erd.png)

- The Monster model is designed to be a database full of monsters that a user may look at when wanting to start an encounter.
It is purposefully designed with D&D roleplaying in mind, where a dungeon master might wish to create a new encounter on the fly.

- The Monster model will include eight fields:
1. id (primary key)
2. name
3. challenge_rating
4. health
5. armour_class
6. description
7. type
8. size

![Flow of Entity Relationship Diagram](/static/images/erd-pt.png)

#### Review of Models and Relationships

Below are the relationships between each database model:

1.	User to Campaign (One-to-Many):
- A user can have multiple campaigns.
- Campaign includes a user_id as a Foreign Key to User.

2.	Campaign to Character (One-to-Many):
- A campaign can have many characters.
- Character includes a campaign_id as a Foreign Key to Campaign.

3.	Character to Inventory (One-to-One):
- Each character has a single inventory.
- Inventory includes a character_id as a Foreign Key to Character.

4.	Inventory to InventoryItems (One-to-Many):
- An inventory can have multiple items.
- InventoryItems includes an inventory_id as a Foreign Key to Inventory.

5.	InventoryItems to Item (Many-to-One):
- Each entry in InventoryItems corresponds to a single Item, but an Item can belong to multiple inventories.
- InventoryItems includes an item_id as a Foreign Key to Item.
