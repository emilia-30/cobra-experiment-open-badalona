import csv
import platform


class Results_csv:
    def __init__(self, file_name):
        results_folder = 'results\\' if platform.system() == 'Windows' else 'results'

        self.file = open(
            results_folder + file_name + '.csv', mode='w')
        self.writer = csv.writer(self.file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header_row = ['trial_index', 'stim', 'speaker_is_participant']
        self.writer.writerow(header_row)

    def __del__(self):
        self.file.close()

    def add_entry(self, trial_results, trial_index):
        entry_as_row = [trial_index, trial_results["stim"], trial_results['speaker']]
        print(entry_as_row)
        self.writer.writerow(entry_as_row)
