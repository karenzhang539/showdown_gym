from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="showdown_gym",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "colab": [
            "jupyter>=1.0.0",
            "ipywidgets>=8.0.0",
            "tqdm>=4.65.0",
            "requests>=2.25.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "wheel>=0.40.0",
            "build>=0.10.0",
        ],
    },
    url="https://github.com/UoA-CARES/showdown_gym",
    license="MIT",
    author="CARES",
    author_email="cares@aucklanduni.ac.nz",
    description="Pokemon Showdown Reinforcement Learning Environment",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
