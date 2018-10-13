seconds_per_earth_year = 31557600


class SpaceAge(object):
    def __init__(self, seconds: int):
        self.seconds = seconds

    def on_mercury(self) -> float:
        return self._convert(0.2408467)

    def on_venus(self) -> float:
        return self._convert(0.61519726)

    def on_earth(self) -> float:
        return self._convert(1)

    def on_mars(self) -> float:
        return self._convert(1.8808158)

    def on_jupiter(self) -> float:
        return self._convert(11.862615)

    def on_saturn(self) -> float:
        return self._convert(29.447498)

    def on_uranus(self) -> float:
        return self._convert(84.016846)

    def on_neptune(self) -> float:
        return self._convert(164.79132)

    def _convert(self, period: float) -> float:
        return round(self.seconds/seconds_per_earth_year/period, 2)
