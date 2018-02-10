from web import create_app, logger

app = create_app()

if __name__ == '__main__':
    logger.info('Starting BPLeague API ...')
    app.run(host='0.0.0.0', port=5000)
    logger.info('End of BPLeague')
