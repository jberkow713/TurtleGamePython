import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TicTacAI", 
    version="0.0.1",
    author="Jesse Berkowitz",
    author_email="jberkow@brandeis.edu",
    description="Tic-Tac-Toe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jberkow713/TurtleGamePython/tree/main/TicTacGame",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

