from setuptools import setup

setup(name='just_tweet_and_code',
      version='0.1',
      description='A simple cli-twitter client',
      url='http://github.com/chin8628/just-tweet-and-code',
      author='Boonyarith Piriyothinkul',
      author_email='boonyarith.pir@gmail.com',
      license='MIT',
      packages=['src'],
      entry_points={
          'console_scripts': ['tw=src.main:cli'],
      },
      install_requires=[
          'python-twitter==3.5',
          'fire==0.1.3'
      ],
      zip_safe=False)
