# **Milestone Project 4**  &nbsp;
# Table of Contents
1. [Purpose and Features](#purpose)
2. [Site Pages and Menu](#sitepgs)
	1. ['Home' page](#homepage)
	2. ['Navigation Menu'](#navmenu)
	3. ['All Products'](#allproducts)
	4. ['Product Details'](#pdetails)
	5. ['Edit Product' page](#edproduct)
	6. ['Shopping Bag' page](#bag)
	7. ['Checkout' page](#checkout)
	8. ['Sign Up' pages](#signup)
	9. ['Log In' page](#login)
	10. ['Profile'](#profile)
	11. ['Blog' page](#blog)
	12. ['Blog Details' page](#blogdetails)
	13. ['Edit Blog' page](#editblog)
	14. 'Add Blog' pages](#myaccount)
	15. ['Product Management' page](#pmanage)
	16. ['Logout' page](#logout)

3. [Responsivity](#responsivity)
4. [Design](#design)
	1. [Wireframes](#wireframes)
	2. [Schema and Models](#schemamodels)
	3. [Colour Palette](#palette)
	4. [Images](#images)
	5. [Typography](#typography)
	6. [Current Features](#current)
	7. [Future Features](#future)
5. [UX (User Experience)](#userexperience)
	1. [Strategy Plane](#strategy)
	2. [Scope Plane](#scope)
	3. [Structure Plane](#structure)
    	4. [Skeleton Plane](#skeleton)
	5. [Surface Plane](#surface)
6. [User Stories](#userstories)
	1. [Viewing and Navigation](#van)
	2. [Registration and User Accounts](#reg)
	3. [Sorting and Searching](#sorts)
	4. [Purchasing and Checkout](#pac)
	5. [Admin and Store Management](#adminsm)
7. [Testing](#testing)
    	1. [Manual User Testing](#usertesting)
	2. [Defensive User Testing](#defensive)
	3. [Bug Fixes](#bugfixes)
8. [Validation](#validation)
9. [Technologies](#technologies)
	1. [Languages](#languages)
	2. [Frameworks and Libraries](#frameworks)
10. [Deployment](#deployment)
11. [Credit and Acknowledgements](#credits)
	1. [Mentor](#mentor)
	2. [Code](#code)
    	3. [Commits](#commits)
	4. [Images](#imagesa)
	5. [Text Content](#textcontent)  

 

# Indulgem Jewellery Store - Milestone Project 4

GitHub Repository: https://github.com/Saraholoughlin5/Milestone_Project_4

Heroku App: https://indulgem-mp4.herokuapp.com/

![alt Indulgem Homepage](static/img/design/homepage.PNG "Kooky Kids Homepage" )  


### **Purpose and Features**<a name="purpose"></a>
For this milestone project I have built an e-commerce jewellery store. Features include easily navigated and sorted products, a blog, blog commenting, 
Users can sign up, view their profile, view products, change product size where applicable and increase/decrease quiantity (max: 5), add items to the shopping bag, use Stripe payments, checkout, and receive confirmation emails. 
The can also view the blog page, which displays a summary of all available blogs, and they can add comments if logged in to their profile.
A back to top button has been included on the 'All Products', 'Blog' and 'Blog Details' pages.
An Admin account can be used to add/edit/delete products. They can also add/edit/delete a blog, and add and delete comments.
This fulfils the CRUD requirement, as users can create, read, edit and delete content, depending on their profile type.

### **Site Pages and Menu**<a name="sitepgs"></a>

#### **'Home' page**<a name="homepage"></a>
The Indulgem homepage is accessible via the logo on desktop and via the dropdown navigation menu on smaller screens.
The 'Home' page contains the navigation menu and a 'Shop Now' button, which links to the 'All Products' page.
#### **'Navigation Menu**<a name="navmenu"></a>
The navigation menu on large screens contains the Indulgem logo (links to homepage), the 'My Account' and shopping bag icons/headings, a list of menu items and a search bar.
On smaller screens, the logo is not present. A toggle button can be clicked on to reveal the menu items and search field. The 'My Account' and shopping bag icons/headings are displayed across from the toggle button.
Clicking on a menu option (all screen sizes) displays further dropdowns where available.

#### **'All Products' page**<a name="allproducts"></a>
This page contains a list of all products, the total number of products, a 'Sort by...' menu and a back to top button (only visible once scrolled down a minimum of 200px).
When logged in using the Admin account, 'Edit/Delete' links are displayed.
A 'Delete Product?' modal has been added to the delete link, to ensure that products are not accidentally removed.
The navigation menu lists products by category, and user choices are displayed on the 'All Products' page, e.g. 'All Rings'.
#### **'Product Details' page**<a name="pdetails"></a>
Once the user clicks on a product image on the 'All Products' page, they are redirected to the 'Product Details' page. This page contains an enlarged image of the product and a white card that displays the product details, including the title, description, cost, category, rating, size menu (if applicable), quantity input field, and 'Keep Shopping'/'Add to Bag' buttons. 

Users can change the size of some products and increase the quantity to a maximum of 5. Clicking on the 'Keep Shopping' button brings the user back to the 'All Products' page, and clicking 'Add to Bag' keeps the user on the 'Product Details' page, while displaying a success toast message and a button linked to the 'Checkout' page.
#### **'Edit Product' page**<a name="edproduct"></a>
The 'Edit Product' page is only accessible by an Admin user on the 'All Products' and 'Product Details' pages. The user can update all details of the product.

#### **'Shopping Bag' page**<a name="bag"></a>
The 'Shopping Bag' page can be accessed via the bag icon in the navigation menu, or via a 'Return To Bag' button on the 'Checkout' page. If empty, a message and a 'Keep Shopping' button is displayed. If populated, the product image, details, price, quantity and subtotal are displayed, along with the bag total, delivery cost and grand total. 
If the user has not exceeded the free delivery threshold, a message will be displayed to notify them.
'Keep Shopping' and 'Secure Checkout' buttons are present also.

#### **'Checkout' page**<a name="checkout"></a>
The Checkout page contains the 'Order Summary' and 'Complete Order' form, as well as a card payment field (Stripe) and two buttons ('Return to Bag' and 'Pay Now').
If not signed in, links to login or sign up are displayed. Alert text highlighting the total charge is present beneath the buttons.

#### **'Sign Up' page**<a name="signup"></a>
The sign up page can be found in the 'My Account' navigation menu item. It contains a sign up form, as well as a link to log in, a 'Home' button, and a 'Sign Up' button.
A link to this page is also available on the checkout page, and at the bottom of the 'Blog Details' page.

#### **'Log In' page**<a name="login"></a>
Click on 'Log In' in the 'My Accounts' menu item to view the page. This page contains a login form, as well as a register link, a forgot password link, a 'Home' button and a 'Sign In' button.

#### **'Profile' page**<a name="profile"></a>
Once a user is logged in they can view their profile page, which contains their 'Order History' and 'Default Delivery Information', which can be set on the 'Checkout' page when making a purpose, if required.

#### **'Blog' page**<a name="blog"></a>
The 'Blog' page displays a panel list of summarised blogs. Each blog panel includes a title, summarised description, image and a 'Read On' button to access the 'Blog Details' page. 
The username and date/time submission information is also displayed. 
If logged in as Admin, 'Edit' and 'Delete' links are present - NOTE: there is no modal linked to the blog delete link (future feature).
The back-to-top button is also present on this page, visible once scroll threshold is reached.
The blog can be read without logging in.

#### **'Blog Details' page**<a name="blogdetails"></a>
The 'Blog Details' page is accessible via the 'Read On' button on the 'Blog' page. The page includes the title, image and full description, as well as the username and date/time submission information. 
A 'Comments' box is featured beneath the blog panel if comments have been added. The user, date/time and comment are displayed, as well as the total number of comments for the blog.
'Login' and 'Signup' links are present if the user is logged out and wishes to add a comment.

#### **'Edit Blog' page**<a name="editblog"></a>
The 'Edit Blog' link is available on the 'Blog' and 'Blog Details' page, and only for an Admin user. A form is displayed for the Admin user to edit the title, description, and replace or remove the image as required. A 'Cancel' button is present if edits need to be discarded. An 'Update Blog' button is also present.
An 'Alert' toast is displayed at the top-right of the page.

#### **'Add Blog' page**<a name="addblog"></a>
The Admin user can add a blog via the 'My Account' navigation menu item. A form is displayed for the user to enter a title, description, and upload an image.A 'Cancel' button is present if the blog needs to be discarded. An 'Add Blog' button is also present.

#### **'Product Management' page**<a name="pmanage"></a>
The 'Product Management' page can only be accessed by an Admin user. Here, the user can choose the category, enter an SKU number, name, description, price, rating and image. They can also set the 'Has sizes' feature visibility depending on the product. 'Cancel' and 'Add Product'  buttons are displayed.

#### **'Logout' page**<a name="logout"></a>
The 'Logout' page is accessible via a link in the 'My Account' navigation menu item. A confirmation message and 'Log Out' button are displayed. 


### **Responsivity**<a name="responsivity"></a>
The app is responsive on a variety of screen types and sizes, for both the server site and Heroku app. 
It has been checked via the browser tool list of responsive devices, both portrait and landscape. It has also been checked on a variety of browsers, including Chrome, Microsoft Edge, and Safari.
The Heroku deployed app was checked on a Lenovo ThinkPad, iPhone X and Huawei MediaPad T5.
[Bootstrap](https://www.getbootstrap.com/) classes and media queries were utilised throuhout the app to format the pages and elements. 
[Am I Responsive](http://ami.responsivedesign.is/) displays various site pages, including the homepage, log in page, all products and blog details pages.

![alt Responsive Design](media/readme/am_i_responsive_mp4.PNG "Responsive Design")  


### **UX (User Experience)** <a name="userexperience"></a>

#### **Strategy Plane**<a name="strategy"></a>
The 'Indulgem' app is designed to appeal to customers who wish to purchase elegant jewellery. The layout, colour and style are warm, yet muted and earthy, appealing and sublime, as expected based on the product. It is not loud or jarring for the customer.
The customers this site and product appeals to  would be aptly targeted with this design and layout.

#### **Scope Plane**<a name="scope"></a>
The app use is intuitive, with dropdown menus and progress buttons where expected. Users can sign up to create a profile, log in, purchase items at various sizes and quantities, and comment on the blogs.
Admin users can also create, edit and delete content. 
Toast messages are displayed to relay success, alert and error messages, where appropriate. 

#### **Structure Plane**<a name="structure"></a>
The structure of the app brings the users attention to the products, blogs and forms. The homepage contains an image and a single button. This image is an underlay on all remaining site pages. 
All other pages contain a light-coloured, offset overlay, which hosts the product images, for example. Forms and details contain white card backgrounds along with the overlay (product details, blogs and  for example).
Layout design, form design and buttons are uniform and intuitive. All links and buttons work as expected per user type. 

#### **Skeleton Plane**<a name="skeleton"></a>
Balsamiq wireframes were used to plan the app layout (desktop and portrait mobile views). Media queries and bootstrap classes were used to hide/display different layouts for the shopping bag and checkout pages.  
The app layout is as intended from the start of the project.

#### **Surface Plane**<a name="surface"></a>
The colour scheme of the app was drawn heavily from the banner and background images, and are consistent in the site. The buttons format is consistent throughout the site also, with red text for cancel buttons. Text-transform was used to enlarge buttons on hover where appropriate.


### **User Stories**<a name="userstories"></a>

#### **Viewing and Navigation**<a name="van"></a>
As a Shopper I want to be able to:
- View a list of products so that I can select some products to purchase
- View individual product details so that I can identify the price, description, product rating, product image and available sizes (if available)
- Quickly identify clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase
- Easily view the total of my purchases at any time so that I can avoid spending too much
As a Site User I want to be able to: 
- View a blog, whether logged in or not so, that I can read about items that might interest me and inform my purchases
- Add a comment to a blog so that I can take part in discussions or ask for advice
#### **Registration and User Accounts**<a name="reg"></a>
As a Site User I want to be able to: 
- Easily register for an account so that I can have a personal account and be able to view my profile
- Easily login or logout so that I can access my personal account information
- Easily recover my password in case I forget it so that I can recover access to my account
- Receive a verification email confirmation after registering so that I can confirm that my account registration was successful
- Have a personalised user profile so that I can view my personal order history and order confirmations, and save my delivery information
#### **Sorting and Searching**<a name="sorts"></a>
As a Shopper I want to be able to: 
- Sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products
- Sort a specific category of product so that I can find the best priced or best rated product in a specific category, or sort the products in that category by name
- Sort multiple categories of products simultaneously so that I can find the best priced or best rated product across broad categories, such as "rings" or "necklace sets"
- Search for a product by name or description so that I can find a specific product I'd like to purchase
- Easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available
#### **Purchasing and Checkout**<a name="pac"></a>
As a Shopper I want to be able to: 
- Easily select the size and quantity of a product when purchasing it so that I can ensure I don’t accidentally select the wrong product quantity or size
- View items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive
- Adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout
- Easily enter my payment information so that I can checkout quickly and with no hassle
- Feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
- View an order confirmation after checkout so that I can verify that I havent made any mistakes
- Receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records (also available in my profile)
#### **Admin and Store Management**<a name="adminsm"></a>
 As a Store Owner I want to be able to: 
- Add a product so that I can add new items to my store
- Edit/Update a product so that I can change product prices, descriptions, images and other product criteria
- Delete a product so that I can remove items that are no longer available
- Add a blog so that I can interest new site users and shoppers and build an audience
- Edit/Update a blog so that I can rewrite, if necessary, or change an image
- Delete a blog or blog comment so that blogs can be replaced and comments are policed

