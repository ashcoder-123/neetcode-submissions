class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = []
        for i in range(len(speed)):
            distance = target - position[i]
            speed_of_car = speed[i]
            time = distance/speed_of_car
            arrival_times.append([position[i],time])
        arrival_times.sort(key = lambda car: car[0], reverse = True)
        last_fleet_time = None
        fleet_count = 0
        for pos,time in arrival_times:
            if last_fleet_time is None:
                last_fleet_time = time
                fleet_count += 1
                continue
            if time <= last_fleet_time:
                continue
            else:
                fleet_count += 1
                last_fleet_time = time
        return fleet_count