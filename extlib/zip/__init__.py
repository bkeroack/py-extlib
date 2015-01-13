__author__ = 'bk'

import zipfile
import os
import logging

#create zip of a folder, prepending subpath to all archive paths if supplied
def zipfolder(path, zipname, subpath=""):
    assert os.path.isdir(path)
    empty_dirs = list()
    if os.path.exists(zipname):  # delete if exists
        logging.warning("zipfolder: warning: zipfile exists, deleting")
        os.remove(zipname)
    root_len = len(os.path.abspath(path))
    zf = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirs, files in os.walk(path):
        archive_root = os.path.abspath(dirpath)[root_len+1:]
        empty_dirs.extend([dir for dir in dirs if os.listdir(os.path.join(dirpath, dir)) == []])
        for d in empty_dirs:
            zif = zipfile.ZipInfo(os.path.join(subpath, archive_root, d) + "/")
            zf.writestr(zif, "")
        for f in files:
            archive_name = os.path.join(subpath, archive_root, f)
            zf.write(os.path.join(dirpath, f), archive_name)
        empty_dirs = list()
    zf.close()