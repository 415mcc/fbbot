import logging


def disable_requests_logging():
    logging.getLogger('urllib3').propagate = False


class FBHandler(logging.Handler):
    def __init__(self, session, dest_id, *args, **kwargs):
        if not session._logged_in:
            raise Exception('session must be logged in')
        super().__init__(*args, **kwargs)
        self.session = session
        self.dest_id = dest_id
        self.addFilter(self)  # filter out requests lib logging

    def emit(self, record):
        try:
            msg = self.format(record)
            self.session.message(self.dest_id, msg)
        except Exception:
            self.handleError(record)

    def filter(self, record):
        # filter out LogRecords created by requests library
        bad = (
            'urllib3',
            'urllib3.connectionpool',
        )
        return 0 if record.name in bad else 1
