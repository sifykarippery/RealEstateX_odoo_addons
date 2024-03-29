# RealEstateX Compliant Management
odoo custom module for RealEstate complaint management
# Problem Statement /Requirement Work Flow
![WorkFlow](realestate_complaint_management/static/src/screenshot/complaintsystem.png "Work Flow")
### How to Run
Setup odoo System and Configure the custom addons(RealEstateX_odoo_addons) in odoo config file
```
addons_path = /opt/odoo16/odoo16/addons,opt/odoo16/odoo16/RealEstateX_odoo_addons
```
Restart Server Enable developer mode  App menu->Update App list->RealEstateX complaint Management System

1. Dependency module Website,mail,l10n_din5008
2. Enable din5008 layout for report from settings
![enable din5008](realestate_complaint_management/static/src/screenshot/din5008.png)

create user/employee and configure user in relative group supervisor/representative realestate
![representative](realestate_complaint_management/static/src/screenshot/Representative.png)
![supervisor](realestate_complaint_management/static/src/screenshot/supervisor.png)

### Complaint Website Form 
Router url: /ask_realestatex/ 
```
http://localhost:8069/ask_realestatex/

```
1. Website have required fields like customer name,email,complaint type,description,address
2. Many2one Field complaint type,state,country
![websiteform](realestate_complaint_management/static/src/screenshot/websiteform.png)
3. Response to customer to success page with reference number after form submit 
![Reponse](realestate_complaint_management/static/src/screenshot/reponsepage.png)
4. Send email with confirmation by reference number
![Response email](realestate_complaint_management/static/src/screenshot/responseemail.png)

### Kanban view (supervisor/representative)
![kanban view](realestate_complaint_management/static/src/screenshot/kanbanview.png)
### List view
![list view](realestate_complaint_management/static/src/screenshot/list.png)
#### search/filter/groupby
![search](realestate_complaint_management/static/src/screenshot/filter.png)
![filter](realestate_complaint_management/static/src/screenshot/filter by.png)
![group](realestate_complaint_management/static/src/screenshot/groupby.png)

### Pipeline flow
1. when customer submit the form assign to representative complaint in draft state
2. In review for complaints that are being classified by a customer
service representative
![form1review](realestate_complaint_management/static/src/screenshot/form1.png)
3. In Progress: for complaints that are being addressed with an action
plan If the complaint is a question, the customer service representative can just
message the tenant with the answer and close the complaint.
Email button left side
![form2](realestate_complaint_management/static/src/screenshot/form2.png)
4. Solved: for complaints that have been solved
![form3.png](realestate_complaint_management%2Fstatic%2Fsrc%2Fscreenshot%2Fform3.png)
![form4](realestate_complaint_management/static/src/screenshot/form4.png)
Auto send email tenant for solved
![solvedemail](realestate_complaint_management/static/src/screenshot/emailsolved.png)
5. Dropped: for complaints that have been dropped
![form5](realestate_complaint_management/static/src/screenshot/form5.png)
Auto email send dropped complaint
![dropedemail](realestate_complaint_management/static/src/screenshot/dropemail.png)

## Work order
For those complaints that need intervention, the customer service
supervisor should print a work order containing the data of the complaint (customer,
address, date, action plan, etc). This report should follow the DIN5008 standard.

![work order](realestate_complaint_management/static/src/screenshot/workorder.png)

### Tracked/logged Activity
![track](realestate_complaint_management/static/src/screenshot/track.png)

### Vision Furture Development
1. If time allows, I envision implementing an automated system to assign complaint 
representatives based on an algorithm. This algorithm would consider various factors 
such as the number of available representatives and their recent activity. 
Specifically, if there are five or more representatives available, 
the system would assign a representative based on factors such as the 
representative's last update time, prioritizing those who have been more active recently. 
By optimizing the assignment process in this way, we aim to improve efficiency and 
cost-effectiveness while ensuring timely resolution of complaints.
