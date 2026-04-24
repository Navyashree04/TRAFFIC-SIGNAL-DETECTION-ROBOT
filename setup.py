import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'traffic_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.sdf')),
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.sdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sharvani',
    maintainer_email='sharvani@todo.todo',
    description='Traffic Sign Detection Robot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sign_detector   = traffic_robot.sign_detector:main',
            'robot_controller = traffic_robot.robot_controller:main',
        ],
    },
)
