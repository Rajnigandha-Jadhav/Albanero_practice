# logging is used to track events that occur in software when it runs.
# it is used in development,debugging,testing etc.
# useful to track error and exception.
# if there is no logging it may long time to find the root cause.

# problems software can face:
# Exception present in program, network/connection issues,access denied,server down, file not found.

# some functions in logging module 
# notset  0
# debug() #10 level
# info() 20
# warning() 30
# error() 40
# critical() 50

# Debug = 10: This level gives detailed information, useful only when a problem is being diagnosed.
# Info = 20: This is used to confirm that everything is working as it should.
# Warning = 30: This level indicates that something unexpected has happened or some problem is about to happen in the near future.
# Error = 40: As it implies, an error has occurred. The software was unable to perform some function.
# Critical = 50: A serious error has occurred. The program itself may shut down or not be able to continue running properly.

# import logging

# logging.basicConfig(filename="app.log",
#         level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s"
#     )
# # logging.basicConfig(level=logging.DEBUG)
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


import logging

logging.basicConfig(filename='example.log', level=logging.INFO)
logging.debug('debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')



# Logging is an important aspect of software development as it allows developers to record and track various events that occur during the execution of their code. These events can be used to monitor performance, troubleshoot issues, and analyze user behavior. Logging levels are used to categorize these events according to their level of importance or severity. There are several different logging levels, each with its own specific purpose.

# DEBUG: This is the lowest level of logging and is used to record detailed information about the execution of the code. Debug messages are typically used by developers during development and testing to diagnose issues. They are generally not useful in production environments, as they can generate a large amount of log data that may be difficult to analyze.

# INFO: This level of logging is used to record general information about the execution of the code. Info messages are useful for tracking the progress of the application and can be used to provide status updates to users. They are also useful for troubleshooting issues, as they can provide context about the state of the application.

# WARNING: This level of logging is used to record events that may indicate a problem, but are not critical. Warning messages are typically used to alert developers or system administrators about potential issues before they become critical. They can also be used to provide users with warnings about potential problems.

# ERROR: This level of logging is used to record events that indicate an error has occurred. Error messages are typically used to alert developers or system administrators about critical issues that require immediate attention. They can also be used to provide users with error messages that explain why an operation has failed.

# CRITICAL: This is the highest level of logging and is used to record events that indicate a critical failure has occurred. Critical messages are typically used to alert developers or system administrators about issues that require immediate attention and may result in data loss or system failure.

# In general, developers should use the appropriate logging level based on the severity of the event being recorded. Debug messages should only be used during development and testing, while info messages can be used to provide status updates and context about the application. Warning messages should be used to indicate potential issues, while error and critical messages should be used to indicate critical failures. It is important to use logging levels consistently throughout the application to ensure that the logs are useful and easy to analyze.