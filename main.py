import tkinter as tk
from tkinter import Canvas

class TowerOfHanoi:
    def __init__(self, master, n):
        self.master = master
        self.n = n
        self.canvas = Canvas(master, width=600, height=400, bg='white')
        self.canvas.pack()
        self.pegs = {'A': [], 'B': [], 'C': []}
        self.peg_coords = {'A': 100, 'B': 300, 'C': 500}
        self.disks = []

        for i in range(n, 0, -1):
            self.pegs['A'].append(i)
            disk = self.canvas.create_rectangle(0, 0, i * 20, 20, fill='blue')
            self.disks.append(disk)

        self.draw_pegs()
        self.draw_disks()

    def draw_pegs(self):
        for peg in self.peg_coords.values():
            self.canvas.create_line(peg, 100, peg, 300, width=10)

    def draw_disks(self):
        for peg in 'ABC':
            for i, disk in enumerate(self.pegs[peg]):
                x = self.peg_coords[peg] - disk * 10
                y = 300 - (i + 1) * 20
                self.canvas.coords(self.disks[disk - 1], x, y, x + disk * 20, y + 20)

    def move_disk(self, from_peg, to_peg):
        disk = self.pegs[from_peg].pop()
        self.pegs[to_peg].append(disk)
        self.draw_disks()
        self.master.update()
        self.master.after(500)  # Pause for animation effect

    def solve_tower_of_hanoi(self, n, source, auxiliary, target):
        if n == 1:
            self.move_disk(source, target)
        else:
            self.solve_tower_of_hanoi(n-1, source, target, auxiliary)
            self.move_disk(source, target)
            self.solve_tower_of_hanoi(n-1, auxiliary, source, target)

def main():
    root = tk.Tk()
    root.title("Tower of Hanoi")
    n = 3  # Number of disks
    tower = TowerOfHanoi(root, n)
    root.after(1000, lambda: tower.solve_tower_of_hanoi(n, 'A', 'B', 'C'))
    root.mainloop()

if __name__ == "__main__":
    main()
