from datetime import datetime
from matplotlib.figure import Figure

class depth_graphing:

    def __init__(self) -> None:
        pass

    def cleanup(self, data):
        without_brackets = data.replace("[", "").replace("]", "").replace(" ", "")
        data_list = without_brackets.split(",")
        clean_data_list = data_list[1:]
        length = len(clean_data_list)
        final_data_list = [tuple(clean_data_list[i:i + 3]) for i in range(0, length, 3)]
        return final_data_list

    test_string = "[31, 00:00:00, 0, 60, 00:00:05, 15, 60, 00:00:10, 30, 60, 00:00:15, 45, 60, 00:00:20, 60, 60, 00:00:25, 75, 60, 00:00:30, 90, 60, 00:00:35, 105, 60, 00:00:40, 120, 60]"

    def parse_time(self, time_str):
        return datetime.strptime(time_str, "%H:%M:%S").time()

    def time_to_seconds(self, time_obj):
        """ Convert a datetime.time object to seconds since midnight. """
        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second


    def process(self, data_list):
        times = [self.parse_time(data[0]) for data in data_list]
        start_time = self.time_to_seconds(times[0])
        elapsed_times = [self.time_to_seconds(time) - start_time for time in times]
        depth = [float(data[1]) for data in data_list]

        return elapsed_times, depth


    def create_plot(self, x_values, y_values):

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(1, 1, 1)

        # Plot data
        ax.plot(x_values, y_values)

        # Set labels and title
        ax.set_title("Depth Vs Time Graph")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Depth (m)")

        return fig

    def listen(self):

        return None

    def run(self):
        data = self.listen()
        if data:
            return ("figure", "raw_data")
        else:
            return None
