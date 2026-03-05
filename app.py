from flask import Flask, render_template, request, jsonify
import chess
import chess.engine
from stockfish import Stockfish
import os

app = Flask(__name__)

# This works both locally and on Render automatically
def get_engine():
    sf = Stockfish(path="/opt/homebrew/bin/stockfish")
    return sf

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/best_move", methods=["POST"])
def best_move():
    try:
        fen = request.json.get("fen")
        
        # Validate the FEN
        board = chess.Board(fen)
        if board.is_game_over():
            return jsonify({"error": "Game is already over!"})
        
        sf = get_engine()
        sf.set_fen_position(fen)
        
        best = sf.get_best_move_time(2000)  # 2 seconds thinking time
        evaluation = sf.get_evaluation()
        
        # Format score
        if evaluation["type"] == "cp":
            score = f"{evaluation['value'] / 100:+.2f}"
        else:
            score = f"Mate in {abs(evaluation['value'])}"
        
        return jsonify({
            "move": best,
            "score": score
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)