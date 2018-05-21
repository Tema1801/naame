import sys
import pygame

pygame.init()

r = 20
m = 1
R = 30


width = 1056
height = 548

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

score = [['a', 0], ['b', 0]]

def switch(q):
    if q == 0:
        return 1
    else:
        return 0

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:>3},{:>3})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, a):
        if isinstance(a, Vector):
            return self.x * a.x + self.y * a.y
        else:
            return Vector(self.x * a, self.y * a)

    def __rmul__(self, a):
        if isinstance(a, Vector):
            return self.x * a.x + self.y * a.y
        else:
            return Vector(self.x * a, self.y * a)

    def __neg__(self):
        return Vector(self.x * -1, self.y * -1)

    def div(self, a):
        if not isinstance(a, Vector):
            return Vector(self.x / a, self.y / a)

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def proection(self, other):
        return self * other / lenn(other)


def cos(self, other):
    return (self.x * other.x + self.y * other.y) / (lenn(self) * lenn(other))


def lenn(self):
    return float(self.x ** 2 + self.y ** 2) ** 0.5


def aff(self, base, need):
    base1 = Vector(-base.y, base.x)
    need1 = Vector(-need.y, need.x)
    x = self.x * base.x - self.y * base1.y
    y = self.x * base.y + self.y * base1.y
    return Vector(x / lenn(base), y / lenn(base))


class Ball():
    def __init__(self, c, v, r, colour):
        self.c = c
        self.v = v
        self.r = r
        self.colour = colour

    def __str__(self):
        return 'c = {} , v = {}'.format(self.c, self.v)

    def fut(self, dt=0.001):
        return self.c + self.v * dt


def collision(self, other):
    n1 = other.c + other.v * dt - self.c - self.v * dt
    n2 = Vector(n1.y, -n1.x)
    v1 = Vector(self.v.proection(n1), self.v.proection(n2))
    v2 = Vector(other.v.proection(n1), other.v.proection(n2))
    s = v1.x
    v1.x = v2.x
    v2.x = s
    c = Vector(1, 0) * n1 / lenn(n1)
    s = Vector(-1, 0) * n2 / lenn(n1)
    v1 = Vector((v1.x * c) - (v1.y * s), -(v1.x * s) - (v1.y * c))
    v2 = Vector((v2.x * c) - (v2.y * s), -(v2.x * s) - (v2.y * c))
    a = [v1, v2]
    return a


def collisionn(self, other1, other2):
    n1 = other1.c + other1.v * dt - self.c - self.v * dt
    n2 = other2.c + other2.v * dt - self.c - self.v * dt


class Line:
    def __init__(self, c1, c2, n=0):
        self.s = Vector(c1[0], c1[1])
        self.e = Vector(c2[0], c2[1])
        self.c = self.e - self.s
        self.n = Vector(self.e.y - self.s.y, self.s.x - self.e.x)

    def __str__(self):
        return str(self.s) + ' ->' + str(self.e)


def line_chk(d, line):
    mx = min(line.e.x, line.s.x)
    Mx = max(line.e.x, line.s.x)
    my = min(line.e.y, line.s.y)
    My = max(line.e.y, line.s.y)
    if int(d.x) in range(mx, Mx) or int(d.y) in range(my, My):
        return True
    else:
        return False


def line_coll(balls, lines, dt=0.001):

    c = (ball.fut(dt) - line.s) * line.n / lenn(line.n)
    d = ball.fut(dt) - c / lenn(line.n) * line.n
    print(line.chk(d,line))
    if abs((ball.fut(dt) - line.s) * line.n / lenn(line.n)) <= ball.r and line_chk(d, line):
        ball.v = -2 * ball.v.proection(line.n) / lenn(line.n) * line.n + ball.v

    return ball


point1 = Vector(width // 4, height // 2)

point3 = Vector(width * 3 / 4, height // 2)

d = 10

walls = [
    [(R * 2, R), (3 * R + d, 2 * R), (width // 2 - 4 * R // 3, 2 * R), (width // 2 - R, R)],
    [(width // 2 + R, R), (width // 2 + 4 * R // 3, 2 * R), (width - 3 * R - d, 2 * R), (width - 2 * R, R)],
    [(width - R - 1, 2 * R), (width - 2 * R, 3 * R + 10), (width - 2 * R, height - 3 * R - d),
     (width - R - 1, height - 2 * R)],
    [(width // 2 + R, height - R), (width // 2 + 4 * R // 3, height - 2 * R), (width - 3 * R - d, height - 2 * R),
     (width - 2 * R, height - R)],
    [(R * 2, height - R), (3 * R + d, height - 2 * R), (width // 2 - 4 * R // 3, height - 2 * R),
     (width // 2 - R, height - R)],
    [(R, 2 * R), (2 * R, 3 * R + d), (2 * R, height - 3 * R - d), (R, height - 2 * R)]
]

borders = [(R, R), (R * 2, R), (width - R, R), (width - R, height - R), (R, height - R), (R - 1, R - 1), (0, R - 1), (0, height),
           (width, height), (width, 0), (0, 0), (0, R)]

for i in range(len(walls)):
    pygame.draw.polygon(screen, (0, 0, 0), walls[i], 1)


def table():
    screen.fill((51, 102, 0))
    for i in range(len(walls)):
        pygame.draw.polygon(screen, (0, 0, 0), walls[i], 1)
    pygame.draw.polygon(screen, (150, 75, 0), borders)
    pygame.draw.circle(screen, (0, 0, 0), (R, R), R)
    pygame.draw.circle(screen, (0, 0, 0), (R, height - R), R)
    pygame.draw.circle(screen, (0, 0, 0), (width - R, height - R), R)
    pygame.draw.circle(screen, (0, 0, 0), (width - R, R), R)
    pygame.draw.circle(screen, (0, 0, 0), (width // 2, R), R)
    pygame.draw.circle(screen, (0, 0, 0), (width // 2, height - R), R)

def strike():
    if pygame.mouse.get_pressed()[0]:
        d = pygame.mouse.get_pos()
        ball[0].v = Vector(d[0] - ball[0].c.x, d[1] - ball[0].c.y)


holes = [[R, R], [width // 2, R], [width - R, R], [width - R, height - R], [width // 2, height - R], [R, height - R]]


def collisions(ball, i=0):
    c = []
    for j in range(len(ball)):
        n = ball[j].c + ball[j].v * dt - ball[i].c - ball[i].v * dt
        if 2 * r > lenn(n) and i != j:
            c.append(j)
    if len(c) == 1 and c[0] != i:
        a = collision(ball[i], ball[c[0]])
        ball[i].v = a[0]
        ball[c[0]].v = a[1]
    elif len(c) > 1:
        for k in c:
            if k != i:
                a = collision(ball[i], ball[k])
                ball[i].v = a[0]
                ball[k].v = a[1]


ball = [


    Ball(Vector(point1.x, point3.y), Vector(0, 0), r, 0),

    Ball(Vector(point3.x, point3.y), Vector(0, 0), r, 3),
    Ball(Vector(point3.x + 36, point3.y + 20), Vector(0, 0), r, 3),
    Ball(Vector(point3.x + 36, point3.y - 20), Vector(0, 0), r, 3),
    Ball(Vector(point3.x + 36 * 2, point3.y + 20 * 2), Vector(0, 0), r, 3),
    Ball(Vector(point3.x + 36 * 2, point3.y), Vector(0, 0), r, 3),
    Ball(Vector(point3.x + 36 * 2, point3.y - 20 * 2), Vector(0, 0), r, 3)

]

N = len(ball)

collision_chk = [[0 for i in range(len(ball))] for j in range(len(ball))]
dt = 0.001

clr = [[255, 255, 255], [255, 0, 0], [0, 0, 255], [255, 255, 0], [0, 0, 0], [255, 128, 0], [0, 255, 0], [90, 0, 157]]

a = 100


coll = 0

q = 0

def pow():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            power = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONUP:
            power = pygame.time.get_ticks() - power
    return power

def mode_game():
    game = True
    q = 0
    strk = 'finished'
    while game:
        dt = 0.001
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            elif pygame.key.get_pressed()[pygame.K_p]:
                draw(q)
                p = pygame.font.SysFont('Comic Sans MS', 30)
                text_p = p.render('PAUSE', False, (255, 255, 255))
                screen.blit(text_p, (width // 2 - 60, height // 2 - 30))
                pygame.display.flip()
                waiting()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                power = pygame.time.get_ticks()
                strk = 'started'
                draw(q)
                pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONUP:

                if movement and strk == 'started':
                    power = pygame.time.get_ticks() - power
                    ball[0].v = Vector(pygame.mouse.get_pos()[0] - ball[0].c.x,
                                       pygame.mouse.get_pos()[1] - ball[0].c.y) * (power/100)
                    strk = 'done'
                    print(strk)


        movement = True

        for i in range(len(ball)):

            l_all = []
            collisions(ball, i)
            for j in range(6):
                for k in range(3):
                    line = Line(walls[j][k], walls[j][k + 1])
                    c = (ball[i].fut(dt) - line.s) * line.n / lenn(line.n)
                    d = ball[i].fut(dt) - c / lenn(line.n) * line.n
                    if abs(c) <= ball[i].r and line_chk(d, line):
                        l_all.append([j,k])

            if l_all != []:
                print(*l_all)
            if len(l_all) == 1:
                j = l_all[0][0]
                k = l_all[0][1]
                l = k + 1
                line = Line(walls[j][k], walls[j][l])
                ball[i].v = -2 * ball[i].v.proection(line.n) / lenn(line.n) * line.n + ball[i].v
            elif len(l_all) > 1:
                j = l_all[0][0]
                k = l_all[0][1]
                l = k + 2
                line = Line(walls[j][k], walls[j][l])
                print(walls[j][k], walls[j][l])
                ball[i].v = -2 * ball[i].v.proection(line.n) / lenn(line.n) * line.n + ball[i].v



            if lenn(ball[i].v) > 0:
                accel = -ball[i].v * (1 / lenn(ball[i].v)) * a
                ball[i].v += dt * accel

            ball[i].c += ball[i].v * dt

            if lenn(ball[i].fut() - ball[i].c) < 0.001:
                ball[i].v = Vector(0, 0)
            else:
                movement = False

        u = set()

        for i in range(len(ball)):
            for k in holes:
                if lenn(Vector(k[0], k[1]) - ball[i].c) <= R * 0.75:
                    u.add(i)

        for i in u:
            ball.pop(i)
            score[q][1] += 1

        if movement and strk == 'done':
            q = switch(q)
            draw(q)
            pygame.display.flip()
            strk = 'finished'


        draw(q)

        pygame.display.flip()



def waiting():
    d = True
    while d:
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_s]:
                d = False


def draw(q):
    table()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    score_1 = myfont.render(score[0][0] + ' ' + str(score[0][1]), False, (255,255,255))
    score_2 = myfont.render(score[1][0] + ' ' + str(score[1][1]), False, (255, 255, 255))
    turn_1 = myfont.render('0' + "'s turn", False, (255, 255, 255))
    turn_2 = myfont.render('1' + "'s turn", False, (255, 255, 255))
    for i in range(len(ball)):
        pygame.draw.circle(screen, clr[ball[i].colour], (round(ball[i].c.x), round(ball[i].c.y)), r)
    screen.blit(score_1, (3 * R, 0))
    screen.blit(score_2, (width//2+3*R, 0))

    if q == 0:
        screen.blit(turn_1, (width//4, height - 30))
    else:
        screen.blit(turn_2, (width // 4, height - 30))

pygame.font.init()
mode_game()