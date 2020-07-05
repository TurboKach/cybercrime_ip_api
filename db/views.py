import os


def read_iplists_to_db():
    pass


def update_ipsets():
    os.system('update-ipsets --enable-all')
    #  TODO проверить, что айписета обновились на диске, потом обновить их в БД
