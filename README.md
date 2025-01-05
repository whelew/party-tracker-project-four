# **Party Tracker - A Dungeons and Dragons Role Playing Party Tracker**

# Table of Contents

## [Design](#design-1)

- [Entity Relationship Diagram](#entity-relationship-diagram)

## [Functionality](#functionality-1)

- [Views](#views)
- [Forms](#forms)

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

## Functionality

### Views

#### monster_library

- This view returns all monsters stored in the Monster database model.
- It then renders this information to a monster_library.html template.
- A future implementation will increase the number of objects inside the database to add more content for users.
- All users can access the database without needing to be an authenticated user.

#### campaign_list

- This view displays all the campaigns created by the current user. 
- It uses @login_required which ensures that only authenticated users can access or modify their campaigns. 
- The campaign_list uses user=request.user to filter all campaigns so the user only sees their own campaigns.
- It returns the campaigns name and description.
- It then uses campaign.html as a template to render the request.

#### create_campaign

- This view allows users to create a new instance of the Campaign model.
- When the form is submitted it will be saved to the database.
- It also uses @login_required to ensure only authenticated users can create a new instance of Campaign.
- After a new campaign is created the user is redirected back to campaign.html through the campaign_list view.

#### campaign_info

- This view is to allow the user to load an individual campaign to see it in more detail.
- In a future implementation it will display all characters and items assosicated with that campaign.
- It also requires an authenticated user through @login_required.

### Forms

Django Forms is a useful tool to handle user input. During my research I found that if I used a form.py it would allow me to validate data from user
input and map it to my backend automatically.

#### Key Features:

- Automatically ensures data is valid.
- ModelForms integrates easily with the Django framework.

#### The Process:

- Create a form.py within your app.
- Create a python class within the form.
- Call this class when building your view.
- Then you will be able to render the form in your template using {{ form.as_p }}.
- {{ form.as_p }} this tells django each field from the form will be wrapped in a p.
- During development this has let me test to see if my model, view and form is working correctly.
I will most likely change this at a later date.
- {% csrf_token %} this is used to protect my site from cross-site attacks.

#### CampaignForm

- This simplifies creating and updating campaigns. 
- It is directly tied to the Campaign model.
- It is used in the create_campaign view to handle submissions for new campaigns.
- Thanks to Django it will automatically send the new data to the database.