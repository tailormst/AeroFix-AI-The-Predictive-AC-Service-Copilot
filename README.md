# AeroFix AI: Predictive AC Service Copilot

> **Intelligent predictive maintenance for air conditioning systems using real-time IoT monitoring and machine learning**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-green?style=flat-square&logo=fastapi)
![Supabase](https://img.shields.io/badge/Supabase-Database-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 📋 Overview

AeroFix AI is an enterprise-grade predictive maintenance platform designed to monitor, analyze, and predict failures in air conditioning systems before they occur. By leveraging real-time IoT sensor data and advanced analytics, AeroFix helps facility managers and technicians reduce downtime, optimize maintenance schedules, and lower operational costs.

## 🎯 Key Features

- **Real-Time IoT Monitoring** - Continuous sensor data collection from AC units across multiple facilities
- **Predictive Failure Detection** - Machine learning models that identify potential failures before they impact operations
- **Anomaly Detection** - Intelligent pattern recognition for uncommon system behaviors
- **Multi-Building Support** - Scalable architecture supporting various facility types (offices, server rooms, etc.)
- **RESTful API** - Easy integration with existing HVAC management systems
- **Comprehensive Analytics** - Historical analysis and performance insights

## 🏗️ Architecture

The system consists of four main components:

```
┌─────────────────────────────────────────┐
│      FastAPI Backend Server             │
├─────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────────┐ │
│  │  IoT Logs    │  │   Analytics      │ │
│  │  Router      │  │   Router         │ │
│  └──────────────┘  └──────────────────┘ │
│  ┌──────────────┐  ┌──────────────────┐ │
│  │  Context     │  │   Priority       │ │
│  │  Router      │  │   Router         │ │
│  └──────────────┘  └──────────────────┘ │
└────────────┬────────────────────────────┘
             │
      ┌──────▼───────┐
      │  Supabase    │
      │  (PostgreSQL)│
      └──────────────┘
```

### Components

- **Main API** (`main.py`) - FastAPI application entry point with routing
- **Log Generator** (`generator.py`) - Simulates AC system sensor data with various failure scenarios
- **Database Layer** (`db.py`) - Supabase integration for data persistence
- **Routes** - Modular API endpoints for different data streams

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Supabase account and credentials
- Environment variables configured

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tailormst/AeroFix-AI-The-Predictive-AC-Service-Copilot.git
   cd AeroFix-AI-The-Predictive-AC-Service-Copilot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   export SUPABASE_URL=your_supabase_url
   export SUPABASE_KEY=your_supabase_key
   ```

5. **Initialize the database**
   ```bash
   python seed_devices.py
   ```

6. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### Base URL
```
http://localhost:8000
```

### Available Routes

| Endpoint | Description |
|----------|-------------|
| `GET /` | Health check - Backend status |
| `/logs/*` | IoT log ingestion and retrieval |
| `/analytics/*` | System performance analytics |
| `/context/*` | Device context and metadata |
| `/priority/*` | Maintenance priority calculations |

### Example Request

```bash
curl -X GET http://localhost:8000/
```

Response:
```json
{
  "message": "AeroFix Backend Running"
}
```

## 🔧 Data Models

### AC System Telemetry

The system monitors the following parameters:

| Parameter | Range | Unit |
|-----------|-------|------|
| Compressor Frequency | 0-100 | Hz |
| Power Consumption | 1100-3000 | W |
| Ambient Temperature | -5-40 | °C |
| Evaporator Temperature | 8-26 | °C |
| Refrigerant Pressure | 40-130 | PSI |

### Error Codes

- **E1** - Gas Leak Detected
- **P4** - Compressor Overheat
- **E6** - Sensor Fault
- **F9** - Motor Jam
- **NONE** - System Healthy

## 📊 Failure Scenarios

The system can identify and predict:

1. **Gas Leak** - Low refrigerant pressure with elevated evaporator temperatures
2. **Compressor Overheat** - High frequency and power consumption
3. **Sensor Failure** - Invalid temperature readings
4. **Motor Jam** - Zero compressor frequency with high power draw

## 🗂️ Project Structure

```
AeroFix-AI-The-Predictive-AC-Service-Copilot/
├── main.py              # FastAPI application
├── generator.py         # IoT data simulator
├── db.py                # Database configuration
├── seed_devices.py      # Initial device setup
├── routes/              # API route modules
│   ├── logs.py
│   ├── analytics.py
│   ├── context.py
│   └── priority.py
├── requirements.txt     # Python dependencies
└── .env.example         # Environment template
```

## 📦 Dependencies

Key libraries include:

- **FastAPI** (0.136+) - Web framework
- **Uvicorn** (0.46+) - ASGI server
- **Supabase** (2.30+) - Backend-as-a-Service
- **Pandas** (2.3+) - Data analysis
- **NumPy** (2.2+) - Numerical computing
- **Pydantic** (2.13+) - Data validation

See `requirements.txt` for complete dependency list.

## 🤖 Running the Data Simulator

To generate realistic AC telemetry data:

```bash
python generator.py
```

This will continuously:
- Fetch active devices from the database
- Generate sensor readings with realistic failure scenarios
- Insert logs every 10 seconds
- Display a summary of generated logs

## 🔐 Security Considerations

- Store Supabase credentials in environment variables
- Never commit `.env` files to version control
- Use strong API keys for production
- Implement rate limiting for API endpoints
- Enable row-level security (RLS) on Supabase tables

## 📈 Performance Optimization

The system is optimized for:

- **Scalability**: Handle thousands of concurrent device connections
- **Latency**: Sub-second response times for analytics queries
- **Reliability**: Automatic retry logic with exponential backoff
- **Efficiency**: Bulk operations for large datasets

## 🐛 Troubleshooting

### Connection Issues
```bash
# Verify Supabase credentials
echo $SUPABASE_URL
echo $SUPABASE_KEY

# Test API connectivity
curl http://localhost:8000/
```

### Database Errors
```bash
# Reset devices
python seed_devices.py

# Check logs in Supabase dashboard
```

### Performance Issues
- Monitor query execution times
- Enable database connection pooling
- Consider caching frequently accessed data

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💼 Author

**Taylor M. Smith**  
[GitHub](https://github.com/tailormst) | [LinkedIn](https://linkedin.com/in/taylorsmith)

## 🙏 Acknowledgments

- FastAPI and Starlette communities
- Supabase for database hosting
- IoT and predictive maintenance enthusiasts

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/tailormst/AeroFix-AI-The-Predictive-AC-Service-Copilot/issues)
- Check existing documentation
- Review API logs for debugging information

---

**Last Updated:** June 2026  
**Status:** Active Development
