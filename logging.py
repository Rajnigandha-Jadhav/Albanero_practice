# logging is used to track events that occur in software when it runs.
# it is used in development,debugging,testing etc.
# useful to track error and exception.
# if there is no logging it may long time to find the root cause.

# problems software can face:
# Exception present in program, network/connection issues,access denied,server down, file not found.

# some functions in logging module 
# debug() #10 level
# info() 20
# warning() 30
# error() 40
# critical() 50
# exception()

# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')



# import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# import logging

# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)


