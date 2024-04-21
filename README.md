# Isolation Game Solver

## Overview

This repository contains Python code for solving the Isolation game using various search algorithms and heuristics. Isolation is a two-player strategy board game where the players alternate turns, moving a single piece from one cell to another on the board. The goal is to isolate the opponent's piece so that it has no legal moves.

## Files

- `alpha_beta_isolation.py`: Contains functions for the Alpha-Beta Pruning algorithm.
- `heuristic_alpha_beta_isolation.py`: Implements heuristics for the Alpha-Beta Pruning algorithm.
- `heuristics.py`: Defines basic and advanced heuristics for evaluating game states.
- `minimax_isolation.py`: Implements the Minimax algorithm for game state evaluation.
- `game_state.py`: Defines the GameState class representing the current state of the game.
- `player_agent.py`: Implements player agents that make moves based on different strategies and heuristics.
- `game_engine.py`: Provides functions for running and playing Isolation games with different strategies.

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Run `game_engine.py` to play Isolation games using various algorithms and heuristics.
4. Modify the code and experiment with different strategies, heuristics, and game configurations.

## Playing Strategies

- **Minimax**: Uses the Minimax algorithm to evaluate game states.
- **Alpha-Beta Pruning**: Implements the Alpha-Beta Pruning algorithm for more efficient search.
- **Heuristic-based Strategies**: Utilizes different heuristics to evaluate game states and make optimal moves.

## How to Play

1. Run `game_engine.py`.
2. Choose a playing strategy.
3. Follow the prompts to play against the computer.
4. Enjoy the game!

