"""Unit tests for python_hiring_test.run.py module."""

import os
import datetime
import hashlib
import binascii
import python_hiring_test
import python_hiring_test.run


def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.digest()


def md5sum(path):
    return binascii.hexlify(hashfile(open(path, 'rb'), hashlib.md5()))


def test_pitchdata_file_checksum():
    """Verify that the pitchdata file is complete and not corrupt."""
    path = os.path.join(python_hiring_test.RAW, 'pitchdata.csv')
    assert md5sum(path) == b'491002353654ad834b21a3bd77915b4a'


def test_output_file_checksum():
    """Verify that the output file's checksum matches the reference file's."""
    path = os.path.join(python_hiring_test.PROCESSED, 'output.csv')
    assert md5sum(path) == b'4a8d57410dd6503fe02424597248c1b6'


def test_output_time():
    """Verify that the script completes within 5 seconds."""
    start_time = datetime.datetime.now()
    python_hiring_test.run.main()
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    assert elapsed_time.seconds <= 5
