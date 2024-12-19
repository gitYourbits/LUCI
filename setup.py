from setuptools import setup, find_packages

setup(
    name="luci-cli",
    version="1.0.0",
    description="LUCI Command-Line Interface Tool",
    author="Aditya",
    author_email="aditya.mail.personal@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "django",
    ],
    entry_points={
        "console_scripts": [
            "luci=luci_downloadable.cli:main",  # Parent command
        ],
    },
)
