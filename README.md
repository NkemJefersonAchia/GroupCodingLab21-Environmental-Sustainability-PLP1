
#  AFRI‑RECYCLE CLI App

**Turn waste into rewards: log recyclables, earn points, request pickups, and learn how to manage waste—all from your terminal!**

##  Overview

AFRI-RECYCLE is a **menu-driven Python CLI application** that helps users:

1. **Log recyclables** (plastic, glass, paper, cans) by entering the item and its weight.
2. **Earn points** calculated as 25% of the material’s value in Rwandan Francs (RWF).
3. **View points and cash equivalent** to track recycling progress.
4. **Redeem rewards** — exchange points for cash or gift coupons.
5. **Locate recycling centers** and **request home pickup** for recyclables.
6. **Get daily tips**—displaying two random waste education tips each session.

All data is stored and managed using a **relational MySQL database on Aiven.io**.


## 🛠 Prerequisites

Before running the app, ensure you have:

* **Python 3.8+** (Ubuntu 20.04 recommended)
* **Virtual environment support**:

  ```bash
  sudo apt update
  sudo apt install python3-venv
  ```
* **MySQL Connector for Python**:

  ```bash
  pip install mysql-connector-python
  ```
* **Aiven MySQL service** ready with these environment variables set:

  ```bash
  export MYSQL_HOST="your-aiven-host"
  export MYSQL_PORT="your-port"
  export MYSQL_USER="avnadmin"
  export MYSQL_PASSWORD="your-password"
  export MYSQL_DB="afrirecycle"
  export MYSQL_CA_PEM="/path/to/ca.pem"
  ```
* **SSL Certificate** downloaded from Aiven console to enable secure DB connection.


##  Project Structure

```
afrirecycle/
├── db.py                 # Handles Aiven MySQL connection and sets up tables
├── init_data.py          # Populates initial data: centers, tips, rewards
├── log_recyclables.py    # Records recyclables and computes points
├── estimate_value.py     # Shows user’s total points and RWF value
├── redeem_rewards.py     # Lets users convert points into rewards
├── collection_points.py  # Lists centers and enables pickup requests
├── waste_education.py    # Shows two random waste-education tips
├── main.py               # Main menu launcher and orchestration
└── README.md             # This guide
```

##  Setup & Run

1. **Clone the repo**

   ```bash
   git clone <repo-url>
   cd afrirecycle
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install mysql-connector-python
   ```

4. **Set Aiven DB environment vars**

   ```bash
   export MYSQL_HOST=...
   export MYSQL_PORT=...
   export MYSQL_USER=...
   export MYSQL_PASSWORD=...
   export MYSQL_DB=afrirecycle
   export MYSQL_CA_PEM=/path/to/ca.pem
   ```

5. **Run the app**

   ```bash
   python main.py
   ```

---

##  Application Features & Flow

Upon launching (`python main.py`):

* **Database initialization** runs: creates tables (`users`, `centers`, `rewards`, `tips`) and seeds them.
* Prompts for **your username** to identify your session.
* Presents the following options:

### 1. Log Recyclables Collected

* Prompts you to **choose an item** (via easy menu).
* Ask for its **weight in kg**.
* Calculates **awarded points** as:
  `points = rate(RWF/kg) * weight * 0.25`.
* Stores the update in `users` table.

### 2. Check Estimated Cash Value

* Fetches your current points from the database.
* Converts points 1:1 into RWF.
* Displays both points and currency equivalent.

### 3. Convert Points into Rewards

* Shows a list of rewards (e.g., voucher, coupon) with required points.
* Lets you **redeem** a reward by entering its ID.
* Deducts points and confirms redemption.

### 4. Locate Collection Points

* Lists all centers with:

  * Name
  * Location
  * Status (open/closed)
  * Distance (in km)

### 5. Request Home Pickup

* Prompts you for:

  * Name of your local collection center
  * Weight of recyclables
* Displays confirmation for pickup request (logs simulated, no DB write).

### 6. Waste Education

* Shows **two random tips** from the database.
* Encourages responsible waste behavior.

### 0. Exit

* Safely quits the application.

##  Checking Your Database

To inspect tables, connect via MySQL CLI:

```bash
mysql \
  --host=$MYSQL_HOST \
  --port=$MYSQL_PORT \
  --user=$MYSQL_USER \
  --password=$MYSQL_PASSWORD \
  --ssl-ca=$MYSQL_CA_PEM \
  $MYSQL_DB
```

Then run:

```sql
SHOW TABLES;
DESCRIBE users;
SELECT * FROM centers LIMIT 5;
SELECT * FROM tips;
```

---

##  Troubleshooting

* **SSL errors**? Ensure `MYSQL_CA_PEM` path is valid and Aiven certificate is correct.
* **Missing tables or tips?** Re-run `python main.py` to initialize.
* **Invalid user input**? The app asks politely again—just follow prompts.
* **DB issues**? Confirm your Aiven instance is running and your network allows outbound connections.

---

##  Thank You!

* Anyone can use this app—no heavy installs, no GUI needed.
* Activate the venv, set your variables, run `main.py`, and you’re good to go.
* Environmentally friendly, easy to track, and motivating!
