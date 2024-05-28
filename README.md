# Main Application for AutoService

## Introduction

This project is part of a comprehensive car service management system designed to optimize the process of managing car service records, customer interaction, and service analytics. The complete project consists of three main components:

1. **Website**: Allows customers to sign up for service, view available services, and receive information about car service.
2. **Telegram Bot**: Provides customers with an alternative and convenient way to interact with the car service, offering the same features as the website.
3. **Main Application**: Used by car service center staff to book appointments, process customer information, and analyze car service data.

Each component is integrated with the MongoDB cloud database to ensure seamless data synchronization and availability.

![Project Structure](https://github.com/boghtml/TelegramBot_AutoServiceProject_part_1/assets/119760440/f30720c6-70fe-47de-a98a-502ae62bf98f)

## Main Application Overview

The main application is an integral part of this system, created to facilitate the management of car service operations. It allows staff to:
- Manage customer appointments and service orders.
- Maintain and update car and service records.
- Track employee workloads and performance.
- Perform data analysis to optimize business operations.

## Features

### Main Features:
- **Appointment Management**: Staff can book, view, and update customer appointments.
- **Service Management**: Manage a comprehensive list of services offered by the car service.
- **Car Records Management**: Maintain and update records of cars serviced by the center.
- **Employee Management**: Track employee details, workloads, and performance metrics.
- **Analytics and Reporting**: Generate reports on various aspects of the car service operations.

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

## Project Structure

- **main.py**: Entry point for the main application.
- **database/**: Contains scripts for database interactions.
- **models/**: Contains classes for data models used in the application.
- **views/**: Contains modules for the graphical user interface.
- **controllers/**: Contains the logic for managing the flow of the application.
- **utils/**: Utility functions used across the project.

## Functionality

To view the functionality of the application, open the file: **"Пояснювальна записка(Рибак Андрій Вікторович)_захищена.docx"** and go to page **62** and read to **81**.

### Appointment Management
- **Book Appointment**: Staff can book appointments by entering customer details, car information, and selecting the desired date and time.
- **View Appointments**: Staff can view a list of upcoming and past appointments.
- **Update Appointment**: Staff can update the details of an existing appointment.

### Service Management
- **Add Service**: Admin can add new services to the list of available services.
- **Update Service**: Admin can update details of existing services.
- **Delete Service**: Admin can delete services that are no longer offered.

### Car Records Management
- **Add Car**: Staff can add new cars to the records.
- **Update Car**: Staff can update details of existing cars.
- **View Car History**: Staff can view the service history of a particular car.

### Employee Management
- **Add Employee**: Admin can add new employees to the system.
- **Update Employee**: Admin can update details of existing employees.
- **View Employee Performance**: Admin can track the performance and workload of employees.

### Analytics and Reporting
- **Generate Reports**: Admin can generate various reports on service performance, employee productivity, and customer satisfaction.
- **View Analytics**: Admin can view detailed analytics to make informed business decisions.

## Screenshots

### Main Dashboard
![Main Dashboard](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/main_dashboard.png)

### Appointment Management
![Appointment Management](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/appointment_management.png)

### Service Management
![Service Management](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/service_management.png)

### Car Records Management
![Car Records Management](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/car_records_management.png)

### Employee Management
![Employee Management](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/employee_management.png)

### Analytics and Reporting
![Analytics and Reporting](https://github.com/boghtml/Desktop_AutoServiceProject_main_part_3/assets/analytics_reporting.png)

## Advantages

- **Comprehensive Management**: Provides a complete solution for managing car service operations.
- **Data Integration**: Ensures seamless integration and data consistency across all components.
- **User-Friendly**: Intuitive and easy-to-use interface for efficient management.
- **Scalability**: Can easily scale with the growing needs of the business.
- **Advanced Analytics**: Leverages Data Science for detailed insights and reporting.

## Conclusion

The main application for AutoService is a vital component of a larger system aimed at improving car service management. By providing a comprehensive and user-friendly interface, it enhances operational efficiency and customer satisfaction. Integrated with MongoDB, it ensures data consistency and availability, contributing to an efficient and comprehensive car service management system.

---

This README provides a detailed overview of the main application for AutoService, highlighting its features, installation steps, project structure, and advantages. It serves as a comprehensive guide for understanding and utilizing the application effectively.
