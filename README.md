# **Party Tracker - A Dungeons and Dragons Role Playing Party Tracker**

# Table of Contents

## [Design](#design-1)

### Design

#### Entity Relationship Diagram

![Flow of Entity Relationship Diagram](/static/images/erd-pt.png)

##### Review of Models and Relationships

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
