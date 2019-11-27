"""Commit notion export to TIL

Usage:
    til.py <zip_filename>
    til.py (-h | --help)

"""
from docopt import docopt
from pathlib import Path
import zipfile
from glob import glob
import re
import subprocess
import os

DOWNLOAD_DIR = Path(os.environ['HOME'] + '/Downloads')
TIL_REPO = Path(os.environ['HOME'] + '/Codes/personal/TIL')


def main():
	args = docopt(__doc__)
	zip_filename = args["<zip_filename>"] + '.zip'
	path_to_zip_file = Path(DOWNLOAD_DIR, zip_filename)
	directory_to_extract_to = Path(DOWNLOAD_DIR, path_to_zip_file.stem)
	with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
		zip_ref.extractall(directory_to_extract_to)
	glob_result = list(directory_to_extract_to.glob('*.md'))
	assert len(glob_result) == 1
	markdown_to_edit = glob_result[0]
	subject_name = '-'.join(markdown_to_edit.stem.split('-'))
	new_name = subject_name + '.md'
	new_markdown = TIL_REPO.joinpath(new_name)
	with markdown_to_edit.open() as to_edit, new_markdown.open('w') as editted:
		for line in to_edit:
			match = re.match('\!\[\]\((.+?)\)', line)
			if match:
				image_name = match.group(1)
				image_path = directory_to_extract_to.joinpath(image_name)
				image_path.rename(TIL_REPO.joinpath('images', image_name))
				line = f"![](images/{image_name})"
			editted.write(line)

	os.chdir(TIL_REPO)
	subprocess.run(['git', 'pull'])
	subprocess.run(['git', 'add', '--all'])
	subprocess.run(['git', 'commit', '--message', subject_name])
	subprocess.run(['git', 'push'])

if __name__ == '__main__':
	main()
