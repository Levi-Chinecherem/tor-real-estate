
# TOR - Real Estate Management System

TOR (The Online Realty) is a Real Estate Management System built with Django, designed to facilitate the buying, selling, and surveying of land properties. It allows users to create accounts based on their roles as Sellers, Buyers, or Surveyors, and provides features for listing properties, bidding on properties, and verifying property authenticity.

## Features

- **User Roles**: The system supports three user roles: Sellers, Buyers, and Surveyors. Each role has its specific functionalities and access levels.
- **Seller Features**:
  - Upload land properties for sale.
  - Track the status of uploaded properties.
- **Buyer Features**:
  - Explore and bid on listed properties.
  - Track bidding history and property details.
- **Surveyor Features**:
  - Verify the authenticity of listed properties.
  - Provide confirmation of property details.
- **Land Listings**:
  - Detailed property listings with images, descriptions, and pricing.
  - Ownership and Confirmation status for property verification.
- **History**:
  - View user and land history.
  - Track actions such as property uploads, bids, and survey confirmations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/tor-real-estate.git
   ```
2. Navigate to the project directory:

   ```bash
   cd tor-real-estate
   ```
3. Create a virtual environment:

   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:

   - On Windows:

     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:

   ```bash
   python manage.py migrate
   ```
7. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
8. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage

1. **Register Users**:

   - Users can register as Sellers, Buyers, or Surveyors.
   - Each user role has specific functionalities:

     - Sellers: Upload properties for sale.
     - Buyers: Bid on listed properties.
     - Surveyors: Verify property authenticity.
2. **Login**:

   - Users can log in with their registered credentials.
3. **Seller Dashboard**:

   - Sellers can upload properties for sale.
   - Track the status of uploaded properties.
   - View and manage their profile details.
4. **Buyer Dashboard**:

   - Buyers can browse listed properties.
   - Place bids on properties they are interested in.
   - Track bidding history and property details.
5. **Surveyor Dashboard**:

   - Surveyors can verify the authenticity of listed properties.
   - Confirm property details and provide survey reports.
   - View and manage their profile information.
6. **Property Listings**:

   - Users can view detailed property listings.
   - Check property images, descriptions, and pricing.
   - Verify property ownership and confirmation status.
7. **User History**:

   - View user history including roles and actions.
   - Track property uploads, bids, and survey confirmations.

## Additional Information

- **Technologies**:

  - Backend: Django
  - Frontend: HTML, CSS, JavaScript
  - Database: SQLite (for development, can be replaced with other databases like PostgreSQL for production)
- **Contributing**:

  - Contributions are welcome! Feel free to fork the repository and submit pull requests.
  - For major changes, please open an issue first to discuss the changes.
- **License**:

  - This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

- This project was created by Levi Chinecherem Chidi.
- Special thanks to Essien for bringing this project.

## Contact

- For inquiries or support, please contact lchinecherem2018@gmail.com.
