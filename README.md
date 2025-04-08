# AI-XO

An intelligent Tic-Tac-Toe game implementation featuring both player vs. player and player vs. AI modes. The AI uses the minimax algorithm with alpha-beta pruning to make optimal moves.

## Features

- **Multiple Game Modes**:
  - Player vs. Player: Challenge a friend on the same device
  - Player vs. AI: Test your skills against an unbeatable AI opponent
  
- **Smart AI Implementation**:
  - Utilizes the minimax algorithm with alpha-beta pruning
  - AI analyzes possible future moves to make optimal decisions
  - Provides a challenging opponent that plays perfectly

- **Clean UI**:
  - Simple and intuitive interface
  - Visual feedback for game status and results
  - Responsive design for different screen sizes

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ishi-ta-lal/AI-XO.git
cd AI-XO
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

## How to Play

1. Launch the game
2. Select your preferred game mode:
- Human vs. Human
- Human vs. AI
3. For Human vs. Human mode:
- Players take turns clicking on the grid to place their marks (X and O)
4. For Human vs. AI mode:
- Player makes a move by clicking on the grid
- AI automatically responds with its move
5. The game ends when a player wins by forming a line (horizontal, vertical, or diagonal) or when the board is full (draw)

## Implementation Details

### Minimax Algorithm

The AI uses the minimax algorithm to determine the best possible move. This algorithm:

1. Explores all possible future game states
2. Assigns scores to each state (+10 for AI win, -10 for human win, 0 for draw)
3. Chooses the move that maximizes the AI's chances of winning

### Alpha-Beta Pruning

To improve performance, the algorithm uses alpha-beta pruning to reduce the number of nodes evaluated in the search tree. This optimization allows for quicker AI responses without sacrificing intelligence.

## Project Structure

- `main.py`: Entry point that initializes the game
- `game.py`: Core game logic and state management
- `board.py`: Board representation and move validation
- `ai.py`: AI implementation with minimax algorithm
- `ui.py`: User interface elements and rendering

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The minimax algorithm implementation is inspired by various resources on game theory and AI
- Thanks to the Pygame community for their excellent documentation and resources
