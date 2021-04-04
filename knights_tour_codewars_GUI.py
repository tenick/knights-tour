from tkinter import *
import random
import time
import queue
import threading


def print_list(arr):
    for x in arr:
        print(x)


def possible_coordinate(r, c, grid, row_length, col_length):
    if r < 0 or c < 0:
        return False
    elif r >= row_length or c >= col_length:
        return False
    elif (r, c) in visited_moves.keys():
        return False
    else:
        return True


def get_possible_moves(grid, k):
    possible_moves = []
    grid_row_length = len(grid)
    grid_col_length = len(grid[0])

    # UP
    # UP LEFT
    r = k[0] - 2
    c = k[1] - 1
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])
    # UP RIGHT
    r = k[0] - 2
    c = k[1] + 1
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])

    # RIGHT
    # RIGHT UP
    r = k[0] - 1
    c = k[1] + 2
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])
    # RIGHT DOWN
    r = k[0] + 1
    c = k[1] + 2
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])

    # DOWN
    # DOWN RIGHT
    r = k[0] + 2
    c = k[1] + 1
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])
    # ODWN LEFT
    r = k[0] + 2
    c = k[1] - 1
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])

    # LEFT
    # LEFT UP
    r = k[0] - 1
    c = k[1] - 2
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])
    # LEFT DOWN
    r = k[0] + 1
    c = k[1] - 2
    if possible_coordinate(r, c, grid, grid_row_length, grid_col_length):
        possible_moves.append([r, c])

    return possible_moves


def draw_grid(c, size):
    cnt = 0
    size_mul = 500//size
    size_mul2 = round(500 / (500 / size))
    for x in range(int(size_mul2)):
        for y in range(int(size_mul2)):
            if cnt % 2 == 1:
                c.create_rectangle(x * size_mul, y * size_mul, x * size_mul + size_mul, y * size_mul + size_mul, fill="#574733")
            else:
                c.create_rectangle(x * size_mul, y * size_mul, x * size_mul + size_mul, y * size_mul + size_mul, fill="#f5ddbf")
            cnt += 1
        if size % 2 == 0:
            cnt += 1


def start_solving():
    threading.Thread(target=solve).start()


def solve():
    global count
    moves.put(start)
    visited_moves[tuple(start)] = count

    while not moves.empty():
        node = moves.get()
        neighbor = get_possible_moves(grid, node)
        neighbor_deg = [len(get_possible_moves(grid, x)) for x in neighbor]
        print(neighbor)
        for x in range(len(neighbor)):
            print(min(neighbor_deg))
            ind = neighbor_deg.index(min(neighbor_deg))
            neighbor_deg.pop(ind)
            min_neighbor = neighbor.pop(ind)
            if tuple(min_neighbor) not in visited_moves.keys():
                time.sleep(0.025)
                count += 1
                moves.put(min_neighbor)
                print(min_neighbor)
                visited_moves[tuple(min_neighbor)] = count
                c.delete(knight_pos.pop())
                knight_pos.append(c.create_image([y * size_mul for y in min_neighbor], image=knight, anchor="nw"))
                c.create_line([y * size_mul + (size_mul // 2) for y in node], [y * size_mul + (size_mul // 2) for y in min_neighbor], width=3, fill="red")
                print(visited_moves)
                break


def knights_tour(start, size):
    m = n = size


#def knights_tour_gui(start, size):
root = Tk()

count = 0
size = 250
start = [random.randint(0, size - 1), random.randint(0, size - 1)]
size_mul = 500 // size
grid = [[0 for x in range(size)] for y in range(size)]
knight_pos = []

visited_moves = {}
moves = queue.Queue()

bg = Frame(root, width=1280, height=720, bg="#415446")
bg.pack()
c = Canvas(bg, width=500, height=500, bd=0, highlightthickness=0, relief='ridge', bg="#415446")
c.place(relx=0.1, rely=0.15)
draw_grid(c, size)
knight = PhotoImage(file="knight.png").subsample(500//size_mul, 500//size_mul)
knight_pos.append(c.create_image([y*size_mul for y in start], image=knight, anchor="nw"))
print(get_possible_moves(grid, [start[0], start[1]]))

next_step_btn = Button(bg, width=200, height=100, text="Next Move", command=start_solving)
next_step_btn.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.1)
# solve time



root.mainloop()


#knights_tour_gui([0, 0], 1)
