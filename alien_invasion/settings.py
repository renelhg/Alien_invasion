class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's static settings"""
		# screen settings
		self.screen_width = 1260
		self.screen_height = 740
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 3

		# Bullet Settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 26, 26)
		self.bullets_allowed = 3

		# Alien settings
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.1
		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""
		self.ship_speed_factor = 6.5 
		self.bullet_speed_factor = 30

		self.alien_speed_factor = 2

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point values"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)


