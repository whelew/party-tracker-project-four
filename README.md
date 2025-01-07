# **Party Tracker - A Dungeons and Dragons Role Playing Party Tracker**

# Table of Contents

## [Design](#design-1)

- [Entity Relationship Diagram](#entity-relationship-diagram)

## [Functionality](#functionality-1)

- [Views](#views)
- [Forms](#forms)

## [Bugs and Debugging](#bugs-and-debugging-1)

- [Integrity Error](#integrity-error)
- [Circular Import Error](#circular-import)

## [Credits](#credits-1)

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

#### delete_campaign

- This view allows a user to delete a prexisting campaign from their campaign list.
- When the user sends the POST request to delete the campaign, the campaign with the specified campaign_id will be deleted.
- It does this using campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)
- The message is yet to be set up correctly to let the user know they successfully deleted the campaign.
- This will be a future implementation.
- It uses @login_required which ensures that only authenticated users can delete campaigns. 

#### campaign_info

- This view is to allow the user to load an individual campaign to see it in more detail.
- In a future implementation it will display all characters and items assosicated with that campaign.
- It also requires an authenticated user through @login_required.

#### create_character

- This view allows the user to create a character within a campaign.
- It renders the create_character.html template.
- It uses CharacterForm from the forms.py to generate the fields for the user to use as inputs for their character.
- It uses campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user) verifies the current campaign belongs to the logged in user.
- Once the character is created the character will be linked to the campaign and saved to the database and the user will be redirected to the campaign_info page.
- It uses @login_required which ensures that only authenticated users can add or modify characters. 

#### delete_character

- This view allows the user to delete a previously made character within their campaign.
- It renders the confirm_delete_character.html template to double check the user wishes to delete the character.
- If True, the character will be deleted from the database and campaign.
- If False, the user will be redirected to the campaign_info page.
- When the user sends the POST request to delete the character, the character with the specified character_id will be deleted.

#### update_character_stat

- This view allows a user to adjust their characters attributes. 
- I took inspiration from how I programmed the delete_item view, which lets the user delete an item in the inventory without actually leaving the inventory page.
- This view allows the user to increment their attributes by 1 or decrement them by 1.
- The view requires a character_id, attribute and action arguement, using these arguements I can target specific attributes from a list within the view.
- The character_id will allow us to target the correct character.
- The attribute will be the specific attribute chosen.
- If the action 'increment' will increment the chosen attribute.
- If the action is 'decrement' will decrement the chosen attribute.
- This view requires a template to have a way to send the view these arguements.
- I used an anchor tag containing a django tag. Here is an example:
{% url 'update_character_stat' character.id 'strength' 'increment' %}
- This anchor tag is then placed within the same cell of the table as its relative attribute. In this case 'strength'.
- character.id is the characters id, and because it is inside a for loop I can use character.id to fetch the id.
- The 'strength' is the second argument refering to the attribute parameter.
- The 'increment' is the last argument refering to the action parameter.
- There is also another tag within the same cell however this will be targeting the 'decrement' action.
- The view also uses a current_value, attributes in D&D can not go below 1 or above 20, therefore I made sure to put some validation in 
using an if statement.
- If the current_value of the selected attribute is 20, then it can not be incremented and if it is 1, it can not be decremented.
- Lastly I had to make sure 'health' was seperate from the attributes in the if statement, as health should be and is allowed to go above 20.
Health can currently go to any number.      

#### home_page

- This is a very basic view.
- It was designed with the intention that when the url path is empty for example path(''), the user will be directed towards the homepage.
- It simply renders the home.html template.
- Within this tempalte users are able to login or signup if they are not currently.
- When the user is logged in 3 buttons will appear, campaigns, monster library and logout.

#### item_list

- This view is very similar to the monster_library view.
- It gets all item objects within the Item model.
- It returns all items within that model.
- It then renders the item_list.html where the table tag will be populated with all item objects.

#### add_item_to_inventory

- This view became very complicated.
- It was initally designed to add an item to an inventory.
- After first setting up the view to perform this function, because it rendered the character_inventory.html template.
I thought it was appropriate to make the view both add items to the user's character's inventory and also display the current inventory.
- The view begins by first retrieving the inventory associated with the specific character using character_id provided in the url.
- This ensures the inventory belongs to that character. I had an error with [Circular Imports](#circular-import) when programming this which I explain in the debugging section.
- If request.method == POST, the view processes the AddItemForm. It checks if the form is valid. 
- If it is, the view will either create a new InventoryItem or update the current quantity of items.
- If request.method == GET it will simply render an empty AddItemForm() and all items currently in the Inventory will be displayed.
- A useful feature that I added was the redirect, I orignally had it as form = AddItemForm() but doing it like this would have caused items to be duplicated once the page was refreshed.
Therefore using a redirect was a much safer option to avoid duplications.
- Combining both dispalying the inventory and adding items to the inventory helps keep the 
functionality kept in once place allowing users to view and edit their inventories from the same place.

#### delete_item

- This view allows a user to delete an item from their inventory.
- Unlike delete_character and delete_campaign, delete_item will not render a new template.
This was a concious decision as deleting an item is far less important than deleting a character or campaign.
- The user would find the task of deleting an item out of their inventory quite tedious after the first 3 times 
if the delete button redirected you to a different web page everytime.
- Therefore the view only redirects the user to the character_inventory page after the delete button has been clicked.
- I set up the delete button on the character_inventory template. It uses {% url 'delete_item' inventory_item.id %} as an action.
- This then uses the url path I set up for the view. Where the view will delete the specific item based on it id if the request.method == 'POST'.
- The user is then redirected to the page they are currently on allowing for a quick and easy removal of unwanted items.

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

#### CharacterForm

- This simplifies creating characters.
- It is directly to the Character model.
- It will show the fields that will need to be filled in.
- It is used in the create_character view to handle submissions for new characters.
- It automatically sends this new data to the database to be saved.
- It previously used a def __init__() method to override the default init method.
This was to allow users to select from a list of current campaigns and asign their character to that campaign.
- However during a mentor session, my mentor suggested that this feature was not needed, 
and during testing the new character was not even saved to the correct campaign.
- Therefore I decided to remove this feature.
- It will be commented out for now, during later implementations it might be useful to use this method to prepopulate 
character health and stats based on what class type the user selects.

#### AddItemForm

- This form allows users add items to their inventory.
- It will create a Item field and a Quantity field for the user to select from.
- It uses a querset to retrieve all items in the Item database, this will allow users to select from the item list.
- The intfield uses a min_value=1, this ensures the users can't add an item of quantity 0.

### Bugs and Debugging

#### Integrity Error

- Example:

IntegrityError at /accounts/signup/
insert or update on table "account_emailaddress" violates foreign key constraint "account_emailaddress_user_id_2c513194_fk_user_user_id"
DETAIL:  Key (user_id)=(25) is not present in table "user_user".

##### Main Issue:

The main issue with this error was my database was out of sync. I tried to manually fix it within my command line through commands such as:

- python3 manage.py shell
- python3 manage.py dbshell

- I tried many different approaches to fix this error, however, none of the attempts i made to fix the issue worked. 
- The database schema was correctly mapped however and I made sure all migrations were completed. 
- Everytime a user created a new account this error would appear. The user email was not being correctly associated with the user id.
- Users were not properly being created and saved to the user=user table which caused a foreign key violation when attempting to associate emails.
- I tried to ensure manually that the users were being saved correctly to the user_user table.
- Each I was presented with this error:
- Error with user 1: insert or update on table "account_emailaddress" violates foreign key constraint "account_emailaddress_user_id_2c513194_fk_user_user_id"
DETAIL:  Key (user_id)=(1) is not present in table "user_user".
- I tried to flush my database but ran into issues due to using a database link.


##### Main Solution:

- To fix this issue, I decided to delete my old database. 
- I first deleted the current link in my heroku DATABASE_URL and env.py file.
- I then got a fresh new database and link from Code Institute. 
- Using this new database link I changed both the heroku DATABASE_URL value and the one in my env.py file to the new value.
- I ran migrations again with python3 manage.py migrate.
- Created a new superuser.
- Then tested the new database by creating a new user through the allauth signup form.
- After testing no error was encountered and the integrity error was fixed.

###### Conclusion:

My inital thoughts on what caused the issue in the first place was due to my own fault. 
When i first started the project i created a superuser and a test signup before properly implementing the allauth package.
I believe this was the main cause of the error. 
This would have caused the allauth migrations to be out of sync with the rest of the database resulting in allauth not being able to automatically handle the post request correctly.
Thankfully this issue has now been resolved.

#### Circular Import


- Example:

- from campaign.models import Character
- ImportError: cannot import name 'Character' from partially initialized module 'campaign.models' 
(most likely due to a circular import) (/workspace/party-tracker-project-four/campaign/models.py)

##### Main Issue

This error occured because:

- campaign.models imported Inventory from the item app.
- item.models imported Character from the campaign app.
- This resulted in a circular import error, where each model required the other file to be fully loaded first.
This was not possible as python doesn't allow circular dependencies. 

##### Main Solution

The easiest fix for this bug was removing one of the imports from the other.

- Instead of directly import Character into the item.models, I instead used a string method calling 'campaign.Character'.
- This allowed Django to resolve the circular import at runtime.
- My database schema didn't change structure, so no migrations were needed.
- I did run makemigrations and migrate to ensure this was correct. 
- When these commands were used no migrations were made.

##### Conclusion

This was a relatively easy bug to fix, having DEBUG set to True quickly helped me identify the error as a circular import.
Resolving the issue with using a string method instead of importing the Character model was a lot more efficient and fixed the error straight away.
Although I created ERD's to help with model creation, in the future I will have to be more prepared with how my models will interact with one another.
Keeping this lesson in mind will help me avoid errors such as this. 

## Credits

1. [Django Documentation](https://docs.djangoproject.com/) was very useful in helping me understand and implement my models, views, forms and templates.
2. [Python Documentation](https://docs.python.org/) was helpful when handling custom logic in my models and views. It is a useful reference for when you are working with Python.
3. [Bootstrap Documentation](https://getbootstrap.com/docs/) was very helpful when structuring and styling my website. It allowed me to create a simply designed website which i could
then customise later with my own css style sheet.
4. [Stack Overflow](https://stackoverflow.com/) when troubleshooting coding issues and errors.
5. [W3Schools](https://www.w3schools.com/) is a helpful guide when after quick references.
6. [Django AllAuth Documentation](https://django-allauth.readthedocs.io/) when setting up the allauth user system.
7. [Google Fonts](https://fonts.google.com/) for helping choose an appropriate typography for my website.
8. [Slack](https://app.slack.com/) provided useful when also researching issues and bugs as I was able to look at other students projects and see how they fixed previous similar issues.
9. [Pixabay](https://pixabay.com/) is a great website to find free images to use for your website.
10. I would also like to thank my mentor Luke for his insight and support during this project.