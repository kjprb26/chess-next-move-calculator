# ♟ Chess Next-Move Calculator

A web application that lets you set up any chess position on an interactive board and calculates the best possible next move using the Stockfish chess engine — one of the strongest chess engines in the world.

---

## 📌 What It Does

- Drag and drop chess pieces on a fully interactive chessboard
- Click **Calculate Best Move** to get the strongest move for the current position
- View a live **evaluation bar** showing who is winning
- Browse **popular openings** and **checkmate patterns** on the side panels and load them directly onto the board
- **Flip** the board, **undo** moves, or **reset** to the starting position at any time

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Chessboard UI | chessboard.js |
| Chess Rules | chess.js |
| Backend Server | Python + Flask |
| Chess Engine | Stockfish (via Homebrew) |
| Production Server | Gunicorn |
| Deployment | Render.com |

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.11 or later
- Stockfish installed via Homebrew (`brew install stockfish`)
- Git

### Steps

1. Clone the repository:
```bash
git clone https://github.com/kjprb26/chess-next-move-calculator.git
cd chess-next-move-calculator
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

3. Start the server:
```bash
python3 app.py
```

4. Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🌐 Live Demo

The application is deployed and accessible at:
```
https://chess-next-move-calculator.onrender.com
```

> Note: The site may take up to 30 seconds to wake up on first visit due to Render's free tier sleep policy.

---

## 🧪 Testing Instructions

### Test 1 — Starting Position (Basic)
- Open the website
- Without moving any pieces, click **Calculate Best Move**
- **Expected result:** The engine suggests `e2e4` or `d2d4` (standard opening moves) with an evaluation near `+0.00`

### Test 2 — Drag and Drop
- Drag the white pawn from `e2` to `e4`
- Drag the black pawn from `e7` to `e5`
- Click **Calculate Best Move**
- **Expected result:** Engine suggests a response move and evaluation bar updates

### Test 3 — Load a Reference Position
- Click **Load Position** under **Sicilian Defence** in the left panel
- The main board should update to the Sicilian position
- Click **Calculate Best Move**
- **Expected result:** Engine calculates best move for that specific position

### Test 4 — Scholar's Mate Detection
- Click **Load Position** under **Scholar's Mate** in the right panel
- **Expected result:** App returns an error message saying the game is already over

### Test 5 — Undo Move
- Make any move on the board
- Click **Undo**
- **Expected result:** The piece returns to its previous square

### Test 6 — Flip Board
- Click **Flip Board**
- **Expected result:** Board flips so Black pieces are at the bottom

### Test 7 — Evaluation Bar
- Make several moves favouring White (move white pieces aggressively)
- **Expected result:** Evaluation bar shifts towards White (bottom fills up) and score shows a positive number

### Test 8 — Reset
- Make several moves
- Click **Reset**
- **Expected result:** Board returns to the standard starting position

---

## 📁 Project Structure
```
chess-next-move-calculator/
├── app.py              # Python Flask server — handles requests and Stockfish communication
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for Render deployment
├── static/             # Static assets (background image)
└── templates/
    └── index.html      # Frontend — chessboard, styling, and JavaScript logic
```

---

## 📦 Dependencies

- `flask` — Python web server framework
- `python-chess` — Chess board and FEN string handling
- `stockfish` — Python wrapper for the Stockfish engine
- `gunicorn` — Production WSGI server for deployment

---

## 👤 Author

Made by [Kartik Patek]  
Student Project — [CS1301 Project]
