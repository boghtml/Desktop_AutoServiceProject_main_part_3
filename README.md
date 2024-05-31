## Functionality

To view the functionality of the application, open the file: **"Explanation_note_of_my_work(courses-project).docx"** and go to page **62** and read to **81**.

# Car Service System - Main Application

This repository contains the code for the main application of the Car Service System, a comprehensive solution designed to automate car service operations.

## Overview

The Car Service System is comprised of three main components:
- **Website/Telegram Bot**: This component provides a user-friendly interface for clients to book service appointments, view available services, and get information about the car service. It can be accessed through a website or a Telegram bot.
- **Main Application**: This application is used by employees and administrators to manage the day-to-day operations of the car service, including creating and managing orders, tracking client history, and analyzing data.
- **Database**: A MongoDB database is used to store all the data for the car service, including information about clients, cars, services, employees, and orders.

This repository focuses on the Main Application, which is built using the Python programming language and the PyQt5 framework for its graphical user interface (GUI).

![Project Structure](https://github.com/boghtml/TelegramBot_AutoServiceProject_part_1/assets/119760440/f30720c6-70fe-47de-a98a-502ae62bf98f)

## Main Application Overview

The main application is an integral part of this system, created to facilitate the management of car service operations. It allows staff to:
- Manage customer appointments and service orders.
- Maintain and update car and service records.
- Track employee workloads and performance.
- Perform data analysis to optimize business operations.

## Features

### User Management:
- Create, edit, and delete user accounts for employees and administrators.
- Assign roles and permissions to users.

### Service Management:
- Add, edit, and delete services offered by the car service.
- Manage service pricing and descriptions.

### Car Management:
- Add, edit, and delete car models.
- Track service history for each car.

### Order Management:
- Create and process new service orders for clients.
- Assign orders to specific employees.
- Manage order status (pending, in progress, completed, canceled).
- Calculate and track order costs.
- Add comments to orders for additional information.

### Client Management:
- View and manage client information, including contact details and service history.
- Track client workload (frequency of visits, types of services used).

### Data Analysis:
- Generate reports on revenue, service popularity, and employee workload.
- Visualize data using graphs and charts.

![image](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/119760440/5db2f272-e222-41af-ad08-ce565dcac0b9)

![image](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/119760440/c7106fe3-c758-498c-a7d7-d4b1181ddc90)

### Additional Features:
- **Data Synchronization**: Ensures that data is consistent and available across all components of the system.
- **User-Friendly Interface**: Easy-to-use interface designed for efficiency and productivity.
- **Data Science Integration**: Utilizes Data Science techniques for advanced analytics and reporting, providing insights into service performance, customer satisfaction, and operational efficiency.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Desktop_AutoServiceProject_main_part_3
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables for the application, such as the database connection string.

5. Run the application:
    ```bash
    python main.py
    ```

## Advantages

- **Comprehensive Management**: Provides a complete solution for managing car service operations.
- **Data Integration**: Ensures seamless integration and data consistency across all components.
- **User-Friendly**: Intuitive and easy-to-use interface for efficient management.
- **Scalability**: Can easily scale with the growing needs of the business.
- **Advanced Analytics**: Leverages **Data Science** for detailed insights and reporting.

## Conclusion

The main application for AutoService is a vital component of a larger system aimed at improving car service management. By providing a comprehensive and user-friendly interface, it enhances operational efficiency and customer satisfaction. Integrated with MongoDB, it ensures data consistency and availability, contributing to an efficient and comprehensive car service management system.

---

This README provides a detailed overview of the main application for AutoService, highlighting its features, installation steps, project structure, and advantages. It serves as a comprehensive guide for understanding and utilizing the application effectively.
