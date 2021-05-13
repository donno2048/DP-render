from numpy import zeros, ones, sin, cos, uint8, pi
from sys import argv
from tqdm import tqdm
from png import Writer
try: from PIL.Image import open as iopen
except ImportError: from Image import open as iopen
class DoublePendulum():
    def __init__(self, thetas): self.t, self.td, self.l, self.m = thetas, zeros(thetas.shape), ones(thetas.shape), ones(thetas.shape)
    def step(self):
        self.td[:, 0] += (-10 * (2 * self.m[:, 0] + self.m[:, 1]) * sin(self.t[:, 0]) - self.m[:, 1] * 10 * sin(self.t[:, 0] - 2 * self.t[:, 1]) - 2 * sin(self.t[:, 0] - self.t[:, 1]) * self.m[:, 1] * (self.td[:, 1] ** 2 * self.l[:, 1] + self.td[:, 0] ** 2 * self.l[:, 0] * cos(self.t[:, 0] - self.t[:, 1]))) / (2000 * self.l[:, 0] * (2 * self.m[:, 0] + self.m[:, 1] * (1 - cos(2 * (self.t[:, 0] - self.t[:, 1])))))
        self.td[:, 1] += (2 * sin(self.t[:, 0] - self.t[:, 1]) * (self.td[:, 0] ** 2 * self.l[:, 0] * (self.m[:, 0] + self.m[:, 1]) + 10 * (self.m[:, 0] + self.m[:, 1]) * cos(self.t[:, 0]) + self.td[:, 1] ** 2 * self.l[:, 1] * self.m[:, 1] * cos(self.t[:, 0] - self.t[:, 1]))) / (2000 * self.l[:, 1] * (2 * self.m[:, 0] + self.m[:, 1] * (1 - cos(2 * (self.t[:, 0] - self.t[:, 1])))))
        self.t += self.td / 2000
color = lambda x, y: (127 * cos(x / 4 - y / 4), 127 * (cos(x / 4 - y / 4) - sin(x / 4 + y / 4)), 127 * (sin(x / 4 - y / 4) + cos(x / 4 + y / 4)))
thetas = ones((893025, 2))
for i in range(893025): thetas[i, 0], thetas[i, 1] = pi * (2 * (i % 945) / 945 - 1), pi * (2 * (i // 945) / 945 - 1)
p, frames, FRAMES = DoublePendulum(thetas), [], int(argv[1])
for frame in tqdm(range(FRAMES)):
    fractal, file, writer = uint8([[a for i in range(945) for a in color(p.t[j * 945 + i, 0], p.t[j * 945 + i, 1])] for j in range(945)]), open(f'frames/frame{frame}.png', 'wb+'), Writer(945, 945, greyscale = False)
    writer.write(file, fractal)
    frames += [iopen(file)]
    for _ in range(33): p.step()
frames[0].save('output.gif', format = 'GIF', append_images = frames[1:], save_all = True, duration = FRAMES / 60)