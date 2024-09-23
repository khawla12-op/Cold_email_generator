# Cold Email Generator

## Overview

The *Cold Email Generator* is an innovative tool designed to assist software services companies in crafting personalized cold emails to potential clients. By leveraging advanced technologies such as Llama 3.1, Chroma DB, LangChain, and Streamlit, this project automates the email generation process based on job postings from various job portals. 

## Problem Statement

Software services companies often have a large pool of software engineers. To attract clients, they frequently send cold emails based on job requirements found on career pages. The challenge lies in formulating relevant and appealing emails that highlight the skills and expertise of their engineers, particularly for contract-based hiring.

## Technical Architecture

1. **Extract Text from Career Pages**: The system scrapes and processes job postings from various career pages to gather relevant information.
  
2. **Utilize Llama 3.1**: The extracted data is analyzed using Llama 3.1, which identifies key elements such as roles, required skills, and job descriptions. This information is then structured into a JSON format.

3. **Store in Chroma DB**: The JSON data is stored in Chroma DB, which facilitates quick access to related portfolio links based on the extracted skills and roles.

4. **Generate Email**: Using the portfolio links and the information from the JSON file, the system generates a tailored cold email that addresses the client’s requirements.

## Features

- **Automated Email Generation**: Quickly create personalized cold emails based on job postings.
- **JSON Output**: Role descriptions, skills, and other relevant data are structured for easy processing.
- **Portfolio Integration**: Automatically includes links to relevant portfolios in the generated emails.
- **User-friendly Interface**: Built with Streamlit for an intuitive user experience.

## Technologies Used

- **Llama 3.1**: For natural language processing and understanding.
- **Chroma DB**: For efficient data storage and retrieval.
- **LangChain**: For building language model applications.
- **Streamlit**: For creating interactive web applications.

## Installation

To set up the *Cold Email Generator*, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cold_email_generator.git
   cd cold_email_generator
