from threading import Timer


class PzTimer:
	def __init__(self, secs, func):
		self._secs = secs
		self._func = func
		self._thread = None

	def start(self):
		self._thread = Timer(self._secs, self._event)
		self._thread.start()

	def _event(self):
		self._func()
		self.start()
