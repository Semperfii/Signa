from .web import create_app, logger

app = create_app()

if __name__ == '__main__':
    logger.info('Starting signa API ...')
    app.run(host='0.0.0.0', port=5000, threaded=True)
    logger.info('End of BPLeague')
