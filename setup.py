from setuptools import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="tgdsmells",
    packages=["tgdsmells"],
    version="1.0.0b",
    license="MIT",
    description="Helper classes for the Team Group Data Sharing Medium & Electronic Local Link System.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Viliam Vadocz",
    author_email="viliam.vadocz@gmail.com",
    url="https://github.com/L0laapk3/tgdsmells/",
    download_url="https://github.com/L0laapk3/tgdsmells/releases/download/v_1_0_0b/tgdsmells-1.0.0b0.tar.gz",
    keywords=["RLBot", "protocol"],
    install_requires=["rlbot"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
