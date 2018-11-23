from setuptools import setup

setup(
    name='simple_robot_state_subscriber',
    version='0.0.0',
    packages=[],
    py_modules=[],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Alona Kharchenko',
    author_email='unicorn@roboy.org',
    maintainer='Alona Kharchenko',
    maintainer_email='unicorn@roboy.org',
    keywords=['CARDSFlow'],
    description='Package containing examples receive CARDSflow data using the rclpy API.',
    license='BSD-3',
    entry_points={
        'console_scripts': [
            'subscriber = subscriber:main'
        ],
    },
)
