# Basic logging template that works in both Python 2 and 3.
# TODO: I don't know if this is the best way to do it - is basicConfig
# better?

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
if sys.version_info[0] >= 3:
    logging.lastResort.setLevel(logging.INFO)
else:
    # lastResort isn't set up in python2.
    ch = logging.lastResort = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    LOG.addHandler(ch)


# if __name__ == __main__:
    if args.verbose:
        logging.lastResort.setLevel(logging.DEBUG)
