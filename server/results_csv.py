import csv


class Results_csv:
    def __init__(self, file_name):
        self.file = open('results/' + file_name + '.csv', mode='w')
        self.writer = csv.writer(self.file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header_row = ['trial_index', 'prime_type', 'stim']
        self.writer.writerow(header_row)

    def __del__(self):
        self.file.close()

    def add_entry(self, stim, trial_index):
        entry_as_row = [trial_index, stim["prime"], stim["stim"]]
        print(entry_as_row)
        self.writer.writerow(entry_as_row)
