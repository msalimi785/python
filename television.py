class Television:
    def __init__(self):
        self.power_status = False
        self.channel = 0
        self.volume = 0
        self.is_muted = False

    def power(self):
        self.power_status = not self.power_status

    def channel_up(self):
        if self.power_status:
            self.channel = (self.channel + 1) % 10

    def channel_down(self):
        if self.power_status:
            self.channel = (self.channel - 1) % 10

    def volume_up(self):
        if self.power_status and not self.is_muted:
            if self.volume < 5:
                self.volume += 1

    def volume_down(self):
        if self.power_status and not self.is_muted:
            if self.volume > 0:
                self.volume -= 1

    def mute(self):
        if self.power_status:
            self.is_muted = not self.is_muted
            if self.is_muted:
                self.volume = 0

    def __str__(self):
        return f"Power = {self.power_status}, Channel = {self.channel}, Volume = {self.volume}"

