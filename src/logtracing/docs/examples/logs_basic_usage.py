from logger import *

def main():
    log = Logger('Logs basic usage', {
        'slack_integration': True,
    })

    group = log.get_or_create_group('LOGS_BASIC_EXAMPLE')

    trace = log.trace('This is a trace log', { 'group': group })
    debug = log.debug('This is a debug log', { 'group': group })
    info = log.info('This is a info log')
    warn = log.warn('This is a warn log')
    error = log.error('This is a error log')
    fatal = log.fatal('This is a fatal log')

    # prints the id of the record stored in the database
    print(trace)
    print(debug)
    print(info)
    print(warn)
    print(error)
    print(fatal)

if __name__ == '__main__':
    main()
