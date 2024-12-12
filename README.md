# Monitoring ELK Flask Application

This project is a log monitoring application that integrates Elasticsearch, Logstash, Kibana (ELK Stack), Flask, MongoDB, and Redis. It processes log files in CSV and JSON formats, stores them in Elasticsearch and MongoDB, and supports real-time log searches with caching via Redis.

## **Features**
- Upload logs in CSV and JSON formats
- Store logs in Elasticsearch and MongoDB
- Search logs with Redis caching
- Visualize data using Kibana
- REST API with Flask backend

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/azizswebni/monitoring-elk-flask.git
cd monitoring-elk-flask
```

### **2. Set Up Environment Variables**
Create a `.env` file in the root directory and configure the following:
```env
FLASK_SECRET_KEY=some_secure_key
ELASTICSEARCH_HOST=http://localhost:9200
MONGODB_URI=mongodb://localhost:27017
MONGO_DB_NAME=logs_db
MONGO_COLLECTION_NAME=logs
REDIS_HOST=localhost
REDIS_PORT=6379
KIBANA_API=http://localhost:5601
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Start the Application with Docker Compose**
```bash
docker-compose up --build
```

---

## **Usage**

### **1. Access the Web Interface**
- Visit: `http://localhost:5000`

### **2. Upload Logs**
- Upload CSV or JSON files using the provided forms.

### **3. Search Logs**
- Search logs using keywords.

### **4. Visualize in Kibana**
- Visit Kibana: `http://localhost:5601`

---

## **Project Structure**
```
monitoring-elk-flask/
│
├── app.py               # Flask application
├── Dockerfile           # Docker image setup for Flask
├── docker-compose.yml   # Docker Compose configuration
├── logstash.conf        # Logstash configuration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── templates/           # HTML templates
│   └── index.html       # Main web interface
├── tests/               # Unit tests
│   └── test_app.py      # Test cases
└── README.md            # Project documentation
```

---

## **Technologies Used**
- Flask (Backend API)
- Elasticsearch (Data Search Engine)
- Logstash (Data Ingestion)
- Kibana (Data Visualization)
- MongoDB (Data Storage)
- Redis (Caching)
- Docker & Docker Compose


## **Author**
- **azizswebni** - [GitHub Profile](https://github.com/azizswebni)
