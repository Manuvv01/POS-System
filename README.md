# POS-System

A Point of Sale (POS) system for small businesses that allows scanning items and managing product data in a spreadsheet.  

This project is a full-stack desktop application using Python for the backend, with plans to integrate a React frontend. It is currently being developed for a small business owned by a friend and his family.

---

## Development Process & GitHub Workflow

During initial discussions, the client preferred using spreadsheets over a traditional database to manage product data. To accommodate this requirement while keeping the system flexible, spreadsheets are used as the primary data storage solution. Although a database would typically be used for scalability, this approach was chosen to better align with the client's workflow and preferences.

After gathering these requirements, user stories (labeled as **user stories** in GitHub issues) were created to define user needs and guide development.


### GitHub Issues
The project uses GitHub issues to track tasks, organized with labels:

- **In Progress** – Issues currently being worked on  
- **Todo** – Tasks planned for future sprints  
- **Completed** – Issues that have been finished  

---

## Technologies
- Python (backend, Tkinter UI)  
- React (frontend)  
- Electron (desktop integration)  
- Spreadsheet-based data storage (Excel)

---

## Libraries

All libraries used in the project for development are listed in `requirements_dev.txt`. The ones most frequently used are:

- Pandas  
- Openpyxl  
- Jupyter Notebook (for data analysis)

---

## Features

- Product management (name, price, quantity, category)
- Cart system for handling transactions
- Input validation for reliable data entry
- Excel integration for storing sales records
- Modular architecture using Python packages (models, services)
- Designed for future barcode scanner and GUI integration
---

## Workflow

The development is organized in phases:

### 1. Python App (Tkinter) `In Progress`
Initial version using Python and Tkinter for a console interface.

### 2. React App
Modern frontend implementation using React.

### 3. Electron App
Integration of the React frontend with the Python backend to create a full desktop application.

The approach is to first implement the essential features in a simple interface, then gradually improve usability and functionality.

---

## How to Run

1. Clone the repository:
   git clone https://github.com/Manuvv01/POS-System

2. Navigate to the project folder:
   cd POS-System/src

3. Install dependencies:
   pip install -r requirements.txt

4. Run the program:
   python main.py
   
You can explore the repository and issues to see the development process in detail.
