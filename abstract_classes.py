from abc import ABCMeta, abstractmethod, abstractproperty, ABC

class I_input_getTime():
	__metaclass__=ABCMeta
	@abstractmethod
	def geted():
		pass


class I_Button():
	__metaclass__=ABCMeta
	@abstractmethod
	def LetsGetStart():
		pass
	@abstractmethod
	def LetsGetPause():
		pass
	@abstractmethod
	def LetsGetStop():
		pass