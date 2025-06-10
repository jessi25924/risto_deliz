# Testing
This project was tested manually to verify core functionality and usability. No automated testing was implemented.

## Table of Contents

- [Validation](#validation)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Manual Testing](#manual-testing)
- [User Stories](#user-stories)
- [Bug](#bug)

## Validation

- To validate all HTML files, the recommended validator service by Code Institute which is [HTML Validator](https://validator.w3.org/) was used.

| Page      | Comment   | Screenshot         |
| --------- | --------- | ------------------ |
| Home/Base | No Errors | ![](documentation) |
|           | No Errors | ![](documentation) |
|           | No Errors | ![](documentation) |
|           | No Errors | ![](documentation) |
|           | No Errors | ![](documentation) |

- To validate the CSS file, the recommended validator service by Code Institute which is [CSS Validator](https://jigsaw.w3.org/css-validator/) was used.

| Validator                                          | Comment  | Screenshot                                    |
| -------------------------------------------------- | -------- | --------------------------------------------- |
| [Jigsaw W3C](https://jigsaw.w3.org/css-validator/) | No Error | ![](documentation/testing/validation-css.png) |

- To validate Python code, the recommended validator service by Code Institute which is [Python PEP8 Checker](https://ww7.pep8online.com/?usid=24&utid=12257950545) was used.

<details>
 
 **<summary> View Python Code Testing </summary>**

| File              | Comment | Screenshot         |
| ----------------- | ------- | ------------------ |
| **risto_deliz**   |         |                    |
| **setting.py**    |         | ![](documentation) |
| **url.py**        |         | ![](documentation) |
| **booking_table** |         |                    |
| **admin.py**      |         | ![](documentation) |
| **apps.py**       |         | ![](documentation) |
| **forms.py**      |         | ![](documentation) |
| **models.py**     |         | ![](documentation) |
| **views.py**      |         | ![](documentation) |

 </details>

- For auditing Performance, Accessibility, and Best Practices [Developer Tools Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used.

 <details>
 
 **<summary> View Lighthouse Testing </summary>**

| Device      | Page         | Screenshot                                   |
| ----------- | ------------ | -------------------------------------------- |
| **Desktop** | Home         | ![](documentation/testing/lighthouse-hd.png) |
| **Mobile**  | Home         | ![](documentation/testing/lighthouse-hm.png) |
| **Desktop** | Menu         | ![](documentation/testing/lighthouse-md.png) |
| **Mobile**  | Menu         | ![](documentation/testing/lighthouse-mm.png) |
| **Desktop** | Booking form | ![](documentation/testing/lighthouse-bd.png) |
| **Mobile**  | Booking form | ![](documentation/testing/lighthouse-bm.png) |
| **Desktop** | My Account   | ![](documentation/testing/lighthouse-dd.png) |
| **Mobile**  | My Account   | ![](documentation/testing/lighthouse-dm.png) |
| **Desktop** | Edit booking | ![](documentation/testing/lighthouse-ed.png) |
| **Mobile**  | Edit booking | ![](documentation/testing/lighthouse-em.png) |

 </details>

[Back To Top](#table-of-contents)

## Responsiveness
- The application was tested to ensure it will respond correctly on desktop, tablet, and mobile devices, maintaining usability and layout integrity.
<details>
 
 <summary>View Responsiveness Screenshot on Different Devices</summary>

| Device      | Comment | Screenshot             |
| ----------- | ------- | ---------------------- |
| **Desktop** |         | ![home](documentation) |
| **Tablet**  |         | ![home](documentation) |
| **Mobile**  |         | ![home](documentation) |

</details>

## Browser Compatibility
- The application was tested for basic compatibility on major browsers including Chrome, Firefox, MS Edge and Opera. Core functionality and layout appeared consistent across these browsers.
<details>
 
 <summary>View Compatibility Screenshot on Different Browser</summary>

| Browser     | Comment | Screenshot             |
| ----------- | ------- | ---------------------- |
| **Chrome**  |   Performs as intended      | ![home](documentation/testing/browser-chrome.png) |
| **Firefox** |   Performs as intended      | ![home](documentation/testing/browser-firefox.png) |
| **MS Edge** |   Performs as intended      | ![home](documentation/testing/browser-edge.png) |
| **Opera**   |   Performs as intended      | ![home](documentation/testing/browser-opera.png) |

</details>

[Back To Top](#table-of-contents)

## Manual Testing
Defensive programming techniques—such as form validation, access control, and error handling—were manually tested through user acceptance scenarios. In addition, all buttons and links were manually tested to ensure they function correctly and navigate as intended.

### Navbar
![](documentation/navbar-logged-in.png)
![](documentation/navbar-log-out.png)
| Action | Expected Result | Comment |
| --------------------- | -------------------------------------- | ---------------------------------------- |
| click on logo | should navigate to homepage | **Pass**- Achieves desired functionality |
| click on Home | should navigate to homepage | **Pass**- Achieves desired functionality |
| click on Menu | should navigate to menu page | **Pass**- Achieves desired functionality |
| click on Sign Up | should navigate to signup page | **Pass**- Achieves desired functionality |
| click on Log In | should navigate to login page | **Pass**- Achieves desired functionality |
| click on Book a Table | should navigate to booking form page | **Pass**- Achieves desired functionality |
| click on My Account | should navigate to user's dashboard | **Pass**- Achieves desired functionality |
| click on Log Out | logged out and redirect to log in page | **Pass**- Achieves desired functionality |

### Footer

![](documentation/testing/footer-links.png)
| Action | Expected Result | Comment |
| ----------------------- | ---------------------------------------------------------- | ---------------------------------------- |
| click on Facebook Icon | should navigate to the facebook page in a separate window | **Pass**- Achieves desired functionality |
| click on Instagram Icon | should navigate to the instagram page in a separate window | **Pass**- Achieves desired functionality |
| click on X Icon | should navigate to the x page in a separate window | **Pass**- Achieves desired functionality |

### Homapage Buttons

| Action                                     | Expected Result                             | Comment                                  |
| ------------------------------------------ | ------------------------------------------- | ---------------------------------------- |
| ![](documentation/testing/home-button.png) | ![](documentation/testing/home-button2.png) |                                          |
| click on Book a Table                      | should navigate to booking form page        | **Pass**- Achieves desired functionality |
| click on View our Menu                     | should navigate to Menu page                | **Pass**- Achieves desired functionality |
| click on Click here to join!               | should navigate to Sign Up page             | **Pass**- Achieves desired functionality |

### Menu Page Button

![](documentation/testing/menu-button.png)
| Action | Expected Result | Comment |
| ----------- | ------- | ---------------------- |
| click on Back to Booking | should navigate to booking form page | **Pass**- Achieves desired functionality |

### Sign Up Form

![](documentation/testing/sign-up-form.png)
| Action | Expected Result| Comment |
| ----------- | ------- | ---------------------- |
| Enter Username | Prompt the user to fill the field when username is blank | **Pass**- Achieves desired functionality |
| Enter First name | prompt the user to fill the field when first name is blank | **Pass**- Achieves desired functionality |
| Enter Last name | prompt the user to fill the field when last name is blank | **Pass**- Achieves desired functionality |
| Enter valid Password (twice) | field will only accept password format | **Pass**- Achieves desired functionality |
| Click Create Account | redirect user to user's dashboard | **Pass**- Achieves desired functionality |

### Log In Page

![](documentation/testing/us-login.png)
| Action | Expected Result | Comment |
| ----------- | ------- | ---------------------- |
| Enter Username | prompt the user to fill the field when username is blank | **Pass**- Achieves desired functionality |
| Enter Valid Password | only valid password will be accepted, incorrect password will display invalid email or password message | **Pass**- Achieves desired functionality |
| click on Log in | redirect user to user's dashboard | **Pass**- Achieves desired functionality |

### Dashboard/My Account

| Action                              | Expected Result                     | Comment                                  |
| ----------------------------------- | ----------------------------------- | ---------------------------------------- |
| ![](documentation/dashboard-t1.png) | ![](documentation/dashboard-t2.png) |                                          |
| no booking                          | no bookings yet message             | **Pass**- Achieves desired functionality |
| Click on Edit(booking exist)        | redirect user to user's edit form   | **Pass**- Achieves desired functionality |
| Click on Cancel(booking exist)      | redirect user to cancellation page  | **Pass**- Achieves desired functionality |
| Click on Back to Booking            | redirect user to booking form       | **Pass**- Achieves desired functionality |

### Booking Form / Edit Form

![](documentation/book-table1.png)
| Action | Expected Result | Comment |
| ----------- | ------- | ---------------------- |
| Enter the date | prompt the user to fill the field when date name is blank | **Pass**- Achieves desired functionality |
| Enter the time | prompt the user to fill the field when time is blank | **Pass**- Achieves desired functionality |  
| Enter the guest count | prompt the user to fill the field when guest count is blank | **Pass**- Achieves desired functionality |
| n/a | pre-filled email address | **Pass**- Achieves desired functionality |
| Enter phone number | prompt the user to fill the field when phone number is blank | **Pass**- Achieves desired functionality |
| nullable | Suggestion box is not required | **Pass**- Achieves desired functionality |
| Click on Book Now | if all fields are satisfied, it will redirect to the user's dashboard where the booking will reflect | **Pass**- Achieves desired functionality |
| Click on Save Changes(Edit Form) | if all fields are satisfied, it will redirect to the user's dashboard where the changes will reflect | **Pass**- Achieves desired functionality |

### Cancel Booking Page

![](documentation/cancel-booking.png)
| Action | Expected Result | Comment |
| ----------- | ------- | ---------------------- |
| Click on **Yes** | successfully cancelled page will display | **Pass**- Achieves desired functionality |  
| Click on **No** | redirect to user's dashboard | **Pass**- Achieves desired functionality |

### Cancel Success Page

![](documentation/cancel-success.png)
| Action | Expected Result | Comment |  
| ----------- | ------- | ---------------------- |
| Click on Back to your account | redirect to user's dashboard | **Pass**- Achieves desired functionality |
| Click on Make a new booking | redirect to booking form | **Pass**- Achieves desired functionality |

[Back To Top](#table-of-contents)

## User Stories

| User Story                                                                                                                                                                                                                                                                                                                     | Comment                                | Screenshot                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- | ---------------------------------------------- |
| As a user I want to sign up so that I can create an account and manage my bookings                                                                                                                                                                                                                                             | Achieves desired functionality         | ![](documentation/testing/sign-up-form.png)    |
| As a user I want to log in so that I can securely view, create, update, or cancel my bookings.                                                                                                                                                                                                                                 | Achieves desired functionality         | ![](documentation/testing/us-login.png)        |
| As a user I want to select a date and time (separate fields) and the number of guests so that I can book a table for my party                                                                                                                                                                                                  | Achieves desired functionality         | ![](documentation/testing/us-booking-form.png) |
| As a user I want to update or cancel my existing booking so that I can change plans without contacting the restaurant directly.                                                                                                                                                                                                | Achieves desired functionality         | ![](documentation/testing/us-dashboard.png)    |
| As a user I want to view the restaurant’s menu while booking so that I can plan my meal in advance.                                                                                                                                                                                                                            | Achieves desired functionality         | ![](documentation/testing/us-menu.png)         |
| As a user I want to receive an email confirmation after booking so that I have a record of my reservation.                                                                                                                                                                                                                     | Achieves desired functionality         | ![](documentation/testing/us-email.png)        |
| As a user I want to know if the date and time is not available so that I avoid double-booking.                                                                                                                                                                                                                                 | Achieves desired functionality         | ![](documentation/testing/us-db.png)           |
| As a user I want the system to automatically assign me an appropriate table and prevent bookings that would exceed the restaurant’s 20-guest capacity per time slot so that I can be confident my reservation is both confirmed and within the restaurant’s limits, and I receive clear feedback if my requested slot is full. | Achieves desired functionality         | ![](documentation/testing/us-db.png)           |
| As a site owner I want to mark a booking as "Confirmed", "Cancelled", “Completed” or “No-show” so that I can keep accurate records of actual seating.                                                                                                                                                                          | Achieves desired functionality         | ![](documentation/testing/admin-status.png)    |
| As a site owner I want to view a list of all bookings so that I can manage the restaurant’s schedule (CRUD).                                                                                                                                                                                                                   | Achieves desired functionality         | ![](documentation/testing/admin-bookings.png)  |
| As a site owner I want to prevent overlapping bookings for the same table at the same date/time so that I avoid double-bookings.                                                                                                                                                                                               | Functionality achieved but bug present | ![](documentation/testing/admin-bug.jpg)       |

[Back To Top](#table-of-contents)

## Bugs

| Bug                            | Summary                                                        | Fix                                                                                                          | Screenshot                                    |                                               |
| ------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | --------------------------------------------- |
| Booking allowed for past dates | Users could create or edit bookings for past date/time values. | Added validation in booking and editing views to block past date/time selections using datetime.now() check. | ![](documentation/testing/past-date-book.png) | ![](documentation/testing/past-date-edit.png) |

**Existing Bug**
| Bug | Summary | Screenshot |
| ----------- | ------- | ---------------------- |
| Duplicate Error Messages on Guest Limit Exceeded | In the Django admin panel, exceeding the guest limit triggers two identical error messages instead of one. The limit enforcement works correctly, but the duplicate messages affect clarity.| ![](documentation/testing/admin-bug.jpg) |

[Back To Top](#table-of-contents)
