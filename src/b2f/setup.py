from setuptools import find_packages, setup

package_name = 'b2f'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='edward',
    maintainer_email='edward.sun2015@gmail.com',
    description='Converts and saves rosbag frames to local directory',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'b2f = b2f.subscriber_func:main',
        ],
    },
)
