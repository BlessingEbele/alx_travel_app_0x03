alx_travel_app_0x02 – Chapa Payment Integration

This project is a Django travel booking application with integrated payment processing via the Chapa API.
Users can make secure payments for bookings, and the system verifies and updates payment status automatically.

📦 Project Setup

Clone the Repository

git clone https://github.com/<your-username>/alx_travel_app_0x02.git
cd alx_travel_app_0x02


Create a Virtual Environment & Install Dependencies

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Run Migrations

python manage.py makemigrations
python manage.py migrate


Create a Superuser

python manage.py createsuperuser


Run the Development Server

python manage.py runserver

🔑 How to Set .env

Create a .env file in the root of your project:

SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CHAPA_SECRET_KEY=your_chapa_secret_key


Notes:

Use the Sandbox API Key from your Chapa dashboard for testing.

Keep .env in .gitignore to avoid committing credentials.

🌐 API Endpoints
Method	Endpoint	Description
POST	/initiate-payment/	Initiates a payment with Chapa and returns payment link
GET	/verify-payment/<tx_ref>/	Verifies a payment status with Chapa
📩 Example Request/Response
1️⃣ Initiate Payment

Request

POST /initiate-payment/
Content-Type: application/json

{
    "booking_reference": "BOOK12345",
    "amount": "5000",
    "email": "user@example.com"
}


Successful Response

{
    "status": "success",
    "message": "Hosted Link",
    "data": {
        "checkout_url": "https://checkout.chapa.co/checkout/payment/XYZ123..."
    }
}

2️⃣ Verify Payment

Request

GET /verify-payment/BOOK12345/


Successful Response

{
    "status": "success",
    "message": "Payment verified successfully",
    "data": {
        "status": "success",
        "amount": "5000.00",
        "currency": "ETB"
    }
}

🧪 Testing Steps

Start Server

python manage.py runserver


Initiate a Payment

Use Postman or frontend to send a POST request to /initiate-payment/ with booking details.

You’ll get a checkout_url from Chapa.

Complete Payment in Sandbox

Open the checkout_url in your browser.

Use Chapa’s test card details for sandbox payments.

Verify Payment

After payment, call /verify-payment/<tx_ref>/.

Check if the Payment model status changes to "Completed" in Django Admin.

Check Database

In the Django Admin panel, confirm that the transaction ID, amount, and status are correctly stored.



# alx_travel_app_0x03

## Setup Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Start RabbitMQ:
   sudo systemctl start rabbitmq-server

3. Run migrations:
   python manage.py migrate

4. Start Celery worker:
   celery -A alx_travel_app worker -l info

5. Start Django server:
   python manage.py runserver

6. Test:
   - Create a booking via API
   - Check email inbox for confirmation
