# 📆 django-agenda

**django-agenda** is a web application built with Django for managing contacts and scheduling appointments. It offers an intuitive interface to add, edit, and view contacts, as well as to schedule appointments efficiently.

## 🚀 Demo

A video showing the features of the website <a href="https://youtu.be/Mbav1DLsPy0" target="_blank">here</a>.

## 💻 Features

**django-agenda** is a Django-based web application designed for efficient contact management. It provides a user-friendly interface to manage contacts seamlessly.

### 🔐 User Authentication and Verification

- **Secure Authentication**: Implements Django's built-in authentication system, allowing users to register, log in, and log out securely.

### 👥 User and Contact Management (CRUD)

- **User Management**: Administrators can create, read, update, and delete user accounts, managing access and permissions effectively.
- **Contact Management**: Users can add new contacts, view detailed contact information, update existing contacts, and remove contacts as needed.

## 🛠️ Technologies Used

- [Python 3.10+](https://www.python.org/downloads/)
- [Django 4.x](https://www.djangoproject.com/)
- HTML5, CSS3, and JavaScript
- SQLite (default) or PostgreSQL

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/thallystorres/django-agenda.git
   cd django-agenda
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate # On Unix
   venv\Scripts\activate # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

## 📁 Project Structure

```bash
django-agenda/
├── base_static/           # Global static files
├── base_templates/        # Base templates
├── contact/               # Contact management app
├── project/               # Main project configurations
├── utils/                 # Utility functions
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🤡 utils/mock.py

Run this script with `python utils/mock.py` to mock data in the application's database. You can change the number of contacts to be mocked by editing the `NUMBER_OF_OBJECTS` constant.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙋‍♂️ Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📞 Contact

Developed by [Thallys Torres](https://github.com/thallystorres).

## 💭 Next steps

I was planing to deploy this application on Google Cloud Plataform to practice deployment concepts, but i found it requires extra steps that i can't afford now. Hopefully, someday, you could access this web application in just one click. So... Help with this!

<a href="https://buymeacoffee.com/thallysauu4" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60" width="217">
</a>
