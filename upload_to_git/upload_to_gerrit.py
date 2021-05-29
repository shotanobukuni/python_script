import os
import sys
import datetime
import shutil
import git

COMPONENT_MAP_FILE_NAME = "component_map.csv"
CATEGORY_MAP_FILE_NAME = "category_map.csv"
_GIT_URL = ""
_TARGET_BRANCH = ""


def upload_to_gerrit():
    # ファイル存在確認
    current_directory = os.getcwd()
    if not (os.path.exists(os.path.join(current_directory, CATEGORY_MAP_FILE_NAME))):
        print("{} is not exist !!".format(CATEGORY_MAP_FILE_NAME))
        sys.exit(1)
    if not (os.path.exists(os.path.join(current_directory, COMPONENT_MAP_FILE_NAME))):
        print("{} is not exist !!".format(COMPONENT_MAP_FILE_NAME))
        sys.exit(1)

    # Commit Message 決定
    d_today = datetime.date.today()
    commit_message = "Commit Component Map at {}".format(d_today)

    # clone ~ push
    clone_directory = os.path.join(current_directory, 'clone_dir')
    git.Repo.clone_from(
        _GIT_URL,
        clone_directory,
        branch=_TARGET_BRANCH
    )
    repo = git.Repo(clone_directory)
    shutil.copy(CATEGORY_MAP_FILE_NAME, clone_directory)
    shutil.copy(COMPONENT_MAP_FILE_NAME, clone_directory)
    repo.git.add(CATEGORY_MAP_FILE_NAME)
    repo.git.add(COMPONENT_MAP_FILE_NAME)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()
    shutil.rmtree(clone_directory)


if __name__ == '__main__':
    upload_to_gerrit()