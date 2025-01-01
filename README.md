# 🌍 Sensor Fusion for Disaster Forecasting and Environmental Surveillance

This project is a Disaster Detection and Prediction System developed using Arduino Uno and various sensors to monitor critical environmental parameters such as earthquake activity, rain duration, temperature, humidity, CO2 concentration, and dust density. The system collects data in real-time and provides dynamic visualizations to aid in disaster preparedness and environmental surveillance.

## 📋 Table of Contents
- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [⚙️ Setup Instructions](#️-setup-instructions)
- [🚀 Usage](#-usage)
- [📂 File Descriptions](#-file-descriptions)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## ✨ Features
- 📡 Real-time data collection from multiple sensors using Arduino Uno.
- 🔗 Data transmission to a Python environment via the Serial library.
- 💾 Storage of sensor data in CSV format for easy access and analysis.
- 📊 Interactive web application built with Streamlit for dynamic data visualization.
- 📈 Visual analytics provided by Matplotlib, Seaborn, and Plotly.

## 🛠 Tech Stack
- **Hardware:** Arduino Uno
- **Programming Languages:** Python
- **Libraries:** 
  - Serial Library
  - Pandas
  - Matplotlib
  - Seaborn
  - Plotly
  - Streamlit
- **Data Format:** CSV

## ⚙️ Setup Instructions

1. **🔗 Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. ** 🔌 Connect Arduino Uno:

- Attach the sensors to your Arduino Uno as per the project configuration.
- Ensure that the Arduino IDE is installed and properly set up on your machine.

3.## 🏃‍♂️ Run the tracker script:

1. Open the `tracker.py` file in Visual Studio Code.
2. If you encounter errors related to the CSV file path, replace the relative path with the absolute path in the script.
3. Execute the `tracker.py` script to start collecting sensor data:
   ```bash
   python tracker.py
   
## 4. 🚀 Launch the Streamlit App:

- Open a terminal in the project directory.
- Run the Streamlit application to visualize the collected data:
  ```bash
  streamlit run final.py


## 5. 🚀 Usage

### 📡 Data Collection:
- The `tracker.py` script continuously collects sensor data from the Arduino Uno and appends it to the `sensor_data.csv` file.

### 📊 Data Visualization:
- The Streamlit app (`final.py`) reads data from `sensor_data.csv` and provides interactive analytics and visualizations.

## 📂 File Descriptions

- **`final.py`:** 
  - A Streamlit application that reads the `sensor_data.csv` file and provides interactive data visualizations using Plotly, Matplotlib, and Seaborn.
  
- **`sensor_data.csv`:**
  - The CSV file where sensor data is stored. Each row represents a set of readings from the sensors at a given time.
  
- **`tracker.py`:**
  - A Python script that collects real-time data from the sensors via the Arduino Uno and appends it to the `sensor_data.csv` file in a predefined format.
 
    ```python
  x=(lambda y:y*4)
print(x(5))

    ```

