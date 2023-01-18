import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()


setuptools.setup(
    name="generate-routers-fastapi-generator_jvngarcia",
    version="0.1.1",
    author="Ángel García",
    author_email="angelgarciaweb@gmail.com",
    description=(
        "Sistema para crear rutas para proyecto de nuevo generador de código SQL: fastapi-generator "
    ),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/jvngarcia/generate-routers-fastapi-generator",
    project_urls={
        "Bug Tracker": "https://github.com/jvngarcia/generate-routers-fastapi-generator/issues",
    },
    install_requires=["requests"],
    packages = ['generate_routers'], 
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "makerouter = generate_routers.cli:main",
        ]
    }
)
