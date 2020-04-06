# https://packaging.python.org/guides/distributing-packages-using-setuptools/
# 'wheel' may be a build-dependency, it's also dep of twine

from os.path import join
import setuputils

with open("README.rst", "r") as fh:
    long_description = fh.read()

requirementstxt = join(dirname(__file__), "requirements.txt")
requirements = [ line.strip() for line in open(requirementstxt, "r") if line.strip() ]

setuputils.setup(name='xxx',
      version='0.1.0',
      description='xxx',
      long_description=long_description,
      long_description_content_type="text/x-rst",  # ReST is the default
      url="https://github.com/xxx/xxx",
      author='xxx',
      #author_email='',
      packages=['xxx'],           # packages
      #py_modules=["nbscript"],   # single modules
      keywords='xxx xxx',
      python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*,",
      install_requires=requirements,
      entry_points={
          'console_scripts': [
                'CMDNAME=modulename:main',
        ],
    },
      # https://pypi.org/classifiers/
      classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx"
        "Framework :: Sphinx :: Extension",
        "Operating System :: OS Independent",
    ],
  )

# python setup.py sdist bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*
