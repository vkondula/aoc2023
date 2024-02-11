from queue import Queue
import math


class Module:
    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self.destinations = destinations

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def handle(self, pulse: bool, from_: str):
        pass

    def register_input(self, from_: str):
        pass


class Broadcaster(Module):
    def handle(self, pulse: bool, from_: str):
        return pulse


class FlipFlop(Module):
    def __init__(self, name: str, destinations: list[str]):
        super().__init__(name, destinations)
        self.state = False

    def handle(self, pulse: bool, from_: str):
        if not pulse:
            self.state = not self.state
            return self.state
        return None


class Conjunction(Module):
    def __init__(self, name: str, destinations: list[str]):
        super().__init__(name, destinations)
        self.state = {}

    def handle(self, pulse: bool, from_: str):
        self.state[from_] = pulse
        return not all(self.state.values())

    def register_input(self, from_: str):
        self.state[from_] = False


def solve(data_in: str):
    modules = {}
    for row in data_in.splitlines():
        from_raw, to_raw = row.split(" -> ")
        destinations = to_raw.split(", ")
        if from_raw == "broadcaster":
            modules[from_raw] = Broadcaster(from_raw, destinations)
        if from_raw[0] == "%":
            modules[from_raw[1:]] = FlipFlop(from_raw[1:], destinations)
        if from_raw[0] == "&":
            modules[from_raw[1:]] = Conjunction(from_raw[1:], destinations)
    for module in modules.values():
        for destination in module.destinations:
            if destination in modules:
                modules[destination].register_input(module.name)
    lows, highs = 0, 0
    i = 0
    firsts = {}
    while True:
        i += 1
        broadcast = modules["broadcaster"]
        queue = Queue()
        queue.put((broadcast, False, "_"))
        lows += 1
        while not queue.empty():
            module, pulse, from_ = queue.get()
            pulse = module.handle(pulse, from_)
            if pulse is None:
                continue
            for destination in module.destinations:
                if pulse:
                    highs += 1
                else:
                    lows += 1
                if destination in modules:
                    queue.put((modules[destination], pulse, module.name))
                if destination == "rx":
                    for name, value in modules['cn'].state.items():
                        if value:
                            if name not in firsts:
                                firsts[name] = i
                    if len(firsts) == len(modules['cn'].state):
                        total = math.lcm(*firsts.values())
                        print(total)
                        return total
