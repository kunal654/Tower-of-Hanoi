
# Tower of Hanoi

This repository contains a Python application that visualizes the solution to the Tower of Hanoi problem using the Tkinter library for the graphical interface. The program demonstrates the recursive algorithm to solve the puzzle with a user-defined number of disks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Visual representation of the Tower of Hanoi puzzle.
- Customizable number of disks.
- Animated movement of disks following the recursive solution.

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/kunal654/tower-of-hanoi.git
cd tower-of-hanoi
```

### Install Dependencies

Ensure you have Python installed. The only required library is Tkinter, which is included with most Python installations.

## Usage

### Define Number of Disks

1. Open `tower_of_hanoi.py`.
2. Modify the variable `n` in the `main()` function to set the number of disks.

### Run the Script

Execute the script to start the application:

```bash
python tower_of_hanoi.py
```

## Script Overview

### `TowerOfHanoi`

This class initializes the Tkinter canvas and sets up the pegs and disks. It includes methods to draw the pegs and disks, move a disk, and solve the Tower of Hanoi puzzle recursively.

#### `__init__(self, master, n)`

Initializes the canvas and the initial state of the pegs and disks.

#### `draw_pegs(self)`

Draws the three pegs on the canvas.

#### `draw_disks(self)`

Draws the disks on the respective pegs based on their current state.

#### `move_disk(self, from_peg, to_peg)`

Moves a disk from one peg to another and updates the canvas.

#### `solve_tower_of_hanoi(self, n, source, auxiliary, target)`

Recursively solves the Tower of Hanoi puzzle and animates the disk movements.

### `main()`

Sets up the Tkinter window, initializes the TowerOfHanoi class, and starts the solution process after a brief delay.

## Customization

### Adjusting the Number of Disks

To change the number of disks, modify the `n` variable in the `main()` function.

```python
def main():
    root = tk.Tk()
    root.title("Tower of Hanoi")
    n = 4  # Set the number of disks here
    tower = TowerOfHanoi(root, n)
    root.after(1000, lambda: tower.solve_tower_of_hanoi(n, 'A', 'B', 'C'))
    root.mainloop()
```

### Change Disk Colors

You can change the color of the disks by modifying the `fill` attribute in the `__init__` method of the `TowerOfHanoi` class.

```python
disk = self.canvas.create_rectangle(0, 0, i * 20, 20, fill='red')
```

## Dependencies

- `tkinter`: For creating the GUI (usually comes pre-installed with Python).
- `time`: For adding delays to create animation effects.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub or contact me directly at [kunalgautam489@gmail.com](mailto:kunalgautam489@gmail.com).

