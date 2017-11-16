LOG_DEFAULT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format':
                '%(asctime)s | %(levelname)5s | %(filename)15s:%(name)10s:%(lineno)4d | %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)s | %(levelname)5s | %(filename)15s:%(name)10s:%(lineno)4d | %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'yellow',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'colored',
            'class': 'logging.StreamHandler',
            # 'class': 'logutils.colorize.ColorizingStreamHandler'
        },

        'rotate_file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'rotated.log',
            'encoding': 'utf8',
            'maxBytes': 100000,
            'backupCount': 10,
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'rotate_file'],
            'level': 'DEBUG',
        },
    }
}
