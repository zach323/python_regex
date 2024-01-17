import re

class Event:
    
    def __init__(self, event_string):
        self.event_string = event_string
    

class EventReader:

    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_event_from_file(self):
        with open(self.file_path, 'r') as f:
            return f.read()






def search(event, event_reader, pattern):

    results = re.findall(pattern, event.event_string)
    return results

