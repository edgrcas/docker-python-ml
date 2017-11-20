from os import path, popen, makedirs
import shutil
import zipfile
import urllib.request as ur


class DownloadData:
    @staticmethod
    def unzip(source_filename, dest_dir):
        with zipfile.ZipFile(source_filename) as zf:
            zf.extractall(dest_dir)

    @classmethod
    def unzip_from_source(self, zip_name, dest_dir):
        urlretrieve = '{0}/{1}.zip'.format(self.BASE_URL, zip_name)
        print('unzip: ' + urlretrieve)
        zip, headers = ur.urlretrieve(urlretrieve)
        self.unzip(zip, dest_dir)
        return True

    @classmethod
    def download(self):
        home = path.expanduser("~")
        ntltk_path = path.join(home, 'nltk_data')

        print('remove data from: ' + ntltk_path)

        self.BASE_URL = 'https://s3-us-west-2.amazonaws.com/lemmes'
        print('Extract from: ', self.BASE_URL)
        self.unzip_from_source('taggers', ntltk_path)
        self.unzip_from_source('tokenizers', ntltk_path)
        self.unzip_from_source('corpora', ntltk_path)
        print('done!')
        return True


if __name__ == '__main__':
    DownloadData.download()
