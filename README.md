# **Party Tracker - A Dungeons and Dragons Role Playing Party Tracker**

# Table of Contents

## [Design](#design-1)

- [Wireframes](#wire-frames)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [User Stories](#user-stories)
- [Color Scheme](#color-scheme)
- [Typography](#typography)

## [Functionality](#functionality-1)

- [Views](#views)
- [Forms](#forms)

## [Testing](#testing-1)

- [Manual](#manual-testing)
- [Automated](#automated-testing)

## [Bugs and Debugging](#bugs-and-debugging-1)

- [Integrity Error](#integrity-error)
- [Circular Import Error](#circular-import)

## [Future Implementations](#future-implementations-1)

- [Community Page](#community-page-1)
- [Contact Page](#contact-page-1)
- [Chat Box](#chat-box)
- [Invite to Campaign](#invite-to-campaign)

## [Overview](#overview-1)

## [Deployment](#deployment-1)

## [Credits & Technologies](#credits--technologies-1)

## Design

### Wire Frames

The wire frames were the first thing I worked on when designing my website. The final product may not look exactly like the wireframes, 
however being able to visualise the website allowed me to plan out the structure of each page but also the models I would need. 

#### Login Page
- My initial idea for the login page was going to pay tribute to how I remember the classic runescape login form. I wanted to have 
the login box directly in the middle surronded by two images. I was able to achieve what I had imagined with it as I was able to find a 
good free source image to use for my background.
![Image of login page wireframe](/static/images/login-wireframe.png)



#### Home Page
- Initally the home page was going to be seperate from the login page and act as a news area where updates would be posted.
However I did not have enough time to get that implemented and the project already has a lot of detailed functions within the views
I would love to implement this feature at another time. The home page became a shared page with the login page.
![Image of home page wireframe](/static/images/home-wireframe.png)


#### Campaign Page
- The campaign page is very similar to my original design, however the add and delete campaign buttons exist within the actual
campaign table.
![Image of campaign page wireframe](/static/images/campaign-wireframe.png)


#### Campaign Detail Page
- The original design for the campaign page was quite bold. This is one of the designs that made me really have to think about how
I could create models that would allow for new characters to be added, with inventories and then the ability to add an item.
The design is very different from how it currently looks but I would love to be able to get the website looking like this one day.
![Image of campaign detail page wireframe](/static/images/campaign-detail-wireframe.png)

#### Community Page
- Originally I had planned a lot of features for my website, after a initial meeting with my mentor I showed him my wireframes and 
he mentioned that covering such a wide variety of features will be a very difficult challenge. Therefore I decided to focus on the main
purpose of the website and focused on the features that linked to the purpose the most.
![Image of community page wireframe](/static/images/community-wireframe.png)

#### Contact Page
- I wanted to be able to add a contact page but due to time constraints and the detail that my models, views and forms required it was 
difficult to implement every original feature and idea.
![Image of contact page wireframe](/static/images/contact-wireframe.png)

#### Monster Library
- The monster library turned out just like I had imagined.
![Image of monster library page wireframe](/static/images/monster-library-wireframe.png)



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

1. User to Campaign (One-to-Many):

- A user can have multiple campaigns.
- Campaign includes a user_id as a Foreign Key to User.

2. Campaign to Character (One-to-Many):

- A campaign can have many characters.
- Character includes a campaign_id as a Foreign Key to Campaign.

3. Character to Inventory (One-to-One):

- Each character has a single inventory.
- Inventory includes a character_id as a Foreign Key to Character.

4. Inventory to InventoryItems (One-to-Many):

- An inventory can have multiple items.
- InventoryItems includes an inventory_id as a Foreign Key to Inventory.

5. InventoryItems to Item (Many-to-One):

- Each entry in InventoryItems corresponds to a single Item, but an Item can belong to multiple inventories.
- InventoryItems includes an item_id as a Foreign Key to Item.

### User Stories

- User stories were a useful and producive tool for designing the website. It allowed me to think about being both a user and 
a developer. 
- It also helped focus my workflow, allowing me to focus on the most important factors first and leaving the less important features for 
another time.

#### Structure

I created a user story template to help me populate my issues faster and then allowing me to get them associated with my project swiftly.
The template consisted of:

1. An empty title
2. As a **role** I can **capability** so that **received benefit**
3. **Acceptance Criteria:**
- Acceptance criteria 1
- Acceptance criteria 2
- Acceptance criteria 3

This allowed me to quickly name the user story, write about the needs of a feature for a site user or a developer.
What it will do and why it will be of benefit. Following on from this will be a list of acceptance criteria before the user story
can be marked as closed.

![User Story Template Image](/static/images/user-story-template.png)


#### Labels

Using a label system also made the decision making easier.

##### Must Do
A must do label told me that without fail this task needs to be completed.

##### Should Do
A should do label told me that this feature needs adding when it is next possible.

##### Could Do
A could do label told me that if I get time and I have no other important features that need working on then I will be able to focus my 
time on implementing this feature.

##### Won't Do
A won't do label told me that I will not work on this feature at all as it will either take to much time or the feature is of no value to
the user or developer.

#### Workflow

Overall the user stories were very useful. I believe I should have been more prepared when planning my user stories as during production I 
found myself having to write new issues and add them. The benefit of this and also argument in favour of how I did my approach was that I was 
keeping in line with an agile mindset. I would review my user stories, adjust the labels, create new user stories as my project developed, both for 
site users and developers. I wasn't always perfect at keeping track of them at times, I found myself realising I had already finished one of the user 
stories by working in another. With more practice and refinement I will get a lot more adept at using them. It is a useful tool to know and I have learnt
alot from working with user stories as it allowed me to have a visual representation of my production workflow. 

Below is a visual representation of my workflow whilst using user stories.

<details>
  <summary>User Story WorkFlow Images</summary>
  ![user story one](/static/images/user-story-one.png)
  <img src="/static/images/user-story-one.png" alt="user story one"/>
  <img src="/static/images/user-story-two.png" alt="user story two"/>
  <img src="/static/images/user-story-three.png" alt="user story three"/>
  <img src="/static/images/user-story-four.png" alt="user story four"/>
  <img src="/static/images/user-story-five.png" alt="user story five"/>
  <img src="/static/images/user-story-six.png" alt="user story six"/>
  <img src="/static/images/user-story-seven.png" alt="user story seven"/>
  <img src="/static/images/user-story-eight.png" alt="user story eight"/>
</details>

### Color Scheme

The asthetic of the website went through a few ideas, I originally wanted to make a theme selector button which would allow the user
to select a required theme. I was going to have D&D inspired themes such as, a dark dungeon, a forest, arcane magic. During the production
the theme was not a major priorty as a lot of focus was required on the functionality of the website. 

However the current design is working well, the color scheme works well together and I was able to finalise my design on the website [Coolers](https://coolors.co/).

Here is a picture of the latest design:

![Image of color scheme](/static/images/coolers-board.png)

### Typography

I wanted to use a typography that really captured the essence of fantasy so I went with a classic Uncial Antiqua for all my headings and IM Fell English for 
all other text.

#### Uncial Antiqua
![Image of Uncial Antiqua Typography](/static/images/google-font-uncial.png)

#### IM Fell English
![Image of IM Fell English Typography](/static/images/google-font-im-fell.png)


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
- It previously used a def **init**() method to override the default init method.
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

## Testing

### Manual Testing

| Function/Feature | Test Performed | Expected Outcome | Final Outcome | Pass |
| :--------------: | :------------: | :--------------: | :-----------: | :--: |
| Click sign up button. | Clicked register on the navbar or the signup button.  | User will be redirected to signup.html | User is correctly redirected to signup page. | Pass |
| Signing up to the website | User inputs valid data into signup fields. | User successfully signs up and is redirected to home page. | User successfully signs up and is redirected to homepage | Pass |
| Click the login button home page | Clicked login button on hompage or navbar. | User will be redirected to login.html template. | User is successfully redirected to login page. | Pass |
| Click the login button login page | Clicked the login button after filling fields with valid data. | User will be signed into their existing account. | If the user has an account the user is successfully signed in, homepage is loaded with user authenticated features. | Pass |
| Click logout button on navbar or home page | Clicked logout button on navbar or homepage. | User will be redirected towards logout.html template. | User is successfully redirected to the logout page. | Pass |
| Click signout button on signout page | Clicked signout button on logout page | User will be signed out and redirected towards home page. | User is successfully redirected to homepage after signing out, all authenticated features are now unavailable. | Pass |
| Click home button on navbar | Clicked home button on the navbar. | User will be redirected towards homepage. | User is successfuly redirected towards homepage. | Pass |
| Click campaign button on navbar or homepage | Clicked campaign button on the navbar or homepage. | If user is signed in they will be redirected towards campaign.html template | If user is signed in they will be successfully redirected towards campaign page. | Pass |
| Click item button on navbar | Clicked item button on navbar | User will be redirected to the item library tempalte.  | User is successfully redirected towards item library page. | Pass |
| Click Monster Library button on navbar or home page | Clicked monster library button on navbar or homepage. | User will be redirected towards monster library template. | User is successfuly redirected towards the monster library. | Pass |
| Load campaign.html | Campaign.html template on load shows users current campaigns. | If user has no campaigns, no campaigns will be shown, create new campaign button is displayed. | User without any campaigns is shown empty table with an add campaign button within it. | Pass |
| campaign.html Add Campaign | Clicked create new campaign, user is redirected to create_campaign.html. | User will be redirected towards create_campaign.html. | User is successfully redirected to create campaign page. | Pass |
| create_campaign.html add campaign | Added valid data to create character form and added campaign. | The user after adding valid data to the fields and clicking create campaign will be redirected to campaign.html with their newly created campaign being displayed. | User is successfully redirected to the campaign page where their newly created campaign is displayed. | Pass |
| Click delete campaign on campaign page | Clicked delete campaign button. | User will be redirected to confirm_delete.html template. | User is successfully redirected to confirm delete page. | Pass |
| Click confirm delete | Clicked confirm delete button | If confirm delete is clicked it will delete the campaign it is associated with and be removed from the users display. | Once clicked the campaign is successfully deleted from the database and removed from the users display. | Pass |
| Click cancel delete | Clicked cancel delete button | The user will be redirected to campaign.html template. | The user is successfully redirected to the campaign page. | Pass |
| Click campaign name button | Clicked the button associated with campaigns name. | User will be redirected to campaign_info.html template. | User is successfully redirected to campaign info page where all campaign information will be displayed. | Pass |
| Click add character | Click add character button | If user clicks add character they will be redirected to create_character.html template. | User is successfully redirected to create character page. | Pass |
| User has no characters | If the user has no characters no characters will be displayed in campaign_info.html template. | User will not have any characters populating their campaign info page. | A user who has no characters has the option to add characters but no characters are displayed. | Pass |
| Click add character to campaign button. | Valid data is passed into fields and the add character to campaign button is clicked. | User will be able to add a new character to their current campaign. | User is able to successfully add a new character to their campaign. | Pass |
| Click return to {title of their campaign button}. | Clicked return to {title of their campaign button} | User will be redirected back to campaign_info.html template. | USer is successfully redirected to their campaign info page. | Pass |
| Invalid Input Create Character | Invalid data is passed into all fields. | If user inputs invalid data they will be asked to change their input before being able to create new character. | User inputs invalid data, for example 21 in a stat field, and is told it needs to be equal to or lower than 20. | Pass |
| Click delete character on campaign info page | Clicked delete character button on the campaign info page. | User will be redirected to confirm_delete_character.html templte. | User is successfully redirected towards delete character page. | Pass |
| Confirm delete, delete character page | Clicked confirm delete button. | User will delete associated character and be redirected towards campaign info page. | User successfully deletes character from the database, they are redirected towards campaign info page and the character is no longer displayed. | Pass |
| Cancel delete, delete character page | Clicked cancel delete button. | User will be redirected to campaign info page. | User is successfully redirected to campaign info page. | Pass |
| Click inventory button | Clicked inventory button on campaign info page. | User will be redirected to inventory.html. | User is successfully redirected to inventory page. | Pass |
| Inventory Page | Load inventory page. | Associated characters inventory will be displayed. Add Item button will also be displayed. | User can view current characters inventory and has the option to add items. | Pass |
| Click add item | Valid data is passed into fields and the add item button is clicked | User is able to add items to their inventory, new items added will be displayed in their inventory. | If the user adds valid data into the fields, they can successfully add an item to their inventory, it is then displayed in their inventory. | Pass |
| Validators add item | Invalid data is passed into fields and the add item button is clicked. |If the user adds invalid data they will be asked to input a valid form of data into the specific field. | User is unable to add an item with invalid data. | Pass |
| Click delete item (X) | Clicked (X) delete item button. | User will click the (X) delete item button and the current item will be removed from their inventory. | User is able to successfully remove an item from their inventory. | Pass |
| Click return to campaign button | Clicked return to campaign button. | The user will be redirected to the campaign info page. | User is successfully redirected towards the campaign info page. | Pass |
| Update character attributes | Clicked (+) or (-) button. | Clicking this button will increment (+) or decrement (-) targeted attribute. | User is able to successfully adjust attributes. | Pass |
| Update character attributes validators. | Clicked (+) or (-) button. | User will be unable to adjust the 6 stat attributes (excluding health) past 20 or below 1. | User is successfully unable to adjust the 6 stat attributes past 20 or below 1. | Pass |
| Footer icons | Clicked footer icon. | User will be redirected to associated website. | User is successfully redirected towards targeted sight, example, user clicked discord logo and is taken to a seperate tab and the discord website is loaded. | Pass |



### Automated Testing

- Django uses a standard python library module called [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
  to run automated tests.
- Automated tests are important as it is a useful way to ensure your application is working correctly.
- Each test was created within either a test_forms.py file or a test_views.py file. This was to allow seperation from the views and forms.
- Here is a screenshot of my completed automated tests.
- 26 tests in total.
- 0 issues found.

![Image of 26 Automated Tests completed without issue.](/static/images/unittest.png)

#### View Tests

The test_views.py are where the main percentage of my automated tests reside. Coding the tests was challenging at first,
this was mostly due to the way my models interact with one another. As a user creates a campaign, within that campaign a user can have
create many characters, each character then has one individual inventory. Therefore when I wanted to test my views I needed to create instances
of every model: User, Campaign, Character, Inventory, Item, InventoryItem. After being able to complete one test, the methodology became
more understandable and easier to implement. I was able to reuse part of my code when creating these instances.

- DRY (Don't Repeat Yourself). Trying to keep inline with DRY principles, within each app I would normal create only one instance of the
  models. For instance CampaignTest, defines the setUp().
- Here is the CampaignTest example:
- self.user = User.objects.create_user(username='test', password='password123', email='test@test.com')
- self.campaign = Campaign.objects.create(name='Testcampaign', description='This is a test', user=self.user)
- self.character = Character.objects.create(
  name='Gandalf',
  character_class = 'wizard',
  health = 50,
  strength = 18,
  dexterity = 1,
  constitution = 20,
  intelligence = 20,
  wisdom = 20,
  charisma = 20,
  campaign=self.campaign
  )
- self.inventory = Inventory.objects.get(character=self.character)
- login_success = self.client.login(username='test', password='password123')
- self.assertTrue(login_success)

Here I define my User, Campaign, Character and Inventory, I also pass in a user authentication check as most of my views
require the user to be logged in as I use the @login_required decorator.

- After creating instances of my models, I am then able to test all of my other views from within this one test.
- This helped me stick to a DRY rule of thumb and reduce the amount of code that would have been repeated if i hadn't.

#### Form Tests

The test_forms.py were created to test all forms.py. I only had a total of 3 form classes in total.
I detail their design in the prior section. When designing the tests for these classes I had to take into account
all the validation processes required when a user would fill the field inputs.

- Firstly I checked if the form was valid. I would pass a valid entry of data to the form and then use assertTrue to check
  that the data being passed is valid. If it was the test would pass.
- Secondly I needed to check if when the data passed to the form is in valid, that it is recognised as invalid. Using assertFalse
  I was able to check that the data being passed in was invalid. The difficulty with checking if that data was invalid was trying to
  maintain a DRY principle. Therefore I used for loops to help pass in different invalid fields or values throughout
  the forms.

### Coverage Report

Here is a coverage report using [coverage](https://coverage.readthedocs.io/en/7.6.10/)

|                             Name                              | Stmts | Miss | Cover |
| :-----------------------------------------------------------: | :---: | :--: | :---: |
|                     campaign/**init**.py                      |   0   |  0   | 100%  |
|                       campaign/admin.py                       |   4   |  0   | 100%  |
|                       campaign/apps.py                        |   4   |  0   | 100%  |
|                       campaign/forms.py                       |  10   |  0   | 100%  |
|              campaign/migrations/0001_initial.py              |   7   |  0   | 100%  |
| campaign/migrations/0002_alter_character_charisma_and_more.py |   5   |  0   | 100%  |
|      campaign/migrations/0003_alter_character_health.py       |   5   |  0   | 100%  |
|                campaign/migrations/**init**.py                |   0   |  0   | 100%  |
|                      campaign/models.py                       |  34   |  2   |  94%  |
|                    campaign/test_forms.py                     |  45   |  0   | 100%  |
|                    campaign/test_views.py                     |  102  |  11  |  89%  |
|                       campaign/tests.py                       |   1   |  0   | 100%  |
|                       campaign/urls.py                        |   3   |  0   | 100%  |
|                       campaign/views.py                       |  67   |  11  |  84%  |
|                            env.py                             |   3   |  0   | 100%  |
|                       home/**init**.py                        |   0   |  0   | 100%  |
|                         home/admin.py                         |   1   |  0   | 100%  |
|                         home/apps.py                          |   6   |  0   | 100%  |
|                  home/migrations/**init**.py                  |   0   |  0   | 100%  |
|                        home/models.py                         |   1   |  0   | 100%  |
|                        home/signals.py                        |  10   |  5   |  50%  |
|                         home/tests.py                         |   1   |  0   | 100%  |
|                      home/tests_views.py                      |   8   |  0   | 100%  |
|                         home/urls.py                          |   3   |  0   | 100%  |
|                         home/views.py                         |   3   |  0   | 100%  |
|                       item/**init**.py                        |   0   |  0   | 100%  |
|                         item/admin.py                         |   5   |  0   | 100%  |
|                         item/apps.py                          |   4   |  0   | 100%  |
|                         item/forms.py                         |   5   |  0   | 100%  |
|                item/migrations/0001_initial.py                |   7   |  0   | 100%  |
|                  item/migrations/**init**.py                  |   0   |  0   | 100%  |
|                        item/models.py                         |  17   |  0   | 100%  |
|                      item/test_views.py                       |  67   |  0   | 100%  |
|                         item/tests.py                         |   1   |  0   | 100%  |
|                         item/urls.py                          |   3   |  0   | 100%  |
|                         item/views.py                         |  29   |  2   |  93%  |
|                           manage.py                           |  11   |  2   |  82%  |
|                      monster/**init**.py                      |   0   |  0   | 100%  |
|                       monster/admin.py                        |   3   |  0   | 100%  |
|                        monster/apps.py                        |   4   |  0   | 100%  |
|              monster/migrations/0001_initial.py               |   5   |  0   | 100%  |
|                monster/migrations/**init**.py                 |   0   |  0   | 100%  |
|                       monster/models.py                       |  17   |  1   |  94%  |
|                       monster/tests.py                        |   1   |  0   | 100%  |
|                    monster/tests_views.py                     |  18   |  0   | 100%  |
|                        monster/urls.py                        |   3   |  0   | 100%  |
|                       monster/views.py                        |   7   |  0   | 100%  |
|                   party_tracker/**init**.py                   |   0   |  0   | 100%  |
|                   party_tracker/settings.py                   |  38   |  0   | 100%  |
|                     party_tracker/urls.py                     |   3   |  0   | 100%  |
|                             TOTAL                             |  597  |  36  |  94%  |


### Validation Tests

#### The W3C CSS Validation Service
![Image of CSS validation service passed](/static/images/css-validation.png)

#### CI Python Linter

All apps py files were tested using the [CI Python Linter](https://pep8ci.herokuapp.com/#).

|App|File|Result|
|:--:|:--:|:--:|
|Campaign|views.py|Pass|
|Campaign|urls.py|Pass|
|Campaign|test_views.py|Pass|
|Campaign|test_forms.py|Pass|
|Campaign|models.py|Pass|
|Campaign|forms.py|Pass|
|Campaign|apps.py|Pass|
|Campaign|admin.py|Pass|
|Home|views.py|Pass|
|Home|urls.py|Pass|
|Home|test_views.py|Pass|
|Home|apps.py|Pass|
|Monster|views.py|Pass|
|Monster|urls.py|Pass|
|Monster|test_views.py|Pass|
|Monster|models.py|Pass|
|Monster|apps.py|Pass|
|Monster|admin.py|Pass|
|Item|views.py|Pass|
|Item|urls.py|Pass|
|Item|test_views.py|Pass|
|Item|test_forms.py|Pass|
|Item|models.py|Pass|
|Item|forms.py|Pass|
|Item|apps.py|Pass|
|Item|admin.py|Pass|
|Party Tracker|wsgi.py|Pass|
|Party Tracker|urls.py|Pass|
|Party Tracker|asgi.py|Pass|
|Party Tracker|settings.py|Fail|

- Note Party Tracker settings.py failed due to AUTH_PASSWORD_VALIDATORS
being too long.

## Bugs and Debugging

### Integrity Error

- Example:

IntegrityError at /accounts/signup/
insert or update on table "account_emailaddress" violates foreign key constraint "account_emailaddress_user_id_2c513194_fk_user_user_id"
DETAIL: Key (user_id)=(25) is not present in table "user_user".

#### Main Issue:

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
  DETAIL: Key (user_id)=(1) is not present in table "user_user".
- I tried to flush my database but ran into issues due to using a database link.

#### Main Solution:

- To fix this issue, I decided to delete my old database.
- I first deleted the current link in my heroku DATABASE_URL and env.py file.
- I then got a fresh new database and link from Code Institute.
- Using this new database link I changed both the heroku DATABASE_URL value and the one in my env.py file to the new value.
- I ran migrations again with python3 manage.py migrate.
- Created a new superuser.
- Then tested the new database by creating a new user through the allauth signup form.
- After testing no error was encountered and the integrity error was fixed.

#### Conclusion:

My inital thoughts on what caused the issue in the first place was due to my own fault.
When i first started the project i created a superuser and a test signup before properly implementing the allauth package.
I believe this was the main cause of the error.
This would have caused the allauth migrations to be out of sync with the rest of the database resulting in allauth not being able to automatically handle the post request correctly.
Thankfully this issue has now been resolved.

### Circular Import

- Example:

- from campaign.models import Character
- ImportError: cannot import name 'Character' from partially initialized module 'campaign.models'
  (most likely due to a circular import) (/workspace/party-tracker-project-four/campaign/models.py)

#### Main Issue

This error occured because:

- campaign.models imported Inventory from the item app.
- item.models imported Character from the campaign app.
- This resulted in a circular import error, where each model required the other file to be fully loaded first.
  This was not possible as python doesn't allow circular dependencies.

#### Main Solution

The easiest fix for this bug was removing one of the imports from the other.

- Instead of directly import Character into the item.models, I instead used a string method calling 'campaign.Character'.
- This allowed Django to resolve the circular import at runtime.
- My database schema didn't change structure, so no migrations were needed.
- I did run makemigrations and migrate to ensure this was correct.
- When these commands were used no migrations were made.

#### Conclusion

This was a relatively easy bug to fix, having DEBUG set to True quickly helped me identify the error as a circular import.
Resolving the issue with using a string method instead of importing the Character model was a lot more efficient and fixed the error straight away.
Although I created ERD's to help with model creation, in the future I will have to be more prepared with how my models will interact with one another.
Keeping this lesson in mind will help me avoid errors such as this.

## Future Implementations

Unfortunately I was unable to add all of the features I wanted. Here are some of the future implementations that I would like to add to my 
application.

### Community Page
A community page. This would take inspiration from the Code Institute blog walkthrough. 
- A place for users to share posts, comment, like posts, share news of their quests and adventures.
- It would be a great way for like minded people to get to know each other.
- The website was designed with the idea of community in mind, a group of friends playing dungeons and dragons together. 
Where they can keep track of their characters together with a simple but user friendly design.

### Contact Page
A contact page. This would allow users to get in touch if they have any user queries or require support.
- It would include a contact box for the user to leave a message.
- When sent the user will be emailed an automatic email saying the dev team will be in touch as soon as possible.

### Chat Box
A chat box inside the campaign pages.
- This would be a really incredible feature to add, it would tie the site together. 
- It would allow users to invite each other to chat like facebook or instagram. It would be useful for players who live 
far away and don't have a microphone. That way they can still play D&D online and chat with their group about what they would
like for their character to do. It could also be used for chatting and catching up.

### Invite To Campaign
The invite another player to your campaign.
- I really wanted to add this feature as it would really help the purpose of the website.
- The idea was to invite people to your campaign so each user can track their character personally. At the moment the website is set up
for only one user to use a single campaign at a time. 
- For this to be implemented would take a lot of time but it is a feature that I would be very keen on adding as soon as possible.

### Theme Selector
This will allow players to choose an active theme for the website.
- The player will be able to cycle through different asthetic themes with the click of a button.
- A forest theme, a dark dungeon, arcane magic, fire magic, deep waters. 
- This is a nice feature to add however due to the time required to code it, it didn't have high priority on my list compared to other areas.

## Overview 

Overall, I am really proud of my website. I have a great love for the world of dungeons and dragons. It is a wonderful land of fantasy and 
adventure, and working on this project has brought me a lot of joy. Working out all the challenges and bugs has been difficult but the more I 
have progressed and worked on this project, the more I can see it being a real asset to a great community of people. It might not be the most 
intricate of designs however I am proud of the functionality of the models, views and forms as they have worked well and as intended. I set out to design a tool for 
D&D players to create and track campaigns, characters and items and that is what I have. There are many features I would like to add which I 
wanted from the start and some others that came later on as I was designing the website. Keeping an agile frame of mind, I would add these features 
later on in order of importance. 

I hope you enjoy the design and functionality of the website so far, when I am able to improve this website I will as I can see a lot of potential 
in what this website can become. I even have an idea about creating an AI bot that will create D&D adventures on the fly for a solo player or a 
group of friends who don't have a Dungeon Master. Thank you for spending the time looking at my project, it is appreciated. Happy Questing. 


## Deployment

### Cloning

1. Go to the [party tracker](https://github.com/whelew/party-tracker-project-four) repository on github.
2. Click on the "<> Code" button.
3. Copy Https url or Github CLI link
4. Open Git Bash
5. Change your current working directory to the location where you want the clone directory 
6. Type git clone, followed by copied url
7. Create your local clone

### Deploying to Heroku

1. Create a new app on heroku
2. Add required key:value pairs to app configurations. (SECRET_KEY, DATABSE_URL)
3. Install a production ready webserver for heroku, I used [Gunicorn](https://gunicorn.org/)
4. Add [Gunicorn](https://gunicorn.org/) to your requirements.txt
5. Create a Procfile and declare the web process. (web: gunicorn project_name.wsgi)
6. Set your DEBUG=False in your projects settings.py file
7. Add herokuapp.com to ALLOWED_HOSTS list in your settings.py file
8. Git commit and push your changes
9. Connect heroku app to github repository
10. Deploy to main branch
11. Test your application has deployed correctly

## Credits & Technologies

### Technologies

Here is a list of technologies I used to compelte my project.

1. The Framework [Django](https://www.djangoproject.com/).
2. I used [Django Allauth](https://docs.allauth.org/en/latest/) for handling user authentication.
3. [Bootstrap]() was throughout the project to easily format and structure my site.
4. [Gunicorn](https://gunicorn.org/) to help my python based web application run.
5. [Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) to allow my web app to serve its own staticfiles.
6. [Psycopg2](https://pypi.org/project/psycopg2/) a widely used PostgreSQL adapter.

### Credits

Here is a list of documents I used to help create my project.

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
10. [Favicon](https://favicon.io/) was used to create and generate a free favicon for my website.
11. [Coolers](https://coolors.co/) was used to map out and finalise my css color scheme.
12. I would also like to thank my mentor Luke for his insight and support during this project.
