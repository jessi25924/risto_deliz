# risto_deliz (Milestone Project 3)

![Responsiveness](documentation/testing/responsiveness-header.png)

[View Live Site Here](https://risto-deliz-9958e7302963.herokuapp.com/)

## Overview

This project is a restaurant booking system that allows customers to easily reserve tables online through a simple and intuitive interface. Users can register, log in, and make bookings by selecting a date, choosing a time slot, and entering the number of guests.
The system enforces a maximum capacity of 20 guests per time/date slot, preventing overbooking and ensuring efficient table management. This rule is consistently applied on the user-facing site and the admin panel. When a time/date slot is fully booked, users are notified and prompted to choose a different time or reduce their party size.
Registered users can book tables and manage reservations through a personalised dashboard, with options to edit or cancel bookings. Upon submitting a booking request, users receive a confirmation message. Overall, the system provides a seamless, controlled, and user-friendly reservation experience from start to finish.

## Table of Contents
* [Project Goals](#project-goals)
* [User Stories](#user-stories)
* [Features](#features)
* [Design Choices](#design-choices)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits and Acknowledgement](#credits-and-acknowledgement)

## Project Goals

The goal of this project is to provide an efficient and user-friendly platform for customers to book restaurant tables online, while helping restaurant staff manage reservations seamlessly. By automating availability checks and offerring self-service features like account creation, booking management, and real-time confirmations. The system aims to improve the overall dining reservation experience and reduce the risk of overbooking or scheduling conflicts.

## User Stories

As a **User**, I want to:

- Sign up so that I can create an account and manage my bookings.
- Log in so that I can securely view, create, update, or cancel my bookings.
- Select a date and time, and the number of guests so that I can book a table for my party.
- Know if the date and time is not available so that I avoid double-booking.
- update or cancel my existing booking so that I can change plans without contacting the restaurant directly.
- view the restaurant’s menu while booking so that I can plan my meal in advance.
- receive an email confirmation after booking so that I have a record of my reservation.
- the system to automatically assign me an appropriate table and prevent bookings that would exceed the restaurant’s 20-guest capacity per time slot so that I can be confident my reservation is both confirmed and within the restaurant’s limits, and I receive clear feedback if my requested slot is full.

As a **Site owner**, I want to:

- Mark a booking as "Confirmed", "Cancelled", “Completed” or “No-show” so that I can keep accurate records of actual seating.
- view a list of all bookings so that I can manage the restaurant’s schedule (CRUD).
- prevent overlapping bookings for the same table at the same date/time so that I avoid double-bookings.

As a **Developer**, I want to:

- Design a clear and logical booking flow so that users can reserve a table without confusion or unnecessary steps.
- Ensure that bookings are accurately recorded and reflect real-time availability to prevent double bookings.
- Create a system that supports both customer-facing features and administrative needs to ensure smooth operation for both users and the site owner.
- Provide users with the ability to manage their bookings independently so they can view, update, or cancel their reservations easily.
- Ensure the application is responsive and intuitive so that it works well on different devices and provides a positive user experience.

The development of this project was guided by **Agile principles**, promoting flexibility, user feedback, and iterative improvement. User stories were created to reflect real user needs and managed through a Kanban board style in GitHub Projects. To prioritise features effectively, the MoSCoW method was used—categorising tasks into **Must Have, Should Have, Could Have, and Won’t Have** for now. This helped streamline development by focusing first on essential functionality. Working in short, focused iterations made it easier to test, evaluate, and refine the system regularly. A backlog of lower-priority or out-of-scope features was maintained for future planning, keeping the initial release manageable while ensuring room for growth.

**GitHub Project in a Kanban board style**

![kanban-board](documentation/kanban-board.png)

[Back To Top](#table-of-contents)

## Features

### Existing Features

The Restaurant Booking System includes the following core features to ensure a smooth and user-friendly dining reservation experience:

#### Header

- Consistent navigation bar displayed across all pages.
- Includes links to key pages: Logo (Home), Home, Menu, Sign Up, Log In, Book a Table. When logged in, links include Logout and My Account.
- Responsive design ensures menu collapses into a hamburger icon on tablet and mobile screens.

<details>

**<summary>View Navigation Feature Screenshots Here</summary>**

| Device / Comment      | Screenshot                                     |
| --------------------- | ---------------------------------------------- |
| **Desktop**           | ![desktop](documentation/navbar-log-out.png)   |
| **Desktop**/logged In | ![desktop](documentation/navbar-logged-in.png) |
| **Tablet**            | ![tablet](documentation/navbar-tablet.png)     |
| **Mobile**            | ![mobile](documentation/navbar-mobile.png)     |

</details>

#### Footer

- Present on all pages.
- Displays business information such as Contacts and Opening Times, Social media icons, and Copyright.
- Styled consistently with the overall theme and responsive across devices.

<details>

**<summary>View Footer Feature Screenshots Here</summary>**

| Device      | Screenshots                                  |
| ----------- | -------------------------------------------- |
| **Desktop** | ![desktop](documentation/footer-desktop.png) |
| **Tablet**  | ![tablet](documentation/footer-tablet.png)   |
| **Mobile**  | ![mobile](documentation/footer-mobile.png)   |

</details>

#### Home Page

- Welcoming landing page introducing the restaurant.
- Includes information about the venue, ambiance, and offerings.
- Prominent call-to-action buttons such as **Book a Table** or **View our Menu**.
- Visually engaging design with high quality imagery and easy navigation.

<details>

**<summary>View Home Page Feature Screenshots Here</summary>**

| Device      | Screenshots                                |                                            |                                            |
| ----------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| **Desktop** | ![desktop1](documentation/homepage-d1.png) | ![desktop2](documentation/homepage-d2.png) | ![desktop3](documentation/homepage-d3.png) |
| **Tablet**  | ![tablet1](documentation/homepage-t1.png)  | ![tablet2](documentation/homepage-t2.png)  | ![tablet3](documentation/homepage-t3.png)  |
| **Mobile**  | ![mobile1](documentation/homepage-m1.png)  | ![mobile2](documentation/homepage-m2.png)  | ![mobile3](documentation/homepage-m3.png)  |

</details>

#### Menu Page

- Displays a selection of the restaurant’s dishes with names, price and brief descriptions, allowing users to browse before making a reservation. Enhances user engagement by showcasing the variety and quality of meals available.

<details>

**<summary>View Menu Page Feature Screenshots Here</summary>**

| Device      | Screenshots                                 |
| ----------- | ------------------------------------------- |
| **Desktop** | ![desktop1](documentation/menu-desktop.png) |
| **Tablet**  | ![tablet1](documentation/menu-tablet.png)   |
| **Mobile**  | ![mobile1](documentation/menu-mobile.png)   |

</details>

#### Booking Page

- Provides a simple and intuitive booking form where users can choose a date and time, enter the number of guests and phone number, with the email field pre-filled and an optional suggestion or note field. Automatically checks availability and limits bookings to 20 guests per time/date slot. Users receive confirmation after submitting, ensuring a smooth and reliable booking experience. The page features a visually appealing background image with a white, glass-effect booking form overlay, creating a modern and inviting look.

<details>

**<summary>View Booking Page Feature Screenshots Here</summary>**

| Device      | Screenshots                               |
| ----------- | ----------------------------------------- |
| **Desktop** | ![desktop](documentation/book-table1.png) |
| **Tablet**  | ![tablet](documentation/book-table2.png)  |
| **Mobile**  | ![mobile](documentation/book-table3.png)  |

</details>

#### User Dashboard / My Account

- A personalised dashboard where users can view, edit, or cancel their bookings. It provides a clear overview of upcoming reservations. If no bookings are found, a helpful message is displayed to inform the user. Users also receive clear feedback messages for booking request confirmation, successful cancellations, and other booking actions.

<details>

**<summary>View User Dashboard Feature Screenshots Here</summary>**

| Device      | Comment                                      | Screenshots                                |                                            |
| ----------- | -------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| **Desktop** | without bookings / with bookings             | ![desktop](documentation/dashboard-d1.png) | ![desktop](documentation/dashboard-d2.png) |
| **Tablet**  | without bookings / with bookings             | ![tablet](documentation/dashboard-t1.png)  | ![tablet](documentation/dashboard-t2.png)  |
| **Mobile**  | (Table is horizontally scrollable on mobile) | ![mobile](documentation/dashboard-m1.png)  | ![mobile](documentation/dashboard-m2.png)  |

</details>

<details>

**<summary>View Other User Dashboard Feature Screenshots Here</summary>**

| Comment                      | Screenshots                            |
| ---------------------------- | -------------------------------------- |
| Edit Booking                 | ![](documentation/edit-booking.png)    |
| Booking Request Confirmation | ![](documentation/booking-confirm.png) |
| Cancel Booking               | ![](documentation/cancel-booking.png)  |
| Cancel Successful            | ![](documentation/cancel-success.png)  |

</details>

#### ADMIN Panel

- The admin panel, accessible via **/admin** with a superuser account (log in details will be provided during project submission), provides full control over the system. Admins can add or manage bookings while enforcing the 20-guest per time/date slot limit. It also allows easy management of menu items and table configurations. Informative success messages are displayed after adding or updating bookings, menu items, or tables, ensuring clarity and feedback throughout admin operations.

<details>

**<summary>View Admin Feature Screenshots Here</summary>**

| Comment               | Screenshots                            |                                       |
| --------------------- | -------------------------------------- | ------------------------------------- |
| /admin                | ![](documentation/admin-url.png)       |
| Admin Interface       | ![](documentation/admin-interface.png) |
| Admin Booking         | ![](documentation/admin-booking1.png)  | ![](documentation/admin-booking2.png) |
| Admin Menu            | ![](documentation/admin-menu1.png)     | ![](documentation/admin-menu2.png)    |
| Admin Table           | ![](documentation/admin-table.png)     | ![](documentation/admin-table2.png)   |
| Displayed Messages    | ![](documentation/admin-message1.png)  | ![](documentation/admin-message2.png) |
| Verifying Mssg Sample | ![](documentation/admin-message3.png)  |

</details>

### Future Features
- Menu Image Upload : Allow admin to add images for each menu item to make the menu page more visually engaging.
- Waitlist System : If all slots are full, allow users to join a waitlist and get notified if a spot becomes available.
- Online Payment Integration: Allow users to make secure online payments when booking a table, including options for deposits or full payments using payment gateways like Stripe or PayPal.

[Back To Top](#table-of-contents)

## Design Choices
The project’s design emphasizes clarity, simplicity, and user-friendliness. A clean layout with a stylish background image and a frosted glass effect keeps the interface both elegant and easy to read. The booking form highlights essential fields like date, time, and guest count, while responsive design ensures smooth usability across all devices—mobile users can scroll horizontally to view table content with ease.

Key features like automated table assignment and enforcing a 20-guest limit per time slot are consistently applied across both the user interface and admin panel, ensuring bookings remain accurate and manageable throughout the system.

### Entity Relationship Diagram (ERD)
The database structure is centered around four main models: User, Table, Booking, and MenuItem.
- User: Represents the customer making a booking. Each user can have multiple bookings.
- Table: Represents a physical table in the restaurant, each with a defined seating capacity.
- Booking: Connects users to tables with details like date, time, number of guests, and contact info. Each booking is linked to a user and a table.
- MenuItem: Stores the restaurant’s dishes, including names, descriptions, categories, and prices. This model is independent but helps power the Menu page.

These models work together to support the core functionality of the system, including booking management, menu display, and table capacity control.

![](documentation/erd.png)


### Wireframe

The wireframes provided a clear visual guide for the structure and layout of the site before development began. They helped me plan user flow, design decisions, and ensure a smooth user experience across different screen sizes.

<details>

**<summary>Balsamiq Wireframes</summary>**

| Page                     | Screenshot (Mobile, Tablet, Desktop)                                       |
| ------------------------ | -------------------------------------------------------------------------- |
| **Home**                 | ![home](documentation/wireframes/home-page.png)                            |
| **Home-2**               | ![home-2](documentation/wireframes/home-page-2.png)                        |
| **SignUp**               | ![signup](documentation/wireframes/signup.png)                             |
| **Booking Form**         | ![booking-form](documentation/wireframes/booking-form.png)                 |
| **Booking Confirmation** | ![booking-confirmation](documentation/wireframes/booking-confirmation.png) |
| **Menu**                 | ![menu](documentation/wireframes/menu.png)                                 |
| **LogIn**                | ![login](documentation/wireframes/login.png)                               |
| **Dashboard**            | ![dashboard](documentation/wireframes/dashboard.png)                       |
| **Edit Booking**         | ![edit-booking](documentation/wireframes/edit-booking.png)                 |
| **Cancel Booking**       | ![cancel-booking](documentation/wireframes/cancel-booking.png)             |
| **Cancel Confirmation**  | ![cancel-confirmation](documentation/wireframes/cancel-confirmation.png)   |

</details>

### Font

Playfair Display was chosen from [Google Fonts](https://fonts.google.com/specimen/Playfair+Display) for the font style to give the site a refined and stylish appearance, fitting for a restaurant brand.

### Colour Scheme

The colour palette for this site was generated using [Color Adobe](https://color.adobe.com/create/color-wheel). The colour palette was chosen to create a warm, inviting atmosphere that reflects the character of a quality dining experience.

![](documentation/colour-palette.png)

[Back To Top](#table-of-contents)

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML): Utilised for structuring the main site content.

- [CSS](https://en.wikipedia.org/wiki/CSS): Applied for styling the website.

- [Python](https://www.python.org/downloads/): The core programming language used to build the backend logic of the application.

### Frameworks 

- [Bootstrap](https://getbootstrap.com/): A front-end framework used for responsive design and pre-built UI components, making the site visually consistent across devices.

- [Django](https://www.djangoproject.com/): A high-level Python web framework used to build and manage the restaurant booking system, including routing, models, views, authentication, and admin interface.

### Platform

- [PostgreSQL](https://www.postgresql.org/): A powerful open-source relational database system used to securely store and manage user data, bookings, tables, and menu items.

- [Heroku](https://www.heroku.com/): A cloud platform used to deploy and host the live version of this restaurant booking system project.

- [Cloudinary] (https://cloudinary.com/): Cloud-based service for storing, optimizing, and delivering images efficiently across the site.

### Libraries

- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/): Enables Django to serve static files efficiently in production.

- [psycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter for Python/Django.

### Tools

- [VS Code](https://code.visualstudio.com/): The primary code editor used for writing, debugging, and managing the application code.

- [GitHub](https://github.com/): Used for version control, and remote code storage. Also serves as the source repository for deployment.

- [Markdown](https://en.wikipedia.org/wiki/Markdown): Used to write and format documentation efficiently with a clean and structured layout.

- [Gunicorn](https://gunicorn.org/): A Python WSGI HTTP server used to run the Django app on Heroku.

- [LucidChart](https://lucid.app/documents#/home?folder_id=recent) used to create the ERD.

- [Google Font](https://fonts.google.com/) used for typography and text styling on the site.

- [freepik.com](https://www.freepik.com/) and [Unsplash](https://unsplash.com/) sourced high-quality images used for this site.

- [bulkresizephotos](https://bulkresizephotos.com/en) and  [squoosh.app](https://squoosh.app/) utilised for compressing and optimising image for better performance.

- MS Snipping tool was used to capture and save screenshots or print screen images for documentation purposes.

- [Adobe Color](https://color.adobe.com/create/image) used in generating the colour palette for the site's design.

- [Favicon](https://www.favicon-generator.org/) used to create the favicon displayed on the browser tab.

- [Font Awesome](https://fontawesome.com/): Icon library used to display clean links in the site’s footer.

- [Canva](https://www.canva.com/) : Used to design the restaurant's logo.

- [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images) by Adam Pritchard: A reference for writing README.md and TESTING.md files, supplemented by guidance from Code Intitute.

- [Grammarly](https://www.grammarly.com/) this documentation has been grammar-proofed using Grammarly to ensure clarity and professionalism.

- [ui.dev](https://ui.dev/amiresponsive) used to show website appearance on desktop, laptop, tablet, and phone.

- [Responsive Design Checker](https://responsivedesignchecker.com/) used to check responsiveness across different devices.

### Email Service

- [Googel Mail Gmail SMTP](https://mail.google.com/): Used as the backend SMTP service to send booking confirmation emails to users automatically.

[Back To Top](#table-of-contents)

## Testing

All testing procedures and results for this project are detailed in the [TESTING.md](TESTING.md) file. The testing scope includes:
- Manual Testing: A full walkthrough of every user flow—navigation, booking, admin tasks, and edge cases—to confirm correct behavior and identify any functional bugs.

- Validation: Ensuring code quality and standards compliance through: [HTML Validator](https://validator.w3.org/), [CSS Validator](https://jigsaw.w3.org/css-validator/), [JavaScript Validator](https://jshint.com/), [Python PEP8 Checker](https://ww7.pep8online.com/?usid=24&utid=12257950545), [Developer Tools Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/).

- Responsiveness : Verified that the site adapts gracefully across screen sizes by simulating devices in Chrome DevTools and confirming breakpoint behavior.

- Browser Compatibility: Ensured consistent functionality and styling in the leading browsers: Chrome, Firefox, Opera, and Edge.

- Bug: Known bug in Django admin panel, enforcing the 20-guest limit per date/time slot currently triggers two displayed messages instead of one.

[Back To Top](#table-of-contents)

## Deployment 

To ensure a smooth development process and avoid unexpected issues later, the project was deployed to [Heroku](https://www.heroku.com/) at an early stage. 

**Initial deployment**
1. Create the App: 
- In your Heroku dashboard, click New → Create new app, give it a unique name, and choose the closest region.
- Under Settings → Config Vars, set DISABLE_COLLECTSTATIC=1.

2. Code Preparation
- Install Gunicorn and pin it in requirements.txt:<br>
pip3 install gunicorn~=20.1 <br>
pip3 freeze --local > requirements.txt
- Add a Procfile entry to launch your WSGI app with Gunicorn.
- In settings.py, change DEBUG = False and add '.herokuapp.com' to ALLOWED_HOSTS.
- Commit and push your changes to GitHub.

3. Deploy
- In your app’s Deploy tab, connect the GitHub repo and manually deploy the main branch.
- Under Resources, ensure you’re on an eco dyno and remove any default Postgres add-on.
- Click Open App

**Below is the second deployment, with those repeated steps removed so it picks up after the app is already live and ready to connect to PostgreSQL**

**Database Setup and Connection**
1. Add Your Database Config Var:
- In your Heroku Dashboard, select your app → Settings → Reveal Config Vars.
- Add: DATABASE_URL = your-CI-PostgreSQL-URL

2. Adjust Django Settings:
- In settings.py, ensure you have:<br>
import os
import dj_database_url<br>

if os.path.isfile('env.py'):
    import env           <br>

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}        <br>

DEBUG = False            <br>

- Comment out the default SQLite block entirely.

3. Install & Pin Database Dependencies:<br>
pip3 install psycopg2~=2.9 dj-database-url~=0.5
pip3 freeze --local > requirements.txt

4. Run Migrations & Create Superuser: <br>
python3 manage.py migrate<br>
python3 manage.py createsuperuser

5. Verify in Production:
- Open your app (heroku **Open**), log in via /admin, and confirm your superuser can access the admin.
- Your Heroku-hosted Django app is now fully connected to your CI-Database PostgreSQL instance.

**Fork the Repository on GitHub**
1. Sign in to your GitHub account and navigate to the original project’s page (e.g. https://github.com/original-owner/your-repo).
2. In the top-right corner, click Fork.
3. Select your personal account.
4. GitHub will create https://github.com/your-username/your-repo as your forked copy.

**Cloning**
1. Open VS Code (no folder loaded).
2. Press: <br>

- Windows/Linux: Ctrl + Shift + P <br>

- Mac: ⌘ + Shift + P
and type Git: Clone, then select it.

3. Paste your fork’s HTTPS URL (e.g. https://github.com/you/your-repo.git) and press Enter.
4. Pick a local folder when prompted.
5. Click **Open** in the prompt to load the cloned repo.


[Back To Top](#table-of-contents)


## Credits and Acknowledgement

This project has been brought to life through the support, inspiration, and expertise of many individuals and resources: <br>
**Code Institute Walkthrough “I Think Therefore I Blog”** <br>
The foundational architecture, project structure, and development best practices were drawn directly from this lesson. In particular, the following configuration patterns were adapted from the walkthrough’s code examples: 
- Environment variable loading via an env.py file and os.environ.setdefault calls. 
- Database connection using dj_database_url.parse(os.environ.get("DATABASE_URL")) in settings.py.
- Procfile setup to launch the app with Gunicorn (web: gunicorn your_project_name.wsgi).
- Requirements management with pip3 freeze --local > requirements.txt
These patterns ensured a consistent, battle-tested setup for both local development and Heroku deployment.

**Cohort Facilitator Lewis Dillon** 
- I'm grateful to my cohort facilitator for recommending the integration of an email notification system, which proved to be a valuable addition. I also deeply appreciate the consistent support and willingness to answer all my questions.

**To My Mentor Rory Sheridan** 
- Special thanks to Rory for proposing the final features—automatic table assignment and the 20-guest capacity enforcement. His feedback and practical tips were invaluable in bringing these complex functionalities to life.

**Online Tutor: Roman Rakic**
- Special thanks to Roman, my online tutor, whose patient support was invaluable when my database crashed. He guided me step-by-step through creating a fresh PostgreSQL instance and resolving configuration challenges, restoring stability and ensuring the backend was correctly set up.

**Design Inspiration from Leading Restaurants**
-  I drew inspiration from industry-leading restaurant sites like [Ask Italian](https://www.askitalian.co.uk/) and [Bella Italia](https://www.bellaitalia.co.uk/). I observed their layout strategies, menu presentation techniques, and color palettes—and then adapted those ideas into unique designs that align with this project’s own brand identity and usability goals.

**Open-Source References** <br>
To explore different implementation approaches and gain insights into project structure, I reviewed several open-source GitHub repositories—studying their patterns.
- https://github.com/adamshaw90/Trip-easy
- https://github.com/Jahooli4/witches-society
- https://github.com/Pramilashanmugam/Restaurant

**Writing & Documentation Tools**
- To ensure clarity and polish in the README documentation, I used [Grammarly](https://app.grammarly.com/?msockid=1642eb6570d860442d60f9db71976156) and [ChatGPT](https://chatgpt.com/) to refine the language and improve overall readability.

[Back To Top](#table-of-contents)
