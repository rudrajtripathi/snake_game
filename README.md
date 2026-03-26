# 🐍 Snake Game

A classic Snake Game built using **Python 3.11** and **Pygame**. Control the snake, eat the food, grow longer, and try not to hit the walls or yourself!

---

## 🎮 Demo

> Run the game locally by following the steps below.

---

## 🖥️ Requirements

- Python 3.11
- Pygame

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rudrajtripathi/snake-game.git
   cd snake-game
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python snake.py
   ```

---

## 🕹️ Controls

| Key            | Action                        |
|----------------|-------------------------------|
| ⬆️ Arrow Up    | Move Up                       |
| ⬇️ Arrow Down  | Move Down                     |
| ⬅️ Arrow Left  | Move Left                     |
| ➡️ Arrow Right | Move Right                    |
| `P`            | Play Again (after losing)     |
| `Q`            | Quit Game                     |

---

## 🌟 Features

- 🟢 Dark green background
- 🟡 Golden yellow snake
- 🔴 Dark red food block
- 📈 Real-time score display
- 💀 Game Over screen with **Play Again** and **Quit** options
- 🚧 Collision detection — walls 

---

## 🎨 Color Scheme

| Element        | Color Name     | RGB Value       |
|----------------|----------------|-----------------|
| Background     | Dark Green     | (0, 100, 0)     |
| Snake          | Golden Yellow  | (255, 185, 15)  |
| Food           | Dark Red       | (139, 0, 0)     |
| Score / Text   | Red            | (255, 0, 0)     |

---

## 🔧 Game Configuration

| Setting        | Value               |
|----------------|---------------------|
| Window Size    | 600 x 400           |
| Snake Speed    | 15 FPS              |
| Snake Block    | 10 px               |
| Font (Score)   | Comic Sans MS, 30px |
| Font (Message) | Calibri, 26px       |

---

## 🚀 Upcoming Features

Here are some exciting features planned for future updates:

- 🏆 **Best Score Display** — Track and show the highest score achieved across sessions
- 🚫 **Reverse Direction Block** — Snake will not be allowed to move in the opposite direction (e.g. if moving right, pressing left will be ignored)
- 🎵 **Sound Effects** — Add sounds for eating food and game over
- 🌈 **Multiple Difficulty Levels** — Easy, Medium, and Hard modes with different speeds
- 🍎 **Different Food Types** — Special food items that give bonus points

---

## 📁 Project Structure

```
snake-game/
│
├── snake.py       # Main game file
└── README.md      # Project documentation
```

---

## 👤 Author

**Rudraj Tripathi**  
GitHub: [@rudrajtripathi](https://github.com/rudrajtripathi)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
