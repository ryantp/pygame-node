#PYTHON3.5.1 (Anaconda3, 64-BIT);

# DEVELOPMENT TOOL

import datetime
import os


class DEVTool(object):


	class PointManager(object):
		"""docstring for PointManager"""

		def __init__(self, write_to = None):
			self.write_to = write_to
			self.points = []
			self.MASTERSTRING = ''


		def get_time(self):
			return "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) # datestamp

		def check_for_and_create_file(self):
			if os.path.exists(self.write_to):
				pass
			else:
				with open(self.write_to, 'w') as f:
					pass
				f.close()

		def append_points(self, points = []):
			self.points.append(points)

		def lenp(self):
			return len(self.points)
			
		def format_mstring(self):
			for i in range(len(self.points)):
				self.MASTERSTRING += str(i) + ': ' + str(self.points[i - 1][0]) + ', ' + str(self.points[i -1][1]) + '\n'
			self.MASTERSTRING += '\n'

		def flush_mstring(self):
			self.MASTERSTRING = ''

		def write_to_file(self):
			self.check_for_and_create_file()
			self.format_mstring()
			header = '=' * 30 + ' ' + self.get_time() + '\n\n'
			footer = '\n=' * 40 + '\n\n'
			with open(self.write_to, 'a') as f:
				f.write(header)
				f.write(self.MASTERSTRING)
				f.write(footer)
				f.close()
			self.flush_mstring()


	class GeneratePlayerData(object):

		def __init__(self, blit_points = []):
			self.blit_points = blit_points

	def __init__(self):
		self.pm_object = None
		self.gpd_object = None

	def init_pm(self, file):
		self.pm_object = DEVTool.PointManager(write_to = file)

	def init_gpd(self, blit_points = []):
		self.gpd_object = DEVTool.GeneratePlayerData(blit_points = blit_points)
