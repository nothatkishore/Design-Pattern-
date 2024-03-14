from abc import ABC, abstractmethod


class TrafficLightState(ABC):

    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def __str__(self):
        pass


class RedState(TrafficLightState):

    def change(self, traffic_light):
        print("Changing from RED --> GREEN")
        traffic_light.set_state(GreenState())

    def __str__(self):
        return "RED State"


class GreenState(TrafficLightState):

    def change(self, traffic_light):
        print("Changing from GREEN --> YELLOW")
        traffic_light.set_state(YellowState())

    def __str__(self):
        return "GREEN State"


class YellowState(TrafficLightState):

    def change(self, traffic_light):
        print("Changing from YELLOW --> RED")
        traffic_light.set_state(RedState())

    def __str__(self):
        return "YELLOW State"


class TrafficLight:
    def __init__(self):
        self._state = RedState()

    @property
    def state(self):
        return str(self._state)

    def set_state(self, state):
        self._state = state

    def change(self):
        self._state.change(self)

    def __str__(self):
        return f"Current state: {self.state}"


if __name__ == "__main__":

    T1 = TrafficLight()
    print(T1)

    T1.change()
    print(T1)

    T1.change()
    print(T1)

    T1.change()
    print(T1)
