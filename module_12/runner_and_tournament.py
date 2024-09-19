class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

    def true_start(self):
        finishers = {}
        data_participant = []
        place = 1
        counter = 0

        while self.participants:
            counter += 1
            copy_list = list(self.participants)
            list_iter = [counter]
            for participant in copy_list:
                participant.run()
                dist_ranner = participant.distance
                if dist_ranner >= self.full_distance:
                    tuple_ = (dist_ranner, [participant])
                    list_iter.append(tuple_)
                    self.participants.remove(participant)
            if len(list_iter) > 1:
                data_participant.append(list_iter)

        while data_participant:
            list_iter = data_participant[0]
            list_iter.remove(list_iter[0])
            length_iter = len(list_iter)
            if length_iter == 1:
                finishers[place] = list_iter[0][1]
                place += 1
            else:
                list_iter.sort(key=lambda x: x[0], reverse=True)
                tuple_dist = ()
                for i in range(length_iter):
                    dist = list_iter[i][0]
                    #  list_participant_in_iter = list_iter[1]
                    if dist not in tuple_dist:  # НЕ пришли вместе с кем то в этой итерации.
                        finishers[place] = list_iter[i][1]
                        tuple_dist = (dist, place)
                        place += 1
                    else:
                        finishers[tuple_dist[1]].append(list_iter[i][1][0])

            data_participant.remove(data_participant[0])

        return finishers
