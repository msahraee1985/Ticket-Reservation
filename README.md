🎟️ Ticket Reservation System API (Django REST Framework)
This project is a ticket reservation system for transportation (flights, trains, buses) built using Django and Django REST Framework. It provides a robust API for user authentication, transport listing, ticket booking, and mock payment processing.

✅ Features (MVP + Enhancements)
🧑‍💻 Authentication & Users (users/)

User registration and login using JWT (JSON Web Tokens).
Access token and refresh token handling.
API endpoints protected with IsAuthenticated permissions.

🚍 Transport (transport/)

Transport model with fields:
transport_type (flight, train, bus).
origin, destination, departure_time, arrival_time, price.
Total seat capacity (capacity).


API for listing available transports with:
Filtering by origin, destination, and transport_type.
Sorting by price and departure_time.
Pagination (10 items per page).



🧾 Ticket Booking (bookings/)

Booking model includes:
user, transport, seat_number, total_price, booking_date, status.


Booking API with validations:
Prevents booking the same seat twice.
Prevents multiple bookings by the same user on the same transport.
Checks available capacity.
Blocks bookings for past departures.


List bookings for the current user.
Cancel booking (only by the booking owner).

💳 Mock Payment System

Payment model added to bookings/models.py (mock implementation).
API to simulate and confirm payments.
Includes validations for secure mock payment scenarios.
Note: Currently in bookings/ app; should be moved to a separate app in production.

🧪 Automated Testing

test_booking.py: Covers booking-related features and APIs.
test_payment.py: Tests booking and payment integration scenarios.
Note: Some test mismatches require clarification of business rules.
Run tests: ```bashpython manage.py test




📦 Project Structure
ticket_booking/
├── bookings/        # Booking and payment logic
├── transport/       # Transport services
├── users/           # Authentication and registration
├── config/          # Project settings and configuration
├── manage.py        # Django management script


🔐 Sample Endpoints
POST   /api/v1/register/                  # Register a new user
POST   /api/v1/token/                    # Get JWT token
GET    /api/v1/transport/                # List transports (with filters & sorting)
POST   /api/v1/bookings/                 # Book a ticket (authenticated users)
GET    /api/v1/bookings/                 # View current user's bookings
POST   /api/v1/bookings/{id}/cancel/     # Cancel a booking
POST   /api/v1/payments/{booking_id}/confirm/   # Confirm mock payment


🛠️ Installation & Setup

Clone the repository:git clone <repository-url>


Create a virtual environment:python -m venv venv


Activate the virtual environment:
Windows: ```bashvenv\Scripts\activate


Linux/Mac: ```bashsource venv/bin/activate




Install dependencies:pip install -r requirements.txt


Run migrations:python manage.py migrate


Start the server:python manage.py runserver




📋 Dependencies

Python 3.8+
Django 4.2+
Django REST Framework 3.14+
djangorestframework-simplejwt 5.2+


🤝 Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

👨‍💻 Developers

Matin Pakzadan
Mehrdad Ranjbar


🎟️ سیستم API رزرو بلیت (Django REST Framework)
این پروژه یک سیستم رزرو بلیت برای وسایل نقلیه (پرواز، قطار، اتوبوس) است که با Django و Django REST Framework توسعه داده شده است. این سیستم یک API قدرتمند برای احراز هویت کاربران، لیست وسایل نقلیه، رزرو بلیت، و پردازش پرداخت ساختگی ارائه می‌دهد.

✅ ویژگی‌های پیاده‌سازی‌شده (MVP + توسعه)
🧑‍💻 احراز هویت و کاربران (users/)

ثبت‌نام و ورود کاربران با استفاده از JWT.
مدیریت توکن دسترسی و توکن تازه‌سازی (refresh token).
حفاظت از APIها با استفاده از مجوز IsAuthenticated.

🚍 وسایل نقلیه (transport/)

مدل Transport با فیلدهای:
transport_type (پرواز، قطار، اتوبوس).
origin (مبدا)، destination (مقصد)، departure_time (زمان حرکت)، arrival_time (زمان رسیدن)، price (قیمت).
ظرفیت کلی صندلی‌ها (capacity).


API برای لیست کردن وسایل نقلیه با:
فیلتر بر اساس مبدا، مقصد، و نوع وسیله.
مرتب‌سازی بر اساس قیمت و زمان حرکت.
صفحه‌بندی (۱۰ آیتم در هر صفحه).



🧾 رزرو بلیت (bookings/)

مدل Booking شامل:
user (کاربر)، transport (وسیله نقلیه)، seat_number (شماره صندلی)، total_price (قیمت نهایی)، booking_date (تاریخ رزرو)، status (وضعیت).


API رزرو با اعتبارسنجی:
جلوگیری از رزرو صندلی تکراری.
جلوگیری از رزرو چندباره توسط یک کاربر برای یک وسیله.
بررسی ظرفیت باقی‌مانده.
جلوگیری از رزرو برای وسایل نقلیه‌ای که زمان حرکت‌شان گذشته است.


لیست رزروهای کاربر جاری.
امکان کنسل کردن رزرو (فقط توسط صاحب رزرو).

💳 سیستم پرداخت ساختگی

مدل Payment به‌صورت ساختگی در bookings/models.py پیاده‌سازی شده است.
API برای شبیه‌سازی و تأیید پرداخت.
شامل اعتبارسنجی‌های لازم برای سناریوهای پرداخت ساختگی.
توجه: در حال حاضر در اپ bookings/ قرار دارد؛ در سیستم‌های واقعی بهتر است به اپ جداگانه منتقل شود.

🧪 تست‌های اتوماتیک

فایل test_booking.py: پوشش ویژگی‌ها و APIهای مربوط به رزرو.
فایل test_payment.py: پوشش سناریوهای رزرو و پرداخت.
توجه: برخی تست‌ها نیاز به شفاف‌سازی قوانین تجاری دارند.
اجرای تست‌ها:python manage.py test




📦 ساختار پروژه
ticket_booking/
├── bookings/        # منطق رزرو و پرداخت
├── transport/       # خدمات وسایل نقلیه
├── users/           # احراز هویت و ثبت‌نام
├── config/          # تنظیمات پروژه
├── manage.py        # اسکریپت مدیریت جنگو


🔐 نمونه Endpointها
POST   /api/v1/register/                  # ثبت‌نام کاربر
POST   /api/v1/token/                    # دریافت توکن (JWT)
GET    /api/v1/transport/                # لیست وسایل نقلیه (با فیلتر و مرتب‌سازی)
POST   /api/v1/bookings/                 # رزرو بلیت (کاربران لاگین‌شده)
GET    /api/v1/bookings/                 # مشاهده رزروهای کاربر جاری
POST   /api/v1/bookings/{id}/cancel/     # کنسل کردن رزرو
POST   /api/v1/payments/{booking_id}/confirm/   # تأیید پرداخت ساختگی


🛠️ نصب و راه‌اندازی
۱. کلون کردن مخزن:
git clone <repository-url>

۲. ایجاد محیط مجازی:
python -m venv venv

۳. فعال‌سازی محیط مجازی:

ویندوز:venv\Scripts\activate


لینوکس/مک:source venv/bin/activate



۴. نصب وابستگی‌ها:
pip install -r requirements.txt

۵. اجرای مهاجرت‌ها:
python manage.py migrate

۶. اجرای سرور:
python manage.py runserver


📋 وابستگی‌ها

پایتون ۳.۸ یا بالاتر
جنگو ۴.۲ یا بالاتر
Django REST Framework نسخه ۳.۱۴ یا بالاتر
djangorestframework-simplejwt نسخه ۵.۲ یا بالاتر


🤝 مشارکت
از مشارکت شما استقبال می‌کنیم! لطفاً یک pull request ارسال کنید یا برای بحث، یک issue باز کنید.

👨‍💻 توسعه‌دهندگان

متین پاکزادان
مهرداد رنجبر
