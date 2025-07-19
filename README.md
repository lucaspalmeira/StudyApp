# StudyApp

This project is part of my studies with the Flask framework.

I developed a REST API to retrieve data on fungal enzymes from the GH32 family, including their sequences. The API allows users to make requests using filters, enabling the download of data based on the enzyme classification number (EC number).

### Technologies Used:

- Flask
- MongoDB

### Start MongoDB in Linux Terminal:

```
sudo docker star mongodb
```

### Run

```
python app.py
```

### Project Structure:

```
StudyApp
├── app
│   ├── API
│   │   ├── __init__.py
│   │   └── items.py
│   └── __init__.py
├── app.py
├── README.md
├── static
│   ├── css
│   │   ├── footer.css
│   │   ├── header.css
│   │   └── styles.css
│   └── js
│       └── main.js
├── structure.txt
└── templates
    ├── about.html
    ├── api.html
    ├── base.html
    ├── components
    │   ├── footer.html
    │   └── header.html
    ├── contact.html
    └── index.html
```
