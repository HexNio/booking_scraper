import threading


class ThreadScraper(threading.Thread):

   process_result = []

   def __init__(self, session, offset, people, country, city, datein, dateout, parsing_data):
      threading.Thread.__init__(self)
      self.session = session
      self.offset  = offset
      self.people   = people
      self.country = country
      self.city = city
      self.datein = datein
      self.dateout = dateout
      self.parsing_data = parsing_data

   def run(self):
      self.process_result.append(self.parsing_data(self.session, self.people, self.country, self.city, self.datein, self.dateout, self.offset))