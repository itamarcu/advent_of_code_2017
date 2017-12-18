from Lib import queue


def day_18():
    with open("input.txt") as file:
        lines = file.readlines()
    
    N = len(lines)
    
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def part_1():
        registers = [0 for _ in range(16)]
        last_sound = None
        curr = 0
        while 0 <= curr < N:
            cmd, *args = lines[curr].strip().split(" ")
            a1 = ord(args[0]) - ord('a')
            a2 = int(args[-1]) if is_int(args[-1]) else registers[
                ord(args[-1]) - ord('a')]
            if cmd == "snd":
                last_sound = registers[a1]
            elif cmd == "set":
                registers[a1] = a2
            elif cmd == "add":
                registers[a1] += a2
            elif cmd == "mul":
                registers[a1] *= a2
            elif cmd == "mod":
                registers[a1] %= a2
            elif cmd == "rcv":
                if registers[a1] != 0:
                    break
            elif cmd == "jgz":
                if registers[a1] > 0:
                    curr += a2 - 1
            else:
                print("Error!" + cmd)
            curr += 1
            
        print("Part 1:", last_sound)  # 4601
    
    def part_2():
        class Program():
            def __init__(self):
                self.registers = [0 for _ in range(16)]
                self.curr = 0
                self.terminated = False
                self.waiting = False
                self.send_queue = None  # should be set by me later
                self.receive_queue = queue.Queue()
                self.times_sent = 0
            
            def step(self):
                while not self.terminated:
                    if self.waiting:
                        if self.receive_queue.empty():
                            self.terminated = True
                            return
                        else:
                            self.waiting = False
                    cmd, *args = lines[self.curr].strip().split(" ")
                    a1 = ord(args[0]) - ord('a')
                    a2 = int(args[-1]) if is_int(args[-1]) else self.registers[
                        ord(args[-1]) - ord('a')]
                    if cmd == "snd":
                        self.send_queue.put(self.registers[a1])
                        self.times_sent += 1
                    elif cmd == "set":
                        self.registers[a1] = a2
                    elif cmd == "add":
                        self.registers[a1] += a2
                    elif cmd == "mul":
                        self.registers[a1] *= a2
                    elif cmd == "mod":
                        self.registers[a1] %= a2
                    elif cmd == "rcv":
                        if self.receive_queue.empty():
                            self.waiting = True
                            return
                        else:
                            self.registers[a1] = self.receive_queue.get()
                    elif cmd == "jgz":
                        if a1 < 0 or a1 >= N:
                            if is_int(args[0]) and int(
                                    args[0]) > 0:  # Fucking jgz 1 3
                                self.curr += a2 - 1
                        elif self.registers[a1] > 0:
                            self.curr += a2 - 1
                    else:
                        print("Error!", cmd)
                    self.curr += 1
                    if not (0 <= self.curr < N):
                        self.terminated = True
        
        prog0 = Program()
        prog1 = Program()
        prog0.registers[15] = 0
        prog1.registers[15] = 1
        prog0.send_queue = prog1.receive_queue
        prog1.send_queue = prog0.receive_queue
        
        while True:
            prog0.step()
            prog1.step()
            if prog0.terminated and prog1.terminated:
                print("Part 2:", prog1.times_sent)  # 6858
                return
    
    part_1()
    part_2()


day_18()
